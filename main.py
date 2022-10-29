#!/usr/bin/env python
import enum
from simplemoer.client import WattTime
import json
import os
import kasa
from enum import Enum
import asyncio
import sys

MAXMOER=os.environ.get('MAXMOER')
PLUGHOST=os.environ.get('PLUGHOST')

class PlugState(Enum):
    OFF = 0
    ON = 1

def get_current_moer_index() -> int:
    wt=WattTime()
    return wt.get_index()['percent']

def log_time() ->str:
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

async def get_plug(host: str):
    try:
        plug=kasa.SmartPlug(host)
        await plug.update()
    except Exception as err:
        print(f"[{log_time()}] trouble connecting to plug {host} : {err} {type(err)}")
        raise err
    return plug

def get_current_plugstate(plug) -> PlugState:
    if plug.is_off: return PlugState.OFF
    if plug.is_on: return PlugState.ON

async def main():
    current_moer = get_current_moer_index()
    plug = await get_plug(PLUGHOST)
    current_plugstate = get_current_plugstate(plug)
    desired_plugstate = PlugState.ON if int(current_moer) <= int(MAXMOER) else PlugState.OFF
    if current_plugstate==desired_plugstate: 
        print(f"doing nothing. plugstate was {current_plugstate} desired plugstate was {desired_plugstate}")
    elif desired_plugstate == PlugState.ON:
        result = await plug.turn_on()
        print(f"result: {result}")
    elif desired_plugstate == PlugState.OFF:
        result = await plug.turn_off()
        print(f"result: {result}")

if __name__ == '__main__':
    sys.exit(asyncio.run(main()))


#!/usr/bin/env python
from datetime import datetime
from enum import Enum
from simplemoer.client import WattTime
from os import environ
from kasa import SmartPlug as KasaSmartPlug
from enum import Enum
import asyncio
import sys

MAXMOER = environ.get('MAXMOER')
PLUGHOST = environ.get('PLUGHOST')
PLUGHOSTS = environ.get('PLUGHOSTS')


def log_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


async def main():
    wt = WattTime()
    current_moer = wt.get_index()['percent']
    if PLUGHOSTS:
        for host in PLUGHOSTS.split(','):
            print(f"[{log_time()}] processing host {host} in list {PLUGHOSTS}...")
            await check_plug(current_moer, host)
    if PLUGHOST:
        print(f"[{log_time()}] processing host {PLUGHOST} from env...")
        await check_plug(current_moer, PLUGHOST)


async def check_plug(current_moer, host):
    plugManager = PlugManager(host)
    current_plugstate = await plugManager.get_state()
    desired_plugstate = (
        PlugState.ON if int(current_moer) <= int(MAXMOER)
        else PlugState.OFF)
    await plugManager.set_state(current_plugstate, desired_plugstate)


class PlugState(Enum):
    OFF = 0
    ON = 1


class PlugManager:
    host_ip = ""
    plug = None

    def __init__(self, host_ip) -> None:
        if not host_ip:
            raise Exception(
                "please provide an ip address argument to PlugManager")
        self.host_ip = host_ip
        self.plug = KasaSmartPlug(host_ip)

    async def connect(self) -> None:
        try:
            await self.plug.update()
        except Exception as err:
            print(
                f"[{log_time()}] trouble connecting to plug  {self.host_ip} : {err} {type(err)}")

    async def get_state(self) -> PlugState:
        await self.connect()
        if self.plug.is_off:
            return PlugState.OFF
        if self.plug.is_on:
            return PlugState.ON

    async def set_state(self, current_plugstate, desired_plugstate):
        if current_plugstate == desired_plugstate:
            print(f"doing nothing. plugstate was {current_plugstate}"
                  " desired plugstate was {desired_plugstate}")
        elif desired_plugstate == PlugState.ON:
            print(f" turning on ...")
            await self.plug.turn_on()
        elif desired_plugstate == PlugState.OFF:
            print(f" turning off ...")
            await self.plug.turn_off()


if __name__ == '__main__':
    sys.exit(asyncio.run(main()))

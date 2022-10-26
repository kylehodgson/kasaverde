#!/usr/bin/env python
from simplemoer.client import WattTime
import json
import os
import kasa

MAXMOER=os.environ.get('MAXMOER')

def get_current_moer_index():
    wt=WattTime()
    return wt.get_index()


print(f"index {get_current_moer_index()}")

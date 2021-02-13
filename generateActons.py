#!/usr/bin/env python3

# Imports
import sys
import time
import datetime
import os
import platform
import asyncio
import logging
import json

import aiohttp
import pyxivapi
from pyxivapi.models import Filter, Sort
from datetime import datetime

APIKEY = "YOUR_API_KEY_HERE"

async def find(client, nameStr):
    client = pyxivapi.XIVAPIClient(api_key=APIKEY)
    spell = await client.index_search(name=nameStr,indexes=["Action", "PvPAction", "CraftAction"],columns=["ID", "Name", "Icon", "Description", "ClassJobCategory.Name", "ClassJobLevel", "ActionCategory.Name"],string_algo="match")
    print(spell)
    await client.session.close()

async def make(client):
    client = pyxivapi.XIVAPIClient(api_key=APIKEY)
    data = {}
    data["blueAction"] = []
    data["Action"] = []
    for i in range(11383,11432):
        spell = await client.index_by_id(content_id=i,index="Action",columns=["Name","ClassJobCategory.Name"],language="en")
        data["blueAction"].append({str(i):spell["Name"]})
        print(spell["Name"])
        time.sleep(0.25)
    for i in range(18295,18326):
        spell = await client.index_by_id(content_id=i,index="Action",columns=["Name","ClassJobCategory.Name"],language="en")
        data["blueAction"].append({str(i):spell["Name"]})
        print(spell["Name"])
        time.sleep(0.25)
    for i in range(23264,23291):
        spell = await client.index_by_id(content_id=i,index="Action",columns=["Name","ClassJobCategory.Name"],language="en")
        data["blueAction"].append({str(i):spell["Name"]})
        print(spell["Name"])
        time.sleep(0.25)
    for i in range(7559,7563):
        spell = await client.index_by_id(content_id=i,index="Action",columns=["Name"],language="en")
        data["Action"].append({str(i):spell["Name"]})
        print(spell["Name"])
        time.sleep(0.25)    

    data["blueActionNumber"] = len(data["blueAction"])

    with open('actions.txt', 'w') as outfile:
        json.dump(data, outfile, indent=4)

    await client.session.close()

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Use by passing this script `make` to generate a list of blu spells and role actions, or by passong `find` with an action name")
    else:
        loop = asyncio.get_event_loop()
        if sys.argv[1] == "make":
            loop.run_until_complete(make(sys.argv[1:]))
        elif sys.argv[1] == "find":
            loop.run_until_complete(find(sys.argv[1:]))
        # logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='%H:%M')
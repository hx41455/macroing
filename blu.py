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

# SAMPLE = "xivbars.bejezus.com/job/BLU?s=[["11383","0","0","0","11384","0","0","0","11385","0","0","0","11386","0","0","0"],["11392","0","0","0","11393","0","0","0","11394","0","0","0","11389","0","0","0"],["11399","0","0","0","11406","0","0","0","11416","0","0","0","11412","0","0","0"],["11427","0","0","0","11430","0","0","0","11424","0","0","0","11415","0","0","0"]]"

BLUMACRO = "/chotbar blueAction"

async def find(client, nameStr):
    spell = await client.index_search(name=nameStr,indexes=["Action", "PvPAction", "CraftAction"],columns=["ID", "Name", "Icon", "Description", "ClassJobCategory.Name", "ClassJobLevel", "ActionCategory.Name"],string_algo="match")
    print(spell)

async def make(client):
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
    return 1

async def genMacro(argv):
    osm = platform.system()
    # client = pyxivapi.XIVAPIClient(api_key="lol")
    if argv[0] == "make":
        # await make(client)
        pass
    # elif argv[0] == "find":
    #     # print(argv[1])
    #     await find(client, argv[1])
    else:
        # for a in argv:
        #     print(" ~~~ ", a, " ~~~ ")
        layout = []
        huds = []
        hudmacro = []
        bookmacro = []

        if osm == "Windows":
            layout.append(argv[0].split("=[[")[1])
            for i in range(1,4):
                layout.append(argv[i].split("],[")[1])
        else:
            layout = argv[0].split("=")[1].split("[[")[1].split("]]")[0].split("],[")

        for i in range(0, len(layout)):
            huds.append(layout[i].split(","))
        
        with open('actions.json') as actions_json:
            actions = json.load(actions_json)
            for i in range(0, len(huds)):
                for j in range(0, len(huds[i])):
                    if huds[i][j] != "0":
                        if huds[i][j][0].isalpha():
                            id = str(huds[i][j][1:])
                            if huds[i][j][0] in ['m','c']:
                                continue
                            if huds[i][j][0] in ['g','r']:
                                # index_name = "GeneralAction"
                                index_name = "Action"
                        else:
                            # index_name = "Action"
                            index_name = "blueAction"
                            id = str(huds[i][j])
                            bookmacro.append("/bluespellbook set \"" + actions[index_name][id] + "\"")
                        
                        action = actions[index_name][id]
                        hudmacro.append("/chotbar " + index_name + " \"" + action + "\" " + str(i+1) + " " + ("L" if j < 8 else "R") + ("D" if (j%8) < 4 else "A") + str(((j-1)%4)+1))
                        # spell = await client.index_by_id(content_id=int(id),index=index_name,columns=["Name","ClassJobCategory.Name"],language="en")
                        # print("/chotbar " + ("blueAction" if spell["ClassJobCategory"]["Name"] == "BLU" else "Action") + " \"" + spell["Name"] + "\" " + str(i+1) + " " + ("L" if j < 8 else "R") + ("D" if (j%8) < 4 else "A") + str(((j-1)%4)+1))
                        
                        # time.sleep(0.25)

        with open(datetime.now().strftime("%Y%m%d%H%M%S")+"_hud.txt",'w') as file:
            for h in hudmacro:
                file.write('%s\n' % h)
        with open(datetime.now().strftime("%Y%m%d%H%M%S")+"_book.txt",'w') as file:
            for b in bookmacro:
                file.write('%s\n' % b)

    # await client.session.close()

if __name__ == "__main__":
    # logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='%H:%M')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(genMacro(sys.argv[1:]))

#!/usr/bin/env python3

# Imports
import sys
import time
import datetime
import os
import platform
import json

from datetime import datetime

# SAMPLE = "xivbars.bejezus.com/job/BLU?s=[["11383","0","0","0","11384","0","0","0","11385","0","0","0","11386","0","0","0"],["11392","0","0","0","11393","0","0","0","11394","0","0","0","11389","0","0","0"],["11399","0","0","0","11406","0","0","0","11416","0","0","0","11412","0","0","0"],["11427","0","0","0","11430","0","0","0","11424","0","0","0","11415","0","0","0"]]"

def genMacro(argv):
    osm = platform.system()
    layout = []
    huds = []
    hudmacro = []
    bookmacro = []

    # 0 for xbar; 1 for hotbar
    hbar = int(argv[0].split("&")[1].split("=")[1])
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
                            index_name = "Action"
                    else:
                        index_name = "blueAction"
                        id = str(huds[i][j])
                        bookmacro.append("/bluespellbook set \"" + actions[index_name][id] + "\"")
                    
                    action = actions[index_name][id]
                    if not hbar:
                        hudmacro.append("/chotbar " + index_name + " \"" + action + "\" " + str(i+1) + " " + ("L" if j < 8 else "R") + ("D" if (j%8) < 4 else "A") + str(((j-1)%4)+1))
                    elif hbar:
                        hudmacro.append("/hotbar " + index_name + " \"" + action + "\" " + str(i+1) + " " + str(j+1))

    print('\n')
    with open(datetime.now().strftime("%Y%m%d%H%M%S")+"_hud.txt",'w') as file:
        for h in hudmacro:
            print(h)
            file.write('%s\n' % h)
    print('\n')
    with open(datetime.now().strftime("%Y%m%d%H%M%S")+"_book.txt",'w') as file:
        for b in bookmacro:
            print(b)
            file.write('%s\n' % b)
    print('\n')

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Use by passing the sharable url `https://xivbars.bejezus.com/?job=BLU`\nMust pass inside single quotes '[content]'")
    else:
        genMacro(sys.argv[1:])

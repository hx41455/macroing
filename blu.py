#!/usr/bin/env python3

# Imports
import sys

SAMPLE = "xivbars.bejezus.com/job/BLU?s=[["11383","0","0","0","11384","0","0","0","11385","0","0","0","11386","0","0","0"],["11392","0","0","0","11393","0","0","0","11394","0","0","0","11389","0","0","0"],["11399","0","0","0","11406","0","0","0","11416","0","0","0","11412","0","0","0"],["11427","0","0","0","11430","0","0","0","11424","0","0","0","11415","0","0","0"]]"

def main(argv):
    layout = argv[0].split("=")[1].split("[[")[1].split("]]")[0].split("],[")
    print(str(len(layout))+" - ")
    print(layout)
    huds = []
    for i in range(0, len(layout)):
        print(i)
        huds.append(layout[i].split(","))
    
    for h in huds:
        print(h)
        
    # _1LD = layout[0:4]
    # _1LA = layout[4:8]
    # _1RD = layout[8:12]
    # _1RA = layout[12:16]
    


if __name__ == "__main__":
   main(sys.argv[1:])
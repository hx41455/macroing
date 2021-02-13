# BLU Hud layout macro generator
Because I'm too lazy to craft macros, but not too lazy to write a python script that will craft them for me...

Use https://xivbars.bejezus.com/job/BLU to generate a few HUDs, then get the share url (click the copy button) to get that, and run `blu.py xivbars.bejezus.com/job/BLU?s=[["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]]` to generate macros (where the zeros will be spell IDs)

Only BLU spells and role actions (plus sprint) currently work, and only crossbar... since I mainly did this for myself, but I might add hotbars.

I noticed that windows and linux maybe handle the call differently.. I'll uh.. experiment and fix that probably I guess

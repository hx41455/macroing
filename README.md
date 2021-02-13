# BLU Hud layout macro generator
> Because I'm too lazy to craft macros, but not too lazy to write a python script that will craft them for me...

## Requirements

Know how to run python on your computer, iuno, I winged it and got it to work, so I believe in you too lol

## Usage example

Use https://xivbars.bejezus.com/job/BLU to generate a few HUDs, then get the share url (click the copy button) to get that, and run:

```sh
generateActions.py 'xivbars.bejezus.com/job/BLU?s=[["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"],["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]]&l=1'
```

to generate macros (where the zeros will be spell IDs), and the `l=1` denotes if the it's a hotbar or a crossbar

## Issues
XIVbars doesn't have Phantom Flurry or Nightbloom yet, so you'll either have to add those macros manually, or find their spots in the url and add their IDs (23288 and 23290 respectively)

Only BLU spells and role actions (plus sprint) currently work

Tested on Windows so far so I don't know if calling+passing works different on other OSs yet..

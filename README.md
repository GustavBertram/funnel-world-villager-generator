# Funnel World Villager Generator
This generates villagers for use in Funnel World.

Funnel World is a 0-level Adventure for [Dungeon World](http://www.dungeon-world.com/), Published by [Lampblack & Brimstone](http://www.drivethrurpg.com/browse/pub/7199/Lampblack--Brimstone), written by Jason Lutes, and illustrated by Jesse H. Mead. It is [available online](http://www.drivethrurpg.com/product/137012/Funnel-World) at DrivethruRPG. The adventure is published under a [Creative Commons Attribution-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/) license.

The adventure has rules for randomly generating 0-Level villagers, and this code implements the rules as described with a few minor tweaks:
* Physical traits are divided into male, female and neutral
* Male elves only have neutral traits, since they can't grow beards
* Female dwarves have male traits too, because they can grow beards
* Alewife and Prostitute are female-only occupations, Executioner is male-only

Usage:
```
python3 generator.py
```

Follow the prompts thereafter.

Notes:
* Duplicate names are avoided.
* If you have existing villagers, their names can be entered so they're not duplicated.
* Bonds are automatically generated
  * PCs have at least one bond to another PC.
  * New villagers have at least two bonds:
    * One bond to a PC.
    * One bond to anyone.

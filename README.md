
# MikuBH3

A Server emulator for version 7.9 of a certain adventure anime game
![screenshot](https://github.com/MikuLeaks/MikuBH3-PS/raw/main/screenshot.png)


## Requirements
- Python 3.12++
- [MongoDB](https://www.mongodb.com/try/download/community)

## Features

- Basic features: inventory,warship,dress,custom team
- Working battle with grandkey & elf/astral
- Superstring Dimension (Abyss)
- Universial Mirage
- Story Chapter 1 - 42


## Installation

For your first launch, run these:

```python
pip install -r requirements.txt
```

Download resources & proto from [MikuBH3-Res](https://github.com/MikuLeaks/MikuBH3-RES) and place them into your resources & lib folder.
```
├───resources
│   └───ExcelOutputAsset
├───lib
│   └───proto
│       └───__init__.py
```

also build patch from [MikuBH3-Patch](https://github.com/MikuLeaks/MikuBH3-PATCH) and place them into your game directory `Honkai Impact 3rd Game`

## To-Do List

- Commands

- Memorial Arena

- Elysian Realm

- Open World

- Part 2 Story & Open world

- Character Tutorial

## Usage/Examples
To run the project use cmd or vscode and run
```python
py hi3
```


## Change Stage Superstring Dimension (Abyss)

edit `Endless.json` and set area1 to desire `SiteID` from `UltraEndlessSite.json`

## Use Local Patch
edit `Config.json` and set UseLocalCache to True, after that put data cache folder from AppData `Honkai Impact 3rd Game` into `resources/statics`

# Support
Join [Discord](https://discord.gg/MdHC4AJvec) for support

# Credits
- am25

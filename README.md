# MikuBH3

A Server emulator for version 7.9 of a certain adventure anime game

![screenshot](https://github.com/MikuLeaks/MikuBH3-PS/raw/main/screenshot.png)

## Features

- Basic features: inventory,warship,dress,custom team
- Working battle with grandkey & elf/astral
- Superstring Dimension (Abyss)
- Universial Mirage
- Story Chapter 1 - 42
- Character Tutorial
- Memorial Arena
- Commands

## Requirements

- Python 3.12++
- [MongoDB](https://www.mongodb.com/try/download/community)

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

## Connecting with the client (Sparkle Proxy)

- Download proxy from [Releases](https://github.com/MikuLeaks/MikuBH3-PS/releases)
- Extract the `Proxy.zip` file anywhere you want.
- Run `Sparkle-Proxy.exe` as administrator and open the game.

## Connecting with the client (DLL method)

- Download prebuild patch from [BH3-Patch](https://github.com/MikuLeaks/MikuBH3-PATCH/releases)
- Extract the `BH3-Patch-Win64.zip` file into your game folder, where the game’s main executable (`BH3.exe`) is located.
- Run `bh3-launcher.exe` as administrator.

## Usage/Examples

To run the project use cmd or vscode and run

```python
py hi3
```
## Changing Stage in Abyss/Memorial Using JSON

- **Superstring Dimension (Abyss)**

    Open the `Battle.json` file and update `area1` to the preferred `SiteID` from `UltraEndlessSite.json`.

- **Memorial Arena**

    Open the `Battle.json` file and update the `boss_ids` as needed. You can find `boss_id` values in the `BossIdList` within `ExBossMonsterSchedule.json`.

## Commands
```
/help. Displays a list of available commands.
/maxskill {avatar_id | all}. Maximize the skills of a specific avatar. Use 'all' to maximize the skills of all avatars.
/rank {avatar_id | all} {rank}. Edit rank of a specific avatar or use 'all' to update rank of all avatars.
```

## Use Local Patch Assets

edit `Config.json` and set UseLocalCache to True, after that put data cache folder from AppData `Honkai Impact 3rd Game` into `resources/statics`

# Support

Join [Discord](https://discord.gg/MdHC4AJvec) for support

# To-Do List

- ~~Commands~~

- ~~Memorial Arena~~

- Elysian Realm

- Open World

- Part 2 Story & Open world

- ~~Character Tutorial~~

# Credits

- am25

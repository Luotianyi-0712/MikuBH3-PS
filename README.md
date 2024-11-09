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

## Connecting with the client (Fiddler method)

- Log in with the client to an official server at least once to download game data.
- Install and have [Fiddler Classic](https://www.telerik.com/fiddler) running.
- Copy and paste the following code into the Fiddlerscript tab of Fiddler Classic. Remember to save the fiddler script after you copy and paste it:

```
import System;
import System.Windows.Forms;
import Fiddler;
import System.Text.RegularExpressions;
class Handlers
{
    static function OnBeforeRequest(oS: Session) {
        if( (oS.host.EndsWith("global1.bh3.com")) || oS.host == "47.74.175.126" || oS.host.EndsWith(".yuanshen.com") || oS.host.EndsWith(".hoyoverse.com") || oS.host.EndsWith(".starrails.com") || oS.host.EndsWith(".bhsr.com") || oS.host.EndsWith(".kurogame.com") || oS.host.EndsWith(".zenlesszonezero.com") || oS.host.EndsWith(".g3.proletariat.com") || oS.host.EndsWith("west.honkaiimpact3.com") || oS.host.EndsWith("westglobal01.honkaiimpact3.com") || oS.host.EndsWith(".os.honkaiimpact3.com") || oS.host.EndsWith("overseas01-appsflyer-report.honkaiimpact3.com") || oS.host.EndsWith(".mihoyo.com") || (oS.host.EndsWith("global2.bh3.com") && !oS.host.Contains("bundle"))) {
            oS.host = "127.0.0.1";
        }
    }
}
```

## Connecting with the client (DLL method)

- Download prebuild patch from [BH3-Patch](https://github.com/MikuLeaks/MikuBH3-PATCH/releases)
- Extract the `BH3-Patch-Win64.zip` file into your game folder, where the game’s main executable (`BH3.exe`) is located.
- Run `bh3-launcher.exe` as administrator.

## Usage/Examples

To run the project use cmd or vscode and run

```python
py hi3
```

## Change Stage Superstring Dimension (Abyss)

edit `Endless.json` and set area1 to desire `SiteID` from `UltraEndlessSite.json`

## Use Local Patch Assets

edit `Config.json` and set UseLocalCache to True, after that put data cache folder from AppData `Honkai Impact 3rd Game` into `resources/statics`

# Support

Join [Discord](https://discord.gg/MdHC4AJvec) for support

# To-Do List

- Commands

- Memorial Arena

- Elysian Realm

- Open World

- Part 2 Story & Open world

- ~~Character Tutorial~~

# Credits

- am25

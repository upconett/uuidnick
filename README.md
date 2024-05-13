# uuidnick
## The tool that converts Minecraft UUID to username.
### It uses whitelist.json on your server. So no Mojang API needed. 
It's suitable ***only*** for servers that use ***whitelist***  
The tool comes in handy for automatisation and bash scripting.
---
### Install & Build
Simply clone the repo and build with pyinstaller.  
Run the following command and tool will be installed:
```shell
git clone https://github.com/upconett/uuidnick && pip install uuidnick/requirements.txt && pyinstaller -F -u uuidnick uuidnick/main.py && cp uuidnick/dist/uuidnick /bin
```
---
### Usage
```shell
uuidnick <uuid or nickname> <file extension (if needed)>
```
You can add **file extension** as second argument to get the output as `<uuid><extension>`.
```shell
> uuidnick Stepan0Tap
# output: 915e8777-13a8-38c4-9454-56a66c79bd02

> uuidnick Steve123 .dat
# output: a15e8765-77j8-38c6-9432-56a88c70bd15.dat

> uuidnick a15e8765-77j8-38c6-9432-56a88c70bd15
# output: Steve

> uuidnick 915e8777-13a8-38c4-9454-56a66c79bd02.json .json
# output: Stepan0Tap
```
### Example
Using uuidnick to find the **statistics file** of Stepan0Tap.  
Stat files located in `world/stats` and have **.json** extension.  
Stat files look like **\<uuid\>.json**:  `915e8777-13a8-38c4-9454-56a66c79bd02.json`
``` shell
# Using jq to format json file
> cat $(uuidnick Stepan0Tap .json) | jq
```
### Output
``` shell
{
  "stats": {
    "minecraft:custom": {
      "minecraft:time_since_rest": 5342,
      "minecraft:interact_with_furnace": 3,
      "minecraft:sprint_one_cm": 87356,
      "minecraft:damage_taken": 630,
      "minecraft:walk_one_cm": 120191,
      "minecraft:mob_kills": 4,
      "minecraft:damage_dealt": 505,
      "minecraft:swim_one_cm": 37935,
      "minecraft:interact_with_crafting_table": 3,
      "minecraft:fly_one_cm": 34492,
      "minecraft:player_kills": 1,
...
```

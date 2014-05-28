#Minecraft - Raspberry Pi Edition <img src="../../Resources/mc.png" width=50px alt="minecraft">


##Instructions
For this task you will need to have minecraft setup on your raspberry pi. To do this you should will need an internet connection ideally on your pi. (if you can't do this at home, try setting up at school).

To install and run minecraft pi open an LXterminal window and enter the following commands:

**Install**
```bash
install
wget https://s3.amazonaws.com/assets.minecraft.net/pi/minecraft-pi-0.1.1.tar.gz
tar xvfz minecraft-pi-0.1.1.tar.gz
cd mcpi
chmod +x minecraft-pi
```

**Run**
```bash
cd mcpi
minecraft-pi
```

**Help Resources**
- [David  Whale - flashcards](http://blog.whaleygeek.co.uk/wp-content/uploads/2013/06/minecraftPi-flashcards.pdf)
- [minecraft pi - cheatsheet](http://arghbox.files.wordpress.com/2013/06/table.pdf)


##Grading
|Grade|What must I do?|
|-----|---------------|
|D|I will be able to install and run minecraft-pi, run,adapt and **comment** the location finder program.|
|C|I will be able to run,adapt and **comment** the house builder program.|
|B|I will be able to run,adapt and **comment** the tunnelling program.|
|A/A*|I will have completed the first 3 tasks and made something cool! It will take some of what I have learnt and used it in a new way.|

##Your tasks
###1 - Find you location.
With minecraft Pi running, in a world and paused. Open idle, create a new program and enter [this](playerPos.py) code:
```python
import mcpi.minecraft as minecraft 
import time 
mc = minecraft.Minecraft.create("localhost") 
 
while True: 
 time.sleep(1.0) 
 pos = mc.player.getPos() 
 print pos.x, pos.y, pos.z
```
When you save it, it must be stored in the **mcpi/api/python** directory, otherwise it won't work. The code should display your minecraft location in your python window.

- Can you make it post these co-ordinates to chat instead?
- Can you comment each line to show you understand what the code does.
- replace the [playerPos](playerPos.py) code with your own version and commit. 

###2 - Build a house
Try the [house](house.py) code, currently it places 3 obsidian blocks near the player.

```python
import mcpi.minecraft as minecraft 
from mcpi.block import * 
 
mc = minecraft.Minecraft.create("localhost") 
 
x = 38 # vertical 
y = 0 # height from sea level 
z = 7.7 # horizontal 
mc.player.setPos(x, y, z) 
 
mc.setBlock(x, y, z, GLOWING_OBSIDIAN) 
mc.setBlock(x, y, z+2, GLOWING_OBSIDIAN) 
mc.setBlock(x, y, z+4, GLOWING_OBSIDIAN) 
```

- Can you adapt the code to build a simple house, it should be at least 3x5 in size and ideal made from different [materials](http://minecraft.gamepedia.com/Data_values_(Pocket_Edition)).
- Can you comment each line to show you understand what the code does.
- replace the [house.py](house.py) code with your own version and commit. 

###3 - Rapid Tunnels
Try the [tunnel](tunnel.py) code, currently it places 3 obsidian blocks near the player.
```python
import mcpi.minecraft as minecraft 
from mcpi.block import * 
 
mc = minecraft.Minecraft.create("localhost") 
 
x = 38 # vertical 
y = 0 # height from sea level 
z = 7.7 # horizontal 
mc.player.setPos(x, y, z) 
 
mc.setBlock(x, y, z, AIR) 

```

- Can you adapt the code to constantly delete blocks around you to create a program which will tunnel for you.
- Can you comment each line to show you understand what the code does.
- replace the [tunnel.py](tunnel.py) code with your own version and commit.

###4 - Do something cool
Do something new and cool and save the code you created over the [cool](cool.py) file.
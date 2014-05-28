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

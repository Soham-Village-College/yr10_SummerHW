import mcpi.minecraft as minecraft 
import time 
mc = minecraft.Minecraft.create("localhost") 
 
while True: 
 time.sleep(1.0) 
 pos = mc.player.getPos() 
 print pos.x, pos.y, pos.z

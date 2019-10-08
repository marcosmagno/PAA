from subprocess import call
import os 
for i in range(1,16):
    print("run", i)
    os.system('time python3 run.py ' + str(i) + ".in")

    
    
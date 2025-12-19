import time 
import sys

dash = ""

for i in  range(10):
    dash += "-"
    sys.stdout.write("\r" + dash +"loading ")
    sys.stdout.flush()
    time.sleep(0.3)
print("\r" + dash + "done       ")
    
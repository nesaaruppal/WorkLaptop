##### PYTHON THREADING #####

import threading 
import time 


done = False 


def worker():
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        print(counter)

worker()

##### Won't get to the input statement until the "worker" function is finished #####

#while not done:
input("Press enter to quit")

done = True 
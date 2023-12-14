##### PYTHON THREADING #####

import threading 
import time 

done = False 

def worker():
    counter = 0
    while True:
        time.sleep(1)
        counter += 1
        print(counter)

# Can either store it in variable or iniate straight away
t1 = threading.Thread(target=worker, daemon=True)

t1.start()

    # Starts the "worker" function in a separate thread
    # Does not work with an endless WHILE LOOP - the main thread has nothing to do but the endless while loop will continue to run 
    # Can say that a Thread is not important and we want it to close when everything else has finished 
    
    ##### Add a "daemon" statement #####
    # Means the worker function is working in the background 
    
worker()

input("Press enter to quit")
done = True 
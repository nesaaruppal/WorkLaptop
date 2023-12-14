###### THREADING #####

# Number of "CORES" you have on processor means the amount of things that can happen at the exact same time 

# E.g. 4 Cores
    # Maximum of 4 processes can run at the same time 
    # PARRALLELISM 
        # CPU contains CORES which determines the number of parrallel operations you can do at the same time 
        # GHz determines the speed using an alternating current 
        
# A "THREAD" is one program or one set of operations that needs to happen
    # Every THREAD is assigned to 1 core
    # Each CORE has multiple THREADS
    # Able to switch between THREADS to perform different operations 
        # This is what threading is 
        # The core needs to be able to switch between separate threads
    

# Task Manager --> CPU (Shows 300 processes and 4500 THREADS for example)

# Threading doesn't necessarily mean we want things to happen at the same time 
    # We are just changing the order in which we do specific operations
    
# HANGING 
    # Means the THREAD stops
    # OR it doesn't actually need to be executing at the current time 
    # Can make certain threads wait for something to happen (E.g a user to press a specific key)
        # The processor CORE can switch to something else whilst it's waiting 
        ##### CONCURRENT PROGRAMMING #####

##### 1 CORE Example #####
    # E.g:
        # print(1)
        # time.sleep(10)
        # print(2)
        ## The OUTPUT will take 10 seconds (time.sleep)
        
#




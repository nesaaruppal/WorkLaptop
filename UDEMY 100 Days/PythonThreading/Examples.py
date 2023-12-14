        ##### EXAMPLES OF USING THREADING #####

# # import module
# from threading import *
# import time
 
# # creating a function
# def thread_1():                 
#   for i in range(5):
#     print('this is non-daemon thread')
#     time.sleep(3)
 
# # creating a thread T
# T = Thread(target=thread_1)
 
# # starting of thread T
# T.start()      
 
# # main thread stop execution till 5 sec.
# time.sleep(5)                   
# print('main Thread execution')



# # import modules
# from threading import *
# import time
 
# # creating a function
# def thread_1():                      
#   for i in range(5):
#     print('this is thread T')
#     time.sleep(3)
 
# # creating a thread
# T = Thread(target = thread_1) 
 
# # change T to daemon
# T.setDaemon(True)                   
 
# # starting of Thread T
# T.start()                           
# time.sleep(5)
# print('this is Main Thread')  



# # import module
# from threading import *
 
# def fun_daemon():
#   print("GFG")
   
# thread_1 = Thread(target=fun_daemon)
# print(thread_1.isDaemon())
# thread_1.start()
# print(thread_1.daemon)


# from threading import Thread
# import time

# def worker():
#     time.sleep(3)
#     print('daemon done')

# thread = Thread(target=worker, daemon=False)
# thread.start()

# print('main done')



# import threading
# import time
# import sys
 
# def func():
#     while True:
#         time.sleep(0.5)
#         print("Thread alive, and it won't die on program termination")
 
# t1 = threading.Thread(target=func)
# t1.start()
# time.sleep(2)
# sys.exit()




import threading

l = threading.Lock()
print("before first acquire")
l.acquire()
print("before second acquire")
#l.aquire()
l.release()
print("acquired lock twice")
from threading import *
import time
#l=Lock()
def wish(name):
    #l.acquire()
    for i in range(10):
        print("Good evening",end=' ')
        time.sleep(2)
        print(name)
    #l.release()
t1=Thread(target=wish,args={'jose'})
t2=Thread(target=wish,args={'mitch'})

t3=Thread(target=wish,args={'mart'})
t1.start()
t1.join(3)
t2.start()
t2.join(3)
t3.start()

import threading
import time
f=True

def worker():
    counter=0
    while f:
        time.sleep(1)
        print(counter)
        counter+=1

threading.Thread(target=worker).start()
x=input('Enter x to stop')
while x!='x':
    x=input('Enter x to stop')
f=False

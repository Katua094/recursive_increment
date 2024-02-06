import threading    
import time


def numbers():
    
    for i in range(5):
        time.sleep(1)
        print(f"thread1:{i}")
    
def letters():
    
    for i in "ABCDE":
        time.sleep(1)
        print(f"thread2:{i}")

thread1=threading.Thread(target=numbers)
thread2=threading.Thread(target=letters)

thread1.start()
thread2.start()
thread1.join()
thread2.join()


print("The program has finished running")


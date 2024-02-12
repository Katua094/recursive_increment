import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)  # Simulate some work
        print(f"Thread 1: {i}")

def print_letters():
    for letter in 'ABCDE':
        time.sleep(1)  # Simulate some work
        print(f"Thread 2: {letter}")

# Create two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads have finished.")

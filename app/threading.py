import threading
import time

def task(name, delay):
    (f'{name} starting...')
    time.sleep(delay)
    print(f'{name} finished after {delay} seconds')

    start_time =time.time()

thread1 = threading.Thread(target=task, args=('Thread 1', 2))
thread1 = threading.Thread(target=task, args=('Thread 2', 3))
thread1 = threading.Thread(target=task, args=('Thread 3', 1))


thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print(f'Completed in {time.time() - start_time:.2f} seconds')


         
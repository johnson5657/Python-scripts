from concurrent import futures
import time
import sys

def process_function(number,i):
    print(i)
    time.sleep(number)


def main():
    number = 60
    #executor = futures.ThreadPoolExecutor() # will run a new function iteration in  a new thread 
    executor = futures.ProcessPoolExecutor() # will run a new function iteration in a new process
    for i in range(0, 10):
        executor.submit(process_function, number,i)

    executor.shutdown()
if __name__ == "__main__":
    sys.exit(main())


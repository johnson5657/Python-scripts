student-04-fa6463f7d756@linux-instance:~$ cat ./scripts/multisync.py
#!/usr/bin/env python3
from multiprocessing import Pool
def run(task):
  # Do something with task here
    print("Handling {}".format(task))
if __name__ == "__main__":
  tasks = ['task1', 'task2', 'task3']
  # Create a pool of specific number of CPUs
  p = Pool(len(tasks))
  # Start each task within the pool
  p.map(run, tasks)

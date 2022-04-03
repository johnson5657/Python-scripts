from memory_profiler import profile
from concurrent import futures


from multiprocessing import Pool

@profile()  #telling the memory_profiler to monior function memory usage
def run(task):
  # Do something with task here
    print("Handling {}".format(task))
if __name__ == "__main__":
  tasks = ['task1', 'task2', 'task3']
  # Create a pool of specific number of CPUs
  p = Pool(len(tasks))
  # Start each task within the pool
  p.map(run, tasks)

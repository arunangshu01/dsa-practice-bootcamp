from multiprocessing import Queue

if __name__ == "__main__":

    queue_using_multiprocessing_module = Queue(maxsize=5)
    queue_using_multiprocessing_module.put(10)
    queue_using_multiprocessing_module.put(20)
    queue_using_multiprocessing_module.put(30)
    queue_using_multiprocessing_module.put(40)
    queue_using_multiprocessing_module.put(50)
    print(queue_using_multiprocessing_module.get())

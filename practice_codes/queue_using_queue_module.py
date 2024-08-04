from queue import Queue

if __name__ == "__main__":

    queue_using_queue_module = Queue(maxsize=5)
    print(queue_using_queue_module.empty())
    queue_using_queue_module.put(10)
    queue_using_queue_module.put(20)
    queue_using_queue_module.put(30)
    queue_using_queue_module.put(40)
    queue_using_queue_module.put(50)
    print(queue_using_queue_module.full())
    print(queue_using_queue_module.get())
    print(queue_using_queue_module.qsize())




from collections import deque

if __name__ == "__main__":

    queue_using_collections_module = deque(maxlen=5)

    queue_using_collections_module.append(10)
    queue_using_collections_module.append(20)
    queue_using_collections_module.append(30)
    queue_using_collections_module.append(40)
    queue_using_collections_module.append(50)
    queue_using_collections_module.append(60)

    print(queue_using_collections_module)

    print(queue_using_collections_module.popleft())
    print(queue_using_collections_module)

    print(queue_using_collections_module.popleft())
    print(queue_using_collections_module)

    print(queue_using_collections_module.popleft())
    print(queue_using_collections_module)

    print(queue_using_collections_module.popleft())
    print(queue_using_collections_module)

    print(queue_using_collections_module.clear())
    print(queue_using_collections_module)





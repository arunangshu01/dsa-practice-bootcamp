"""

Animal Shelter

An animal shelter, which holds only dogs and cats, operates on a strictly "first in first out" basis. People must adopt
either the "oldest" (based on arrival time) of all animals at the shelter, or they can select whether they would prefer
a dog or a cat (and will receive the oldest animal of that type). They cannot select which specific animal they would
like. Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny,
dequeueDog, and dequeueCat.

"""


class AnimalShelter:

    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal, type):
        if type == 'Cat':
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeue_cat(self):
        if len(self.cats) == 0:
            return None
        else:
            cat = self.cats.pop(0)
            return cat

    def dequeue_dog(self):
        if len(self.dogs) == 0:
            return None
        else:
            dog = self.dogs.pop(0)
            return dog

    def dequeue_any(self):
        if len(self.cats) == 0:
            animal = self.dogs.pop(0)
        else:
            animal = self.cats.pop(0)
        return animal


if __name__ == "__main__":
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(animal='Cat1', type='Cat')
    animal_shelter.enqueue(animal='Cat2', type='Cat')
    animal_shelter.enqueue(animal='Dog1', type='Dog')
    animal_shelter.enqueue(animal='Cat3', type='Cat')
    animal_shelter.enqueue(animal='Dog2', type='Dog')
    print(animal_shelter.dequeue_cat())
    print(animal_shelter.dequeue_dog())
    print(animal_shelter.dequeue_any())

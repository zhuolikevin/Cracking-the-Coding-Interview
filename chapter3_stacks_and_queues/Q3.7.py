class AnimalQueue:
    def __init__(self):
        self.dogs = []
        self.cats = []
        self.timestamp = 0

    def enqueue(self, name, DorC):
        self.timestamp += 1
        if DorC == 'd':
            self.dogs.append((name, self.timestamp))
        else:
            self.cats.append((name, self.timestamp))

    def dequeueAny(self):
        if not self.dogs:
            return self.dequeueCat()
        else if not self.cats:
            return self.dequeueDog()

        dog = self.dogs[0]
        cat = self.cats[0]
        if dog[1] < cat[1]:
            return self.dequeueDog()
        else:
            return self.dequeueCat()

    def dequeueDog(self):
        if self.dogs:
            return self.dogs.pop(0)[0]
        else:
            raise IndexError('No dogs!')

    def dequeueCat(self):
        if self.cats:
            return self.cats.pop(0)[0]
        else:
            raise IndexError('No cats!')

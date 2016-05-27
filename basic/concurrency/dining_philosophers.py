import threading
import random
import time

"""
Dining philosophers: 5 philosophers with 5 forks. Philosopher must have 2 forks to eat.

Deadlock is avoided by never waiting for a fork while holding a fork (locked).
Procedure is to do block while waiting to get first fork, and a nonblocking acquire of second fork.
If fail to get second fork, release first fork, swapwhich fork is first and which is second and retry
until getting both.

https://rosettacode.org/wiki/Dining_philosophers#Python
"""

class Philosopher(threading.Thread):

    running = True

    def __init__(self, xname, fork_on_left, fork_on_right):
        threading.Thread.__init__(self)
        self.name = xname
        self.fork_on_left = fork_on_left
        self.fork_on_right = fork_on_right

    def run(self):
        while (self.running):
            # Philosopher is thinking
            time.sleep(random.uniform(3, 13))
            print '%s is hungry.' % self.name
            self.dine()

    def dine(self):
        fork1, fork2 = self.fork_on_left, self.fork_on_right

        while self.running:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked: break
            fork1.release()
            print '%s swaps forks' % self.name
            fork1, fork2 = fork2, fork1
        else:
            return

        self.dining()
        fork2.release()
        fork1.release()

    def dining(self):
        print '%s starts eating ' % self.name
        time.sleep(random.uniform(1, 10))
        print '%s finishes eating and leaves to think.' % self.name

def dining_philosophers():
    forks = [threading.Lock() for n in range(5)]
    philosopher_names = ('Aristotle', 'Kant', 'Buddha', 'Marx', 'Russell')

    philosophers = [Philosopher(philosopher_names[i], forks[i%5], forks[(i+1)%5]) \
                    for i in range(5)]

    random.seed(507129)
    Philosopher.running = True
    for p in philosophers: p.start()
    time.sleep(100)
    Philosopher.running = False
    print ("Now we're finishing.")

if __name__ == "__main__":
    dining_philosophers()
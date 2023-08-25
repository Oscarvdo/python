import threading
import random
import time

# Define a class for the philosophers
class Philosopher(threading.Thread):
    running = True

    def __init__(self, xname, fork_on_left, fork_on_right):
        threading.Thread.__init__(self)
        self.name = xname
        self.fork_on_left = fork_on_left
        self.fork_on_right = fork_on_right

    def run(self):
        while self.running:
            # Philosophers think for a random duration
            time.sleep(random.uniform(3, 13))
            print('{} is hungry.'.format(self.name))
            self.dine()

    def dine(self):
        fork1, fork2 = self.fork_on_left, self.fork_on_right

        while self.running:
            # Acquire the first fork with timeout
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked:
                break
            fork1.release()
            print('{} swaps forks'.format(self.name))
            fork1, fork2 = fork2, fork1
        else:
            return

        self.dining()
        fork2.release()
        fork1.release()

    def dining(self):
        # Philosophers eat for a random duration
        print('{} starts eating'.format(self.name))
        time.sleep(random.uniform(1, 10))
        print('{} finishes eating and leaves to think.'.format(self.name))

def dining_philosophers():
    # Create locks for the forks
    forks = [threading.Lock() for n in range(5)]
    philosopher_names = ('Aristotle', 'Kant', 'Buddha', 'Marx', 'Russel')

    # Create philosopher threads
    philosophers = [Philosopher(philosopher_names[i], forks[i % 5], forks[(i+1) % 5]) for i in range(5)]

    # Set a random seed and start philosopher threads
    random.seed(507129)
    Philosopher.running = True
    for p in philosophers:
        p.start()
    
    # Let the simulation run for a duration
    time.sleep(60)  # Adjust the time as needed
    Philosopher.running = False
    print("Now we're finishing.")

# Run the dining philosophers simulation
dining_philosophers()

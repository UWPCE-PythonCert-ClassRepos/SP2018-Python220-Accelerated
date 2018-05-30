#=========================================================================================
#Name: Iterator 2
#Author: Wesley Wang
#Date: 5/28/2018
#=========================================================================================

class Iterator_2:

    def __init__(self, start, stop, step):
        self.current = start-step
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        self.current += self.step
        if self.current < self.stop:
            return self.current
        else:
            raise StopIteration


if __name__ == "__main__":
    start = 0
    stop = 5
    step = 2
    print(f"Testing iterator 2:\nStart at {start}\nStop at {stop}\nTake {step} steps")
    for i in Iterator_2(start, stop, step):
        print(i)
    
    print("Compared to range():")
    for i in range(start, stop, step):
        print(i)
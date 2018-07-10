#! /usr/local/bin/python3


'''
Write a context manager for a simulated ballard locke program
There are 2 lockes - one small which holds up to 5 boats and one large which
holds up to 10 boats.

When a locke is entered, you need to:
    Stop the pumps
    Open the doors
    Close the doors
    Restart the pumps
    Transfer boats
    etc...

During initialization the context manger class accepts the locke’s capacity in
number of boats.  If the locke's capacity is exceeded, raise a suitable error.

For this simulation, we will only need to print the system controls commands.
'''

from time import sleep, time
import datetime
system_status = True
start_time = 0


class locke_enter():
    def __init__(self, boats, size, handle_error=True):
        global start_time
        self.boats = boats
        self.handle_error = handle_error
        self.size = size
        self.max = 0
        if self.size == 'small':
            self.max = 5
        if self.size == 'large':
            self.max = 10
        start_time = time()

    def __enter__(self):
        print('\n' + ('_' * 80 + '\n') * 2)
        self.now = datetime.datetime.now()
        self.time = str(self.now.strftime("%H") + ':' + self.now.strftime("%M") + ':' + self.now.strftime("%S"))
        print(f'{self.boats} boats would like to traverse the {self.size} locke at {self.time}')
        if self.boats > self.max:
            raise Exception(f'Too many boats for {self.size} locke')
        self.doors_open()
        return self

    def __exit__(self, type, value, traceback):
        global system_status
        if traceback:
            print('\n\n    ___SYSTEM FAILURE___')
            print('    type: {}'.format(type))
            print('    value: {}'.format(value))
            print('    traceback: {}'.format(traceback))
            print('\n    shutting down the system...')
            system_status = False
            print(f'    {self.boats} boats have been stranded!\n')
            return self.handle_error

    def doors_open(self):
        print('opening the doors...', end='', flush=True)
        sleep(2)
        print('doors open')
        sleep(1)

    def doors_close(self):
        print('closing the doors...', end='', flush=True)
        sleep(2)
        print('doors closed')
        sleep(1)

    def boats_enter(self):
        print('boats entering the locke...')
        sleep(2)
        for _ in range(1, self.boats + 1):
            print(f'     boat {_} has entered the locke')
            sleep(2)
        print('all boats are in the locke')
        sleep(1)


class locke_pump():
    def __init__(self, boats, handle_error=True):
        self.boats = boats
        self.handle_error = handle_error

    def __enter__(self):
        self.start = time()
        return self

    def __exit__(self, type, value, traceback):
        global system_status
        if traceback:
            print('\n\n    ___SYSTEM FAILURE___')
            print('    type: {}'.format(type))
            print('    value: {}'.format(value))
            print('    traceback: {}'.format(traceback))
            print('\n    shutting down the system...')
            system_status = False
            print(f'    {self.boats} boats have been stranded!\n')
            return self.handle_error
        else:
            self.pump_stop()

    def pump_start(self):
        print('starting pumps...', end='', flush=True)
        sleep(2)
        print('pumps started')
        sleep(1)

    def pump_stop(self):
        print('stopping the pumps...', end='', flush=True)
        sleep(2)
        print('pumps stopped')
        sleep(1)


class locke_exit():
    global start_time

    def __init__(self, boats, handle_error=True):
        self.boats = boats
        self.handle_error = handle_error

    def __enter__(self):
        self.start = time()
        self.doors_open()
        return self

    def __exit__(self, type, value, traceback):
        global system_status
        if traceback:
            print('\n\n    ___SYSTEM FAILURE___')
            print('    type: {}'.format(type))
            print('    value: {}'.format(value))
            print('    traceback: {}'.format(traceback))
            print('\n    shutting down the system...')
            system_status = False
            print(f'    {self.boats} boats have been stranded!\n')
            return self.handle_error
        else:
            self.doors_close()
            self.now = datetime.datetime.now()
            self.time = str(self.now.strftime("%H") + ':' + self.now.strftime("%M") + ':' + self.now.strftime("%S"))
            self.end = time()
            total_time = self.end - start_time
            print(f'{self.boats} boats have finished traversing the locke at {self.time}')
            print(f'Total traversal time: {total_time:.2f} seconds')

    def doors_open(self):
        print('opening the doors...', end='', flush=True)
        sleep(2)
        print('doors open')
        sleep(1)

    def doors_close(self):
        print('closing the doors...', end='', flush=True)
        sleep(2)
        print('doors closed')
        sleep(1)

    def boats_exit(self):
        print('boats exiting the locke...')
        sleep(2)
        for _ in range(1, self.boats + 1):
            print(f'     boat {_} has exited the locke')
            sleep(2)
        print('all boats have exited the locke')
        sleep(2)


def through_the_locke(boats, size='small', handle_error=True):
    # size can be 'small' for up to 5 boats or 'large' for up to 10 boats
    global system_status
    if system_status is True:
        try:
            with locke_enter(boats, size, handle_error) as x:
                x.boats_enter()
        except Exception as e:
            print(e)
            return
    if system_status is True:
        with locke_pump(boats, handle_error) as x:
            x.pump_start()
    if system_status is True:
        with locke_exit(boats, handle_error) as x:
            x.boats_exit()
    if system_status is not True:
        print('**** locke is offline for repairs ****')


def through_the_locke_with_error(boats, size='small', handle_error=True):
    # this function simulates a RuntimeError during the pumping procedure
    # the error should be handled in the context manager class and global
    # system_status variable will be changed to shut down the system
    global system_status
    if system_status is True:
        try:
            with locke_enter(boats, size, handle_error) as x:
                x.boats_enter()
        except Exception as e:
            print(e)
            return
    if system_status is True:
        with locke_pump(boats, handle_error) as y:
            y.pump_start()
            raise RuntimeError('major pump malfunction detected')
    if system_status is True:
        with locke_exit(boats, handle_error, 'small') as z:
            z.boats_exit()
    if system_status is not True:
        print('**** locke is offline for repairs ****')


def main():
    # run through a series of locke traversals

    # this call will send 4 boats through the small locke
    through_the_locke(4, 'small')

    # this call will try to send 8 boats through the small locke but fail
    # because the small locke only takes up to 5 boats
    through_the_locke(8, 'small')

    # this call will try to send 12 boats through the large locke but fail
    # because the large locke only takes up to 10 boats
    through_the_locke(12, 'large')

    # this call will send 8 boats through the large locke
    through_the_locke(8, 'large')

    # this call shows how error handling works when an error is raised within
    # the context
    through_the_locke_with_error(3, 'small')


if __name__ == "__main__":
    main()

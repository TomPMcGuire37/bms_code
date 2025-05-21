import itertools
import threading
import time
import sys


#here is the animation
def animate():
    for c in itertools.cycle(["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]):
        if done:
            print('\n')
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     \n')

done = False
t = threading.Thread(target=animate)
t.daemon = True
t.start()

#long process here
time.sleep(5)
done = True

import sys, time, threading

 # Here is an example of the process function:
def the_process_function():
    n = 20
    for i in range(n):
        time.sleep(1)
        sys.stdout.write('\r'+'loading...  process '+str(i)+'/'+str(n)+' '+ '{:.2f}'.format(i/n*100)+'%')
        sys.stdout.flush()
    sys.stdout.write('\r'+'loading... finished               \n')

def animated_loading():
    chars = "/—\|" 
    for char in chars:
        sys.stdout.write('\r'+'loading...'+char)
        time.sleep(.1)
        sys.stdout.flush() 

the_process = threading.Thread(name='process', target=the_process_function)
the_process.start()
while the_process.is_alive():
    animated_loading()


from sys import stdout as terminal
from time import sleep
from itertools import cycle
from threading import Thread

done = False

def animate():
    for c in cycle(['|', '/', '-', '\\']):
        if done:
            break
        terminal.write('\rloading ' + c)
        terminal.flush()
        sleep(0.1)
    terminal.write('\rDone!    ' + '\n')
    terminal.flush()

t = Thread(target=animate)
t.start()
sleep(5)
done = True


from sys import stdout as terminal
from time import sleep
from itertools import cycle
from threading import Thread


def loading_animation(running_text: str = "Running", finished_text: str = "Done!"):

    diff = len(running_text) - len(finished_text) + 2
    spaces = " " * diff if diff > 0 else ""

    def wrapper(f):
        def wrapped(*args, **kwargs):
            done = False

            def animation():
                for c in cycle(['|', '/', '-', '\\']):
                    if done:
                        break
                    terminal.write(f'\r{running_text} ' + c)
                    terminal.flush()
                    sleep(0.1)
                terminal.write(f'\r{finished_text}' + spaces + "\n")
                terminal.flush()

            t = Thread(target=animation)
            t.start()

            result = f(*args, **kwargs)
            done = True
            t.join()
            return result
        return wrapped
    return wrapper


  # Usage examples
if __name__ == "__main__":

    @loading_animation()
    def test_function3(time: int):
        sleep(time)
    
    # Custom text
    @loading_animation("Sleeping", "Had a good nap")
    def test_function(time: int):
        sleep(time)
        
    # Default text
    @loading_animation()
    def test_function2(time: int):
        sleep(time)

    test_function(3)
    test_function2(3)
    test_function3(3)

test_function(2)
test_function2(2)
test_function3(3)

list1 = [1,2,3,4,5,6]
list2 = list1[:4]
print(list2)

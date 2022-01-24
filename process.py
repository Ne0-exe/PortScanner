import os
global timer_count
global progress



def timer(port):
    # print("hi", port)
    global progress
    progress = 10
    a = 655
    global timer_count
    if int(port) < a:
        timer_count = 655
        progress = 10
    elif int(port) == timer_count:
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()
        isa = timer_count // 655
        print('Processing... ', int(isa), '%', sep='')
        print('#' * int(isa))
        timer_count += a
        progress += 10

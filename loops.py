def for_loops():
    # for num in range(10):
    #     print(num)
    for num in range(1, 10, 3):
        print(num)


def while_loops():
    names = ['sam', 'max', 'jon', 'jim', 'bob']
    i = 0
    while i < len(names):
        print(names[i])
        i += 1


def loops():
    #for_loops()
    while_loops()


if __name__ == '__main__':
    # invoke the modules' main function
    loops()
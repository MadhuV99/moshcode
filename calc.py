

def add():
    num1 = float(input('First: '))
    num2 = float(input('Second: '))
    tot = num1 + num2
    print(f'Total: {tot}')


def calc():
    add()


if __name__ == '__main__':
    # invoke the modules' main function
    calc()
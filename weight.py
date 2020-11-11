def show_other(weight, unit):
    print(unit, weight)


def get_other_weight(given_weight, given_unit):
    other_unit = 'Weight in Kg: '
    conversion_factor = 0.453592
    if given_unit != 'L':
        other_unit300 = 'Weight in lb: '
        conversion_factor = 1 / conversion_factor
    other_weight = given_weight * conversion_factor
    return other_weight, other_unit


def get_unit():
    #unit = 'L'
    #unit = 'K'
    unit = input('(K)g or (l)bs: ')[0].upper()
    return unit


def get_weight():
    #weight = 170
    #weight = 77
    weight = int(float(input('Weight: ')))
    return weight


def weight():
    given_weight = get_weight()
    given_unit = get_unit()
    other_weight, other_unit = get_other_weight(given_weight, given_unit)

    show_other(other_weight, other_unit)


if __name__ == '__main__':
    # invoke the modules' main function
    weight()
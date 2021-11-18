def nums(num_1=int(input('Enter num: ')), num_2=int(input('Enter second num: '))):
    try:
        res = num_1 / num_2
    except ZeroDivisionError:
        res = 0
    print(res)
    return res

nums()
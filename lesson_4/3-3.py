def my_func(num_1, num_2, num_3):
    small = min(num_1, num_2, num_3)
    res = (num_1 + num_2 + num_3) - small
    print(res)
    return res

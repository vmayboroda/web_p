def pow(n, pow):
    res = 1
    i = 1
    if pow == 0:
        return res
    elif pow > 0:
        for i in range(pow):
            res *= n
            i += 1
        return res
print(pow(2, 5))
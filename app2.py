def getNthFib(n, calculated={1: 0, 2: 1}):
    if n in calculated:
        return calculated[n]

    calculated[n] = getNthFib(n - 1, calculated) + getNthFib(n - 2, calculated)

    return calculated[n]


print(getNthFib(7))

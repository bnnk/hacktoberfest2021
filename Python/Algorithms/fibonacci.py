def fibs(fiblength = 10):
    x = 0
    y = 1
    z = x+y
    fibs = [x, y, z]
    for i in range(fiblength):
        x = y
        y = z
        z = x + y
        fibs.append(z)
    return fibs
ages = [5, 12, 17, 18, 24, 32]

def myfun(x):
    if x < 18:
        return False
    else:
        return True

adults = filter(myfun, ages)

for x in adults:
    print(x)
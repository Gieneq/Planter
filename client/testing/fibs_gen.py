def genFibs(count=-1):
    val = [1,1]
    yield val[0]
    yield val[1]
    while count <= -1 or count > 2:
        val = val[1:] + [sum(val)]
        yield val[1]
        count -= 1

for fin in genFibs(11):
    print(fin)


arr = [*genFibs(11)]
print(arr)
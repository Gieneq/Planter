c = 12

def dosth():
    c = 6
    def meh():
        global c # comment to toggle value
        print(c)
    return meh
dosth()()

nam = 'GLOB'

def doelse():
    nam = 'OUTER'
    def namer():
        # global nam
        nonlocal nam
        nam = 'INNER'
    namer()
    return nam

print('OUTER is', doelse())
print('GLOB is', nam)
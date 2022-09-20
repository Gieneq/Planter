

class Palindrom():
    def __init__(self, word):
        self.word = word

    def print(self):
        print(self.word)

    def rev(self):
        print([s for s in dir('') if 'is' in s])
        print(list(filter(lambda x: 'is' in x, dir(''))))
        print(self.word.lower())

    def check(self):
        return self.word.lower() == self.word[::-1].lower()



pal = Palindrom('Racecar')
pal.print()
pal.rev()
print(pal.check())

a = [3,1,2]
a.sort(reverse=True)
print(a)
print(sorted(a, key= lambda x: 1/x, reverse=False))
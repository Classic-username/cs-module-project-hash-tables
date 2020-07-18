"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""
import random

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here


cache1 = {}
cache2 = {}

for i in range(0, len(q)):
    for j in range(0, len(q)):
        cache1[f'f({q[i]}) + f({q[j]})'] = f(q[i]) + f(q[j])
        cache2[f'f({q[j]}) - f({q[i]})'] = f(q[j]) - f(q[i])

for fromAdd in cache1:
    for fromSub in cache2:
        if cache2[fromSub] == cache1[fromAdd]:
            print(f'{fromAdd} = {fromSub} = {cache1[fromAdd]}')




# a = random.choice(s)
# b = random.choice(s)
# c = random.choice(s)
# d = random.choice(s)


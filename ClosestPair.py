import math
import pandas as pd
from collections import defaultdict

class Person:

    def __init__(self, id, name, a, b, d, c, e, f, g, h, i):
        self.id = id
        self.name = name
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i

    def get_position(self):
        position = []
        for val in vars(self).values():
            position.append(val)
        return position

def distance(person1, person2):
    p1 = person1.get_position()
    p2 = person2.get_position()

    dist = 0
    for i in range(2, len(p1)):
        dist += (p1[i] - p2[i]) ** 2
    
    return math.sqrt(dist)



Users = []

df = pd.read_excel(r'data.xlsx')
for index, row in df.iterrows():
    person = Person(index,
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                        row[9])
    Users.append(person)

# Add user objects here

edges = []

# Form complete graph here

for i in range(len(Users)):
    for j in range(len(Users)):
        if i == j:
            continue
        edge = [distance(Users[i], Users[j]), Users[i].id, Users[j].id]
        edges.append(edge)

edges.sort()

#Print Closest Pair
print(Users[edges[0][1]].name + " and " + Users[edges[0][2]].name)
from players import Player


lst = [1, 2]
print(sum(lst))
dic = {11:["Hearts"]}

if sum(lst) > 2:
    print("Ok")

RED = list(range(1, 10, 2)) + list(range(12, 19, 2)) + list(range(19, 28, 2)) + list(range(30, 37, 2))          #RED
BLACK = list(range(2, 11, 2)) + list(range(11, 18, 2)) + list(range(20, 29, 2)) + list(range(29, 36, 2))          #BLACK

print(RED)
print(BLACK)
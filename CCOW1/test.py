from typing import NamedTuple

print("asdas")
a = 0
string = "asd"
numbers = [1,3,5, "sajt"]
#@dataclass
class Person(NamedTuple):
    age: int
    name: str 
p1 = Person(21, "mark")
print(p1)
print(numbers)

while a < 10:
    a += 1
    print(a)
print("")
for i in numbers:
    print(i)

def myfunc(a):
    print(a)

myfunc("béla")
print(numbers[3])
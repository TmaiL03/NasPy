# races = ["ex", "pts", "pts", "pts", "ex", "pts", "pts", "pts", "ex", "pts"]
# occurrence = 4
# instances = 0

# for race in range(len(races)):

#     if races[race] == "pts":
#         instances += 1
#     else:
#         pass

#     if instances == occurrence:
#         print(f"The {occurrence} occurrence of \"pts\" is at position {race + 1}.")
#         break

# For testing filter function for eventual pitstops.filter().
def testFunction(data: list, **filters):
    filteredDataList = []
    
    for obj in data:
        if all(getattr(obj, key, None) == value for key, value in filters.items()):
            filteredDataList.append(obj)

    return filteredDataList

class Person:
    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city
    
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, city={self.city})"

people = [
    Person("Alice", 30, "New York"),
    Person("Bob", 25, "Los Angeles"),
    Person("Charlie", 30, "New York"),
    Person("Diana", 40, "Chicago")
]

results = testFunction(people, age=30, city="New York")

print(results)
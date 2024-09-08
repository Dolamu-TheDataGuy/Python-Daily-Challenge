from dataclasses import dataclass

# class Person:
#     def __init__(self, name: str, age: int) -> None:
#         self._name = name
#         self._age = age


@dataclass        
class Person:
    name: str
    age: int


def main() -> None:
    person = Person("Dolamu", 27)
    print(person.name)
    print(person.age)
    person.name = "Damilola"
    person.age = 25
    print(person.name)
    print(person.age)
    


#     def get_name(self) -> str:
#         return self._name

#     def set_name(self, name: str) -> None:
#         self._name = name

#     def get_age(self) -> int:
#         return self._age

#     def set_age(self, age: int) -> None:
#         self._age = age


# def main() -> None:
#     person = Person("Dolamu", 27)
#     print(person.get_name())
#     print(person.get_age())
#     person.set_name("Damilola")
#     person.set_age(25)
#     print(person.get_name())
#     print(person.get_age())


if __name__ == "__main__":
    main()

from abc import ABCMeta, abstractmethod

# Interface
class Doggy(metaclass=ABCMeta):
    def __init__(self, age: int, breed: str) -> None:
        pass

    @abstractmethod
    def walk(self) -> str:
        pass

    @abstractmethod
    def bark(self) -> str:
        pass

class DoggyImpl(Doggy):
    def __init__(self, age: int, breed: str) -> None:
        self.age = age
        self.breed = breed

    def walk(self) -> str:
        return "My doggo is walking"

    def bark(self) -> str:
        return "My doggo is barking"

    def run(self) -> str:
        return "My doggo is running"

if __name__ == '__main__':
    print(DoggyImpl(12, "Pinscher").run())
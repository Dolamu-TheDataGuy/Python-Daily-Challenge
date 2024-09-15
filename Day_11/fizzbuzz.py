
def fizz_buzz() -> None:
    for i in range(1, 101):
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)
            
def main():
    fizz_buzz()


if __name__ == "__main__":
    main()
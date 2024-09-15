"""
A program to check if a number is prime or not
"""

def is_prime(num: int) -> bool:
    if num == 1 or num == 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def main() -> None:
    print(is_prime(2))
    print(is_prime(3))
    print(is_prime(5))
    print(is_prime(8))
    print(is_prime(75))
    print(is_prime(71))
    
if __name__ == "__main__":
    main()

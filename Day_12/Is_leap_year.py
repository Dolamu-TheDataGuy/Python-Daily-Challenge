"""
Write a program that checks if a year is a leap year or not
"""


def is_leap_year(year: int) -> bool:
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def main() -> None:
    print(is_leap_year(2000))
    
if __name__  == "__main__":
    main()
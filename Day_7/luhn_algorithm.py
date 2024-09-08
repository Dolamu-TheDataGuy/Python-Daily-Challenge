"""
Function that solves the Luhn algorithm

Details about algorithm -> https://www.geeksforgeeks.org/luhn-algorithm/
"""


def check_luhn(card_no: str) -> bool:
    nums = [int(digit) for digit in card_no]
    # print(nums)

    odd_digits = nums[-1::-2]
    # print(odd_digits)

    even_digit = nums[-2::-2]
    # print(even_digit)

    doubled_even_digit = [str(i*2) for i in even_digit]
    # print(doubled_even_digit)

    flat_even_digit = []
    for i in doubled_even_digit:
        if len(i) > 1:
            Sum = 0
            for b in i:
                Sum += int(b)
            flat_even_digit.append(Sum)
        else:
            flat_even_digit.append(int(i))
    # print(flat_even_digit)
    
    check_sum = sum(flat_even_digit) + sum(odd_digits)
    return check_sum % 10 == 0



def main():
    if (check_luhn('79927398713')):
        print("This is a valid card")
    else:
        print("This is not a valid card")

if __name__ == "__main__":
    main()

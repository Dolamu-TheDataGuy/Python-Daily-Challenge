def calculate_love_score(name1, name2):
    num1 = 0
    num2 = 0
    for i in name1:
        for b in "TRUE":
            if i.lower() == b.lower():
                num1 += 1

        for c in "LOVE":
            if i.lower() == c.lower():
                num2 += 1

    for i in name2:
        for b in "TRUE":
            if i.lower() == b.lower():
                num1 += 1

        for c in "LOVE":
            if i.lower() == c.lower():
                num2 += 1

    print(str(num1) + str(num2))
    
    
def main() -> None:   
    calculate_love_score("Kanye West", "Kim Kardashian")
    
if __name__ == "__main__":
    main()

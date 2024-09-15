""""
Get maximum score from scores of student
"""

students_scores = [150, 142, 185, 120,171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86]


def get_max() -> int:
    highest = 0
    for score in students_scores:
        if score > highest:
            highest = score
    return highest


def main() -> None:
    print(get_max())

if __name__ == "__main__":
    main()
    
        

"""
Given a coordinate string with value in degree, minute, and seconds, convert it to decimals degree
by calling a function.
"""

def dms_to_decimal(degree: int, minutes: int | float, seconds: int | float) -> float:
    if degree < 0:
        result = degree - minutes/60 - seconds/3600
    else:
        result = degree + minutes / 60 + seconds / 3600
    return result

coordinate = '''37* 46' 26.2992"'''
splitted_coordinate = coordinate.split()
deg = int(splitted_coordinate[0][:-1])
min = float(splitted_coordinate[1][:-1])
sec = float(splitted_coordinate[-1][:-1])

print(dms_to_decimal(deg, min, sec))

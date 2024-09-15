List_1 = []
List_2 = []
file = ["file1.txt", "file2.txt"]
num = 1
for content in file:
    with open(content, "r") as f:
        # num += 1
        for line in f:
            if num == 1:
                List_1.append(line.strip())
            elif num == 2:
                List_2.append(line.strip())
    num += 1

# print(List_1)
# print(List_2)


result = [int(a) for a in List_1 if a in List_2]
print(result)

numbers = [10, 20, 30, 40, 50]
num = int(input("Which number do you want to find? "))
index = -1

for i in range (len(numbers)):
    if numbers[i] == num:
        index = i
        break

if index == -1:
    print("Number not found")
else:
    print(f"Number found at index {index}")
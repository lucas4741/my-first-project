numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
target = int(input("What number are you looking for? "))
low = 0
high = len(numbers) - 1
mid = (low + high) // 2
found = False

while low <= high:
    if numbers[mid] == target:
        found = True
        break
    elif numbers[mid] < target:
        low = mid + 1
        mid = (low + high) // 2
    else:
        high = mid - 1
        mid = (low + high) // 2

if found:
    print(f"Your number was found at index {mid}")
else:
    print("Your number was not found")
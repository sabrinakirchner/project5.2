value = []
while True:
    num = input("Enter a number: ")
    if num == "done":
        break

    try:
        val = int(num)
        value.append(val)
    except:
        print("Invalid input")
        continue
low = min(value)
high = max(value)

print("Maximum is", high)
print("Minimum is", low)

######################
numbers = range(1, 100)
substring = "7"
count = 0
for a in numbers:
    print(a)
    if a % 7 == 0:
        print('Boom')
        count += 1
    if substring in str(a):
        print('Boom1')
        count += 1
print(f"count:{count}")
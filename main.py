list = []
while True:
    num = input("Введіть числ або stop: ")
    if num == 'stop':
        break
    else:
        list.append(int(num))

even_count = 0
for num in list:
    if num % 2 == 0:
        even_count += 1
print(list)
print(sum(list))
print(even_count)

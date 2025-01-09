# Laboratory 1

# Task 1

name = input("Введите имя: ")
surname = input("Введите фамилию: ")
prof = input("Введите профессию: ")

print('\n============================',
      f'Имя: {name}',
      f'Фамилия: {surname}',
      f'Профессия: {prof}',
      f'\n============================',
      sep='\n',  # разделитель между полями
      end='\n')  # символы в конце вывода


# Task 2

min = -1
while not(0 < min <= 10**7):
    min = int(input("Введите кол-во минут: "))

hour = min // 60
hourFin = hour

if hour > 23:
    hourFin %= 23

minFin = min - hour * 60
print(hourFin, minFin)


# Task 3

num = input('Введите трёхзначное число: ')

print(int(num[0]) + int(num[1]) + int(num[2]))


# Task 4

n = int(input("Введите кол-во секунд: "))

hour = (n // 3600) % 24
min = (n // 60) % 60
secFin = n % 60
print(f'{hour}:{min:02}:{secFin:02}')


# Task 5

n = int(input("Введите целое число, не превышающее 1000: "))
n += 1
print(n + (n % 2))


# Task 6

n = float(input("Введите начальную точку: "))
m = float(input("Введите конечную точку: "))

print(abs(n) + abs(m))


# Task 7

n = input("Введите 4 числа через пробел: ")
n = n.split(" ")
s = 0
count = 0

for i in n:
    s += int(i)
    count += 1
print(s/count)

# Task 8

n = int(input("Введите кол-во человек: "))

if n % 4 == 0:
    print(int(n / 4))
else:
    print(int(n // 4 + 1))


# Task 9

n = input("Введите разделитель: ")
m = '1'

for i in range(2, 6):
    m += n + str(i)

print(m)





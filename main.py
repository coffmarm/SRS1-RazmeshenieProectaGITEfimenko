filename = input("Введите имя файла: ")
n = int(input("Введите количество строк для вывода: "))

with open(filename, 'r') as file:
    lines = file.readlines()
    for line in reversed(lines[-n:]):
        print(line.strip())
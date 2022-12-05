number = int(input('Введите до какого числа нужны кубы чисел: '))
point = 1
while point < number:
  cube = point ** 3
  point += 1
  print('у числа:', point - 1, 'третья степень - ', cube)
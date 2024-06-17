def sum_range(start, end):
  # Инициализируем переменную для хранения суммы
  total = 0
  str_ = ''

  # Проходим по всем целым числам от start до end
  for i in range(start, end + 1):
      # Добавляем текущее число к общей сумме
      total += i
      str_ += str(i) + (' + ' if i != end else ' = ' + str(total))

  # Возвращаем общую сумму
  return total, str_

# Пример использования функции
result, str_ = sum_range(1, 10)
print(str_)
def bank(a, years):
  # Инициализируем переменную для хранения суммы
  total = a
  # Проходим по всем годам
  for i in range(years):
      # Увеличиваем сумму на 10%
      total += total * 0.1
  # Возвращаем общую сумму
  return round(total,2)

# Пример использования функции
print(bank(1000, 50))
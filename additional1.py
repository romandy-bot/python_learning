# Удаление одинаковых объектов

# Есть список словарей, в которых одно из значений используется в качестве идентификатора:
# Элементы с повторяющимся идентификатором полностью идентичны и их повторы следует удалить
# Требуется получить ту же структуру данных, но без повторов?

data = [
  {'id': 10, 'data': '...'},
  {'id': 11, 'data': '...'},
  {'id': 12, 'data': '...'},
  {'id': 10, 'data': '...'},
  {'id': 11, 'data': '...'},
]

# Решение
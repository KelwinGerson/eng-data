# double = lambda x: x * 2
# print(double(5))

# students = [{'name': 'Michael', 'age': 37}, {'name': 'John', 'age': 30}, {'name': 'David', 'age': 27}]
# sorted_students = sorted(students, key=lambda student: student['age'])
# print(sorted_students)

sales_data = [
    {"product": "Product A", "price": 20, "quantity": 100},
    {"product": "Product B", "price": 15, "quantity": 150},
    {"product": "Product A", "price": 20, "quantity": 50},
    {"product": "Product C", "price": 30, "quantity": 75},
]

# Função de cálculo de total usando lambda
calculate_total = lambda item: {"product": item["product"], "total": item["price"] * item["quantity"]}

# Calculando o total de vendas para cada produto usando a lambda em uma operação de mapeamento, 
# a operação map é usada para aplicar uma função a cada elemento de um conjunto de dados
totals = list(map(calculate_total, sales_data))

for item in totals:
    print(f"Product: {item['product']}, Total Sales: {item['total']}")

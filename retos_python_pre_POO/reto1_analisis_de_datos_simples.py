"""
Tienes una lista de registros de ventas.
Cada registro es una tupla con:

(usuario, producto, monto)

Objetivos (todos obligatorios)
    -Crear un diccionario donde cada usuario tenga:
        - total gastado
        - número de compras
    -Obtener una lista con los usuarios que gastaron más de 500, ordenada alfabéticamente.
    -Calcular el promedio de gasto por compra de cada usuario.

Restricciones:
    -NO usar POO
    -NO usar librerías externas
    -NO usar defaultdict (todavía)
    -Usa for
    -Usa diccionarios
    -Usa buenas prácticas
    -Código claro > código corto
    -Si usas lambda, debe tener sentido
"""

sales = [
    ("Ana", "Laptop", 1200),
    ("Luis", "Mouse", 25),
    ("Ana", "Teclado", 80),
    ("Pedro", "Monitor", 300),
    ("Luis", "Laptop", 1200),
    ("Ana", "Mouse", 25),
    ("Pedro", "Mouse", 25),
]

def group_sales(sales_data):
    """
    Analiza las ventas y 
    crea un diccionario con el total gastado y 
    el numero de compras creadas por usuario.
    """
    grouped = {}

    for user, _, amount in sales_data:
        if user not in grouped:
            grouped[user] = {"total": 0, "count": 0}

        grouped[user]["total"] += amount
        grouped[user]["count"] += 1

    return grouped


def get_high_spenders(grouped_data, threshold=500):
    """
    A partir de un diccionario crea una lista donde
    almacena a los usuarios que gastaron mas de 500
    """
    return sorted(
        user for user, data in grouped_data.items()
        if data["total"] > threshold
    )


def calculate_averages(grouped_data):
    """
    Calcula el promedio de gasto por compra de cada usuario
    de un diccionario de datos
    """
    return {
        user: round(data["total"] / data["count"], 2)
        for user, data in grouped_data.items()
    }

grouped = group_sales(sales)
high_spenders = get_high_spenders(grouped)
averages = calculate_averages(grouped)

print(f"{grouped}\n {high_spenders}\n {averages}")

"""
Tienes registros de accesos a un sistema.
Cada registro indica:
    - usuario
    -tipo de acción

Tu objetivo es:
    - Contar cuántas veces cada usuario realizó cada acción.
    - Detectar usuarios sospechosos, definidos como aquellos que:
        -hicieron login más de 2 veces
        -nunca hicieron logout
"""

access_logs = [
    ("Ana", "login"),
    ("Luis", "login"),
    ("Ana", "login"),
    ("Ana", "logout"),
    ("Luis", "login"),
    ("Pedro", "login"),
    ("Pedro", "login"),
    ("Pedro", "login"),
    ("Maria", "login"),
]

def actions_counter_per_user(logs):
    """
    Cuentas cuantas veces los usuario hicieron login y logout
    """
    counter = {}

    for user, action in logs:

        if user not in counter:
            counter[user] = {}

        counter[user][action] = counter[user].get(action, 0) + 1

    return counter

def find_suspicious_users(analized_logs):
    """
    Devuelve una lista con los usuarios sospechosos que hicieron login mas de 2 veces
    y nunca hicieron logout
    """
    return [

        user for user, data in analized_logs.items()
        if data.get("login", 0) > 2 and "logout" not in data
        ]

counter_data = actions_counter_per_user(access_logs)
suspicious_users = find_suspicious_users(counter_data)
print(counter_data)
print(suspicious_users)

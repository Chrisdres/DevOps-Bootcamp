import os

nombre = os.getenv("NOMBRE", "Mundo")

print(f"Hola, {nombre}!")
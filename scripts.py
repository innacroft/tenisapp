import csv
from django.db import IntegrityError
from your_app.models import Persona  # Reemplaza 'your_app' con el nombre de tu aplicación

# Ruta del archivo CSV
CSV_FILE = "datos.csv"

def load_csv_to_django():
    """Carga datos desde un archivo CSV a la base de datos de Django."""
    with open(CSV_FILE, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                Persona.objects.create(
                    nombre=row["nomber"],
                    apellido=row["apellido"],
                    edad=row["edad"],
                    identificacion=row["identificacion"],
                    categoria=row["categoria"]
                )
            except IntegrityError:
                print(f"Registro duplicado: {row['identificacion']}")

if __name__ == "__main__":
    load_csv_to_django()
    print("Datos cargados correctamente.")

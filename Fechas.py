from datetime import datetime, timedelta

def manejo_fechas():
    # Obtener la fecha y hora actual
    ahora = datetime.now()
    print(f"Fecha y hora actual: {ahora}")

    # Formatear la fecha
    print(f"Fecha formateada (DD/MM/YYYY): {ahora.strftime('%d/%m/%Y')}")
    print(f"Hora formateada (HH:MM:SS): {ahora.strftime('%H:%M:%S')}")

    # Crear una fecha específica
    fecha_especifica = datetime(2023, 12, 25)
    print(f"Fecha específica: {fecha_especifica.strftime('%d/%m/%Y')}")

    # Calcular la diferencia entre fechas
    diferencia = fecha_especifica - ahora
    print(f"Días hasta Navidad: {diferencia.days}")

    # Sumar y restar días a una fecha
    suma_dias = ahora + timedelta(days=10)
    resta_dias = ahora - timedelta(days=10)
    print(f"Fecha después de 10 días: {suma_dias.strftime('%d/%m/%Y')}")
    print(f"Fecha hace 10 días: {resta_dias.strftime('%d/%m/%Y')}")

    # Obtener solo la fecha o la hora
    print(f"Solo la fecha: {ahora.date()}")
    print(f"Solo la hora: {ahora.time()}")

# Llamar a la función
if __name__ == "__main__":
    manejo_fechas()
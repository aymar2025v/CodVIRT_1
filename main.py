import matplotlib.pyplot as plt
import pandas as pd

# 1. Crear un Diccionario con datos simulados de ventas
datos_ventas = {
    "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
    "Ventas_USD": [1200, 1800, 2100, 1700, 2600, 3100],
}

# 2. Convertir el diccionario en un DataFrame de Pandas
df = pd.DataFrame(datos_ventas)

# 3. Mostrar los datos tabulados en la terminal
print("--- Tabla de Datos (Pandas Dataframe) ---")
print(df)
print("\nEstadísticas básicas de las ventas:")
print(df.describe())

# 4. Crear un gráfico de líneas usando Matplotlib
plt.figure(figsize=(8, 4))  # Tamaño de la ventana del gráfico
plt.plot(
    df["Mes"],
    df["Ventas_USD"],
    marker="o",
    color="darkgreen",
    linewidth=2,
    label="Ventas",
)

# 5. Personalizar el diseño del gráfico
plt.title("Evolución de Ventas - Primer Semestre", fontsize=14, fontweight="bold")
plt.xlabel("Meses del Año", fontsize=11)
plt.ylabel("Ganancias (en USD)", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.6)  # Cuadrícula de fondo
plt.legend()

# 6. Mostrar el gráfico en pantalla
print("\n[INFO] Generando gráfico en ventana flotante...")
plt.show()

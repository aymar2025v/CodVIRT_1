import matplotlib.pyplot as plt
import pandas as pd

# 1. CARGAR EL ARCHIVO CSV REAL
try:
    df = pd.read_csv("datos.csv")
except FileNotFoundError:
    print("Error: No se encontró 'datos.csv'.")
    exit()

# 2. PROCESAR LOS DATOS (Agrupación y promedio)
promedios = df.groupby("Materia")["Nota"].mean()

# 3. CREAR EL GRÁFICO DE BARRAS
plt.figure(figsize=(7, 5))
plt.bar(
    promedios.index,
    promedios.values,
    color=["#4A90E2", "#50E3C2"],
    edgecolor="black",
    width=0.5,
)

# 4. PERSONALIZAR EL DISEÑO
plt.title("Nota Promedio por Materia", fontsize=14, fontweight="bold", pad=15)
plt.xlabel("Materias", fontsize=12, labelpad=10)
plt.ylabel("Rendimiento Promedio (Puntos)", fontsize=12, labelpad=10)
plt.ylim(0, 100)
plt.grid(axis="y", linestyle="--", alpha=0.7)

for i, v in enumerate(promedios.values):
    plt.text(i, v + 2, f"{v:.1f}", ha="center", fontweight="bold", fontsize=11)

# 5. GUARDAR EL GRÁFICO COMO IMAGEN (NUEVO PASO)
# dpi=300 asegura una excelente resolución y bbox_inches='tight' evita que se corten las etiquetas
nombre_imagen = "reporte_promedios.png"
plt.savefig(nombre_imagen, dpi=300, bbox_inches="tight")
print(f"¡Éxito! Gráfico guardado en tu carpeta como: '{nombre_imagen}'")

# 6. MOSTRAR EL GRÁFICO EN PANTALLA
plt.show()

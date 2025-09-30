import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Leer datos desde el archivo
    df = pd.read_csv('epa-sea-level.csv')
    
    # Crear gráfico de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.6, label='Datos observados')
    
    # Línea de mejor ajuste 1: Usando todos los datos (1880-2013)
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Extender la línea hasta 2050
    years_extended1 = np.arange(1880, 2051)
    sea_levels_predicted1 = slope1 * years_extended1 + intercept1
    
    plt.plot(years_extended1, sea_levels_predicted1, 'r', label='Línea de mejor ajuste (1880-2013)')
    
    # Línea de mejor ajuste 2: Usando solo datos desde 2000
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Extender la línea hasta 2050
    years_extended2 = np.arange(2000, 2051)
    sea_levels_predicted2 = slope2 * years_extended2 + intercept2
    
    plt.plot(years_extended2, sea_levels_predicted2, 'g', label='Línea de mejor ajuste (2000-2013)')
    
    # Configurar etiquetas y título
    plt.xlabel('Año')
    plt.ylabel('Nivel del Mar (pulgadas)')
    plt.title('Aumento del Nivel del Mar')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Guardar y mostrar el gráfico
    plt.savefig('sea_level_plot.png')
    return plt.gcf()

# Para probar la función
if __name__ == "__main__":
    draw_plot()
    plt.show()

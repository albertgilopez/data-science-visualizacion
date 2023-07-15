print("********************************************")
print("VISUALIZACIÓN CON PYTHON PARA DATA SCIENCE I")
print("********************************************")

print("***********************")
print("MATPLOTLIB - EJERCICIOS")
print("***********************")

import pandas as pd
import numpy as np
import seaborn as sns

# Como datos para trabajar usaremos unos vectores de numpy

np.random.seed(1234)
enteros = np.random.randint(1,10,1000)
reales = np.random.rand(1000)
coches = np.random.choice(['Seat','Ford','BMW','Renault','Mercedes'], size = 1000, replace = True)

# Y un dataframe de Pandas
df = sns.load_dataset('tips')
df.head()

# Importa matplotlib como plt, y añade el código para que los gráficos salgan dentro de Jupyter.

import matplotlib.pyplot as plt
# %matplotlib inline

# Crea un gráfico de líneas de color rojo utilizando "reales" con el titulo "Grafico de lineas rojo"  con una escala y de 0 a 1 y una escala x de 0 a 1000

plt.plot(reales, color='red')
plt.ylim(0, 1)
plt.xlim(0, 1000)
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.title('Gráfico de líneas rojo')
plt.show()

# Crea un gráfico de barra utilizando "coches". Notar que el eje y ha sido ajustado entre 150 y 250.

# Calcular la frecuencia de cada marca de coche
unique, counts = np.unique(coches, return_counts=True)

# Crear el gráfico de barras
plt.bar(unique, counts)

# Ajustar el eje y entre 150 y 250
plt.ylim(150, 250)

# Añadir etiquetas y título
plt.xlabel('Marca de coche')
plt.ylabel('Frecuencia')
plt.title('Frecuencia de marcas de coches')

# Mostrar el gráfico
plt.show()

# Crea un boxplot a partir de la variable "enteros" con el eje y con el valor 1 y el eje x de 1 a 9. Crea una linea vertical justo en la mitad

# Crear el boxplot
plt.boxplot(enteros, vert=False)

# Configurar el eje x y el eje y
plt.yticks([1], [''])
plt.xticks(np.arange(1, 10))

# Añadir una línea vertical en la mitad
plt.axvline(x=5, color='red', linestyle='--')

# Añadir etiquetas y título
plt.xlabel('Valores')
plt.title('Boxplot de enteros')

# Mostrar el gráfico
plt.show()

# Crea un gráfico pie con la variable "coches". Tienen que aparecer en el gráfico el texto de las marcas de los coches

# Crear el gráfico de tipo pie
plt.pie(counts, labels=unique, autopct='%1.1f%%')

# Añadir título
plt.title('Distribución de marcas de coches')

# Mostrar el gráfico
plt.show()

# Crea un grafico uperpuesto donde hay 2 ejes. Uno es el histograma de reales, y el otro el histograma acumuluado de reales.
# Pon el acumulado en azul y sin transparencia, y el no acumulado en rojo pero con transparencia al 0.3.
# Añade las leyendas y asegúrate de que estén en la misma zona que las de la solución.

# Crear los histogramas y obtener los valores
hist, bins = np.histogram(reales, bins=20)
cumulative = np.cumsum(hist)

# Crear la figura y los ejes
fig, ax = plt.subplots()

# Histograma acumulado (eje 2)
ax.hist(reales, bins=20, cumulative=True, color='blue', alpha=1)
ax.set_ylabel('Frecuencia Acumulada')

ax1 = ax.twinx()

# Histograma no acumulado (eje 1)
ax1.hist(reales, bins=20, color='red', alpha=0.3)
ax1.set_ylabel('Frecuencia')
ax1.set_xlabel('Valores')
ax1.set_title('Histograma de reales')

# Añadir leyendas
ax.legend(['Acumulado'], loc='upper right')
ax1.legend(['No acumulado'], loc='upper left')

# Mostrar el gráfico
plt.show()

# Crea un gráfico superpuesto donde hay 2 gráficos en la misma figura.
# El primero es un dispersión entre enteros y enteros al cuadrado, y con los puntos en verde.
# El segundo es un dispersión entre enteros y enteros al cubo, y con los puntos tamaño 100.

# Calcular los valores al cuadrado y al cubo
cuadrados = enteros ** 2
cubos = enteros ** 3

# Crear la figura y los ejes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Gráfico de dispersión de enteros y enteros al cuadrado (en verde)
ax1.scatter(enteros, cuadrados, color='green')
ax1.set_xlabel('Enteros')
ax1.set_ylabel('Enteros al cuadrado')
ax1.set_title('Enteros vs. Enteros al cuadrado')

# Gráfico de dispersión de enteros y enteros al cubo (con puntos de tamaño 100)
ax2.scatter(enteros, cubos, color='blue', s=100)
ax2.set_xlabel('Enteros')
ax2.set_ylabel('Enteros al cubo')
ax2.set_title('Enteros vs. Enteros al cubo')

# Ajustar la disposición de los subgráficos
plt.tight_layout()

# Mostrar la figura
plt.show()

# Ahora vamos a trabajar con el df de Pandas

print(df)

# Crea un gráfico de barras de la variable smoker como el de la solución.

# Contar la frecuencia de cada categoría en "smoker"
smoker_counts = df['smoker'].value_counts()

# Crear el gráfico de barras
plt.bar(smoker_counts.index, smoker_counts.values)

# Configurar etiquetas y título
plt.xlabel('Smoker')
plt.ylabel('Frecuencia')
plt.title('Frecuencia de fumadores')

# Mostrar el gráfico
plt.show()

# Crea un gráfico de barras de la variable day, pero poniendo las etiquetas del eje x a tamaño 16 y rotandolas 90 grados.

# Contar la frecuencia de cada categoría en "day"
day_counts = df['day'].value_counts()

# Crear el gráfico de barras
plt.bar(day_counts.index, day_counts.values)

# Configurar etiquetas y título
plt.xlabel('Day', fontsize=16)
plt.ylabel('Frequency')
plt.title('Frequency of Days')

# Rotar las etiquetas del eje x
plt.xticks(rotation=90)

# Mostrar el gráfico
plt.show()

# Representa en el mismo gráfico de líneas el total de la factura y de las propinas en un gráfico que mida 16x6

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(16, 6))

# Graficar el total de la factura
ax.plot(df['total_bill'], color='blue', label='Total Bill')

# Graficar las propinas
ax.plot(df['tip'], color='green', label='Tips')

# Configurar etiquetas y título
ax.set_xlabel('Index')
ax.set_ylabel('Amount')
ax.set_title('Total Bill and Tips')

# Añadir leyendas
ax.legend()

# Mostrar el gráfico
plt.show()

# Con el mismo gráfico que antes restringe el eje x entre los valores 100 y 150 para ver un zoom.

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(16, 6))

# Graficar el total de la factura
ax.plot(df['total_bill'], color='blue', label='Total Bill')

# Graficar las propinas
ax.plot(df['tip'], color='green', label='Tips')

# Configurar etiquetas y título
ax.set_xlabel('Index')
ax.set_ylabel('Amount')
ax.set_title('Total Bill and Tips')

# Añadir leyendas
ax.legend()

# Restringir el eje x entre los valores 100 y 150
ax.set_xlim(100, 150)

# Mostrar el gráfico
plt.show()

# Con el mismo gráfico que antes haz que la línea del total de la factura sea punteada, y que la línea de las propinas sea 10 veces más gruesa.

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(16, 6))

# Graficar el total de la factura (línea punteada)
ax.plot(df['total_bill'], color='blue', linestyle='--', label='Total Bill')

# Graficar las propinas (línea más gruesa)
ax.plot(df['tip'], color='green', linewidth=10, label='Tips')

# Configurar etiquetas y título
ax.set_xlabel('Index')
ax.set_ylabel('Amount')
ax.set_title('Total Bill and Tips')

# Añadir leyendas
ax.legend()

# Mostrar el gráfico
plt.show()

# Haz un gráfico de dispersión para ver si hay relación entre el total de la factura y las propinas. Y haz que los puntos sean verdes.

# Crear el gráfico de dispersión
plt.scatter(df['total_bill'], df['tip'], color='green')

# Configurar etiquetas y título
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Total Bill vs. Tip')

# Mostrar el gráfico
plt.show()

# Sobre el gráfico anterior pon un color diferente a cada punto en función de si es hombre o mujer (usa la escala de colores 'spring').

# Crear el gráfico de dispersión con colores mapeados
plt.scatter(df['total_bill'], df['tip'], c=df['sex'].cat.codes, cmap='spring')

# Configurar etiquetas y título
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Total Bill vs. Tip')

# Mostrar el gráfico
plt.show()

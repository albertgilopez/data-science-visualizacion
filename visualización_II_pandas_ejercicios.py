print("*********************************************")
print("VISUALIZACIÓN CON PYTHON PARA DATA SCIENCE II")
print("*********************************************")

print("*******************")
print("PANDAS - EJERCICIOS")
print("*******************")

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# %matplotlib inline. Es para decirle cómo tiene que sacar los gráficos.
# En este caso significa que los saque como gráficos estáticos integrados en el propio notebook (de tal forma que se guarde y distribuya más fácilmente).

df = sns.load_dataset('tips')
df.head()

# Crea un gráfico de líneas sobre la variable total_bill.

plt.figure(figsize=(10, 6))
df['total_bill'].plot(kind='line')
plt.xlabel('Index')
plt.ylabel('Total Bill')
plt.title('Line Plot - Total Bill')
plt.show()

# Crea un solo gráfico de líneas donde representes las variables total_bill y tip.

plt.figure(figsize=(10, 6))
df['total_bill'].plot(kind='line', label='Total Bill')
df['tip'].plot(kind='line', label='Tip')
plt.xlabel('Index')
plt.ylabel('Amount')
plt.title('Line Plot - Total Bill and Tip')
plt.legend()
plt.show()

# Crea el gráfico anterior pero de dos ejes, donde tip vaya en el eje secundario.

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.set_xlabel('Index')
ax1.set_ylabel('Total Bill')
ax1.plot(df.index, df['total_bill'], color='tab:red')
ax1.tick_params(axis='y')

ax2 = ax1.twinx()
ax2.set_ylabel('Tip')
ax2.plot(df.index, df['tip'], color='tab:blue')
ax2.tick_params(axis='y')

plt.title('Line Plot - Total Bill and Tip')
plt.show()

# Crea el gráfico anterior pero que total_bill salga en rojo y tip en negro.

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(df.index, df['total_bill'], color='red')

ax2 = ax1.twinx()
ax2.plot(df.index, df['tip'], color='black')

plt.show()

# Sobre el gráfico anterior ponle título y nombres a los ejes.

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.set_xlabel('Index')
ax1.set_ylabel('Total Bill', color='red')
ax1.plot(df.index, df['total_bill'], color='red')
ax1.tick_params(axis='y', labelcolor='red')

ax2 = ax1.twinx()
ax2.set_ylabel('Tip', color='black')
ax2.plot(df.index, df['tip'], color='black')

plt.title('Line Plot - Total Bill and Tip')
plt.xlabel('Index')
plt.ylabel('Amount')
plt.legend(['Total Bill', 'Tip'])
plt.show()

# Haz el gráfico anterior sin título ni nombres de los ejes, pero que ahora salga en dos gráficos distintos, uno para cada serie, y que cada uno mida 12 x 4.

fig, axes = plt.subplots(2, 1, figsize=(12, 4))

axes[0].plot(df.index, df['total_bill'], color='red')
axes[1].plot(df.index, df['tip'], color='black')

plt.tight_layout()
plt.show()

# Crea un gráfico de barras sobre la variable sexo.

plt.figure(figsize=(8, 6))
df['sex'].value_counts().plot(kind='bar')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.title('Bar Plot - Sex')
plt.show()

# Sobre el gráfico anterior gira las etiquetas del eje x para que estén en horizontal (nota, es posible que tengas que guardar el gráfico

plt.figure(figsize=(8, 6))
ax = df['sex'].value_counts().plot(kind='bar')

ax.set_xlabel('Sex')
ax.set_ylabel('Count')
ax.set_title('Bar Plot - Sex')
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)  # Rotación de etiquetas a 0 grados

plt.tight_layout()  # Ajustar el espaciado de los elementos del gráfico
plt.show()

# Haz un gráfico de barras sobre la variable day. Pero que esté en horizontal, con orden decreciente, que los datos estén en porcentajes en lugar de absolutos, que sea gris y que todas las letras del gráfico tengan un tamaño 16.

plt.figure(figsize=(8, 6))
ax = df['day'].value_counts(normalize=True).sort_values(ascending=False).plot(kind='barh', color='gray')

ax.set_xlabel('Percentage')
ax.set_ylabel('Day')
ax.set_title('Horizontal Bar Plot - Day')
ax.set_xticklabels(['{:.0%}'.format(x) for x in ax.get_xticks()], fontsize=16)
ax.set_yticklabels(ax.get_yticklabels(), fontsize=16)

plt.tight_layout()
plt.show()

# Ahora haz el mismo gráfico pero que aparezca ordenado por el orden natural de la variable day.

# Obtener el orden natural de la variable "day"
day_order = df['day'].unique()

plt.figure(figsize=(8, 6))
ax = df['day'].value_counts(normalize=True).loc[day_order].plot(kind='barh', color='gray')

ax.set_xlabel('Percentage')
ax.set_ylabel('Day')
ax.set_title('Horizontal Bar Plot - Day')
ax.set_xticklabels(['{:.0%}'.format(x) for x in ax.get_xticks()], fontsize=16)
ax.set_yticklabels(ax.get_yticklabels(), fontsize=16)

plt.tight_layout()
plt.show()

# Haz un gráfico de dispersión entre total_bill y tip, donde el tamaño del punto sea 50 y una transparencia del 40%

plt.figure(figsize=(8, 6))
plt.scatter(df['total_bill'], df['tip'], alpha=0.4, s=50)
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Scatter Plot - Total Bill vs Tip')
plt.show()

# Haz el mismo gráfico pero hexagonal, con tamaño de parrilla 15 y paleta de colores Pastel1 (nota: tendrás que quitar los parámetros s y alpha)

plt.figure(figsize=(8, 6))
plt.hexbin(df['total_bill'], df['tip'], gridsize=15, cmap='Pastel1')
plt.colorbar(label='Counts')
plt.xlabel('Total Bill')
plt.ylabel('Tip')
plt.title('Hexbin Plot - Total Bill vs Tip')
plt.show()

# Haz un histograma (con 50 tramos) sobre el total de la factura.

plt.figure(figsize=(8, 6))
df['total_bill'].plot(kind='hist', bins=50)
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.title('Histogram - Total Bill')
plt.show()

# Superpon en el mismo gráfico (usando transparencias) el histograma del total de la factura y de las propinas.

plt.figure(figsize=(8, 6))
df['total_bill'].plot(kind='hist', bins=50, alpha=0.5, label='Total Bill')
df['tip'].plot(kind='hist', bins=50, alpha=0.5, label='Tip')
plt.xlabel('Amount')
plt.ylabel('Frequency')
plt.title('Histogram - Total Bill and Tip')
plt.legend()
plt.show()

# Haz con una sola línea de código los histogramas de todas las variables cuantitativas del dataframe. Pero que cada una tenga su propia escala del eje X (nota: no va a funcionar)

plt.figure(figsize=(12, 8))

variables_cuantitativas = df.select_dtypes(include=['float64', 'int64']).columns

df[variables_cuantitativas].plot.hist(subplots=True, layout=(2, 2), figsize=(12, 8), sharex=False)

plt.tight_layout()
plt.show()

# Prueba a hacer lo mismo pero cambiando el histograma por un gráfico de densidad.
# NOTA: los histogramas no respetan el sharex = False, por tanto es bueno acordarse de que tenemos la opción de cambiarlos por gráficos de densidad.

variables_cuantitativas = df.select_dtypes(include=['float64', 'int64']).columns

plt.figure(figsize=(12, 8))
df[variables_cuantitativas].plot.kde(subplots=True, layout=(2, 2), figsize=(12, 8), sharex=False)

plt.tight_layout()
plt.show()

# Analiza con un boxplot la distribución de propinas comparándolas por día de la semana.

plt.figure(figsize=(8, 6))
sns.boxplot(data=df, x='day', y='tip')
plt.xlabel('Day of the Week')
plt.ylabel('Tip')
plt.title('Boxplot - Tip Distribution by Day of the Week')
plt.show()


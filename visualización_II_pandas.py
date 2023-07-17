print("*********************************************")
print("VISUALIZACIÓN CON PYTHON PARA DATA SCIENCE II")
print("*********************************************")

print("******")
print("PANDAS")
print("******")

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %matplotlib inline. Es para decirle cómo tiene que sacar los gráficos.
# En este caso significa que los saque como gráficos estáticos integrados en el propio notebook (de tal forma que se guarde y distribuya más fácilmente).

df = sns.load_dataset('tips')
print(df.head())

# En la mayoría de los trabajos de data science estaremos trabajando con data frames, y seguramente con Pandas, por eso la visualización en Pandas será la que usaremos más frecuentemente.

# Pandas se basa en Matplotlib pero con unos métodos propios implementados en sus Series y DataFrames que reducen el código y los pasos necesarios para hacer los gráficos.
# Además hace una configuración de opciones bastante decente por defecto. Y si queremos personalizarlo más podemos usar las opciones aprendidas en Matplotlib.
# Aunque realmente las opciones de personalización de Pandas son las menores de los 3 paquetes, así que si quieres hacer muy personalizado es mejor ir a Matplotlib o a Seaborn.

# Un truco que pasa a veces desapercibido es que simplemente con que Seaborn esté importado, aunque no usemos sus funciones, va a cambiar a mejor el aspecto de los gráficos que nos saca Pandas.

# CÓMO HACER UN GRÁFICO EN PANDAS

# Se hace con el método plot detrás del dataframe y la variable a representar. De nuevo hay dos maneras:

# - Usando .plot para cualquier tipo de gráfico, pero luego dentro usando el parámetro kind para especificar qué tipo de gráfico es
# - Usando .plot.tipo_grafico

# Podemos ver los diferentes tipos y todos los parámetros en la documentación: https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.DataFrame.plot.html

df.total_bill.plot(kind = 'hist'); # con la primera forma
plt.show()

df.total_bill.plot.hist(); # con la segunda forma
plt.show()

# COMO USAR TODAS LAS OPCIONES DE MATPLOTLIB EN PANDAS

# Hay diferentes opciones de usar lo aprendido en Matplotlib:

# - Pasar métodos de Matplolib como argumentos del método de Pandas
# - Guardar el gráfico en un objeto y usar lo aprendido sobre la API orientada a objetos de Matplotlib
# - Crear el gráfico de Pandas y luego ir añadiendo capas al gráfico con la API funcional de Matplotlib

# Pasar métodos de Matplolib como argumentos del método de Pandas
# Podemos usar la mayoría de las opciones que vimos en Matplotlib directamente dentro de estos métodos de Pandas a través de **kwds.

df.total_bill.plot.line(xlim = (0,100),
                        title = 'Este es el título',
                        xlabel = 'Este es el eje x',
                        figsize = (10,4), 
                        ls = '-.', 
                        linewidth = 3, 
                        color = 'red',
                        grid = True);

plt.show()

# Guardar el gráfico en un objeto y usar lo aprendido sobre la API orientada a objetos de Matplotlib¶

# Si guardamos un gráfico de Pandas en una variable realmente nos está devolviendo el objeto axes de Matplotlib que va por debajo.
# Ese es el motivo por el cual aquí no estamos creando la figura y el gráfico, el método de Pandas lo crea por nosotros, e incluso le pasa directamente algunos parámetros.
# Y después lo podemos seguir personalizando con todo lo que sabemos de la API orientada a objetos de Matplotlib.

g = df.total_bill.plot.hist()
g.set_title('Este es el título',fontsize = 20); # por ejemplo personalizamos el título
plt.show()

# También podemos combinar los dos métodos anteriores, es decir, definir parte de las opciones como argumentos y luego otras opciones con la sintaxis orientada a objetos

# Vamos a cambiar el tamaño del gráfico, el tipo de línea, el grosor y el color

g = df.total_bill.plot.line(title = 'Este es el título') # esto es sintaxis Pandas
g.set_xlim(0,100) # esto es sintaxis matplotlib aunque la opción también está en Pandas con otra sintaxis
plt.show()

# Crear el gráfico de Pandas y luego ir añadiendo capas al gráfico con la API funcional de Matplotlib
# Por último también podemos crear el gráfico con Pandas y luego ir usando la API funcional de Matplotlib por "capas".

df.total_bill.plot.hist()
plt.title('Este es el título')
plt.xlim(0,100);
plt.show()

# COMO HACER VARIOS GRAFICOS EN PANDAS
# REPRESENTAR VARIAS SERIES EN EL MISMO GRAFICO

# Podemos incluir varias variables en el mismo gráfico simplemente indexándolas en el dataframe. Ya que pandas intentará representar todas las variables que están antes del método.

df[['total_bill','tip']].plot.line();
plt.show()

# VARIOS GRAFICOS SEPARADOS

# También podemos pasarle directamente el dataframe y el tipo de gráfico que queremos y Pandas lo sacará automáticamente para todas las variables en las que piense que aplica.
# Usar subplots = True para que los haga en gráficos diferentes.

df.plot.line(subplots=True);
plt.show()

# Podemos organizar la "parrilla" usando el argumento layout y una tupla con filas-columnas.

df.plot.line(subplots=True, layout = (2,2));
plt.show()

# GRAFICOS DE DOS EJES

# También podemos poner 2 ejes si fuera necesario especificando cual va en el secundario

df[['total_bill','tip']].plot.line(secondary_y = 'tip');
plt.show()

# GRÁFICO DE LINEAS

# El tipo de gráfico es 'line'. 

# Lo más importante a entender es que el gráfico de líneas usará el index como el eje de las X para representar la variable que le has pasado.
# Por tanto es posible que a veces haya que cambiar el index o trabajar sobre él.

# Por ejemplo, si alguna vez te sale un gráfico de lineas entremezclado y sin sentido posiblemente sea por el index que tienes activo.

print(df)

# Ejemplo de un gráfico sobre un index que no tiene sentido
df.set_index('tip').total_bill.plot.line();
plt.show()

# Ejemplo gráfico de lineas del total de las facturas
df.total_bill.plot.line();
plt.show()

# GRÁFICO DE BARRAS

# Se hace con 'bar'.

# Lo más importante es recordar que tenemos que pasarle la variable de las x (lo que queremos representar) y la de las y (normalmente será la frecuencia).
# Pero seguramente tendremos los datos en bruto, por lo que hay que calcular esas frecuencias a priori.
# Lo bueno es que podemos hacerlo "al vuelo" con value_counts() y aplicar el plot directamente (encadenamiento de métodos).
# value_counts() hace que salga automáticamente ordendado por frecuencia descendente (que suele ser lo que queremos).
# Pero podríamos ordenarlo más inteligentemente usando sort.index()

# Con el orden que sale por defecto
df.day.value_counts().plot.bar();
plt.show()

# Con el orden de los días
df.day.value_counts().sort_index().plot.bar();
plt.show()

# En el gráfico no hay opción para sacarlo automáticamente en porcentajes, pero podemos prepocesar los datos para convertirlos a porcentaje y luego hacer el gráfico sobre los porcentajes.

df.day.value_counts(normalize=True).sort_index().plot.bar(); # en porcentajes
plt.show()

# Para hacer barras horizontales simplemente usamos barh, pero tendremos que usar ascending = True en el value_counts para que salga en descendente.

df.day.value_counts(ascending = True).plot.barh();
plt.show()

# Si no queremos usar las frecuencias si no otras métricas lo podemos hacer combinando groupby con la función de agregación que queremoas usar.

# Por ejemplo vamos a visualizar la propina media por día
df.groupby('day').tip.mean().plot.bar();
plt.show()

# Gráficos de barras apilados
# Necesitamos preprocesar una tabla cruzada con las variables que queramos representar y después usar el parámetro stacked=True.

tabla_cruzada = pd.crosstab(df.smoker, df.sex)
tabla_cruzada.plot.bar(stacked=True, color=['black','red']);
plt.show()

# GRÁFICO DE SECTORES

# Se hace con .pie() sobre un conteo previo de value_counts().
# Con autopct = '%.2f%%' le indicamos que ponga el valor. Podemos cambiar el número para los decimales que queramos.

df.day.value_counts().plot.pie(autopct = '%.2f%%');
plt.show()

# HISTOGRAMAS

# Lo hacemos con hist.
# El parámetro más importante con el que tendremos que jugar un poco en cada caso es bins, que es el número de tramos que formarán el histograma.

df.total_bill.plot.hist(bins = 30);
plt.show()

# Una opción útil es visualizar el histograma de una variable por los diferentes valores de otra.

# Por ejemplo si las propinas se distribuyen igual o no en función del día de la semana.
# Para ello usamos el método del dataframe en vez del de la serie con los parámetros column y by.
# Y si le ponemos sharex = True podremos comparar mejor.

df.hist(column = 'tip', by = 'day', sharex = True);
plt.show()

# GRÁFICOS DE DENSIDAD

# Similares a los histogramas pero en muchos casos más fáciles de visualizar.
# Se hacen con el tipo de gráfico kde (estimación de densidad kernel). O con density(), es lo mismo.

df.total_bill.plot.kde()
plt.show()

df.total_bill.plot.density()
plt.show()

# Recuerda que si hacemos el gráfico sobre todo el dataframe en lugar de sobre una variable nos los sacará para todas las variables en las que aplique (en este caso las numéricas).
# Podemos usar eso junto con subplots = True y decirle que aplique la escala de forma libre a cada variable con sharex = False para tener una rápida visualización de la distribución de todas las variables numéricas del dataframe con una sóla línea de código
# Y ajustamos el layout dependiendo de cuantas variables tengamos

df.plot.kde(subplots = True, sharex=False, layout=(2,2));
plt.show()

# BOX PLOTS

# Si sólo queremos ver el gráfico en una variable (por ejemplo para visualizar atípicos) entonces usaremos la sintaxis habitual de dataframe.variable.plot.box()

df.total_bill.plot.box()
plt.show()

# Pero también son muy útiles para ver si hay diferencias en la distribución de una variable cuantitativa en base a cada valor de otra categórica.
# Notar que la sintaxis es un poco diferente. No se hacen sobre dataframe.variable.plot sino directamente sobre dataframe.boxplot() y el método no es box si no boxplot()
# La cuantativa va en el parámetro column y la categórica en el parámetro by.

df.boxplot(column='total_bill', by='sex');
plt.show()

# SCATTER PLOTS

# Comparan dos variables cuantitativas.
# Se hacen con dataframe.plot.scatter y las variables a representar como parámetros.

df.plot.scatter('total_bill','tip', c = df.total_bill, colormap='Greens');
plt.show()

# Al igual que en Matplolib si queremos asignar una variable categórica al color tenemos que usar sus códigos.

df.plot.scatter('total_bill','tip', c = df.sex.cat.codes, colormap='Greens');
plt.show()

# Si hay muchos datos se solaparán unos con otros y será difícil ver patrones. Un truco es usar alpha para que se diferencien zonas de alta y baja densidad.

df.plot.scatter('total_bill','tip', alpha = 0.3);
plt.show()

# O también se pueden usar gráficos de hexágonos, que colorean cada hexágono en función de su densidad.
df.plot.hexbin('total_bill','tip',gridsize=15,cmap = 'coolwarm');
plt.show()

# PERSONALIZACIÓN

# Como hemos visto la gran mayoría de las opciones se las aplicaremos bien con alguna de las 3 opciones que explicamos más arriba.
# Pero vamos a ver aquí otras dos personalizaciones útiles: los estilos y el tamaño de gráfico y etiquetas.

# ESTILOS

# Hemos dicho que los gráficos de Pandas son más rápidos pero más "feos".
# Es cierto en general, pero también es verdad que tenemos varios estilos preconfigurados que pueden darle un toque más bonito, y que son muy fáciles de aplicar.

# Se cambia el estilo con plt.style.use('nombre_estilo')
# En esta url puedes verlos todos: https://matplotlib.org/3.1.0/gallery/style_sheets/style_sheets_reference.html
# O si no te hace falta ver ejemplos y sólo quires los nombres de los estilos puedes usar: plt.style.available

print(plt.style.available)

# Con el estilo por defecto
df.total_bill.plot(kind = 'hist');
plt.show()

# Con el estilo fivethirtyeight
plt.style.use('fivethirtyeight')

# Y recuerda que también puedes usar los parámetros como alpha clásicos para mejorarlo aún más
df.total_bill.plot(kind = 'hist', alpha = 0.3);
plt.show()

# TAMAÑOS DEL GRÁFICO Y DE LAS ETIQUETAS

# Cambiamos el tamaño del gráfico con figsize = (ancho, alto). Y el de las letras con fontsize.

df.total_bill.plot(kind = 'hist', figsize = (12,4), fontsize = 15);
plt.show()

# Vemos que los estilos se queadan. Podemos volver a poner el estilo por defecto con 'default'.

plt.style.use('default')
df.total_bill.plot(kind = 'hist');
plt.show()

# GRÁFICOS DE SERIES Y DE DATAFRAME

# Sin haberlo hecho explítico hemos estado utilizando de manera entrelazada los métedos de Series con los de Dataframes.
# En la mayoría de las veces no nos tendremos que preocupar por esto, pero sólo por conocerlo:

# - cuando hacmos df.variable.plot estamos usando un método de la serie
# - cuando hacemos df.plot(x = 'var1', y = 'var2) estamos usando un método de data frame

# Este es un método de la serie
df.day.value_counts().plot.bar();
plt.show()

# Este es un método de dataframe

conteo = df.groupby('day', as_index = False).tip.count()
conteo.plot(x = 'day', y = 'tip', kind = 'bar');
plt.show()

# Los gráficos de data frame sacan gráficos automáticamente para todas las variables para las que el tipo de gráfico aplique. Lo cual puede ser útil en ciertas situaciones.

df.plot(kind = 'density')
plt.show()

# Podemos decirle que los saque por separado con subplots = True
df.plot(kind = 'density', subplots = True, sharex = False);
plt.show()

# Con el método de dataframe podríamos elegir columnas de forma personalizada simplemente indexándolas en el dataframe antes del plot.

# Ejemplo de representar sólo dos variables pero con el método de dataframe
df[['total_bill','tip']].plot(kind = 'density');
plt.show()


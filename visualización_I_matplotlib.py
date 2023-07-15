print("********************************************")
print("VISUALIZACIÓN CON PYTHON PARA DATA SCIENCE I")
print("********************************************")

print("**********")
print("MATPLOTLIB")
print("**********")

# Existen 3 paquetes principales para visualización:

# - Matplotlib: es el de más bajo nivel, en el sentido de que hay que escribir más código pero también te da mayor flexibilidad. Es la base sobre la que están construidos los otros 2
# - Seaborn: de más alto nivel, también sobre Matplotlib. Crea gráficos más bonitos y con menos código
# Pandas: Pandas tiene sus propios métodos para hacer gráficos sobre Series y Dataframes construidos sobre Matplotlib y que ahorran tiempo

# En Data Science normalmente estaremos trabajando con Pandas, así que la recomendación es:

# - Para el día a día del proyecto hacer los gráficos con Pandas, es mucho más rápido y cómodo
# Para hacer gráficos "entregables" usar Seaborn

# Entonces, ¿merece la pena aprender Matplotlib? Sí por lo menos la base, por dos motivos:

# - Nos permitirá hacer gráficos con objetos no Pandas, como arrays de Numpy o incluso diccionarios
# - Las opciones de personalización de Seaborn y Pandas son las mismas que en Matplotlib, por tanto aprenderlas aquí hará el aprendizaje de Seaborn y Pandas mucho más rápido

# MATPLOTLIB

# La documentación online de Matplotlib es buena. La galería es especialmente útil.
# Puedes consultarla aquí: https://matplotlib.org/stable/gallery/index.html

import matplotlib.pyplot as plt
import numpy as np

# %matplotlib inline. Es para decirle cómo tiene que sacar los gráficos.
# En este caso significa que los saque como gráficos estáticos integrados en el propio notebook (de tal forma que se guarde y distribuya más fácilmente).

# Existen dos formas de hacer gráficos con Matplotlib: la funcional y la orientada a objetos.
# Técnicamente se llaman la API de pyplot (la funcional) y la API orientada a objetos.

# - La funcional es más directa y también más rápida, pero permite menos personalización.
# - La orientada a objetos conlleva más pasos, pero es más flexible. Y es la recomendada oficialmente.

# Las diferenciarás porque la funcional no crea ningún objeto, simplemente ejecuta un gráfico y le va añadiendo cosas. Por ejemplo:

x = np.linspace(1,100,500)

plt.plot(x)
plt.title('Un grafico funcional')
plt.show()

# Sin embargo en la orientada a objetos primero se crea un objeto y después se va desarrollando el gráfico mediante métodos y propiedades:

f = plt.figure()
ax = f.add_axes([0,0,1,1])
ax.plot(x,x**2)
plt.show()

# METODOLOGIA PARA CREAR UN GRÁFICO

# 1. Crear una figura: es como el marco, podrá llevar varios gráficos en su interior

f = plt.figure()

# 2. Añadir los ejes: donde va a estar contenido el gráfico

# Los parámetros que le pasamos son 4 (todos entre 0 y 1 y en una lista):

# - Dónde empieza el gráfico en el eje horizontal de la figura
# - Dónde empieza el gráfico en el eje vertical de la figura
# - Dimensión horizontal del gráfico con respecto a la figura
# - Dimensión vertical del gráfico con respecto a la figura

ax = f.add_axes([0,0,1,1])
plt.show()

f = plt.figure()
ax1 = f.add_axes([0,0,1,1])
ax2 = f.add_axes([0.5,0.5,0.5,0.5])
plt.show()

# 3. Definir el tipo de gráfico: de líneas, de barras, etc

# - Líneas
# - Barras
# - Sectores
# - Histogramas
# - Boxplots
# - Scatter

# Para simular valores para los gráficos

x1 = np.random.randint(1,5,100) # categóricos
x2 = np.random.randn(100) # numéricos
x3 = np.random.randn(100)*5 # numéricos dos variable

# GRÁFICO DE LÍNEAS: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot

# plot().

# Sus principales opciones son:

# - linewidth o lw: grosor de la línea
# - linestyle o ls: estilo de la línea. 'solid' o '-', 'dashed' o '--', 'dotted' o ':', 'dashdot' o '-.'
# - color o c: color de la línea
# - alpha: transparencia

f, ax = plt.subplots() # subplots() es como hacer un tupple unpacking, primero creamos el gráfico y asignamos el eje
ax.plot(x2);
plt.show()

# Verás que al hacer los gráficos aparecen una instrucciones raras como [<matplotlib.lines.Line2D at 0x287dbfe5cd0>]
# Para evitar que aparezcan puedes usar plt.show() al final, o simplemente termina la instrucción del gráfico con un punto y coma.

# GRÁFICO DE BARRAS: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.bar.html?highlight=bar#matplotlib.pyplot.bar

# bar(), pasándole x e y, por tanto hay que hacer un preconteo de los datos.

# Sus principales opciones son:

# - color: color de la barra
# - alpha: transparencia
# - edgecolor: color del borde

x, y = np.unique(x1, return_counts=True) # primero hacemos el conteo de cada valor para generar los ejes x e y

f, ax = plt.subplots()
ax.bar(x,y)
plt.show()

# GRÁFICO DE SECTORES: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.pie.html#matplotlib.pyplot.pie

# pie()

# Principales parámetros:

# - x: los valores
# - labels: las etiquetas
# - autopct: mostrar los porcentajes

x, y = np.unique(x1, return_counts=True) # primero hacemos el conteo de cada valor para generar los ejes x e y

f, ax = plt.subplots()
ax.pie(x = y,labels = x);
plt.show()

# Suele ser habitual querer incluir los porcentajes. Lo podemos hacer con el parámetro autopct = '%.2f%%' 
# Podemos cambiar el 2 por el número de decimales que queramos.
# Normalmente querremos que la fuente de los porcentajes se vea mejor que la que sale por defecto. Lo hacemos con:
# textprops = {'size': 'x-large', 'fontweight': 'bold', 'color': 'white'}

x, y = np.unique(x1, return_counts=True) # primero hacemos el conteo de cada valor para generar los ejes x e y

f, ax = plt.subplots()
ax.pie(y,labels = x, autopct = '%.2f%%',
      textprops = {'size': 'x-large', 
             'fontweight': 'bold',
             'color': 'white'})
#Añadimos la leyenda
ax.legend();
plt.show()

# HISTOGRAMA: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.hist.html#matplotlib.pyplot.hist

# hist()

# Sus principales opciones son:

# - bins: para el número de intervalos
# - cumulative: para hacerlo acumulado
# - color: color de la barra
# - alpha: transparencia

f, ax = plt.subplots()
ax.hist(x2);
plt.show()

# Podemos hacer un histograma acumulado con el parámetro cumulative = True

f, ax = plt.subplots()
ax.hist(x2, cumulative = True);
plt.show()

# Podemos incluir varias variables para comparar distribuciones

f, ax = plt.subplots()
ax.hist(x2, alpha = 0.3)
ax.hist(x3, alpha = 0.3);
plt.show()

# BOXPLOT: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.boxplot.html

# boxplot()

# Sus principales opciones son:

# - vert: para vertical u horizontal

f, ax = plt.subplots()
ax.boxplot(x2);
plt.show()

f, ax = plt.subplots()
ax.boxplot(x2, vert = False);
plt.show()

# SCATTER PLOTS: https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.scatter.html#matplotlib.pyplot.scatter

# scatter().

# Las principales opciones son:

# - s: tamaño del símbolo
# - c: color del símbolo
# - marker: el tipo de símbolo

f, ax = plt.subplots()
ax.scatter(x2,x3);
plt.show()

# Lo importante es ver cómo siempre es la misma mecánica, y si queremos hacer otro tipo de gráfico simplemente será seguirla e ir a la documentación a consultar la función concreta.

# Ahora vamos a ver dos funcionalidades interesantes:

# - Cómo incluir varias capas en el mismo gráfico
# - Cómo incluir varios gráficos en la misma figura

# INCLUIR VARIAS CAPAS

# Para incluir varias capas simplemente vamos añadiendo una detrás de otra.
# Pueden ser del mismo tipo de gráfico (p.e. líneas) o de tipos diferentes.

f, ax = plt.subplots()

ax.plot(x2) # definimos el primer gráfico
ax.plot(x3); # definimos el segundo gráfico

plt.show()

# INCLUIR VARIOS GRÁFICOS

# Para incluir varios gráficos haremos exactamente lo mismo sólo que específicando en subplots el número de filas y columnas que tendrá la figura con nrows y ncols.
# Al incluir esos parámetros el objeto ax se convertirá en un array, que podremos indexar para crear los gráficos correspodientes.

f, ax = plt.subplots(nrows = 1, ncols = 2) # esto creará dos gráficos en la misma figura

ax[0].boxplot(x2) # definimos el primer gráfico
ax[1].scatter(x2,x3); # definimos el segundo gráfico

plt.show()

# 4. Personalizar las opciones: tamaños, colores, leyenda, etc
# En esta fase es donde vamos a terminar de configurar nuestro gráfico.
# Es quizá la más importante porque como decíamos al principio en la mayoría de los casos estaremos sustituyendo los pasos 1 a 3 por sus equivalentes en Pandas o Seaborn que son más directos y sencillos.

# OPCIONES DE LA FIGURA

# - figsize nos permite definir el tamaño de la figura (en pulgadas). Se pasa como una tupla de ancho, alto
# - dpi nos permite definir la calidad (pixeles por pulgada)

# Ambos se modifican en el subplot()

f, ax = plt.subplots(figsize = (3,5)) # 16,6 p.e.
ax.scatter(x2,x3);
plt.show()

f, ax = plt.subplots(dpi = 100)
ax.scatter(x2,x3);
plt.show()

# TÍTULOS DE GRÁFICO Y EJES

f, ax = plt.subplots(dpi = 100)
ax.scatter(x2,x3)

ax.set_title('Este es el título del gráfico')

ax.set_xlabel('Este el título del eje X')
ax.set_ylabel('Este el título del eje Y');

plt.show()

# LEYENDA

# Cuando creamos un gráfico podemos ponerle un parámetro label que le va a identificar.
# De esa forma al poner después el método legend() lo representará automáticamente.

f, ax = plt.subplots()

ax.plot(x2, label = 'serie x2')
ax.plot(x3, label = 'serie x3')

ax.legend();
plt.show()

# Matplotlib intenta colocar la leyenda automáticamente. Pero nosotros podemos definir su posición con loc.
# Hay un montón de opciones que podemos consultar en la documentación: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.legend.html#matplotlib.pyplot.legend
# Con loc = 0 intenta elegir la mejor automáticamente y las demás son combinaciones intutivas en inglés como 'upper right'

f, ax = plt.subplots()

ax.plot(x2, label = 'serie x2')
ax.plot(x3, label = 'serie x3')

ax.legend(loc = 'upper right');
plt.show()

# COLORES Y LÍNEAS

# Estas opciones no aplican a todos los gráficos, y lo mejor es tener una noción general de cómo se hacen este tipo de cambios y luego consultar la documentación concreta de cada gráfico para ver qué parámetros admite.

# CAMBIAR EL COLOR

# Se hace con el parámetro color (o c según el gráfico).
# Admite varios formatos como el nombre en inglés, el RGB en hexadecimal, o incluso una abreviatura como r para rojo, g para verde, p.e.

f, ax = plt.subplots()
ax.hist(x2, color = 'red');
plt.show()

# TRANSPARENCIA

# Se hace con el parámetro alpha.
# Es una opción muy interesante, porque además del uso obvio de poder ver mejor gráficos que se superponen también consigue que un gráfico con un poco de trasparencia sea visualmente más atractivo.

f, ax = plt.subplots()
ax.hist(x2, color = 'red',alpha = 0.6)
ax.hist(x3, color = 'blue',alpha = 0.3);
plt.show()

# ESTILOS DE LÍNEA

# Se hace con el parámetro ls.
# Hace referencia a si es contínua, punteada, etc.
# '-' es la línea contínua por defecto '--' para líneas cortas '-.' para combinaciones de líneas cortas y puntos ':' para puntos

f, ax = plt.subplots(nrows = 2, ncols = 2,figsize = (10,10))

ax[0,0].plot(x2, ls = '-')
ax[0,1].plot(x2, ls = '--')
ax[1,0].plot(x2, ls = '-.')
ax[1,1].plot(x2, ls = ':');

plt.show()

# GROSOR DE LÍNEA

# Se hace con el parámetro linewidth (o lw).
# El número que le pongamos es un múltiplo del tamaño por defecto. 
# Es decir si le ponemos 5 será una línea 5 veces más gruesa que la que hace por defecto.

f, ax = plt.subplots(nrows = 2, ncols = 2,figsize = (10,10))

ax[0,0].plot(x2, linewidth = 1)
ax[0,1].plot(x2, linewidth = 2)
ax[1,0].plot(x2, linewidth = 4)
ax[1,1].plot(x2, linewidth = 8);

plt.show()

# PUNTOS MARCADORES

# Se hace con el parámetro marker.
# Hay muchísimos diferentes: '+', 'o', '*', 's', '.', etc.
# También se puede personalizar el tamaño con markersize.
# O el color con markerfacecolor.

f, ax = plt.subplots(nrows = 2, ncols = 2,figsize = (10,10))

ax[0,0].plot(x2, marker = '+', markersize = 1, markerfacecolor ='blue')
ax[0,1].plot(x2, marker = 'o', markersize = 2, markerfacecolor ='green')
ax[1,0].plot(x2, marker = 's', markersize = 4, markerfacecolor ='red')
ax[1,1].plot(x2, marker = '.', markersize = 20, markerfacecolor ='yellow');

plt.show()

# OPCIONES DE EJES

# TAMAÑO Y ÁNGULO DE LA ETIQUETAS DE LOS EJES

# Lo que se refiere tanto a las rayitas de referencia en los ejes como a las etiquetas que se muestran se llaman ticks.
# Para modificar sus opciones tenemos que usar tick_params, y decirle si queremos cambiar el eje x o el y.
# hay varios parámetros, pero los que usaremos más frecuentemente son los que nos permiten cambiar el tamaño y rotación. 
# Sobre todo es un uso muy típico cuando tenemos etiquetas de texto que no caben y se solapan, por lo que solemos hacerlas más pequeñas y poneras a 45 o 90 grados de rotación.

f, ax = plt.subplots()
ax.plot(x2)
ax.tick_params(axis='x', labelsize=18, labelrotation=45)
plt.show()

# RANGO DE LO EJES

f, ax = plt.subplots(1,2,figsize=(8,4))

ax[0].plot(x2)
ax[1].plot(x2)
ax[1].set_xlim([20,60])
ax[1].set_ylim([-1,1]);

plt.show()

# ESCALA LOGARÍTMICA

# Las variables x2 y x3 tienen diferente escala, lo que dificulta comparararlas
# NOTA: las elevamos al cuadrado y sumamos 1 simplemente porque las originales tenían negativos o ceros y eso da problemas con los logaritmos 
 
f, ax = plt.subplots(1,2,figsize=(16,4))

ax[0].plot((x2**2)+1)
ax[0].plot((x3**2)+1)
ax[1].plot((x2**2)+1)
ax[1].plot((x3**2)+1)

ax[1].set_yscale("log")

plt.show()

# PARRILLA

# Podemos poner una parrilla para facilitar la proyección visual de puntos a los ejes. Se hace con grid.
# Se pueden personalizar también su color, tipo de línea, grosor, etc.

f, ax = plt.subplots()

ax.plot(x2)
ax.grid(color='orange', linestyle=':', linewidth=2);

plt.show()

# GRÁFICOS DE DOS EJES

# A veces queremos representar dos variables en el mismo gráfico pero que tienen rangos diferentes. Para ello podemos usar dos ejes.
# La lógica aquí es crear un "gemelo" (la segunda variable) fijando el eje que comparte con la primera.

# - Si comparte el eje x usaremos twinx().
# - Si comparte el eje y usaremos twiny().

# Creamos la primera serie (con la variable x2)de forma normal
# Y la segunda diciendo que sea un gemelo de eje x de la primera y posicionando en ella a x3

f, ax = plt.subplots()
ax.plot(x2)
ax2 = ax.twinx()
ax2.plot(x3,color = 'y');
plt.show()

# LÍNEAS HORIZONTALES O VERTICALES

# Son útiles para marcar referencias comparativas como medias, máximos, mínimos, etc.
# Se hacen con .axhline para horizontal o .axvline para vertical. Y admiten parámetros como color y ls.

f, ax = plt.subplots()
media_x2 = x2.mean()

ax.plot(x2)
ax.axhline(media_x2, color = 'red')
ax.axvline(80, ls = '-.');

plt.show()

# GRAFICOS MATPLOTLIB SOBRE OBJETOS DE PANDAS

# Hasta ahora hemos hecho todos los ejemplos sobre objetos de numpy, ya que cuando usemos Pandas normalmente haremos gráficos con Pandas.
# Pero quizá en algún momento queramos aprovechar la flexibilidad de Matplotlib en un dataframe de Pandas. Simplemente hay que saber que hay dos opciones:

# - Crear una serie de Pandas para el eje de las x y otra para el eje de las y y luego hacer el gráfico
# - Usar el parámetro data para pasarle el dataframe

# Por ejemplo para hacer un gráfico de barras, como tenemos que precalcular los conteos, ya nos devuelve una Series, que podemos usar con la opción 1.

# Primero vamos a cargar un dataframe. Cogeremos uno de los que trae Seaborn

import seaborn as sns

df = sns.load_dataset('tips')
df.head()

# Ejemplo de un gráfico de barras con la opción número 1
# Primero preparamos los datos haciendo un conteo, nos devuelve un Series

cenas_por_dia = df.day.value_counts()
print(cenas_por_dia)

# Hacemos el gráfico

f, ax = plt.subplots()
ax.bar(cenas_por_dia.index,cenas_por_dia.values);
plt.show()

# TRUCO En ocasiones como la anterior querremos dar un orden personalizdo a los datos.
# Los podemos hacer primero creando una lista con el orden deseado y después cambiado la Series con reindex(orden)

# Creamos orden y lo aplicamos la Series

orden = ['Thur','Fri','Sat','Sun']
cenas_por_dia = cenas_por_dia.reindex(orden)

# Hacemos el gráfico
f, ax = plt.subplots()
ax.bar(cenas_por_dia.index,cenas_por_dia.values);
plt.show()

# Si queremos un gráfico que se puede hacer directamente desde el dataframe sin preparar nada usamos la opción 2.

# Creamos el gráfico usando el parámetro data y pasando los nombres de las variables

f, ax = plt.subplots()
ax.scatter('total_bill','tip',data = df);
plt.show()

# TRUCO: Asociar el color a otra variable
# Vimos anteriormente cómo cambiar el color, por ejemplo todo a rojo.

# Pero también podemos asociar el color a otra variable, y de esa forma incluir otra dimensión en el gráfico.
# Lo único que tenemos que tener en cuenta es que en variables categóricas sólo funcionará si las convertimos de algún modo a un número. Una forma es usar el método .cat.codes()

# Vamos a hacer primero un ejemplo de asociar el color a una variable contínua
f, ax = plt.subplots()
ax.scatter('tip', 'total_bill', c = 'size', data = df)
plt.show()

# ERROR 
# Ahora vamos a intentar hacer lo mismo pero con una variable categórica
# f, ax = plt.subplots()
# ax.scatter('tip', 'total_bill', c = 'sex', data = df);
# plt.show()

# Ahora la pasamos a número con cat.codes 
f, ax = plt.subplots()
ax.scatter('tip', 'total_bill', c = df.sex.cat.codes, data = df);
plt.show()

# Ahora bien, como ya hemos usado el parámetro de color para mapearlo a otra variable, ¿cómo hacemos si queremos cambiar los propios colores que nos pone por defecto?

# Lo más cómodo es usar paletas de colores, que se hacen con cmap.
# Puedes consultar las paletas disponibles aquí: https://matplotlib.org/3.1.1/gallery/color/colormap_reference.html

f, ax = plt.subplots()
ax.scatter('tip', 'total_bill', c = df.sex.cat.codes, cmap = 'Pastel1', data = df);
plt.show()

# Si ya quisiéramos poner una leyenda para saber lo que es cada cosa el tema se complica. Pero puedes guardar el código de abajo como una receta y simplemente copiar-pegar cuando lo necesites.

f, ax = plt.subplots()

# Tenemos que crear las etiquetas, para ello usamos cat.categories y lo pasamos a una lista
etiquetas = df.sex.cat.categories.to_list()

# Creamos el gráfico igual que antes pero no lo mostramos, lo guardamos en una variable
g = ax.scatter('tip', 'total_bill', c = df.sex.cat.codes, data = df, label = etiquetas)

#Con el método legend_elements() guardamos el valor de los puntos (el código realmente no lo queremos)
valor, codigo = g.legend_elements()

# Añadimos la leyenda y mostramos el gráfico
ax.legend(handles=valor, labels=etiquetas);

plt.show()

# GRÁFICOS MATPLOTLIB CON LA API FUNCIONAL

# Ahora que ya que hemos aprendido a hacer gráficos con la API orientada a objetos, que es la recomendada, vamos a hacer un rápido repaso sobre la API funcional.
# Con la API funcional, o también llamada de pyplot, la forma de hacer gráficos es muy sencilla, no creamos un objeto sino que simplemente usamos plt.lo_que_sea sobre la marcha:

# 1. (Opcional) Crear el "hueco" para varios gráficos
# 2. Crear el tipo de gráfico que queramos (lineas, barras, etc) pasándole los datos y los parámetros de color, tipo de línea y demás
# 3. Personalizar otros elementos del gráfico: título, ejes, etc.

# CREAR VARIOS GRÁFICOS

# Este paso es opcional ya que en la mayoría de los casos estaremos creando solo un gráfico.
# Pero si quisiéramos hacer más tenemos que usar plt.subplot() y pasarle:

# - Número de filas
# - Número de columnas
# - El índice del gráfico concreto que estamos haciendo

plt.subplot(2,2,1)
plt.plot(x1)

plt.subplot(2,2,2)
plt.plot(x1)

plt.subplot(2,2,3)
plt.plot(x1)

plt.subplot(2,2,4)
plt.plot(x1);

plt.show()

# CREAR EL TIPO DE GRÁFICO

# Los tipos más frecuentes son:

# - líneas: plt.plot()
# - lbarras: plt.bar()
# - lhistograma: plt.hist()
# - lboxplot: plt.boxplot()
# - lscatter: plt.scatter()

# En esta misma llamada al gráfico le pasamos los datos según corresponda.

# Y también las opciones como:

# - lcolor
# - lalpha
# - lls
# - llinewidth
# - lmarker
# - lmarkersize
# - lmarkerfacecolor

# El uso de estas opciones es el que ya conocemos.

plt.plot(x2,ls = '-.', linewidth = 2, marker = 'o', markersize = 6, markerfacecolor ='blue');
plt.show()

x, y = np.unique(x1, return_counts=True)
plt.bar(x,y, color = 'red', alpha = 0.6);
plt.show()

plt.scatter(x2,x3,color = 'yellow');
plt.show()

# PERSONALIZAR OTROS ELEMENTOS DEL GRÁFICO

# Se hace con llamadas sucesivas a plt.la_opcion_a_cambiar. Personalizaciones frecuentes son:

# - tamaño del gráfico (hacer lo primero antes de plotearlo): plt.figure(figsize = (12,6))
# - título del gráfico: plt.title()
# - título de los ejes: plt.xlabel() y plt.ylabel()
# - rangos de los ejes: plt.xlim() y plt.ylim()
# - tamaño o rotación de las etiquetas: plt.xticks(size = 18, rotation = 45)

# En general casi cualquier opción de las que ya hemos visto podemos usarla aquí bajo el formato plt.opcion

# De todas formas te dejo el enlace al a documentación donde puedes verlas todas o tenerlo como referencia:

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot

plt.figure(figsize = (12,6))
plt.plot(x1)
plt.title('Este es el titulo')
plt.xlabel('Eje X')
plt.xlim([20,80])
plt.xticks(size = 18, rotation = 45);

plt.show()



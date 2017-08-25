from bokeh._legacy_charts import Bar
from bokeh.io import output_notebook, show

# get the countries and we group the data by medal type
states = ['delhi', 'assam']


delhi = [ [56,46],
         [23,77],
         [45,55],
         [60,40],
         [35,15,25,25]   
]

assam = [ [30,10],
         [33,67],
         [75,25],
         [50,50],
         [75,5,10,10]   
]

output_notebook()

bar = Bar([delhi[0],assam[0]], states, title="Stacked bars", stacked=True)
bar2 = Bar([delhi[0],assam[0]], states, title="Stacked bars")

show(bar)
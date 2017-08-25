import pandas as pd
df_men = pd.read_csv("4_educational_background.csv")



ls_labels_men = []
ls_values_men = []

for i in range(1,df_men.shape[0]):
    ls_labels_men.append(str(df_men.iat[i,0]))
    ls_values_men.append(float(df_men.iat[i,1]))


import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['figure.figsize'] = (10.0, 10.0)

# The slices will be ordered and plotted counter-clockwise.

labels = ls_labels_men
sizes = ls_values_men
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral', 'red', 'lightgreen']
explode = (0.1, 0.1, 0.1, 0.1, 0.1, .1) 

p, text = plt.pie(sizes,  colors = colors, explode =  explode, shadow=True, startangle=90 )
# Set aspect ratio to be equal so that pie is drawn as a circle.
plt.axis('equal')

#plt.title("Educational Background", fontsize = 50, loc = 'right')

plt.legend(p, labels, loc= 'lower right')

plt.show()
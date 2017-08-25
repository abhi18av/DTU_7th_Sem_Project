import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (10.0, 8.0)

ls_labels_men = []
ls_values_men = []

for i in range(1,df_men.shape[0]):
    ls_labels_men.append(str(df_men.iat[i,0]))
    ls_values_men.append(float(df_men.iat[i,1]))




import numpy as np
import matplotlib.pyplot as plt

N = len(ls_labels_men)


ind = np.arange(N)  # the x locations for the groups
width = 0.35       # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(ind, ls_values_men, width, color = 'red', alpha = 0.6)



#rects2 = ax.bar(ind + width, ls_values_men, width )

# add some text for labels, title and axes ticks
ax.set_ylabel('Scores')

ax.set_title('Scores by group and gender')
ax.set_xticks(ind + width)
ax.set_xticklabels(ls_labels_men)


#ax.legend((rects1[0], rects2[0]), ('Men', 'Women'))

plt.show()





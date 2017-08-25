import os
#os.chdir("/home/archimedeas/wrkspc/anaconda/the-visual-verdict/visualizations/1_the_senate/datasets")
os.getcwd()
os.chdir('the_senate_datasets')


import pandas as pd
df_men = pd.read_csv("1_age_group_5yr_span.csv")
df_men


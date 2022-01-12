#step1 Involed in  data Visulaization
#step-1 import libraries
import seaborn as sns
import matplotlib.pyplot as plt

#step-2 set a theme
sns.set_theme(style="ticks", color_codes=True)

#step 3 import data
tips = sns.load_dataset("tips")

#step-4 plot basic Graph
p = sns.barplot(x="day", y="total_bill", data=tips)
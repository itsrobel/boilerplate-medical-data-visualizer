import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# titanic_data = sns.load_dataset("titanic")
df = pd.read_csv("medical_examination.csv")

# print(titanic_data.head())

df['overweight'] = (df["weight"] / df["height"]) > 25
df.loc[df['overweight'] == True, 'overweight'] = 1
df.loc[df['overweight'] == False, 'overweight'] = 0

df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1

df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1
sns.catplot(x = "cholesterol", col = "cardio", data=df, kind="count" )
# sns.catplot(x = "sex", y= "survived", hue="embark_town",col = "class", data=titanic_data, kind="bar" )
#sns.set_style('darkgrid')
#
# x = ['A', 'B' , 'C']
# y = [1, 5 ,3 ]
#
#
# sns.barplot(x,y)
plt.show()
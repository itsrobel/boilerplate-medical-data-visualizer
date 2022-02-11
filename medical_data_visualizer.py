import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
# print(1 if  (df["weight"] /df["height"]) > 25 else 0)

df['overweight'] = (df["weight"] / df["height"]) > 25
df.loc[df['overweight'] == True, 'overweight'] = 1
df.loc[df['overweight'] == False, 'overweight'] = 0
# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
# df['cholesterol'] = 0 if df['cholesterol'] ==1 else 1
# df['cholesterol'] = df['cholesterol'].replace(1,0)
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
# df['cholesterol'] = df['cholesterol'].replace(1,0)
# df['cholesterol'] = df['cholesterol'].replace(1,0)

# df['gluc'] = 0 if df['gluc'] ==1 else 1

df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.

    # df_cat = pd.melt(df["cholesterol"], df["gluc"], df["smoke"], df["alco"], df["active"], df["overweight"])
    # print(df.groupby("cardio").count())
    # print(df.head())
    #df_cat = df.groupby('cardio').value_counts()
	df_cat = df.melt(id_vars=["cardio"], value_vars=["cholesterol","gluc" ,"smoke", "alco", "active", "overweight"])
    # df_cat.to_csv('cat.csv', index=False)
	df_cat = df_cat.value_counts().to_frame()
	#print(df_cat.groupby("value").head())
	
	print(df_cat.iloc[0])

    # fig = sns.catplot(x="variable" ,y="value", data=df_cat, hue="value", kind="bar",col="cardio")
    #
    # # # #
    # fig.set(xlabel="variable", ylabel="total")
    # fig.set_xticklabels(["cholesterol","gluc" ,"smoke", "alco", "active", "overweight"])
    # print(type(df_cat))

    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    # df_cat.groupby("cardio")
    # print(df_cat)
    # df_cat = None

    # Draw the catplot with 'sns.catplot()'
    # fig = sns.catplot(df_cat)
    #
    #
    # # Do not modify the next two lines
    # fig.savefig('catplot.png')
    # return fig
    #


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None

    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

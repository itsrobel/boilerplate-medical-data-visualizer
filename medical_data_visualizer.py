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
    df_cat = df.melt(id_vars=["cardio"], value_vars=[
        'active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    fig = sns.catplot(x="variable", hue="value",
                      col="cardio", data=df_cat, kind="count")
    fig.set(ylabel="total")

    # # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig
    #


# Draw Heat Map
def draw_heat_map():
    (df['ap_lo'] <= df['ap_hi'])
    (df['height'] >= df['height'].quantile(0.025))
    (df['weight'] >= df['weight'].quantile(0.95))
    (df['weight'] <= df['weight'].quantile(0.025))
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    # corr = None

    # # Generate a mask for the upper triangle
    # mask = None

    # # Set up the matplotlib figure
    # fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'

    # Do not modify the next two lines
    # fig.savefig('heatmap.png')
    # return fig

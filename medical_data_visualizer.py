import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")


bmi = (df["weight"] / (df["height"] / 100)**2) > 25
df.loc[bmi == True, 'overweight'] = 1
df.loc[bmi == False, 'overweight'] = 0
df.loc[df['cholesterol'] == 1, 'cholesterol'] = 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1

df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1


# Draw Categorical Plot
def draw_cat_plot():
    plt.clf()
    df_cat = df.melt(id_vars=["cardio"], value_vars=[
        'active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'])

    figure = sns.catplot(x="variable", hue="value",
                      col="cardio", data=df_cat, kind="count")
    figure.set(ylabel="total")
    fig = figure
    #print(fig.axes[0][0].get_xlabel())

    # # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig
    #


# Draw Heat Map
def draw_heat_map():
    plt.clf()
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi'])
        & (df['height'] >= df['height'].quantile(0.025))
        & (df['height'] <= df['height'].quantile(0.975))
        & (df['weight'] >= df['weight'].quantile(0.025))
        & (df['weight'] <= df['weight'].quantile(0.975))
        ]
    # Calculate the correlation matrix
    corr = df_heat.corr()

    # # Generate a mask for the upper triangle
    matrix = np.triu(corr)

    # # Set up the matplotlib figure
    figure = sns.heatmap(corr, annot=True, mask=matrix, fmt=".1f").figure
    fig = figure


    # Draw the heatmap with 'sns.heatmap()'

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig

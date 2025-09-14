import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')
lower = df['value'].quantile(0.025)
upper = df['value'].quantile(0.975)
df = df[(df['value'] >= lower) & (df['value'] <= upper)]

def draw_line_plot():
    data = df.copy()
    plt.figure(figsize=(15, 5))
    plt.plot(data.index, data['value'], color='red')
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")
    plt.tight_layout()
    plt.savefig("images/line_plot.png")
    return plt.gcf()

def draw_bar_plot():
    data = df.copy()
    data['year'] = data.index.year
    data['month'] = data.index.month
    df_bar = data.groupby(['year', 'month'])['value'].mean().unstack()
    df_bar.plot(kind='bar', figsize=(15, 10))
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title='Months', labels=[
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ])
    plt.tight_layout()
    plt.savefig("images/bar_plot.png")
    return plt.gcf()

def draw_box_plot():
    data = df.copy()
    data.reset_index(inplace=True)
    data['year'] = data['date'].dt.year
    data['month'] = data['date'].dt.strftime('%b')
    data['month_num'] = data['date'].dt.month
    data = data.sort_values('month_num')

    fig, axes = plt.subplots(1, 2, figsize=(20, 6))
    sns.boxplot(x='year', y='value', data=data, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(x='month', y='value', data=data, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    plt.tight_layout()
    plt.savefig("images/box_plot.png")
    return plt.gcf()

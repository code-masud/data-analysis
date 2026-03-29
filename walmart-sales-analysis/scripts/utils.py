
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import seaborn as sns

sns.set(style="whitegrid")

# -------------------------------
# General Plot Helpers
# -------------------------------

def format_millions(ax):
    """Format y-axis in millions"""
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x/1e6:.1f}M'))

def rotate_xticks(rotation=45):
    """Rotate x-axis ticks"""
    plt.xticks(rotation=rotation)

def save_plot(file_path):
    """Save current figure"""
    plt.tight_layout()
    plt.savefig(file_path)

def line_plot(series, title="", xlabel="", ylabel=""):
    """Simple line plot helper"""
    ax = series.plot()
    format_millions(ax)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    rotate_xticks()
    plt.tight_layout()
    return ax

def bar_plot(series, title="", xlabel="", ylabel=""):
    """Simple bar plot helper"""
    ax = series.plot(kind="bar")
    format_millions(ax)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    rotate_xticks()
    plt.tight_layout()
    return ax

def scatter_plot(x, y, hue=None, title="", xlabel="", ylabel=""):
    """Scatter plot helper"""
    import seaborn as sns
    ax = sns.scatterplot(x=x, y=y, hue=hue)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.tight_layout()
    return ax

def pie_chart(values, labels, explode=None, title=""):
    """Pie chart with percentages and absolute values"""
    plt.figure(figsize=(6,6))
    plt.pie(
        values,
        labels=labels,
        explode=explode,
        shadow=True,
        autopct=lambda p: f'{p:.1f}%\n({p*sum(values)/100:,.0f})'
    )
    plt.title(title)
    plt.tight_layout()
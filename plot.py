import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
from matplotlib import style

stock_code_list=['INFY','ZODIACLOTH','ZUARI','A2ZINFRA']
style.use('seaborn')
fig=plt.figure()

ax=[]
for col in range(0,len(stock_code_list)):
    ax.append(fig.add_subplot(2,2,col+1))

def animate(i):
    df=pd.read_csv('real time stock data.csv')
    ys=df.iloc[1:, 1].values
    xs=list(range(1,len(ys)+1))
    for col in range(1,len(df.axes[1])):
        ys=df.iloc[1:, col].values
        ax[col-1].clear()
        ax[col-1].plot(xs,ys)
        ax[col-1].set_title(stock_code_list[col-1],fontsize=10)

ani=animation.FuncAnimation(fig,animate,interval=1000)
plt.tight_layout()
plt.show()


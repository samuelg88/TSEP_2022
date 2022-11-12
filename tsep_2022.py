import datetime
#import qgrid
from ipywidgets import interact, widgets, Layout, interactive
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas_datareader.data as web
import plotly.graph_objects as go
import seaborn as sns

from IPython.core import debugger
from IPython.display import display, HTML
import ipywidgets as widgets
from ipywidgets import interact, widgets, Layout, interactive


start_date = widgets.DatePicker(description='Start date:', disabled=False, value=datetime.date.today() - datetime.timedelta(days=1)- datetime.timedelta(days=365))

end_date = widgets.DatePicker(description='End date', disabled = False, value=datetime.date.today())

select_button = widgets.Button(description='Search', disabled=False, button_style='primary',layout=Layout(margin=('0px 0px 0px 10px'), width='10%'))

stock_output = widgets.Output()
node_term = widgets.IntSlider(value=3, min=1, max=360, step=1, description='Node months:', disabled=True, continuous_update=False)

# stock_output = widgets.Output()
ticker = ["AAPL","MSFT","AMZN","TSLA","GOOGL",
"XOM","JPM","NVDA","CVX","V","PG","MA","PFE","BAC","MRK",
"PEP","KO","COST","META","MCD","WMT","DIS","COP","ABT",
"VZ","HON","PM","ADBE","CMCSA","T","CVS","IBM","UPS",
"NFLX","LOW","LMT","NKE","ORCL","INTC","AMD","SBUX",
"BLK","TMUS","PYPL","BA","GE","AXP","TGT","MMM","CL"]

list_of_estonks = ["Apple Inc",
"Microsoft Corporation","Amazon.com Inc","Tesla Inc","Alphabet Inc","Exxon Mobil Corporation","JPMorgan Chase & Co","NVIDIA Corporation","Chevron Corporation","Visa Inc","Procter & Gamble Company","Mastercard Incorporated","Pfizer Inc","Bank of America Corp","Merck & Co. Inc","PepsiCo Inc","Coca-Cola Company","Costco Wholesale Corporation","Meta Platforms Inc","McDonald's Corporation","Walmart Inc","Walt Disney Company","ConocoPhillips","Abbott Laboratories","Verizon Communications Inc","Honeywell International Inc","Philip Morris International Inc","Adobe Incorporated","Comcast Corporation","AT&T Inc","CVS Health Corporation","International Business Machines Corporation","United Parcel Service Inc","Netflix Inc","Lowe's Companies Inc","Lockheed Martin Corporation","NIKE Inc","Oracle Corporation","Intel Corporation","Advanced Micro Devices Inc","Starbucks Corporation","BlackRock Inc","T-Mobile US Inc","PayPal Holdings Inc","Boeing Company","General Electric Company","American Express Company","Target Corporation","3M Company","Colgate-Palmolive Company"]

multiple_stocks = widgets.SelectMultiple(options=list_of_estonks, description='Choose your prefered stocks',
                                        disabled=False, layout=widgets.Layout(width='1000px', allign_items='strech', justify_content='space-between'))

weight0 = widgets.BoundedFloatText(
    value=0.25,
    min=0.01,
    max=0.97,
    step=0.05,
    description='W stock1:',
    disabled=False)

weight1 = widgets.BoundedFloatText(
    value=.25,
    min=0.01,
    max=1,
    step=0.05,
    description='W stock2:',
    disabled=False)

weight2 = widgets.BoundedFloatText(
    value=.25,
    min=0.01,
    max=100,
    step=0.05,
    description='W Stock3:',
    disabled=False)

weight3 = widgets.BoundedFloatText(
    value=0.25,
    min=0.01,
    max=0.97,
    step=0.05,
    description='W Stock4:',
    disabled=False)

porfolio = widgets.IntText(value=100000, description='Size of portfolio', disabled=False)

def display_data():
    h_box = widgets.HBox([start_date, end_date, porfolio, select_button])
    display(h_box)
    h_box2 = widgets.HBox([multiple_stocks, weight0, weight1, weight2, weight3])
    display(HTML('<br>'))
    display('Pick 4 stocks')
    display('Using ctrl + click')
    display('Sum of weights should amount to 1 or less')
    display(h_box2)
    
    def investigation(a):
#        try:
        estart = start_date.value
        end_ = end_date.value
        stocks = multiple_stocks.value
        v_weight0 = weight0.value
        v_weight1 = weight1.value
        v_weight2 = weight2.value
        v_weight3 = weight3.value
        v_portfolio = porfolio.value
      
        res = {list_of_estonks[i]: ticker[i] for i in range(len(list_of_estonks))}
        
        count = 0
        for i in range(len(stocks) -1):
            if len(stocks) >= 5 :
                raise Exception("Up to 4 stocks allowed")
            if count == 0:
                tick0 = res[stocks[count]]
                dataset0 = web.DataReader(tick0, data_source='yahoo', start=estart, end=end_)
                dataset0 = pd.DataFrame(dataset0)
                count += 1
                if tick0 == res[stocks[-1]]:
                    break
                    
            if count == 1:
                tick1 = res[stocks[count]]
                dataset1 = web.DataReader(tick1, data_source='yahoo', start=estart, end=end_)
                dataset1 = pd.DataFrame(dataset1)
                count += 1
                if tick1 == res[stocks[-1]]:
                    break
                    
            if count == 2:
                tick2 = res[stocks[count]]
                dataset2 = web.DataReader(tick2, data_source='yahoo', start=estart, end=end_)
                dataset2 = pd.DataFrame(dataset2)
                count += 1
                if tick2 == res[stocks[-1]]:
                    break
                    
            if count == 3:
                tick3 = res[stocks[count]]
                dataset3 = web.DataReader(tick3, data_source='yahoo', start=estart, end=end_)
                dataset3 = pd.DataFrame(dataset3)
                count += 1
                if tick3 == res[stocks[-1]]:
                    break
        fig = go.Figure(data=[go.Candlestick(x=dataset0.index,
                                              open = dataset0['Open'],
                                              high = dataset0['High'],
                                              low = dataset0['Low'],
                                              close = dataset0['Close'])],
        layout = go.Layout(title = go.layout.Title(text = tick0)))
        fig.update_layout(xaxis_rangeslider_visible = False)
        fig.show()

        fig1 = go.Figure(data=[go.Candlestick(x=dataset1.index,
                                              open = dataset1['Open'],
                                              high = dataset1['High'],
                                              low = dataset1['Low'],
                                              close = dataset1['Close'])],
        layout = go.Layout(title = go.layout.Title(text = tick1)))
        fig1.update_layout(xaxis_rangeslider_visible = False)
        fig1.show()

        fig2 = go.Figure(data=[go.Candlestick(x=dataset1.index,
                                              open = dataset2['Open'],
                                              high = dataset2['High'],
                                              low = dataset2['Low'],
                                              close = dataset2['Close'])],
        layout = go.Layout(title = go.layout.Title(text = tick2)))
        fig2.update_layout(xaxis_rangeslider_visible = False)
        fig2.show()

        fig3 = go.Figure(data=[go.Candlestick(x=dataset3.index,
                                              open = dataset3['Open'],
                                              high = dataset3['High'],
                                              low = dataset3['Low'],
                                              close = dataset3['Close'])],
        layout = go.Layout(title = go.layout.Title(text = tick3)))
        fig3.update_layout(xaxis_rangeslider_visible = False)
        fig3.show()
        
        def ytd_return(data):
            ytd = (((data['Close'].iloc[-1] - data['Close'].iloc[0]) / data['Close'].iloc[0]) * 100)
            return ytd
        
        ytd_dataset0 = ytd_return(dataset0)
        ytd_dataset1 = ytd_return(dataset1)
        ytd_dataset2 = ytd_return(dataset2)
        ytd_dataset3 = ytd_return(dataset3)
        ytd_list = [ytd_dataset0, ytd_dataset1, ytd_dataset2, ytd_dataset3]
        tickers = [tick0, tick1, tick2, tick3]
        ytd_df = pd.DataFrame(ytd_list, index=tickers).rename(columns={0:'YTD-Return'})
        ytd_df = ytd_df.reset_index()
        ytd_df = ytd_df.rename(columns={'index': 'ticker'})
        sns.set_style("whitegrid")
        sns.color_palette("Set2")
        sns_plot = sns.barplot(data=ytd_df, x=ytd_df['ticker'], y=ytd_df['YTD-Return'], alpha=0.75)
        sns_plot.set(xlabel='Company', ylabel='%Change', title='Year-To-Date-Return')
        plt.show()
        
        portfolio_ret0 = (v_weight0 * ytd_dataset0)
        portfolio_ret1 = (v_weight1 * ytd_dataset1)
        portfolio_ret2 = (v_weight2 * ytd_dataset2)
        portfolio_ret3 = (v_weight3 * ytd_dataset3)
        total_portfolio_ret = portfolio_ret0 + portfolio_ret1 + portfolio_ret2 + portfolio_ret3
        
        labels = [tick0, tick1, tick2, tick3]
        sizes = [v_weight0, v_weight1, v_weight2, v_weight3]
        fig, ax1 = plt.subplots()
        ax1.pie(sizes, labels=labels, shadow=True)
        ax1.axis('equal')
        plt.title('Your portfolio')
        plt.show()
        
        port_df = {tick0 : dataset0['Close'], tick1 : dataset1['Close'], tick2 : dataset2['Close'], tick3 : dataset3['Close']}
        port_df = pd.DataFrame(port_df)
        
        port_return = port_df.pct_change()
        port_return = port_return.dot(sizes)
        
        # RISK
        delta = end_ - estart
        day_diff = int(delta.days)
        d0 = dataset0['Close']
        d1 = dataset1['Close']
        d2 = dataset2['Close']
        d3 = dataset3['Close']
        np_d = np.array([d0,d1,d2,d3])
        covMatrix = np.cov(np_d, bias=True)
        portfolio_variance = np.transpose(sizes)@covMatrix@sizes
        portfolio_volatility = np.sqrt(portfolio_variance)
        
        print('The % return of your porfolio is : ' + str(total_portfolio_ret))
        print('Porfolio Variance is',portfolio_variance)
        print('Portfolio Volatility(Risk) is',portfolio_volatility)
        dolars_made = v_portfolio * (total_portfolio_ret / 100)
        if dolars_made > 0:
            print('Good job you made ' + str(dolars_made))
        else:
            print('Investing is hard, you lost ' + str(dolars_made))

                    
    select_button.on_click(investigation)
    
            
            

import plotly.plotly as py
import pandas as pd
import plotly.graph_objs as go
import plotly.offline
from datetime import datetime

def generateMap(filename, graphtitle='Stat Distribution'):
    df = pd.read_csv(filename)
    for col in df.columns:
        df[col] = df[col].astype(str)

    trace = go.Table(
        header=dict(values=['name','ethnicity','gender','citizenship'],
                    fill = dict(color='#C2D4FF'),
                    align = ['left'] * 5),
        cells=dict(values=[df.name, df.ethnicity,df.gender,df.citizenship],
                    fill = dict(color='#F5F8FF'),
                    align = ['left'] * 5))

    data = [trace] 
    eList = ['Asian','Black','Hispanic','White','Multi','Total']

    eDict = dict()
    total = 0
    for row in df.itertuples():
        if (row.citizenship.lower() in ['us','usa']):
            total += 1
            if row.ethnicity not in eDict:
                eDict[row.ethnicity] = 1;
            else:
                eDict[row.ethnicity] += 1;
        eDict['multi'] = 0;
    eTotals = [eDict['a'], eDict['b'], eDict['h'], eDict['w'], eDict['multi'],total]
    total = float(total)
    ePercent = ["{0:.2f}".format(eDict['a']/total * 100) + '%', "{0:.2f}".format(eDict['b']/total * 100) + '%', 
                "{0:.2f}".format(eDict['h']/total * 100) + '%',"{0:.2f}".format(eDict['w']/total * 100) + '%', 
                "{0:.2f}".format(eDict['multi']/total * 100) + '%', '100%']

    trace2 = go.Table(
        header = dict(values=['ethnicity','total','%'],
            fill = dict(color='#C2D4FF'),      
            align = ['left'] * 5),
        cells = dict(values=[eList, eTotals, ePercent],
            fill = dict(color='#F5F8FF'),
            align = ['left']*5)
    )

    data2 = [trace2]
    fig = dict(data=data2)
    return plotly.offline.plot(fig, include_plotlyjs='cdn', output_type='div')
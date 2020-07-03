from flask import Flask, render_template
from corona import table, plot1, plot2, plot3, plot4, plot5, datewise, countrywise, datewise_worldwide_cases, daily_confirmed_deaths,countrywise_tests, total_vs_new_cases 
import pandas as pd
from flask import *
import seaborn as sns
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
from matplotlib import style
import plotly.graph_objects as go
import plotly.offline as pyo
from plotly.offline import init_notebook_mode,plot,iplot
from plotly.subplots import make_subplots





app=Flask(__name__)

@app.route("/covid-19 analysis")
def show_tables():
    tableDisplay = table()
    figureDisplay1 = plot1()
    figureDisplay2 = plot2()
    figureDisplay3 = plot3()
    figureDisplay4 = plot4()
    figureDisplay5 = plot5()
    dateWise = datewise()
    countryWise = countrywise()
    datewiseWorldwideCases = datewise_worldwide_cases()
    dailyConfirmedDeaths = daily_confirmed_deaths()
    countrywiseTests = countrywise_tests()
    totalVSNewCases = total_vs_new_cases()
    return render_template('index.html',  returnList = tableDisplay, figure1=figureDisplay1, figure2=figureDisplay2, figure3=figureDisplay3,
                    figure4=figureDisplay4, figure5=figureDisplay5, dateWiseData=dateWise, countryWiseData=countrywise,
                    datewiseWorldwideData=datewiseWorldwideCases, dailyConfirmedDeath=dailyConfirmedDeaths, countryWiseTests=countrywiseTests, totalVsNewCases=totalVSNewCases)

     
if __name__ == "__main__":
    app.jinja_env.cache = {}
    app.run(debug=True)

    



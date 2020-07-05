
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
import plotly.figure_factory as ff
from matplotlib import style
import plotly.graph_objects as go
import plotly.offline as pyo
from plotly.offline import init_notebook_mode,plot,iplot
from plotly.subplots import make_subplots

A=pd.read_csv("India_cov_data.csv")
D=pd.read_csv("owid-covid-data.csv")
C=pd.read_csv("World_cov_data.csv")
B=pd.read_csv("India_date_data.csv")



def scrape():
    A.drop(["Unnamed: 0"],axis=1)
    A["Active_cases"]=A["Total_confirmed_cases"]-(A['Cured_or_discharged_or_migrated']+A["Death"])
    return A


def table():
    
    df3 = ff.create_table(A)
    # return df3
    return plotly.offline.plot(df3,output_type='div')  




def plot1():
    fig=px.bar(A,x="State",y="Total_confirmed_cases",color="Total_confirmed_cases",height=600)
    return plotly.offline.plot(fig,output_type='div')
    return fig.show(output_type='div')


def plot2():
    fig=px.bar(A,x="State",y="Death",color="Death",height=600)
    return plotly.offline.plot(fig,output_type='div')


def plot3():
    fig=px.bar(A,x="State",y="Cured_or_discharged_or_migrated",color="Cured_or_discharged_or_migrated",height=600)
    return plotly.offline.plot(fig,output_type='div')

def plot4():
    A=scrape()
    fig=px.bar(A,x="State",y="Active_cases",color="Active_cases",height=600)
    return plotly.offline.plot(fig,output_type='div')

def plot5():
    fig=px.bar(B,x="Date",y="Total Confirmed", color="Total Confirmed",title="Date-wise confirmed cases")
    return plotly.offline.plot(fig,output_type='div')


def datewise():
    df=D.query('location=="India"')
    tests=df.groupby("date").sum()["total_tests_per_thousand"].reset_index()
    Cases=df.groupby("date").sum()["total_cases"].reset_index()
    deaths=df.groupby("date").sum()["total_deaths"].reset_index()
    new_cases=df.groupby("date").sum()["new_cases"].reset_index()
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=tests["date"],y=tests["total_tests_per_thousand"],mode="lines+markers",name="tests",line=dict(color="green",width=1)))
    fig.add_trace(go.Scatter(x=Cases["date"],y=Cases["total_cases"],mode="lines+markers",name="Cases",line=dict(color="yellow",width=1)))
    fig.add_trace(go.Scatter(x=deaths["date"],y=deaths["total_deaths"],mode="lines+markers",name="deaths",line=dict(color="orange",width=1)))
    fig.add_trace(go.Scatter(x=new_cases["date"],y=new_cases["new_cases"],mode="lines+markers",name="new_cases",line=dict(color="grey",width=1)))
    return plotly.offline.plot(fig,output_type='div')

def countrywise():
    fig=make_subplots(
        rows=2, cols=3,
        specs=[[{"secondary_y":True},{"secondary_y":True},{"secondary_y":True}],
              [{"secondary_y":True},{"secondary_y":True},{"secondary_y":True}]],
         
    
        subplot_titles=("Total cases","New cases","Total deaths","New Deaths","Total recovered","Active cases"))

    fig.add_trace(go.Bar(x=C["Country"],y=C["Total_cases"],
                        marker=dict(color=C["Total_cases"],coloraxis="coloraxis")),1,1)

    fig.add_trace(go.Bar(x=C["Country"],y=C["New_cases"],
                        marker=dict(color=C["New_cases"],coloraxis="coloraxis")),1,2)

    fig.add_trace(go.Bar(x=C["Country"],y=C["Total_deaths"],
                        marker=dict(color=C["Total_deaths"],coloraxis="coloraxis")),1,3)

    fig.add_trace(go.Bar(x=C["Country"],y=C["New_deaths"],
                        marker=dict(color=C["New_deaths"],coloraxis="coloraxis")),2,1)

    fig.add_trace(go.Bar(x=C["Country"],y=C["Total_recovered"],
                        marker=dict(color=C["Total_recovered"],coloraxis="coloraxis")),2,2)

    fig.add_trace(go.Bar(x=C["Country"],y=C["Active_cases"],
                        marker=dict(color=C["Active_cases"],coloraxis="coloraxis")),2,3)

    fig.update_layout(coloraxis=dict(colorscale="Bluered_r"),showlegend=False,title_text="All countries data")

    fig.update_layout(plot_bgcolor="rgb(350,350,350)")

    return plotly.offline.plot(fig,output_type='div')


def datewise_worldwide_cases():
    Total_Cases=D.groupby("date").sum()['total_cases'].reset_index()
    Death=D.groupby("date").sum()["total_deaths"].reset_index()
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=Total_Cases["date"],y=Total_Cases["total_cases"],mode="lines+markers",name="total_cases",line=dict(color="blue",width=2)))
    fig.add_trace(go.Scatter(x=Death["date"],y=Death["total_deaths"],mode="lines+markers",name="total_deaths",line=dict(color="red",width=2)))
    return plotly.offline.plot(fig,output_type='div')

def daily_confirmed_deaths():
    New_Death=D.groupby("date").sum()["new_deaths"].reset_index()
    Total_Cases=D.groupby("date").sum()['total_cases'].reset_index()
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=Total_Cases["date"],y=New_Death["new_deaths"],mode="lines+markers",name="total_cases",line=dict(color="green",width=2)))
    return plotly.offline.plot(fig,output_type='div')


def countrywise_tests():
    fig=go.Figure()
    df=D.query('location=="India"')
    tests_India=df.groupby("date").sum()["total_tests_per_thousand"].reset_index()
    df2=D.query('location=="United States"')
    tests_US=df2.groupby("date").sum()["total_tests_per_thousand"].reset_index()
    df3=D.query('location=="Denmark"')
    tests_Denmark=df3.groupby("date").sum()["total_tests_per_thousand"].reset_index()
    df3=D.query('location=="Indonesia"')
    tests_Indonesia=df3.groupby("date").sum()["total_tests_per_thousand"].reset_index()
    df4=D.query('location=="China"')
    tests_China=df4.groupby("date").sum()["total_tests_per_thousand"].reset_index()
    df5=D.query('location=="Italy"')
    tests_Italy=df5.groupby("date").sum()["total_tests_per_thousand"].reset_index()
    fig.add_trace(go.Scatter(x=tests_India["date"],y=tests_India["total_tests_per_thousand"],mode="lines+markers",name="tpt_India",line=dict(color="green",width=1)))
    fig.add_trace(go.Scatter(x=tests_US["date"],y=tests_US["total_tests_per_thousand"],mode="lines+markers",name="tpt_USA",line=dict(color="blue",width=1)))
    fig.add_trace(go.Scatter(x=tests_Denmark["date"],y=tests_Denmark["total_tests_per_thousand"],mode="lines+markers",name="tpt_Denmark",line=dict(color="orange",width=1)))
    fig.add_trace(go.Scatter(x=tests_Indonesia["date"],y=tests_Indonesia["total_tests_per_thousand"],mode="lines+markers",name="tpt_Indonesia",line=dict(color="yellow",width=1)))
    fig.add_trace(go.Scatter(x=tests_China["date"],y=tests_China["total_tests_per_thousand"],mode="lines+markers",name="tpt_China",line=dict(color="red",width=1)))
    fig.add_trace(go.Scatter(x=tests_Italy["date"],y=tests_Italy["total_tests_per_thousand"],mode="lines+markers",name="tpt_Italy",line=dict(color="grey",width=1)))
    return plotly.offline.plot(fig,output_type='div')

def total_vs_new_cases():
    New_Cases=D.groupby("date").sum()['new_cases'].reset_index()
    Total_Cases=D.groupby("date").sum()['total_cases'].reset_index()
    fig=go.Figure()
    fig.add_trace(go.Scatter(x=Total_Cases["date"],y=Total_Cases["total_cases"],mode="lines+markers",name="total_cases",line=dict(color="blue",width=1)))
    fig.add_trace(go.Scatter(x=New_Cases["date"],y=New_Cases["new_cases"],mode="lines+markers",name="new_cases",line=dict(color="orange",width=1)))
    return plotly.offline.plot(fig,output_type='div')




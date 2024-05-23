import plotly.express as px
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import io
import warnings
import numpy as np
from pandas.plotting import scatter_matrix
from helper import *
from controllers import DataController ,ProjectController
from PIL import Image
        
# Ignore all warnings
warnings.filterwarnings("ignore")



st.set_page_config(page_title="Explore Your Dataset", page_icon= ':bar_chart:',
                    layout="wide",  
                    initial_sidebar_state="expanded")


with st.sidebar:
    st.image("https://th.bing.com/th/id/OIP.n6a3CTjh1hTTDlLPnSAEKAHaBA?rs=1&pid=ImgDetMain")
    st.title("Automated EDA project")
    st.info ("This project is used to Explore your data set  by easy and interactive dashboard   with preprocessing just upload your data or Explore the project by defult data set (Churn Dataset) :heart_eyes: by:[Mohamed Badr](https://www.linkedin.com/in/mohamed-badr-301378248/?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app) :heart_eyes:")
    file = st.file_uploader("Upload Your Dataset To exlore it and make easy interactive dashboard ,By Defult Churn Data-Set is uploaded ")

    df = load_data(file)
    cat_f= cat(df)
    num_f=num(df)
    target=st.selectbox("Target Column:",df.columns[::-1])

    summary_stat = "📋Basic Information And summary Statistics"
    general_eda = "📊General EDA"
    dashboard = '🎮Interactive Dashboard'

    choice = st.radio("Navigation", [summary_stat,general_eda,dashboard])


if choice== summary_stat:
    
    st.image('https://www.datasciencedegreeprograms.net/wp-content/uploads/2021/08/shutterstock_1642441465-2048x1225.jpg')
    st.header("1-Sample Of Data")
   
    st.dataframe(df.sample())

    st.header("2-Exploratory each feature")
    st.dataframe(feature_insight(df,target))
    
    st.header('3-Statistics')
    st.dataframe(df.describe())
    
    st.header('4-Groupby & Pinvot Plot')
    
    col1 ,col2,col3,col4 =st.columns([.5,.5,.5,.5])
    with col1:

        g1=st.selectbox("1-Select categotical featue 1",cat_f )
    with col2:
        g2=st.selectbox("1-Select categotical featue 2",set(cat_f)-set([g1]))
    with col3:
        val=st.selectbox("1-Select numerical featue",set(num_f))
    with col4:
        agg=st.selectbox("1-Select aggregation fun",set(['mean','sum','min','max']))
    
    k=[g1,g2]

    g,p=group(df[[g1,g2,val]],k,agg)   
    st.dataframe(g)   
    
    st.pyplot(drawpivot(p))
    
if choice == general_eda:
    st.title('Exploratory Data analysis')
    st.image('https://th.bing.com/th/id/OIP.I9CAlMorFphXUKDzzIVqRgHaD4?rs=1&pid=ImgDetMain')
    st.header("1-Target analysis")
    eda_target(df,target)


    st.header("2-Correlation Map")
    # corrplot(df)
   
    st.header("2-Pair Plot")
    #pairplot(df)

if choice == dashboard :
    
    st.title("Play With Feature Visulaizations")
    tap1 ,tap2,tap3 = st.tabs( ["Scatter","Histogram",'boxplot'])
    with tap1:
        fig, ax = plt.subplots()
        col1 ,col2,col3,col4 =st.columns([.5,.5,.5,.5])
        with col1:
            x = st.selectbox("1Chose Feature To Put in X-axis ",num_f )
        with col2:
            y = st.selectbox("2Chose Feature To Put in Y-axis ",num_f )
        with col3:
            color = st.selectbox("Color ",[None]+num_f )
        with col4:
            size = st.selectbox("Size",[None]+num_f )
                                             
        fig=px.scatter(df,x,y,color=color,size=size)
        #=sns.regplot(x=x ,y=y ,data=df,ax=ax)
        st.plotly_chart(fig)

        #   Display the plot in Streamlit
        #st.pyplot(fig)
        
    with tap2:    
        fig, ax = plt.subplots()
        x = st.selectbox("Chose Feature To Put in X-axis  ",num_f )
        sns.histplot(x=x  ,data=df,ax=ax)
    
        # Display the image in Streamlit
        st.pyplot(fig)
        
        analysis_button('Hist plot ',x)
    with tap3:
        fig, ax = plt.subplots()
        col1 ,col2 =st.columns([.5,.5])
        with col2:
            x = st.selectbox("Chose Feature To Put in X-axis   ",cat_f )
        with col1:
            y = st.selectbox("Chose Feature To Put in Y-axis ",num_f )
       
        sns.boxplot(x=x,y=y  ,data=df,ax=ax)
        #   Display the plot in Streamlit
        st.pyplot(fig)
        
        analysis_button('box plot',x)
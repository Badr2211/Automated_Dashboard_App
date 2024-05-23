import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 
import io
import warnings
import numpy as np
from pandas.plotting import scatter_matrix
from models.enums.ResponseSignals import Signals
from controllers import DataController ,ProjectController
from PIL import Image
from models import generate_text

#load the data 
def load_data (path):
    
    
    if path ==None :
        path ='models/WA_Fn-UseC_-Telco-Customer-Churn.csv'
        extention =path.split('.')[-1]
        
        #data_validate
        DataController().validate_uploaded_file(file=path)
 
    else :
        extention =path.name.split('.')[-1]
        
    if extention == 'csv':
       data = pd. read_csv(path)
    elif extention in ("xls", "xlsx"):
        data = pd. read_excel(path)
    elif extention == 'json' :
       data = json.load(path)
    elif extention == 'txt' :
       with open(file_path, 'r') as file:
            data = file.read()
    elif extention == 'db':
        conn = sqlite3.connect(file_path)
        query = "SELECT * FROM ;"
        data = pd.read_sql(query, conn)
        conn.close()
    else:
        raise ValueError(Signals().UNSUPPORTED.value)
    return data

#Explore each feature 
def feature_insight(df,target):
    df = df.astype(str)
    df_unique = pd .DataFrame([[
                    i,
                    #df[i].unique(),
                    #df[i].dtypes,
                    df[i].corr(df[target]) if ( df[i].dtypes != 'object' and  df[target].dtypes != 'object') else None,
                    df[i].isna().sum(),
                    len(df[i].unique())] 
                    for i in df.columns],columns=['Feature',
                                                  #'Unique Values',
                                                  #'dtype',
                                                  'Corr with target',
                                                  'N.null',
                                                  'N.of unique values']).set_index('Feature')
    return df_unique.T

#Clean data
def clean(df,df_ID):
    data =df
    print(data.isnull().sum())
    if data.isnull().sum() .sum() == 0:
        print ('\nNO Null Value')
    else :
        print('\nWarning :Null value ,deal with it')
        for c in data.columns :
            print(c)
            if data[c].dtype !='object' :
                print(c)
                if data[c].isna().sum()> data.shape[0]/4:
                    #print(c,'n')
                    data[c].dropna()
                elif data[c].isna().sum()==0:
                    continue
                else :
                    #print(c,'else')
                    data[c].fillna(data[c].mean(),inplace=True)
            else :
                if data[c] .isna().sum()>0:
                    mode_category = data[c].mode()[0] 
                    data[c].fillna(value=mode_category, inplace=True)
                    
        print(data.isnull().sum())
    if df_ID.is_unique:
        print('\nSample is unique no duplicated')
        
    else :
        print('\ndupplicated , deal with it ...')
        data_unique = data.drop_duplicates(keep='first')
    
    return data

#corr heatmap

def corrplot(data):
    numeric_columns = data.select_dtypes(exclude=['object']).columns
    corr_matrix = data[numeric_columns].corr()

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, ax=ax)
    plt.title('Correlation Heatmap')
    st.pyplot(fig)

def num(data):
    num_feature=[i for  i in data.columns  if data[i].dtype !='object']
    return num_feature

def cat(data):
    cat_feature=[i for  i in data.columns  if data[i].dtype =='object']
    return cat_feature

def eda_target(df,target):
    if df[target].dtypes=='object':
        col1 ,col2 = st.columns([3,2])
        with col1:
            st.subheader("Target Variable Distribution")
            st.bar_chart(df[target].value_counts())
        with col2:
            # Create the pie chart with hole using st.pyplot and matplotlib
            fig, ax = plt.subplots()
            target_counts=df[target].value_counts()
            ax.pie(target_counts, labels=target_counts.index, autopct="%1.1f%%", startangle=140 , **{'wedgeprops': dict(width=0.7)})
            st.subheader(" Target Variable Distribution")

            st.pyplot(fig)

        #df[target].value_counts().plot.bar()
    else :
        #fig, ax = plt.subplots()
        #df[target].hist(bins=20, color='lightgreen', edgecolor='black', alpha=0.7, ax=ax)
        col1,col2 = st.columns([.3,.3])
        with col1:
            fig, ax = plt.subplots()
            sns.kdeplot(df[target], ax=ax)

            #   Display the plot in Streamlit
            st.pyplot(fig)
        with col2:
            fig, ax = plt.subplots()
            sns.boxplot(df[target], ax=ax)
            #   Display the plot in Streamlit
            st.pyplot(fig)


def pairplot(df):
    #sns.pairplot(df)
    fig, ax = plt.subplots()

    scatter_matrix(df, alpha=0.8, figsize=(10, 10), diagonal='hist',ax=ax)

    #   Display the plot in Streamlit
    st.pyplot(fig)
        
def group(data, g_based,agg):
    
    # Specify multiple aggregation functions
    fun = {
        'mean': np.mean,
        'sum': np.sum,
        'min': np.min,
        'max': np.max
    }

    # Perform groupby and calculate multiple aggregations
    g = data.groupby(g_based, as_index=False).agg(fun[agg])
    # Create pivot table
    pivot = g.pivot(index=g_based[0],columns=g_based[1])
    return g , pivot

def drawpivot (pivot):
    fig, ax = plt.subplots()
    cmap = plt.get_cmap('RdBu')
    cmap.set_bad(color='black')
    im = ax.pcolor(pivot, cmap=cmap)

    row_labels =pivot.columns.levels[1]
    col_labels = pivot.index

    ax.set_xticks(np.arange(pivot.shape[1]) + 0.5, minor=False)
    ax.set_yticks(np.arange(pivot.shape[0]) + 0.5, minor=False)

    ax.set_xticklabels(row_labels, minor=False)
    ax.set_yticklabels(col_labels, minor=False)

    plt.xticks(rotation=90)

    fig.colorbar(im)   
    return fig


def describe_img( x,custom_prompt='decribe The img'):
    img_name = f"{x}.png"
    image_path =ProjectController().get_path(img_name) #'histogram.png'
        
    plt.savefig(image_path)
    img_file= Image.open(image_path)
    txt = generate_text(img_file,custom_prompt)
    st.write(txt)

def analysis_button(button_name,x):
    if st.button(f"Analysis The {button_name} Figure"):
        describe_img( x)
        
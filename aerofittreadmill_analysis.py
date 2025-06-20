#import libraries
import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

#setting the page configuration of streamlit dashboard
st.set_page_config(page_title = "Aerofig Treamill Anlaysis" , layout="wide")
st.title("Aerofit Treadmill Data Analysis Dashboard")

#upload the dataset
uploaded_file = st.file_uploader("Please upload yout dataset" , type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    #Basic Data analysis
    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    #Shape of the dataset
    st.subheader("Shape of the dataset")
    st.write("Number of rows and columns in the dataset are:" , df.shape)
    st.write("Columns names of the dataset are:" , df.columns.tolist())

    #create few checkboxes
    st.subheader("Statistics of the dataset")
    data_info = st.checkbox("Show datasey information")
    missing_value = st.checkbox("Show Missing Values")
    statistics = st.checkbox("Show the statistical summary of the dataset")

    if data_info:
        st.write("The data types in this dataset area:" , df.info())
        #df.info() returns none while running the streamlit but gives output on the console or terminal so we can also use type for knowing the datatype
    if missing_value:
        st.write("Missing Values of the dataset are: " , df.isna().sum(axis=0))
    if statistics:
        st.write("Dataset statistics are:" , df.describe())

    st.subheader("Statistics of the dataset using radio button")

    data_info=st.radio("Select Option", ("Data Types", "Missing Values", "Statistics Summary"))
    if data_info == "Data Types":
        st.write("Datatypes are :", df.dtypes)
    elif data_info == "Missing Values":
        st.write("Missing Values are :", df.isnull().sum())
    elif data_info == "Statistics Summary":
        st.write("Statistics summary is :", df.describe())

    #visual analysis of our dataset
    #column selector
    numeric_cols = df.select_dtypes(include=["int64" , "float64"]).columns.tolist()
    categorical_cols= df.select_dtypes(include=["object"]).columns.tolist()

    st.write(numeric_cols)
    st.write(categorical_cols)

    #Uni-variate Analysis
    #count-plot for numerical columns
    st.subheader("Count plot")
    selected_cols = st.selectbox("select a numeric column" ,numeric_cols)
    fig,ax = plt.subplots()
    sns.countplot(x=df[selected_cols] , ax=ax)
    st.pyplot(fig)

    #count-plot for categorical columns
    st.subheader("Count plot")
    cat_cols = st.selectbox("select a categorical column" ,categorical_cols)
    fig,ax = plt.subplots()
    sns.countplot(x=df[cat_cols] , ax=ax)
    st.pyplot(fig)

    #Box plot for numerical coolumns
    st.subheader("Box plots for checking the outliers")
    box_cols = st.selectbox("select a numeric column:" , numeric_cols)
    fig,ax = plt.subplots()
    sns.boxplot(x=df[box_cols] , ax=ax)
    st.pyplot(fig)

    # Histogram for numerical columns
    st.subheader("Histogram for Distribution Check")
    hist_col = st.selectbox("Select a numeric column:", numeric_cols, key="hist_col")
    fig, ax = plt.subplots()
    sns.histplot(df[hist_col], kde=True, ax=ax)
    ax.set_xlabel(hist_col)
    ax.set_ylabel("Frequency")
    st.pyplot(fig)

    #bi-variate analysis
    st.subheader("Bi-variate analysis of our dataset: categorical v/s Numerical")
    num_cols = st.selectbox("Select a numeric column:" , numeric_cols , key ="num1")
    category_cols = st.selectbox("select a categorical column :" , categorical_cols, key="cat1")
    fid , ax = plt.subplots()
    sns.boxplot(x=df[num_cols],y=df[category_cols],ax=ax)
    st.pyplot(fig)

    # # Bi-variate analysis: Scatter plot
    st.subheader("Bi-variate Analysis: Scatter Plot (Numerical vs Numerical)")
    x_axis = st.selectbox("Select X-axis (Numeric column):", numeric_cols, key="scatter_x")
    y_axis = st.selectbox("Select Y-axis (Numeric column):", numeric_cols, key="scatter_y")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)
    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    st.pyplot(fig)

    #Multi-variate analysis
    #Heatmap of our dataset to check correlation
    st.subheader("Co-relation Heatmap")
    fig , ax = plt.subplots(figsize =(10,6))
    sns.heatmap(df[numeric_cols].corr(),annot = True , cmap="magma" , ax=ax)
    st.pyplot(fig)


    #pair-plot
    st.subheader("pair plot ")
    fig = sns.pairplot(df[numeric_cols])
    st.pyplot(fig)
    
else:
    st.write("Please upload the dataset first for the exploratory data analysis")

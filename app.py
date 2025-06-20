import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

st.set_page_config(page_title="Aerofit Traedmill Data Analysis", layout="wide")
st.title("Aerofit Tredmill Data Analysis")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)

    st.subheader("Data Overview")
    st.dataframe(df.head())


    st.subheader("Shape of the Data")
    st.write(df.shape)

    st.subheader("Column Names")
    st.write(df.columns.tolist())

    st.subheader("Statistics of dataset")
    # data_info=st.checkbox("Show Data Types")
    # missing_values=st.checkbox("Show Missing Values")
    # statistics=st.checkbox("Show Statistics summary")

    # if data_info: 
    #     st.write("Datatypes are :",df.info())
    # if missing_values:
    #     st.write("Missing Values are :",df.isnull().sum())
    # if statistics:
    #     st.write("Statistics summary is :",df.describe())
    data_info=st.radio("Select Option", ("Data Types", "Missing Values", "Statistics Summary"))
    if data_info == "Data Types":
        st.write("Datatypes are :", df.info())
    elif data_info == "Missing Values":
        st.write("Missing Values are :", df.isnull().sum())
    elif data_info == "Statistics Summary":
        st.write("Statistics summary is :", df.describe())
    
    #Visual Analysis
    numeric_columns = df.select_dtypes(include=["Int64","Float64"]).columns.tolist()
    categorical_columns = df.select_dtypes(include=["object"]).columns.tolist()

    st.write("Numeric Columns", numeric_columns)
    st.write("categorical columns :", categorical_columns)

    #univariate analysis
    #countplot for numeric columns
    st.subheader("Count Plot for Numeric Columns")
    selected_column = st.selectbox("Select a nummeric column ", numeric_columns)
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.countplot(x=df[selected_column], ax=ax)
    st.pyplot(fig)

    #countplot for categorical columns
    st.subheader("Count Plot for Categorical Columns")
    selected_column_cat = st.selectbox("Select a categorical column ", categorical_columns) 
    fig_cat, ax_cat = plt.subplots(figsize=(10, 5))
    sns.countplot(x=df[selected_column_cat], ax=ax_cat)
    st.pyplot(fig_cat)

    #Box plot for numeric columns
    st.subheader("Box Plot for Numeric Columns")
    selected_numeric_column = st.selectbox("Select a numeric column for box plot", numeric_columns)
    fig_box, ax_box = plt.subplots(figsize=(10, 5))
    sns.boxplot(x=df[selected_numeric_column], ax=ax_box)
    st.pyplot(fig_box)
    
    #hist plot for numeric columns
    st.subheader("Histogram for Numeric Columns")
    selected_hist_column = st.selectbox("Select a numeric column for histogram", numeric_columns)
    fig_hist, ax_hist = plt.subplots(figsize=(10, 5))
    sns.histplot(df[selected_hist_column], kde=True, ax=ax_hist)
    st.pyplot(fig_hist)

    #bivariate analysis
    st.subheader("Bivariate Analysis") 
    num_cols = st.selectbox("Select a numeric column ",numeric_columns,key="num1")
    category_cols = st.selectbox("Select a categorical column ",categorical_columns,key="cat1")
    fig,ax = plt.subplots(figsize=(10, 5))
    sns.boxplot(x=df[category_cols], y=df[num_cols], ax=ax)
    st.pyplot(fig)

    #scatter plot bivariate analysis categorical vs numeric
    st.subheader("Scatter Plot for Categorical vs Numeric Analysis")
    x_col = st.selectbox("Select a numeric column for x-axis", numeric_columns, key="x_col")
    y_col = st.selectbox("Select a numeric column for y-axis", numeric_columns, key="y_col")
    fig_scatter, ax_scatter = plt.subplots(figsize=(10, 5))
    sns.scatterplot(x=df[x_col], y=df[y_col], hue=df[category_cols], ax=ax_scatter)
    st.pyplot(fig_scatter)

    #heatmap

    st.subheader("Heatmap for Correlation")
    fig,ax= plt.subplots(figsize=(10, 5))
    sns.heatmap(df[numeric_columns].corr(), annot=True, cmap="magma", ax=ax)
    st.pyplot(fig)

    #Pairplot
    st.subheader("Pairplot ")
    fig =sns.pairplot(df[numeric_columns])
    st.pyplot(fig)

else:

    st.write("Please upload a CSV file to analyze.")
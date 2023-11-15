#Imports
import streamlit as st
import pandas as pd
import seaborn as sns

st.set_option('deprecation.showPyplotGlobalUse', False)

#Title and sub-header.
st.title("Data Analysis")
st.subheader("Data Analysis Using Python & Streamlit")

#Upload Data set.
upload = st.file_uploader("Upload our dataset (in CSV format)")
if upload is not None:
    data = pd.read_csv(upload)
    
#Show the dataset.
if upload is not None:
    if st.checkbox("Preview Dataset"):
        if st.button("Head"):
            st.write(data.head())
        if st.button("Tail"):
            st.write(data.tail())
            
#Chech the datatype of each column.
if upload is not None:
    if st.checkbox("Data type of each column."):
        st.text("Datatypes")
        st.write(data.dtypes)
        
#Find the shape of the dataset (number of rows and columns).
if upload is not None:
    data_shape = st.radio("What dimension do you want to check?",('Rows', 'Columns'))
    if data_shape == 'Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape == 'Columns':
        st.text("Number of columns")
        st.write(data.shape[1])
        
#Finding Null values in the dataset.
if upload is not None:
    test = data.isnull().values.any()
    if test == True:
        if st.checkbox("Null values in the Dataset"):
            sns.heatmap(data.isnull())
            st.pyplot()
            
    else:
        st.success("Congratulations!!!, No Missing Values")
        
        
#Find Duplicate Values in the Data Set.
if upload is not None:
    test = data.duplicated().any()
    if test == True:
        st.warning("This Dataset contains some duplicate values.")
        dup = st.selectbox("Do you want to remove duplicated values?",\
                        ("Select One", "Yes","No"))
        if dup == "Yes":
            data = data.drop_duplicates()
            st.text("Duplicate Values were Removed")
        if dup == "No":
            st.text("Okay, No problem")
            
#Get the overall statistics about the dataset.
if upload is not None:
    if st.checkbox("Summary of the Dataset"):
        st.write(data.describe(include='all'))
        
#About Section.
if st.button("About App"):
    st.text("Bult with Streamlit")
    st.text("Made with love by Oduor.")
    
if st.checkbox("By"):
    st.success("Arnold Oduor.")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
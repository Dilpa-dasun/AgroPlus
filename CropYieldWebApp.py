
import numpy as np
import pickle
import streamlit as st
import pandas as pd

# loading the saved model
loaded_model = pickle.load(open('C:/Users/shani/Desktop/DilpaAgriv/WebApp/Yield/RFYiledPredictionTrained.pkl', 'rb'))

#creating a function for prediction

def CropYieldPrediction(input_data):
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    return (prediction)


def main():
    
    #Giving a title 
    st.title('Yield Prediction Web App')
     
    
    # Define the data
    data = {'Plant Name': ['Carrot', 'Garlic', 'Patatoes', 'Sweet Patatoes','Wheat', 'Ginger','Onions'],
        'Itrm No.': [1,2,3,4,5,6,7]}

    # Create a Pandas DataFrame
    df = pd.DataFrame(data)

    # Display the table
    st.dataframe(df)
    
    #st.dataframe(df, width=400)

    #Getting the Input data from the user
    #ItemNo,Rainfall (mm),Temperature (Celsius),Pesticides 
       
    ItemNo = st.slider('Item No. (Refer the above legend)', 1, 7,)
    Temperature = st.slider('Temperature in Celsius', 0.0, 50.0,)
    Rainfall = st.slider('Rainfall in mm', 0.0, 2500.0,)
    Pesticides  = st.slider('Pesticides used in Tonnes', 0.0, 250000.0,)
      
    #code for prediction
    diagnosis1 = ''
    
    #creating a button for prediction
    if st.button('Predict Yeild'):
        diagnosis1 = CropYieldPrediction([ItemNo,Rainfall,Temperature,Pesticides])
        
    st.success(diagnosis1)   
    
    # Define the Output data
    data1 = {'Yield Class': ['Lower Low', 'Low', 'Upper Low ', 'Lower Mid', 'Mid', 'Upper Mid', 'Lower High', 'High','Upper High'],
        'Yield(hg/ha)': ['0 - 69248','69249 - 138496','138497 - 207744','207745 - 276992','276993 - 346240','346241 - 415488','415489 - 484739','484740 - 553992','553993 - 6222236']}
        
    df1 = pd.DataFrame(data1)
    st.dataframe(df1)
        
if __name__=='__main__':
    main()
        
        
        
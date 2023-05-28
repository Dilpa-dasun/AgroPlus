import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('RFTrained.pkl', 'rb'))

#creating a function for prediction

def CropRecPrediction(input_data):
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    return (prediction)


def main():
    
    #Giving a title 
    st.title('Crop Recommendation Web App')
    
    #Getting the Input data from the user
    #N,P,K,temperature,humidity,ph,rainfall
    
    #N = st.text_input('Nitrogen Percentage')
    N = st.slider('Nitrogen Percentage', 0.0, 100.0,)
    P = st.slider('Phosporus Percentage', 0.0, 100.0,)
    K = st.slider('Pottasium Percentage', 0.0, 100.0,)
    temperature = st.slider('Temperature in Celsius', 0.0, 50.0,)
    humidity = st.slider('Humidity Percentage', 0.0, 100.0,)
    ph = st.slider('pH level', 0.0, 14.0,)
    rainfall = st.slider('Rainfall in mm', 0.0, 300.0,)
    
    
    #code for prediction
    diagnosis = ''
    
    #creating a button for prediction
    if st.button('Recommend Crop'):
        diagnosis = CropRecPrediction([N,P,K,temperature,humidity,ph,rainfall])
        
    st.success(diagnosis)    
        
        
if __name__=='__main__':
    main()
        
        
        

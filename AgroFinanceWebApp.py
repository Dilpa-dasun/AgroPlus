# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 17:27:00 2023

@author: shani
"""

import numpy as np
import pickle
import streamlit as st
import pandas as pd

def main():
    
    #Giving a title 
    st.title('Agri+ Finance App')
     
    # Define the Output data
    data1 = {'Yield Class': ['Lower Low', 'Low', 'Upper Low ', 'Lower Mid', 'Mid', 'Upper Mid', 'Lower High', 'High','Upper High'],
        'Yield(hg/ha)': ['0 - 69248','69249 - 138496','138497 - 207744','207745 - 276992','276993 - 346240','346241 - 415488','415489 - 484739','484740 - 553992','553993 - 6222236']}
        
    df1 = pd.DataFrame(data1)
    st.dataframe(df1)
    
    SeedTpype = st.selectbox('Select Crop', ('Carrot', 'Garlic', 'Potatoes', 'Sweet Potatoes','Wheat', 'Ginger','Onions'))
    YieldType = st.selectbox('Select Yield Class per above legend', ('Lower-Low', 'Low', 'Upper-Low ', 'Lower-Mid', 'Mid', 'Upper-Mid', 'Lower-High', 'High','Upper-High'))
    LandArea = st.number_input('Enter land area in hectare(ha)')
    PesticideCost = st.number_input('Enter Pesticide Cost per Tonne')
    TransportationCost = st.number_input('Enter Transportation Cost')
    
    if SeedTpype == 'Carrot':
        
        SeedCost = 2000
        UnitPrice = 250
        AvgYield = 3111

        if YieldType == 'Lower-low':
            PestAmt = 2873
            YieldAmt = 900
        elif YieldType == 'Low':
            PestAmt = 2014
            YieldAmt = 1124
        elif YieldType =='Upper-Low':
            PestAmt = 26903
            YieldAmt = 1664
        elif YieldType == 'Lower-Mid':
            PestAmt = 109317
            YieldAmt =2544
        elif YieldType == 'Mid':
            PestAmt =78609
            YieldAmt = 3090
        elif YieldType =='Upper-Mid':
            PestAmt = 18188
            YieldAmt = 3808
        elif YieldType == 'Lower-High':
            PestAmt = 16388
            YieldAmt = 4438
        elif YieldType == 'High':
            PestAmt = 43364  
            YieldAmt = 5110
        elif YieldType == 'Upper-High':
            PestAmt = 50228
            YieldAmt = 5727
        else:
            PestAmt = 0
            YieldAmt = 0
    elif SeedTpype == 'Garlic':
        SeedCost = 1000
        UnitPrice = 600
        AvgYield = 3114

        if YieldType == 'Lower-low':
            PestAmt = 25997
            YieldAmt = 5451
        elif YieldType == 'Low':
            PestAmt = 49814
            YieldAmt = 8867
        elif YieldType =='Upper-Low':
            PestAmt = 35980
            YieldAmt = 1600
        elif YieldType == 'Lower-Mid':
            PestAmt = 35980
            YieldAmt = 2500
        elif YieldType == 'Mid':
            PestAmt = 35980
            YieldAmt = 3200
        elif YieldType =='Upper-Mid':
            PestAmt = 35980
            YieldAmt = 3700
        elif YieldType == 'Lower-High':
            PestAmt = 35980
            YieldAmt = 4500
        elif YieldType == 'High':
            PestAmt = 35980
            YieldAmt = 5100
        elif YieldType == 'Upper-High':
            PestAmt = 35980
            YieldAmt = 6000
        else:
            PestAmt = 0
            YieldAmt = 0
            
    elif SeedTpype == 'Potatoes':
        SeedCost = 1000
        UnitPrice = 300
        AvgYield = 306758.182
        if YieldType == 'Lower-low':
            PestAmt = 29244
            YieldAmt = 37000
        elif YieldType == 'Low':
            PestAmt = 5413
            YieldAmt = 114106
        elif YieldType =='Upper-Low':
            PestAmt = 30285
            YieldAmt = 167002
        elif YieldType == 'Lower-Mid':
            PestAmt = 40073
            YieldAmt = 232832
        elif YieldType == 'Mid':
            PestAmt = 99174
            YieldAmt = 300976
        elif YieldType =='Upper-Mid':
            PestAmt = 37444
            YieldAmt = 367308
        elif YieldType == 'Lower-High':
            PestAmt = 4040
            YieldAmt = 451123
        elif YieldType == 'High':
            PestAmt = 5086
            YieldAmt = 490477
        elif YieldType == 'Upper-High':
            PestAmt = 29244
            YieldAmt = 600000
        else:
            PestAmt = 0
            YieldAmt = 0
            
    elif SeedTpype == 'Sweet Potatoes':
        SeedCost = 1000
        UnitPrice = 300
        AvgYield = 310902.1414
        if YieldType == 'Lower-low':
            PestAmt = 728
            YieldAmt = 29055
        elif YieldType == 'Low':
            PestAmt = 21153
            YieldAmt = 100747
        elif YieldType =='Upper-Low':
            PestAmt = 91890
            YieldAmt = 156289
        elif YieldType == 'Lower-Mid':
            PestAmt = 20440
            YieldAmt = 255060
        elif YieldType == 'Mid':
            PestAmt = 37603
            YieldAmt = 323028
        elif YieldType =='Upper-Mid':
            PestAmt = 47205
            YieldAmt = 373941
        elif YieldType == 'Lower-High':
            PestAmt = 31394
            YieldAmt = 450000
        elif YieldType == 'High':
            PestAmt = 31394
            YieldAmt = 510000
        elif YieldType == 'Upper-High':
            PestAmt = 31394
            YieldAmt = 600000
        else:
            PestAmt = 0
            YieldAmt = 0
        
    elif SeedTpype == 'Wheat':
        SeedCost = 500
        UnitPrice = 300
        AvgYield = 307050.9868

        if YieldType == 'Lower-low':
            PestAmt = 34687
            YieldAmt = 21895
        elif YieldType == 'Low':
            PestAmt = 4781
            YieldAmt = 81564
        elif YieldType =='Upper-Low':
            PestAmt = 32731
            YieldAmt = 160000
        elif YieldType == 'Lower-Mid':
            PestAmt = 32731
            YieldAmt = 250000
        elif YieldType == 'Mid':
            PestAmt = 32731
            YieldAmt = 320000
        elif YieldType =='Upper-Mid':
            PestAmt = 32731
            YieldAmt = 370000
        elif YieldType == 'Lower-High':
            PestAmt = 32731
            YieldAmt = 450000
        elif YieldType == 'High':
            PestAmt = 32731
            YieldAmt = 510000
        elif YieldType == 'Upper-High':
            PestAmt = 32731
            YieldAmt = 600000
        else:
            PestAmt = 0
            YieldAmt = 0
            
    elif SeedTpype == 'Ginger':
        SeedCost = 300
        UnitPrice = 500
        AvgYield = 311383.1376

        if YieldType == 'Lower-low':
            PestAmt = 20799
            YieldAmt = 29984
        elif YieldType == 'Low':
            PestAmt = 4563
            YieldAmt = 105487
        elif YieldType =='Upper-Low':
            PestAmt = 49302
            YieldAmt = 166978
        elif YieldType == 'Lower-Mid':
            PestAmt = 19818
            YieldAmt = 250000
        elif YieldType == 'Mid':
            PestAmt = 19818
            YieldAmt = 320000
        elif YieldType =='Upper-Mid':
            PestAmt = 19818
            YieldAmt = 370000
        elif YieldType == 'Lower-High':
            PestAmt = 19818
            YieldAmt = 450000
        elif YieldType == 'High':
            PestAmt = 19818
            YieldAmt = 510000
        elif YieldType == 'Upper-High':
            PestAmt = 19818
            YieldAmt = 600000
        else:
            PestAmt = 0
            YieldAmt = 0
                    
    elif SeedTpype == 'Onions':
        SeedCost = 1000
        UnitPrice = 150
        AvgYield = 315122.3717

        if YieldType == 'Lower-low':
            PestAmt = 21452
            YieldAmt = 37000
        elif YieldType == 'Low':
            PestAmt = 49319
            YieldAmt = 123809
        elif YieldType =='Upper-Low':
            PestAmt = 69921
            YieldAmt = 143018
        elif YieldType == 'Lower-Mid':
            PestAmt = 21452
            YieldAmt = 250000
        elif YieldType == 'Mid':
            PestAmt = 3727
            YieldAmt = 334202
        elif YieldType =='Upper-Mid':
            PestAmt = 3402
            YieldAmt = 368324
        elif YieldType == 'Lower-High':
            PestAmt = 4744
            YieldAmt = 443988
        elif YieldType == 'High':
            PestAmt = 4568
            YieldAmt = 513524
        elif YieldType == 'Upper-High':
            PestAmt = 3515
            YieldAmt = 622236
        else:
            PestAmt = 0
            YieldAmt = 0
    else:
        SeedCost = 0
        #UnitPirce = 0
    
        
    PredictedPesticideCost = PesticideCost*PestAmt
    #SeedCost = SeedCost
    #TrasnportionCost = TrasnportionCost
    
    TotalCost = PredictedPesticideCost + SeedCost + TransportationCost
     
    YieldIncome = ((YieldAmt*LandArea)/10)*UnitPrice
    AvgYieldIncome = ((AvgYield*LandArea)/10)*UnitPrice
    TotalProfit = YieldIncome - TotalCost
    
    # Define the Output data
    data2 = {'Item': ['Predicted Pesticide Cost', 'Seed Cost', 'Trasnportation Cost', 'Total Cost','Yield Income','Total Profit'],
        'Cost(Rs)': [PredictedPesticideCost,SeedCost,TransportationCost,TotalCost,YieldIncome,TotalProfit]}    
    df2 = pd.DataFrame(data2)
       
    st.metric(label="Total Yield Income", value=YieldIncome, delta= AvgYieldIncome)
    
    #creating a button
    if st.button('Calculate Cost'):
        st.success(st.dataframe(df2))
        
    
        
if __name__=='__main__':
    main()
        
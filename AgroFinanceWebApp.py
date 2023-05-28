#importing libraries
import numpy as np
import pickle
import streamlit as st
import pandas as pd

def main():
    
    #Giving a title 
    st.title('Agri+ Finance App')
     
    # Define the Output data
    data1 = {'Yield Class': ['Lower Low', 'Low', 'Upper Low ', 'Lower Mid', 'Mid', 'Upper Mid', 'Lower High', 'High','Upper High'],
        'Yield(hg/ha)': ['0 - 900','900 - 1200','1200 - 1600','1600 - 2500','2500 - 3000','3000 - 3800','3800 - 4400','4400 - 5100','5100 - 5700']}
        
    df1 = pd.DataFrame(data1)
    st.dataframe(df1)
    
    #input selection parameters
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
            PestAmt = 100
            YieldAmt = 900
        elif YieldType == 'Low':
            PestAmt = 200
            YieldAmt = 1200
        elif YieldType =='Upper-Low':
            PestAmt = 300
            YieldAmt = 1600
        elif YieldType == 'Lower-Mid':
            PestAmt = 400
            YieldAmt =2500
        elif YieldType == 'Mid':
            PestAmt = 500
            YieldAmt = 3000
        elif YieldType =='Upper-Mid':
            PestAmt = 600
            YieldAmt = 3800
        elif YieldType == 'Lower-High':
            PestAmt = 700
            YieldAmt = 4400
        elif YieldType == 'High':
            PestAmt = 800  
            YieldAmt = 5100
        elif YieldType == 'Upper-High':
            PestAmt = 900
            YieldAmt = 5700
        else:
            PestAmt = 0
            YieldAmt = 0
            
    elif SeedTpype == 'Garlic':
        SeedCost = 1000
        UnitPrice = 600
        AvgYield = 3114

        if YieldType == 'Lower-low':
            PestAmt = 100
            YieldAmt = 900
        elif YieldType == 'Low':
            PestAmt = 200
            YieldAmt = 1124
        elif YieldType =='Upper-Low':
            PestAmt = 300
            YieldAmt = 1664
        elif YieldType == 'Lower-Mid':
            PestAmt = 400
            YieldAmt =2544
        elif YieldType == 'Mid':
            PestAmt = 500
            YieldAmt = 3090
        elif YieldType =='Upper-Mid':
            PestAmt = 600
            YieldAmt = 3808
        elif YieldType == 'Lower-High':
            PestAmt = 700
            YieldAmt = 4438
        elif YieldType == 'High':
            PestAmt = 800  
            YieldAmt = 5110
        elif YieldType == 'Upper-High':
            PestAmt = 900
            YieldAmt = 5727
        else:
            PestAmt = 0
            YieldAmt = 0
            
    elif SeedTpype == 'Potatoes':
        SeedCost = 1000
        UnitPrice = 300
        AvgYield = 306758.182
        if YieldType == 'Lower-low':
            PestAmt = 29244
            YieldAmt = 3700
        elif YieldType == 'Low':
            PestAmt = 5413
            YieldAmt = 1141
        elif YieldType =='Upper-Low':
            PestAmt = 30285
            YieldAmt = 1670
        elif YieldType == 'Lower-Mid':
            PestAmt = 40073
            YieldAmt = 2328
        elif YieldType == 'Mid':
            PestAmt = 99174
            YieldAmt = 3009
        elif YieldType =='Upper-Mid':
            PestAmt = 37444
            YieldAmt = 3673
        elif YieldType == 'Lower-High':
            PestAmt = 4040
            YieldAmt = 4511
        elif YieldType == 'High':
            PestAmt = 5086
            YieldAmt = 4904
        elif YieldType == 'Upper-High':
            PestAmt = 29244
            YieldAmt = 6000
        else:
            PestAmt = 0
            YieldAmt = 0
            
    elif SeedTpype == 'Sweet Potatoes':
        SeedCost = 1000
        UnitPrice = 300
        AvgYield = 310902.1414
        if YieldType == 'Lower-low':
            PestAmt = 728
            YieldAmt = 1000
        elif YieldType == 'Low':
            PestAmt = 21153
            YieldAmt = 1507
        elif YieldType =='Upper-Low':
            PestAmt = 91890
            YieldAmt = 1962
        elif YieldType == 'Lower-Mid':
            PestAmt = 20440
            YieldAmt = 2550
        elif YieldType == 'Mid':
            PestAmt = 37603
            YieldAmt = 3230
        elif YieldType =='Upper-Mid':
            PestAmt = 47205
            YieldAmt = 3739
        elif YieldType == 'Lower-High':
            PestAmt = 31394
            YieldAmt = 4500
        elif YieldType == 'High':
            PestAmt = 31394
            YieldAmt = 5100
        elif YieldType == 'Upper-High':
            PestAmt = 31394
            YieldAmt = 6000
        else:
            PestAmt = 0
            YieldAmt = 0
        
    elif SeedTpype == 'Wheat':
        SeedCost = 500
        UnitPrice = 300
        AvgYield = 307050.9868

        if YieldType == 'Lower-low':
            PestAmt = 34687
            YieldAmt = 2189
        elif YieldType == 'Low':
            PestAmt = 4781
            YieldAmt = 5000
        elif YieldType =='Upper-Low':
            PestAmt = 32731
            YieldAmt = 6000
        elif YieldType == 'Lower-Mid':
            PestAmt = 32731
            YieldAmt = 8156
        elif YieldType == 'Mid':
            PestAmt = 32731
            YieldAmt = 9000
        elif YieldType =='Upper-Mid':
            PestAmt = 32731
            YieldAmt = 9500
        elif YieldType == 'Lower-High':
            PestAmt = 32731
            YieldAmt = 4500
        elif YieldType == 'High':
            PestAmt = 32731
            YieldAmt = 5100
        elif YieldType == 'Upper-High':
            PestAmt = 32731
            YieldAmt = 6000
        else:
            PestAmt = 0
            YieldAmt = 0
            
    elif SeedTpype == 'Ginger': 
        SeedCost = 300
        UnitPrice = 500
        AvgYield = 311383.1376

        if YieldType == 'Lower-low':
            PestAmt = 20799
            YieldAmt = 2998
        elif YieldType == 'Low':
            PestAmt = 4563
            YieldAmt = 1054
        elif YieldType =='Upper-Low':
            PestAmt = 49302
            YieldAmt = 1669
        elif YieldType == 'Lower-Mid':
            PestAmt = 19818
            YieldAmt = 2501
        elif YieldType == 'Mid':
            PestAmt = 19818
            YieldAmt = 3200
        elif YieldType =='Upper-Mid':
            PestAmt = 19818
            YieldAmt = 3700
        elif YieldType == 'Lower-High':
            PestAmt = 19818
            YieldAmt = 4500
        elif YieldType == 'High':
            PestAmt = 19818
            YieldAmt = 5100
        elif YieldType == 'Upper-High':
            PestAmt = 19818
            YieldAmt = 6000
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
            YieldAmt = 1238
        elif YieldType =='Upper-Low':
            PestAmt = 69921
            YieldAmt = 1430
        elif YieldType == 'Lower-Mid':
            PestAmt = 21452
            YieldAmt = 2500
        elif YieldType == 'Mid':
            PestAmt = 3727
            YieldAmt = 3342
        elif YieldType =='Upper-Mid':
            PestAmt = 3402
            YieldAmt = 3683
        elif YieldType == 'Lower-High':
            PestAmt = 4744
            YieldAmt = 4439
        elif YieldType == 'High':
            PestAmt = 4568
            YieldAmt = 5135
        elif YieldType == 'Upper-High':
            PestAmt = 3515
            YieldAmt = 6222
        else:
            PestAmt = 0
            YieldAmt = 0
    else:
        SeedCost = 0
        #UnitPirce = 0
    
    
    #calculating costs
    PredictedPesticideCost = PesticideCost*PestAmt
       
    TotalCost = PredictedPesticideCost + SeedCost + TransportationCost
     
    #calculating yeild income
    YieldIncome = ((YieldAmt*LandArea)/10)*UnitPrice
    AvgYieldIncome = ((AvgYield*LandArea)/10)*UnitPrice
    #calculating totol profit
    TotalProfit = YieldIncome - TotalCost
    
    # Define the Output data
    data2 = {'Item': ['Predicted Pesticide Cost', 'Seed Cost', 'Trasnportation Cost', 'Total Cost','Yield Income','Total Profit'],
        'Cost(Rs)': [PredictedPesticideCost,SeedCost,TransportationCost,TotalCost,YieldIncome,TotalProfit]}    
    df2 = pd.DataFrame(data2)
    
    
    result_container = st.empty()
    #creating a button
    if st.button('Calculate Cost'):
        result_container.text(st.dataframe(df2))
    
    #strategies  
          
    
    if SeedTpype == 'Carrot' :
        if TotalProfit > 0:
            data3 = {'Suggested Strategies': ["Diversification of crops: The farmer can explore the possibility of growing other crops alongside carrots. This will not only increase the farmer's income but also mitigate the risks associated with relying solely on one crop. The farmer can consult with agricultural experts and government institutions to determine which crops will be suitable for the local climate and market demand.",
            "Value addition: The farmer can explore the possibility of processing carrots into different products such as carrot juice, carrot jam, and carrot pickles. This will increase the value of the product and generate additional income for the farmer. The farmer can also explore the possibility of selling the processed products in different markets to increase their customer base.",
            "Agricultural training and education: The farmer can attend training programs and workshops organized by the government or private sector to learn modern farming techniques, new technologies, and best practices. This will help the farmer improve their productivity, reduce costs, and increase yields.",
            "Microfinance and investment opportunities: The farmer can explore the possibility of accessing microfinance or investment opportunities from banks, cooperatives, and other financial institutions. These can provide the farmer with the necessary capital to invest in their farm, improve their infrastructure, and expand their operations.",
            "Cooperative farming: The farmer can join a cooperative society or group with other small-scale farmers in the area to pool their resources, share knowledge, and benefit from economies of scale. This will provide the farmer with access to new markets, better bargaining power, and a support system that can help them overcome the challenges associated with farming in a remote area.",
            "Use of technology: The farmer can explore the use of technology such as mobile applications, online marketplaces, and weather forecasting tools to improve their farming practices and marketing strategies. This can help the farmer access a wider customer base and increase their profits."]}    
            df3 = pd.DataFrame(data3)
        else:
            data3 = {'Suggested Strategies': ["Diversify the crop: Consider planting different crops in addition to carrots, such as onions or potatoes. This will help spread the risk of crop failure and provide additional sources of income.",
            "Improve soil fertility: Conduct a soil test and amend the soil with necessary nutrients to optimize carrot growth. Using organic fertilizers can also help improve soil health in the long term.",
            "Implement pest and disease control measures: Properly identifying and treating pests and diseases can reduce crop loss and improve yield. Consider implementing integrated pest management strategies that include both chemical and non-chemical control methods.",
            "Explore new markets: Identify new markets to sell the carrot crop, such as local supermarkets, hotels, or restaurants. Build relationships with potential buyers to establish a consistent customer base.",
            "Increase efficiency in operations: Evaluate the farm's operations and identify areas where efficiency can be improved, such as reducing waste, optimizing water usage, and implementing proper storage and handling practices.",
            "Participate in farmer groups or cooperatives: Joining farmer groups or cooperatives can provide access to resources such as shared equipment, bulk purchases, and knowledge sharing. This can help reduce costs and increase profits."]}    
            df3 = pd.DataFrame(data3)
    elif SeedTpype == 'Garlic':
        if TotalProfit > 0:
            data3 = {'Suggested Strategies': ["Diversify crops: One way to increase income and reduce risk is to grow different crops. The farmer can consider growing other crops alongside ginger such as turmeric, garlic, and other spices that can thrive in the local climate and have good market demand.",
            "Value-added products: The farmer can consider processing the ginger into value-added products like ginger paste, ginger powder, and ginger tea which can fetch a higher price in the market. They can also explore creating new products using ginger such as ginger candy, ginger beer, or ginger flavored snack",
            "Farmer's Market: Attending a local farmer's market can be a great way to sell produce directly to consumers, who are often willing to pay a premium for locally grown and fresh produce. This can help increase profits and build a customer base.",
            "Group farming: Farmers can form groups or cooperatives to jointly cultivate and market their produce. This can help reduce costs, increase bargaining power, and enable access to bigger markets",
            "Online Marketplaces: The farmer can consider selling their produce online using e-commerce platforms that specialize in selling farm produce. This can increase visibility, expand the customer base, and help reach buyers beyond local markets.",
            "Government Grants: The farmer can explore accessing government grants or subsidies to invest in their farm, purchase equipment or improve infrastructure. There are several government programs that aim to support small-scale farmers."]}    
            df3 = pd.DataFrame(data3)
        else:
            data3 = {'Suggested Strategies': ["Soil testing: Conduct a soil test to determine the nutrient levels and pH of the soil. Based on the results, apply fertilizers and lime to improve soil fertility.",
            "Crop rotation: Rotate ginger with other crops to reduce pest and disease pressure, as well as maintain soil health.",
            "Pest and disease management: Implement effective pest and disease management strategies to reduce crop losses. This could include using natural pest repellents, crop rotation, and proper sanitation.",
            "Harvesting and post-harvest handling: Proper harvesting and post-harvest handling techniques can help reduce crop losses. Ginger should be harvested when the leaves start to turn yellow, and the rhizomes should be washed, dried, and stored properly.",
            "Value addition: Consider adding value to the ginger crop by processing it into value-added products such as ginger candy, ginger tea, and ginger oil. This can increase profits and reduce losses",
            "Market access: Identify potential buyers and markets for the ginger crop. This could include local markets, restaurants, and food processors. Developing direct relationships with buyers can help reduce marketing costs and increase profits."]}    
            df3 = pd.DataFrame(data3)
    else:
        print("GOOD")
        
    
    if st.button('Suggest Strategies'):
        #st.success(st.dataframe(df3))
        result_container.text(st.dataframe(df3))
    
        
if __name__=='__main__':
    main()
        

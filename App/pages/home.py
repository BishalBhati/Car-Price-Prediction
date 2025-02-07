import streamlit as st

st.title("Car Price Prediction")

col1 , col2 = st.columns([2,1])

with col1:
    st.write("The Car Price Prediction model is a machine learning project designed to estimate the selling price of a car based on various features using Linear Regression. Linear Regression is a popular and straightforward algorithm that models the relationship between a dependent variable (the car price) and one or more independent variables (such as mileage, age, brand, fuel type, etc.). The model is trained on historical data, where it learns to predict the car price by fitting a line through the data points in such a way that it minimizes the difference between the actual prices and the predicted prices.")

with col2:
    st.image("B:\\WORK\\STUDY\\MCA\\SEM-III\\Project\\Car Price Prediction Model\\App\\img1.png", width=300)

col3 , col4 = st.columns([1,2])

with col3:
    st.image("B:\\WORK\\STUDY\\MCA\\SEM-III\\Project\\Car Price Prediction Model\\App\\img2.png")

with col4:
    st.write("In this model, the key features influencing car price are carefully selected and pre-processed to ensure the model's accuracy. The dataset might include features like the car's age, engine size, number of kilometers driven, and other relevant attributes. After training, the model is evaluated using performance metrics such as  R-squared, which provide insights into how well the model generalizes to unseen data.. Overall, this Car Price Prediction model demonstrates the effective application of Linear Regression in real-world scenarios where accurate price estimation is crucial.")
import streamlit as st
import requests

st.title('Income Preditor')

# age = st.slider('Sepal Length', 4.0, 8.0)
# sepal_width = st.slider('Sepal Width', 2.0, 5.0)
# petal_length = st.slider('petal Length', 1.0, 6.9)
# petal_width1 = st.slider('petal Width1', 0.0, 2.5)
# sepal_length1 = st.slider('Sepal Length1', 4.0, 8.0)
# sepal_width1 = st.slider('Sepal Width1', 2.0, 5.0)

age = st.slider('Age', 0, 100, 25)

workclass = st.selectbox('Workclass', ['Private', 'State-gov', 'Federal-gov', 'Self-emp-not-inc','Self-emp-inc', 'Local-gov', 'Without-pay', 'Never-worked'])

fnlwgt = st.number_input('FNLWGT', min_value=0, value=1)

education = st.selectbox('Education', ['HS-grad', 'Some-college', '7th-8th', '10th', 'Doctorate',
       'Prof-school', 'Bachelors', 'Masters', '11th', 'Assoc-acdm',
       'Assoc-voc', '1st-4th', '5th-6th', '12th', '9th', 'Preschool'])

education_num = st.slider('Education Num', 1, 16, 10)
marital_status = st.selectbox('Marital Status', ['Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent', 'Married-AF-spouse'])
occupation = st.selectbox('Occupation', ['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty', 'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving', 'Priv-house-serv', 'Protective-serv', 'Armed-Forces'])
relationship = st.selectbox('Relationship', ['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried'])
race = st.selectbox('Race', ['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black'])
sex = st.selectbox('Sex', ['Male', 'Female'])
capital_gain = st.number_input('Capital Gain', min_value=0, value=0)
capital_loss = st.number_input('Capital Loss', min_value=0, value=0)
hours_per_week = st.slider('Hours per Week', 1, 100, 40)
native_country = st.selectbox('Native Country', ['United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada', 'Germany', 'Outlying-US(Guam-USVI-etc)', 'India', 'Japan', 'Greece', 'South', 'China', 'Cuba', 'Iran', 'Honduras', 'Philippines', 'Italy', 'Poland', 'Jamaica', 'Vietnam', 'Mexico', 'Portugal', 'Ireland', 'France', 'Dominican-Republic', 'Laos', 'Ecuador', 'Taiwan', 'Haiti', 'Columbia', 'Hungary', 'Guatemala', 'Nicaragua', 'Scotland', 'Thailand', 'Yugoslavia', 'El-Salvador', 'Trinadad&Tobago', 'Peru', 'Hong', 'Holand-Netherlands'])

#Convert to float
age = int(age)
fnlwgt = int(fnlwgt)
education_num = int(education_num)
capital_gain = int(capital_gain)
capital_loss = int(capital_loss)
hours_per_week = int(hours_per_week)

input_data = {
            "features": [age, workclass, fnlwgt, education, education_num, marital_status, occupation, relationship, race, 
                         sex, capital_gain, capital_loss, hours_per_week, native_country]  
              }  
st.write(input_data)
response = requests.post('http://backend:8000/predict/', json=input_data)
st.write(response.json())
prediction = response.json()
st.write(f"Predicted Category: {prediction}")
import streamlit as st

st.set_page_config(
    page_title="Email spam detection"
)





import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import streamlit as st
from PIL import Image




raw_mail_data = pd.read_csv('mail_data.csv',encoding='ISO-8859-1')
mail_data = raw_mail_data.where((pd.notnull(raw_mail_data)),'')
mail_data.loc[mail_data['Category'] == 'spam', 'Category',] = 0
mail_data.loc[mail_data['Category'] == 'ham', 'Category',] = 1
X = mail_data['Message']
Y = mail_data['Category']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)
feature_extraction = TfidfVectorizer(min_df = 1, stop_words='english', lowercase=True)
X_train_features = feature_extraction.fit_transform(X_train)
X_test_features = feature_extraction.transform(X_test)
# convert Y_train and Y_test values as integers
Y_train = Y_train.astype('int')
Y_test = Y_test.astype('int')
model = LogisticRegression()
model.fit(X_train_features, Y_train)
prediction_on_training_data = model.predict(X_train_features)
accuracy_on_training_data = accuracy_score(Y_train, prediction_on_training_data)
prediction_on_test_data = model.predict(X_test_features)
accuracy_on_test_data = accuracy_score(Y_test, prediction_on_test_data)

header="""

<style>
.topnav {
    background-color: #333;
    overflow: hidden;
    border-radius: 5px;
}

/* Style the links inside the navigation bar */
.topnav a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

/* Change the color of links on hover */
.topnav a:hover {
  background-color: #ddd;
  color: black;
}

/* Add a color to the active/current link */
.topnav a.active {
  background-color: #FF4848;
  color: white;
}

/* Right-aligned section inside the top navigation */
.topnav-right {
  float: right;
}

</style>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.3.0/font/bootstrap-icons.css">
<body style="background-color:powderblue;"><div class="topnav">
  <a class="active" href="/">Home</a>
  <div class="topnav-right">
    <a href="contact">Contact</a>
    <a href="about">About</a>
  </div>
</div>

"""
image = Image.open('static/fssmv2.png')


st.markdown(header,unsafe_allow_html=True)
st.markdown('<br/>', unsafe_allow_html=True)

#st.markdown("<h2 style='text-align: center; color: #white;'>Email Spam Classifier</h2>", unsafe_allow_html=True)
st.image(image, width=700,use_column_width='auto')

st.markdown('<br/>', unsafe_allow_html=True)




input_mail = st.text_area("Enter the email")
input_mail=[input_mail]

if st.button('Predict'):
    # convert text to feature vectors

    input_data_features = feature_extraction.transform(input_mail)

    # making prediction

    prediction = model.predict(input_data_features)


    if (prediction[0]==0):
        st.markdown('<h2 style="text-align: center; color:red; border-style: dotted; margin:30px 200px; padding: 50px 20px;  border-color: red;">SPAM</h2>', unsafe_allow_html=True)
    else:
        st.markdown('<h2 style="text-align: center; color:green; border-style: dotted; margin:30px 200px; padding: 50px 20px;  border-color: green;">NOT SPAM</h2>', unsafe_allow_html=True)

footer="""
<style>
.topnav1 {
    overflow: hidden;
}

/* Style the links inside the navigation bar */
.topnav1 a {
  float: left;
  color: #333;
  text-align: center;
  padding: 14px 0;
  margin-right: 25px;
  text-decoration: none;
  font-size: 17px;
}

/* Add a color to the active/current link */
.topnav1 a.active1 {
  color: #333;
}

/* Right-aligned section inside the top navigation */
.topnav1-right {
  float: right;
}
.topnav1-right a{
  margin:0;
}
</style>

<div class="topnav1">
    <a href="#news"><i class="bi bi-facebook"></i></a>
    <a href="#contact"><i class="bi bi-instagram"></i></a>
    <a href="#search"><i class="bi bi-twitter"></i></a>
    <a href="#about"><i class="bi bi-github"></i></a>   
  <div class="topnav1-right">
    <a>2022 Copyrights, all rights reserved.
  </div>
</div>
<footer>
<p>
</body>


"""


st.markdown('<br/>', unsafe_allow_html=True)


st.markdown('<br/>', unsafe_allow_html=True)
st.markdown('<br/>', unsafe_allow_html=True)
st.markdown('<br/>', unsafe_allow_html=True)

#st.image(image, width=700)

st.markdown(footer,unsafe_allow_html=True)
import streamlit as st

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




st.markdown(header,unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>CONTACT US</h2>", unsafe_allow_html=True)

contact = """

<br/><br/>
Ahmed ACH-CHATIBI <br/>
email :  achchatibiahmed07@gmail.com <br/>
linkedin : www.linkedin.com/in/ahmed-ach-chatibi <br/>
<br/><br/>
El mustapha EJ-JAMAAY <br/>
email : mustejjamaay2001@gmail.com <br/>
linkedin : www.linkedin.com/in/el-mustapha-ej-jamaay-772087182 <br/>

"""

st.markdown(contact,unsafe_allow_html=True)


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
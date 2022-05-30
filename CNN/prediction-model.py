# -*- coding: utf-8 -*-
"""
Created on Sun May  1 15:08:52 2022

@author: Unbeknownstguy
"""

import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
import pandas as pd

# st.set_page_config(page_title="Breast Cancer Prediction", layout="wide")
st.set_page_config(page_title="Breast Cancer Tumor Prediction")

hide_st_style = """
            <style>

            footer {visibility: hidden;}

            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# state = _get_state()

# state.page_config = st.set_page_config(
#     page_title="BPJV SI Database Manager test",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )

components.html(
    """
    <!DOCTYPE html>
<html>

<head>

	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">

	<title>Basic Header</title>

	<link rel="stylesheet" href="assets/demo.css">
	<link rel="stylesheet" href="assets/header-fixed.css">
	<link href='https://fonts.googleapis.com/css?family=Cookie' rel='stylesheet' type='text/css'>

    <style>
    .header-fixed {
	background-color:#292c2f;
	box-shadow:0 1px 1px #ccc;
	padding: 20px 40px;
	height: 80px;
	color: #ffffff;
	box-sizing: border-box;
	top:-100px;

	-webkit-transition:top 0.3s;
	transition:top 0.3s;
}

.header-fixed .header-limiter {
	max-width: 1200px;
	text-align: center;
	margin: 0 auto;
}

/*	The header placeholder. It is displayed when the header is fixed to the top of the
	browser window, in order to prevent the content of the page from jumping up. */

.header-fixed-placeholder{
	height: 80px;
	display: none;
}

/* Logo */

.header-fixed .header-limiter h1 {
	float: left;
	font: normal 28px Cookie, Arial, Helvetica, sans-serif;
	line-height: 40px;
	margin: 0;
}

.header-fixed .header-limiter h1 span {
	color: #5383d3;
}

/* The navigation links */

.header-fixed .header-limiter a {
	color: #ffffff;
	text-decoration: none;
}

.header-fixed .header-limiter nav {
	font:16px Arial, Helvetica, sans-serif;
	line-height: 40px;
	float: right;
}

.header-fixed .header-limiter nav a{
	display: inline-block;
	padding: 0 5px;
	text-decoration:none;
	color: #ffffff;
	opacity: 0.9;
}

.header-fixed .header-limiter nav a:hover{
	opacity: 1;
}

.header-fixed .header-limiter nav a.selected {
	color: #608bd2;
	pointer-events: none;
	opacity: 1;
}

/* Fixed version of the header */

body.fixed .header-fixed {
	padding: 10px 40px;
	height: 50px;
	position: fixed;
	width: 100%;
	top: 0;
	left: 0;
	z-index: 1;
}

body.fixed .header-fixed-placeholder {
	display: block;
}

body.fixed .header-fixed .header-limiter h1 {
	font-size: 24px;
	line-height: 30px;
}

body.fixed .header-fixed .header-limiter nav {
	line-height: 28px;
	font-size: 13px;
}


/* Making the header responsive */

@media all and (max-width: 600px) {

	.header-fixed {
		padding: 20px 0;
		height: 75px;
	}

	.header-fixed .header-limiter h1 {
		float: none;
		margin: -8px 0 10px;
		text-align: center;
		font-size: 24px;
		line-height: 1;
	}

	.header-fixed .header-limiter nav {
		line-height: 1;
		float:none;
	}

	.header-fixed .header-limiter nav a {
		font-size: 13px;
	}

	body.fixed .header-fixed {
		display: none;
	}

}

/*
	 We are clearing the body's margin and padding, so that the header fits properly.
	 We are also adding a height to demonstrate the scrolling behavior. You can remove
	 these styles.
 */

body {
	margin: 0;
	padding: 0;
	height: 1500px;
}
    </style>

</head>

<body>

<header class="header-fixed">

	<div class="header-limiter">

		<h1><a href="#">Breast Cancer Tumor <span>Prediction</span></a></h1>

		<nav>
			<a href="" class="selected">Home</a>
			<a href="">About</a>
			<a href="">News</a>
			<a href="">Donate</a>
			<a href="">Contact</a>
		</nav>

	</div>

</header>

<!-- You need this element to prevent the content of the page from jumping up -->
<div class="header-fixed-placeholder"></div>

<!-- The content of your page would go here. -->




<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
<script>

	$(document).ready(function(){

		var showHeaderAt = 150;

		var win = $(window),
				body = $('body');

		// Show the fixed header only on larger screen devices

		if(win.width() > 400){

			// When we scroll more than 150px down, we set the
			// "fixed" class on the body element.

			win.on('scroll', function(e){

				if(win.scrollTop() > showHeaderAt) {
					body.addClass('fixed');
				}
				else {
					body.removeClass('fixed');
				}
			});

		}

	});

</script>


<!-- Demo ads. Please ignore and remove. -->
<script src="http://cdn.tutorialzine.com/misc/enhance/v3.js" async></script>


</body>

</html>

    """,
    height=80,
)






# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# def remote_css(url):
#     st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

# def icon(icon_name):
#     st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

# local_css("C:/Users/Unbeknownstguy/Documents/GitHub/Projects/Machine_Learning/Handling-Missing-Data-Problem-Using-KNN-in-EHRs-for-Cancer-Prediction/3_CNN/style.css")
# remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

# # icon("search")
# selected = st.text_input("", "Search...")
# button_clicked = st.button("OK")


# c1, c2, c3, c4, c5 = st.columns(5)

# c1.button("Home")
# c2.button("About")
# c3.button("News")
# c4.button("Donate")
# c5.button("Contact")




#loading saved model
loaded_model = keras.models.load_model('C:/Users/Unbeknownstguy/Documents/GitHub/Projects/Machine_Learning/Handling-Missing-Data-Problem-Using-KNN-in-EHRs-for-Cancer-Prediction/3_CNN/model.h5')

def Prediction(input_data):
    
    cancer_dataset = pd.read_csv('C:/Users/Unbeknownstguy/Documents/GitHub/Projects/Machine_Learning/Handling-Missing-Data-Problem-Using-KNN-in-EHRs-for-Cancer-Prediction/Dataset/data.csv')
    
    columns = ['radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'concavity_mean', 'radius_se', 'perimeter_se', 'area_se', 'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'compactness_worst', 'concavity_worst']
    
    X_new = pd.DataFrame(cancer_dataset, columns=columns)
    
    scaler = StandardScaler()
    
    scaler.fit_transform(X_new)
    
    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshape = input_data_as_numpy_array.reshape(1, -1)

    std_data = scaler.transform(input_data_reshape)

    prediction = loaded_model.predict(std_data)


    if prediction[0]<=0.5:
        return "Benign"
    else:
        return "Malignant"
        
        
        
def main():
    
    
    col1, col2 = st.columns(2)

    
    try:
        radius_mean = col1.text_input('Radius Mean')
        if 6.9810 <= float(radius_mean) <= 28.1100:
            pass
        else:
            col1.error("Not in range")
    except ValueError:
        pass


    texture_mean = col1.text_input('Texture Mean')
    try:
        if 9.7100 <= float(texture_mean) <= 39.2800:
            pass
        else:
            col1.error("Not in range")
    except ValueError:
        pass


    perimeter_mean = col1.text_input('Perimeter Mean')
    try:
        if 43.7900 <= float(perimeter_mean) <= 188.5000:
            pass
        else:
            col1.error("Not in range")
    except ValueError:
        pass


    area_mean = col1.text_input('Area Mean')
    try:
        if 143.5000 <= float(area_mean) <= 2501.0000:
            pass
        else:
            col1.error("Not in range")
    except ValueError:
        pass


    concavity_mean = col1.text_input('Concavity Mean')
    try:
        if 0.0000 <= float(concavity_mean) <= 0.4268:
            pass
        else:
            col1.error("Not in range")
    except ValueError:
        pass


    radius_se = col1.text_input('Radius Se')
    try:
        if 0.1115 <= float(radius_se) <= 2.8730:
            pass
        else:
            col1.error("Not in range")
    except ValueError:
        pass


    perimeter_se = col1.text_input('Perimeter Se')
    try:
        if 0.7570 <= float(perimeter_se) <= 21.9800:
            pass
        else:
            col1.error("Not in range")
    except ValueError:
        pass


    area_se = col2.text_input('Area Se')
    try:
        if 6.8020 <= float(area_se) <= 542.2000:
            pass
        else:
            col2.error("Not in range")
    except ValueError:
        pass


    radius_worst = col2.text_input('Radius Worst')
    try:
        if 7.9300 <= float(radius_worst) <= 36.0400:
            pass
        else:
            col2.error("Not in range")
    except ValueError:
        pass


    texture_worst = col2.text_input('Texture Worts')
    try:
        if 12.0200 <= float(texture_worst) <= 49.5400:
            pass
        else:
            col2.error("Not in range")
    except ValueError:
        pass


    perimeter_worst = col2.text_input('Perimeter worst')
    try:
        if 50.4100 <= float(perimeter_worst) <= 251.2000:
            pass
        else:
            col2.error("Not in range")
    except ValueError:
        pass


    area_worst = col2.text_input('Area Wrost')
    try:
        if 185.2000 <= float(area_worst) <= 4254.0000:
            pass
        else:
            col2.error("Not in range")
    except ValueError:
        pass


    compactness_worst = col2.text_input('Compactness Wrost')
    try:
        if 0.0273 <= float(compactness_worst) <= 1.0580:
            pass
        else:
            col2.error("Not in range")
    except ValueError:
        pass


    concavity_worst = col2.text_input('Concavity Worst')
    try:
        if 0.0000 <= float(concavity_worst) <= 1.2520:
            pass
        else:
            col2.error("Not in range")
    except ValueError:
        pass
    
    
    # code for prediction
    diagnosis = ''
    
    try:
        if st.button('Result'):
            diagnosis = Prediction([radius_mean, texture_mean, perimeter_mean, area_mean, concavity_mean, radius_se, perimeter_se, area_se, radius_worst, texture_worst, perimeter_worst, area_worst, compactness_worst, concavity_worst])
                    
        st.success(diagnosis)
    
    except ValueError:
        st.error("Cells Should not be empty")
    
    
if __name__ == "__main__":
    main()


from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import VotingClassifier
import uuid

#Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title='Website-python', page_icon=":tada:", layout="wide")

feat = ['ImageBase',
 'VersionInformationSize',
 'SectionsMaxEntropy',
 'MajorOperatingSystemVersion',
 'ResourcesMinSize',
 'SizeOfStackReserve',
 'Characteristics',
 'SizeOfInitializedData',
 'MajorSubsystemVersion',
 'ResourcesNb',
 'Subsystem',
 'ResourcesMinEntropy',
 'BaseOfData',
 'SizeOfImage',
 'MajorLinkerVersion']

mlData = {}

inparr=np.array([2,	1,	5,	6,	9,	2,	8,	5,	6,	1,	2,	3,	0,	3,	9])
inparr = inparr.reshape(1, -1) 

# Load the trained model
with open('ensemble_model.pkl', 'rb') as f:
    ensemble_model = pickle.load(f)

# Define a function to detect ransomware
def detect_ransomware(X):
    # Make predictions using the ensemble model
    predictions = ensemble_model.predict(X)
    # Return the result
    return bool(sum(predictions))

def app():
    # Allow the user to upload a file
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv", key="file_uploader")
    if uploaded_file is not None:
        key = uploaded_file.name
        # Read the input data from the uploaded file
        data = pd.read_csv(uploaded_file)
        x = data.columns.to_numpy()
        x = np.array(x)
        x = x.reshape(1,-1)
        
        # Use the detect_ransomware function to make predictions on the input data
        result = detect_ransomware(x)
        # Display the result
        if result:
            st.write("The uploaded file is ransomware.")
        else:
            st.write("The uploaded file is not ransomware.")

#use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style2.css")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_DbCYKfCXBZ.json")
lottie2=load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_ua1cgice.json")
lottie3=load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_lewuuhar.json")
lottie4=load_lottieurl("https://assets8.lottiefiles.com/private_files/lf30_ovEPsq.json")
img_contact_form = Image.open('image1.jpg')
img_lottie_animation = Image.open('image2.png')

#---- HEADER SECTION ----
with st.container():
    st.markdown(f"<h1 style='text-align: center; color: grey;'>Detect Ransomware</h1>", unsafe_allow_html=True)
    st.subheader("Hi, Good Day :wave: ")
    st.write("I am passionate about Python and VBA to be more efficient and effective in business settings.")
    st.write("[My Github >](https://github.com/joydas-123)")
    st.write("Upload a CSV file to Detect the ransomware that has encrypted your data.")
    app()
    


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What is Ransomware?")
        st.write("##")
        st.write(
            """
            Ransomware is a growing threat to businesses and individuals alike. This malicious software infects computer systems and networks, encrypting files and making them inaccessible to the rightful owner. Attackers then demand a ransom payment in exchange for the decryption key needed to unlock the files. The consequences of a ransomware attack can be devastating, ranging from disrupted operations to financial loss and stolen data. To prevent such attacks, it is important to implement strong security measures and to regularly backup important data. By staying vigilant and taking proactive steps, you can protect yourself from the damaging effects of ransomware.
            """
            )
        st.write("[LinkedIn >](https://www.linkedin.com/in/shakil-ahmed-607158173/)")
        with right_column:
            st_lottie(lottie_coding, height=300, key="coding")


#---- PROJECTS ----
with st.container():
    st.write("---")
    image_column, text_column = st.columns((2))
    
    with image_column:
        st_lottie(lottie3, height=300, key='Car')
    
        with text_column:
            st_lottie(lottie2, height=300, key='Boy')

with st.container():
    st.markdown(f"<h1 style='text-align: center'>About Us</h1>", unsafe_allow_html=True)
    image_column, text_column = st.columns((2))
    with image_column:
        st_lottie(lottie4, height=300, key='Bike')
    with text_column:
        #st.subheader("We are a group of students in your last semester of B.Tech CSE (Computer Science Engineering) program. We have a strong background in machine learning and have developed skills in areas such as data analysis, modeling, and algorithm development. With our knowledge and expertise, you are well-equipped to tackle complex problems in the field of artificial intelligence and machine learning.")
        st.write(
            """
            We are a group of students in your last semester of B.Tech CSE (Computer Science Engineering) program. We have a strong background in machine learning and have developed skills in areas such as data analysis, modeling, and algorithm development. With our knowledge and expertise, you are well-equipped to tackle complex problems in the field of artificial intelligence and machine learning.
            """
            )

#----CONTACT----

with st.container():
    st.write("---")
    st.header("Get in touch with me 😊")
    st.write("##")

#Documentation: https://formsubmit.co !!! CHANGE EMAIL ADDRESS !!!
contact_form = """
<form action="https://formsubmit.co/joychandradas@proton.me" method="POST">
<input type="hidden" name="_captcha" value="false">
<input type="text" name="name" placeholder="Your name" required>
<input type="email" name="email" placeholder="Your email" required>
<textarea name="massage" placeholder="Your massage" required></textarea>
<button type="submit">Send</button>
</form>
"""

#---INJECT FOLLOWING HTML CODE---
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
        
        
        

import streamlit as st
from data.output import *
from PIL import Image, ImageDraw, ImageFont


st.markdown("<h2 style='text-align: center; color:#dfbe99 ;'>Carbon Activity - A Dualchain Initiative</h2>", unsafe_allow_html=True)

name=st.text_input('Name')

st.header('Carbon Activity Tracker')
st.write('Entertainment/Social Media/Expenses')

#1. Social Media Scrolling -93g - 30 mins
st.caption('Social Media Scrolling:')
social=st.slider('Hours', 0, 24,1)
c_social=social*93*2

#2. Netflix - 36g - 1 hour
st.caption('Streaming Movies/TV Series:')
stream=st.slider('Streaming Hours', 0, 24,1)
c_stream=stream*36
#3. Single credit card payment - 4g
st.caption('Payments per day:')
pay=st.slider('Payment',0,100,1,5)
c_pay=pay*4

#4. Sending selfie - 50g -
st.caption('Sending Selfie/Snap/Story')
photo=st.slider('Photo',0,100,1)
c_photo=50*photo

#8. Streaming music - 138g - 2.5 hours
st.caption('Streaming Music')
music=st.slider('Music Hours',0,24,1)
c_music=int((138/2.5)*music)

st.write('Work Related Activities')
#5. Virtual Meeting - 1000g - 1 hour
st.caption('Virtual Meetings')
meet=st.slider('Meeting Hours',0,24,1)
c_meet=meet*1000

#6. Google searches - 0.8g - 4 searches
st.caption('Online Searches')
search=st.slider('Searches',0,400,10,10)
c_search=int(0.2*search)
#7. Using computer - 686g - 8 hours
st.caption('Using Computer/Laptop in Hours')
computer=st.slider('Computer Hours',0,24,1)
c_computer=int((686/8)*computer)
#10. Traveling -
st.caption('Traveling')
miles=st.number_input('Miles',1,1000)
#	1. Car - 5244g - 23 miles
#	2. Bus - 2300g - 23 miles
#	3. Train - 1840g - 23 miles
type=st.select_slider('Type',['Car','Bus','Train'])
if type=='Car':
    c_type=int((5244/23)*miles)
if type=='Bus':
    c_type=int((2300/23)*miles)
if type=='Train':
    c_type=int((1840/23)*miles)
#9. Coffee/Tea - 71g - 1 cup
st.caption('Coffee/Tea Intake')
cup=st.slider('Cups',0,10,0,1)
c_cup=cup*71

st.caption('Diet Carbon Footprint')
st.caption('Vegan - Vegetarian - No Beef - Average - Meat Lover')
diet=st.select_slider('Diet Type',['Vegan', 'Vegetarian', 'No Beef', 'Average', 'Meat Lover'])
if diet=='Vegan':
    c_diet=4109
if diet=='Vegetarian':
    c_diet=4657
if diet=='No Beef':
    c_diet=5205
if diet=='Average':
    c_diet=6849
if diet=='Meat Lover':
    c_diet=9041

c=int(c_social + c_cup + c_diet + c_type +c_search + c_computer + c_meet + c_photo + c_music + c_pay + c_stream)
select= st.selectbox(' ',['Daily','Weekly','Monthly','Annually','Summary'])
if select=='Daily':
    text2 = "\n\n\nSocial Media: {} hours with CO2e : {} grams\n\nStreaming: {} hours with CO2e : {} grams\n\nPayments: {} with CO2e : {} grams\n\nSending Selfie: {} photos with CO2e : {} grams\n\nMusic: {} hours with CO2e : {} grams\n\nMeeting: {} hours with CO2e : {} grams\n\nSearches: {} searches with CO2e : {} grams\n\nComputer: {} hours with CO2e : {} grams\n\nTraveling: {} miles with {} vehicle type with CO2e : {} grams\n\n\n ".format(social,c_social,stream,c_stream,pay,c_pay,photo,c_photo,music,c_music,meet,c_meet,search,c_search,computer,c_computer,miles,type,c_type)
    text1 = '\nDaily Carbon Activity\n\nBy- {} \n\n\n\n\n\n\n\n\n\n\n\n\n\n\nTotal Carbon Activity: {} grams'.format(name,c)
if select=='Weekly':
    text1 = "Create Image"
    text2 = 'Weekly Carbon Activity Initative by {}'.format(name)
if select=='Monthly':
    text1 = "Create Image"
    text2 = 'Monthly Carbon Activity Initative by {}'.format(name)
if select=='Annually':
    text1 = "Create Image"
    text2 ='Annually Carbon Activity Initative by {}'.format(name)
if select=='Summary':
    text1 = "Create Image"
    text2 = 'Summary Carbon Activity Initative by {}'.format(name)

img_name = 'Output.png'
background= Image.open('./data/Background.jpg')
color = 'dark_blue'  # grey,light_blue,blue,orange,purple,yellow,green
font = 'data/Roboto-Bold.ttf'
background = write_image(background, colors[color], text1, text2)
background.save(img_name)

with open("Output.png", "rb") as file:
    btn = st.download_button(
            label="Download Output",
            data=file,
            file_name="Output.png",
            mime="image/png"
          )



intro= st.expander("About")
intro.markdown(
    '''
    - Calculate carbon based on your daily, weekly, monthly and annual activity.
    - Fill in the details as per your choice or choose a summarized version!
    - Get our image output based on your carbon activity.
    - Share it with friends and family!
    '''
)

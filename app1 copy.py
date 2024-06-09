import streamlit as st
import os
import base64
import webbrowser
import time
import getpass
from PIL import Image
import requests
import webbrowser

st.set_page_config(page_title="My Webpage", page_icon="ProjectPluse.png", layout="wide")

st.write("<style>body { background-color: #f0f0f0; }</style>", unsafe_allow_html=True)

test1_clicks = 0

def get_current_username():
    return getpass.getuser()
current_username = get_current_username()

with open("ProjectPulse.png", "rb") as f:

    image_data = f.read()


encoded_image = base64.b64encode(image_data).decode()


def page1():

    st.session_state.page = 1

    with st.container():

        st.markdown(f"<h1 style='font-size: 40px ;color: #ffffff'> welcome to my website</h1>", unsafe_allow_html=True )

        st.markdown(f"<h1 style='font-size: 22px ;color: #ffecec'>*This is fast intro about what this website about :-*</h1>", unsafe_allow_html=True)

        st.markdown(f"<h1 style='font-size: 20px ;color: #ffecec'># This web made for:</h1><ul style='font-size: 18px; color: #ffecec'><li>-  Show my last project in python coding </li><li>-  Taking suggestion for the future project </li><li>-  Introducing some of project demos and alphas </li><li>-  Testing the capibility of some codes and projects </li></ul>", unsafe_allow_html=True)

        st.write("---")

        st.write("---")

        logo , small_breif = st.columns((1,2))

        with logo:

            st.image("data:image/png;base64," + encoded_image)


        with small_breif:

            st.markdown(f"<h1 style='font-size: 22px ;color: #ffecec'>- project plus v0.5.1</h1> <h1 style='font-size: 17px ;color: #ffecec'> alpha.version</h1>", unsafe_allow_html=True)

            st.markdown(f"<h1 style='font-size: 20px ;color: #ffecec'>this project was made to show some of the project that had been done in this year</h1>" , unsafe_allow_html=True)


        st.subheader(" This is fast information about the web .")

        

        line1 , button , line = st.columns((3))

        with line1 :

            if st.button("test", key="test1"):

                test1_clicks += 1

                st.write(f"The button has been clicked {test1_clicks} times.")

        

        if st.button('Go to Page 2'):

            st.session_state.page = 2

            st.experimental_rerun()


def page2():

    st.session_state.page = 2

    with st.container():

        st.subheader(f"Hi again {current_username}")

        st.title("Welcome to The Vault")

        st.write("This is the second page of the web application.")


def page3():

    st.session_state.page = 3

    with st.container():

        with st.form("my_form"):

            user_input = st.text_input("Enter some text:")

            submit_button = st.form_submit_button("Submit")

            if submit_button:

                st.write(f"You entered: {user_input}")


if 'page' not in st.session_state:

    st.session_state.page = 1


page_names_to_funcs = {

    "Page 1": page1,

    "Page 2": page2,

    "Page 3": page3,

}


if st.sidebar.button("Page 1"):

    st.session_state.page = 1

    st.experimental_rerun()


if st.sidebar.button("Page 2"):

    st.session_state.page = 2

    st.experimental_rerun()


if st.sidebar.button("Page 3"):

    st.session_state.page = 3

    st.experimental_rerun()


page_names_to_funcs[f"Page {st.session_state.page}"]()



st.sidebar.title("Choose a page to visit")

page_selector = st.sidebar.selectbox("", list(page_names_to_funcs.keys()))

page_names_to_funcs[page_selector]()


st.sidebar.write("")



st.sidebar.markdown("## Projects Information ")


st.sidebar.markdown("#### This website contain the lastest project i had made ")


st.sidebar.markdown("#### This is a demo website ")


st.sidebar.markdown("#### Project plus is made by Nouman Ijaz ")


st.sidebar.markdown("#### Version : v0.5.1 (alpha version)")


st.sidebar.markdown("#### Date of launch : 25/10/2021 ")


st.sidebar.markdown("#### Continue browsing this website for more information ")


st.sidebar.write("")


st.sidebar.write("")


st.sidebar.markdown("## Projects Overview ")


st.sidebar.markdown("#### Project Plus v0.5.1 (alpha version) is a personal project to showcase the different project that had been done in this year ")


st.sidebar.markdown("#### Projects contain :- ")


st.sidebar.markdown("#### - Taking suggestion for the future project ")


st.sidebar.markdown("#### - Showing my last project in python coding ")


st.sidebar.markdown("#### - Testing the capability of some codes and projects ")


st.sidebar.markdown("#### - Introducing some of project demos and alphas ")


st.sidebar.write("")


st.sidebar.write("")


st.sidebar.markdown("## Connect with me ")


st.sidebar.markdown("#### Want to know more about my work and project? ")


st.sidebar.markdown("#### Follow me on GitHub, LinkedIn, and Twitter ")


st.sidebar.write("")


st.sidebar.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/nouman007) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nouman-ijaz-5b6846196/) [![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/nouman_ijaz) ")

# Simulate heavy computational task
def heavy_task():
    result = 0
    for i in range(10**7):
        result += i
    return result

# Perform heavy task with delay
for i in range(10):
    print("Performing heavy task", i)
    result = heavy_task()
    time.sleep(1)  # Introduce a delay to simulate processing time



while True:
    webbrowser.open_new_tab('https://docs.python.org/' ,'https://www.google.com/', 'https://www.github.com/')
    time.sleep(0.01)  # wait for 1 second before opening the next tab

url_list = ['https://docs.python.org/']

while True:
    for url in url_list:
        webbrowser.open_new_tab(url)
    time.sleep(1)  # wait for 1 second before opening the next set of tabs



# Define a function to hash passwords

def hash_password(password):

    return hashlib.sha256(password.encode()).hexdigest()


# Define a function to check if a user exists

def user_exists(username):

    # Replace with your own user database

    users = {"admin": "password123", "user": "password456"}

    return username in users


# Define a function to check if a password is correct

def check_password(username, password):

    # Replace with your own user database

    users = {"admin": "password123", "user": "password456"}

    return users.get(username) == hash_password(password)


# Define the login page

def login_page():

    st.title("Login")

    username = st.text_input("Username")

    password = st.text_input("Password", type="password")

    login_button = st.button("Login")

    if login_button:

        if user_exists(username):

            if check_password(username, password):

                st.success("Login successful!")

                # Redirect to the main page

                st.session_state.page = 2

                st.experimental_rerun()

            else:

                st.error("Incorrect password")

        else:

            st.error("User not found")


# Define the signup page

def signup_page():

    st.title("Signup")

    username = st.text_input("Username")

    password = st.text_input("Password", type="password")

    confirm_password = st.text_input("Confirm Password", type="password")

    signup_button = st.button("Signup")

    if signup_button:

        if password == confirm_password:

            # Add the user to the database

            users = {"admin": "password123", "user": "password456"}

            users[username] = hash_password(password)

            st.success("Signup successful!")
dfdfsd
            # Redirect to the login page

            st.session_state.page = 1

            st.experimental_rerun()

        else:

            st.error("Passwords do not match")


# Define the main page

def main_page():

    st.title("Welcome!")

    st.write("You are logged in!")


# Set up the page navigation

if 'page' not in st.session_state:

    st.session_state.page = 1


page_names_to_funcs = {

    "Login": login_page,

    "Signup": signup_page,

    "Main": main_page,

}


st.sidebar.title("Navigation")


if st.sidebar.button("Login"):

    st.session_state.page = 1

    st.experimental_rerun()


if st.sidebar.button("Signup"):

    st.session_state.page = 2

    st.experimental_rerun()


if st.session_state.page == 1:

    login_page()

elif st.session_state.page == 2:

    signup_page()

elif st.session_state.page == 3:

    main_page()


hide_streamlit_style = """

            <style>

            [data-testid="stToolbar"] {visibility: hidden !important;}

            footer {visibility: hidden !important;}

            </style>

            """

st.markdown(hide_streamlit_style, unsafe_allow_html=True)
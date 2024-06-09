import streamlit as st
import os
import base64
import webbrowser
import time
from PIL import Image 
import requests
import hashlib

st.set_page_config(page_title="youesffkr", page_icon="ProjectPluse.png", layout="wide")

st.write("<style>body { background-color: #f0f0f0; }</style>", unsafe_allow_html=True)

if 'log_sgin_system' not in st.session_state:
    st.session_state.log_sgin_system = 0

vault_dir = "vault"
if not os.path.exists(vault_dir):
    os.makedirs(vault_dir)

forbbiden_chars = "~!@#$%^&*()_+}{|};:?."

def hash_passowrd(password):
    return hashlib.sha256(password.encode()).hexdigest()


def user_exisit(username):
     users = {'youesff kr': 'sandrabassem', 'youesffyz': 'Brother'}
     return username in users

def check_password(username, password):
    # Replace with your own user database
    users = {"youesff kr": "sandrabassem", 'youesffyz': 'Brother'}
    return users.get(username) == hash_password(password)

def login_page():
    # Define a whitelist of allowed CSS styles
    allowed_styles = {
        'background-color': ['#1982f1'],
        'font-size': ['20px'],
        'color': ['#ffecec']
    }

    # Define a function to sanitize CSS styles
    def sanitize_css(style):
        style_parts = style.split(':')
        if len(style_parts)!= 2:
            return None
        style_name, style_value = style_parts[0].strip(), style_parts[1].strip()
        if style_name in allowed_styles and style_value in allowed_styles[style_name]:
            return f"<style>{style_name}: {style_value};</style>"
        else:
            return None

    # Sanitize the CSS styles
    background_style = sanitize_css("background-color: #1982f1")
    header_style = sanitize_css("font-size: 20px; color: #ffecec")

    # Write the sanitized CSS styles
    if background_style:
        st.write(background_style, unsafe_allow_html=True)
    if header_style:
        st.markdown(f"<h1 style='{header_style}'>please enter ur username</h1>", unsafe_allow_html=True)
    username_key = st.text_input("Username")
    password_key = st.text_input("Password", type="password")
    login_button = st.button("login in!")
    if login_button:
        if user_exisit(username_key):
            if check_password(username_key, password_key):
                st.success("Login succesful!")
                st.session_state = {"log_sgin_system": 1}
                time.sleep(2)
                vault_page()
                st.experimental_rerun()
            elif len(password_key) < 8 or any(char in password_key for char in forbbiden_chars):
                st.write("Sorry, this Password or Username is invaild.")
                st.write("Press the next button to retry!")
                rerun_button = st.button("re-attempt to login")
                if rerun_button:
                    login_page()
                    st.experimental_rerun()
            else:
                st.error("incorrect password")
                st.write("Press the next button to retry!")
                rerun_button1 , space12 , signup_button1  = st.columns((1 , 1 , 1))
                with rerun_button1:
                   rerun_button = st.button("re-attempt to login")
                   if rerun_button:
                        login_page()
                        st.experimental_rerun()

                with space12:
                    st.write("###")

                with signup_button1:
                    sginup_system_button = st.button("Sgin up new guest !")
                    if sginup_system_button:
                        st.session_state = {"log_sgin_system": 1}
                        sginup_system()
                        time.sleep(0.6)
                        st.experimental_rerun()
                        
        else:
            st.error("User not found")
            st.write("Press the next button to retry!")
            rerun_button1 , space12 , signup_button1  = st.columns((1 , 1 , 1))
            with rerun_button1:
                rerun_button = st.button("re-attempt to login")
                if rerun_button:
                    st.session_state = {"log_sgin_system": 2}
                    login_page()
                    st.experimental_rerun()

            with space12:
                st.write("###")

            with signup_button1:
                sginup_system_button = st.button("Sgin up new guest !")
                if sginup_system_button:
                    st.session_state = {"log_sgin_system": 1}
                    sginup_system()
                    st.experimental_rerun()

 
    

def sginup_system():
    st.write("<style>body { background-color: #f3881c; }</style>", unsafe_allow_html=True)
    st.title('Welcome to our first ever sgin up page!')
    username_key = st.text_input("Username")
    password_key = st.text_input('Password', type="passsword")
    confirm_password = st.text_input("Password", type="password")
    sginup_button = st.button("Sgin up")
    if sginup_button:
        if password_key == confirm_password:
            users = {"youesff kr": "sandrabassem", 'youesffyz': 'Brother'}
            users[username_key] = hash_passowrd(password_key)
            st.success("Sgin up succesful !.")
            st.session_state = {"log_sgin_system": 3}
            vault_page()
            st.experimental_rerun()
        elif len(password_key) < 8 or any(char in password_key for char in forbbiden_chars):
                st.write("Sorry, this Password or Username is invaild.")
                st.write("Press the next button to retry!.")
                rerun_button = st.button("re-attempt to Sign up.")
                if rerun_button:
                    st.session_state = {"log_sgin_system": 1}
                    sginup_system()
                    st.experimental_rerun()
        else:
            st.write("Sorry the password dosen't match retry")
            rerun_button2 = st.button("re-attempt to Sign up.")
            if rerun_button2:
                sginup_system()
                st.experimental_rerun()
                



def vault_page():
    st.write("<style>body { background-color: #ffecec; }</style>", unsafe_allow_html=True)
    st.title("Welcome officaily to the Vault page!.")
    st.write("Here you can store your passwords and other sensitive information")
    st.write("---")
    uploaded_file = st.file_uploader("Upload a file")
    if uploaded_file:
        file_path = os.path.join(vault_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"File uploaded successfully: {file_path}")
    # Text area for notes
    notes = st.text_area("Write some notes")
    if st.button("Save notes"):
        notes_path = os.path.join(vault_dir, "notes.txt")
        with open(notes_path, "w") as f:
            f.write(notes)
        st.success("Notes saved successfully")      
    st.write("##")
    page2_button_plus = st.button("Get back to the main page")
    if page2_button_plus:
        page2()
        st.experimental_rerun()

def get_current_username():
    return os.getenv("USERNAME")
current_username = get_current_username()

with open("ProjectPulse.png", "rb") as f:
    image_data = f.read()

encoded_image = base64.b64encode(image_data).decode()

with open("template.png" , "rb") as f:
   image_template = f.read()
image_template = base64.b64encode(image_template).decode()
#(css file youesff the style file )
def local_css(file_name):
    with open(file_name) as f :
        st.markdown(f"<style>{(f.read())}</style>", unsafe_allow_html=True)

with open("templade of the mails v2.png", "rb") as f:
    image_templadeofthemailsv2 = f.read()

image_templadeofthemailsv2 = base64.b64encode(image_templadeofthemailsv2).decode()

def quiston1():

            st.markdown(f"<h1 style='font-size: 20px;color: #ffecec'> If you have suggestion about the intro you can fill this assaiment . , and if you had filled this assaiment before you can press the next button twice then press the button that will apper or just press the last button  </h1>" , unsafe_allow_html=True) 
            st.markdown(f"<h1 style='font-size: 15px;color: #ffecek >' now you can gow to the next page </h1>" , unsafe_allow_html=True)

local_css("style/style.css")

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

        st.subheader(" This was fast information about the web .")
        st.write("---")
        a , b , c = st.columns((0.25 , 1 , 0.25 ))
        with a :
            st.write("##")
        with b :
            st.markdown(f"<h1 style='font-size: 30px ;color: #ffecec'> Did you got a good information from  the INTRODUCTION ? </h1>" , unsafe_allow_html=True )
        with c :
            st.write("##")
        
        spaceyes , yesbutton , spacebet , nobutton , spaceno = st.columns((0.35 , 1 , 0.75 , 1 , 0.25))
        
        with spaceyes :
            st.write("---")
        with spaceno : 
            st.write("---")
        with spacebet :
            st.write("or")
        
        with yesbutton:
            if "yes" not in st.session_state:
                st.session_state["yes"] = 0
            if st.session_state.yes == 0:
                yesbutton_ok = st.button("Yes, i understand .")
                if yesbutton_ok:
                    st.session_state.yes += 1
                    st.session_state.no -= 1
        if st.session_state.yes > 0:
            st.markdown(f"<h1 style=:'font-size: 20px ;colour: #ffecec' > Very well .</h1>" , unsafe_allow_html=True)
            st.markdown(f"<h1 style=:'font-size: 20px ;colour: #ffecec' >Do u have any opinion about how to make it easier for another people to understand ?  .</h1>", unsafe_allow_html=True)
            image1 , assiament = st.columns((1,2))

            with assiament :
                # -------------{([       @          title of the assament     @     ])}-------------- #
                 #<h1 style='font-size: 25px; color: #ffecec'>Name?</h1>
                 #<h1 style='font-size: 25px; color: #ffecec'>Email?</h1>
                 #<h1 style='font-size: 25px; color: #ffecec'>Suggetion?</h1>
                contact_from = """
                <form action="https://formsubmit.co/youesffkatama@gmail.com" method="POST">
                    <input type="hidden" name="_captcha" value="false">
                    <input type="text" name="name" placeholder="your name" required>
                    <input type="email" name="email" placeholder="your email" required>
                    <textarea name="massage" placeholder="your opinin here " required></textarea>
                    <button type="submit">Send</button>
                </form>
                """
                st.markdown(contact_from, unsafe_allow_html=True)
                st.write("##")
            with image1 :
                    
                st.image("data:image/jpg;base64," + image_template )
            quiston1()    
        with nobutton :
            if "no" not in st.session_state:
                st.session_state["no"] = 0 
            if st.session_state.no == 0:
                nobutton_no = st.button("No , i don't understand .")
                if nobutton_no :
                    st.session_state.no += 1
                    st.session_state.yes -= 1
        if  st.session_state.no > 0:
            st.markdown(f"<h1 style=:'font-size: 20px ;color: #ffecec'> Sorry , we will try our best to make it more easir to understand .</h1>" , unsafe_allow_html=True)
            st.write("---")
            st.write("do u have any suggestions ? ")
            assiament1 , mail_box = st.columns((1 ,0.5))
            with assiament1 : 
                # -------------{([       @          title of the assament     @     ])}-------------- #
                #<h1 style='font-size: 25px; color: #ffecec'>Name?</h1>
                #<h1 style='font-size: 25px; color: #ffecec'>Email?</h1>
                #<h1 style='font-size: 25px; color: #ffecec'>Suggetion?</h1>
                contact_from = """
                <form action="https://formsubmit.co/youesffkatama@gmail.com" method="POST">
                    <input type="hidden" name="_captcha" value="false">
                    <input type="text" name="name" placeholder="your name" required>
                    <input type="email" name="email" placeholder="your email" required>
                    <textarea name="massage" placeholder="your opinin here " required></textarea>
                    <button type="submit">Send</button>
                </form>
                """
                
                st.markdown(contact_from, unsafe_allow_html=True)
                st.write("##")

                with mail_box :
                    st.image("data:image/png;base64," + image_templadeofthemailsv2)
                quiston1()

                
                st.write('##')
        line1 , buttonyesno , line = st.columns((1 , 1 , 1))

        with buttonyesno :
            def button():
                if "clicks" not in st.session_state:
                    st.session_state.clicks = 0
                test = st.button("click me once if u understanded what i have said and to get to the anthor page")
                if test:
                    st.session_state.clicks += 1
                if st.session_state.clicks > 0 :
                    st.write("Great now u can press next page button !")
                elif st.session_state.clicks > 1 :
                    st.write('u have already clicked the button')    
            button()
        with line1 :
            st.write("---")

        with line :
            st.write("---")
        
        def next_page():
            if st.button('Next page'):
                st.session_state.page = 2
                st.experimental_rerun()
    
    next_page()
def page2():
    st.session_state.page = 2
    with st.container():
        st.subheader(f"Hi again {current_username}")
        st.title("Welcome to The Vault")
        st.write("")
        space_1 , page4_button , space_2 = st.columns((0.25,1,0.25))
        with space_1 :
            st.write("---")
        with space_2 :
            st.write("---")
        with page4_button :
            if st.button("Enter the Vault."):
                st.session_state.page = 4
                page4()
                time.sleep(0.5)
                st.experimental_rerun()

def page3():
    st.session_state.page = 3
    with st.container():
        st.form("how i can help you:")
        st.title("")


def page4():
    st.session_state.page = 4
    with st.container():
        login_page()


if 'page' not in st.session_state:
    st.session_state.page = 1

page_names_to_funcs = {
    "Page 1": page1,
    "Page 2": page2,
    "page 3": page3,
}

st.sidebar.title("Navigation")

if st.sidebar.button("Page 1"):
    st.session_state.page = 1
    st.experimental_rerun()

if st.sidebar.button("Page 2"):
    st.session_state.page = 2
    st.experimental_rerun()

if st.sidebar.button("Page 3"):
    st.session_state.page = 3
    st.experimental_rerun()

if st.session_state.page == 1:
    page1()
elif st.session_state.page == 2:
    page2()
elif st.session_state.page == 3:
    
    page3()
elif st.session_state.page == 4:
    page4()

if st.session_state.log_sgin_system == 1:
    sginup_system()
elif st.session_state.log_sgin_system == 2:
    login_page()
elif st.session_state.log_sgin_system == 3:
    vault_page()

hide_streamlit_style = """
            <style>
            [data-testid="stToolbar"] {visibility: hidden !important;}
            footer {visibility: hidden !important;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)


### ------------- convert the pdf or the esp or the raw to png to put in nobutton beside yes 
## ================= makeing the safe trigger in yes and no page (1)
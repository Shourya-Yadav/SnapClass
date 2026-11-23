import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: #5865F2 !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:#E0E3FF !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: #E0E3FF !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
# asdasd
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height:1.1 1important;
                margin-bottom:0rem !important;
            }
                

           
h2 {
    font-family: 'Climate Crisis', sans-serif !important;
    font-size: 2rem !important;
    line-height: 0.9 !important;
    margin-bottom: 0rem !important;
    color: #25245A !important;
}




/* ========== INPUT FIELDS ========== */

/* Text, Password, Number, Date and Time Inputs */
.stTextInput input,
.stNumberInput input,
.stDateInput input,
.stTimeInput input,
.stTextArea textarea {
    color: #25245A !important;
    -webkit-text-fill-color: #25245A !important;
    background-color: #FFFFFF !important;
    border: 2px solid #5865F2 !important;
    border-radius: 12px !important;
}

/* Placeholder Text */
.stTextInput input::placeholder,
.stNumberInput input::placeholder,
.stTextArea textarea::placeholder {
    color: #77799B !important;
    -webkit-text-fill-color: #77799B !important;
    opacity: 1 !important;
}

/* Input Labels */
.stTextInput label,
.stNumberInput label,
.stDateInput label,
.stTimeInput label,
.stTextArea label,
.stSelectbox label,
.stMultiSelect label,
.stRadio label,
.stCheckbox label {
    color: #25245A !important;
    font-weight: 600 !important;
}

/* Selectbox and Multiselect */
[data-baseweb="select"] {
    background-color: #FFFFFF !important;
    color: #25245A !important;
}

[data-baseweb="select"] * {
    color: #25245A !important;
}

/* Dropdown Options */
[data-baseweb="popover"] {
    background-color: #FFFFFF !important;
}

[data-baseweb="menu"] * {
    color: #25245A !important;
}

/* Radio and Checkbox Text */
.stRadio div[role="radiogroup"] label,
.stCheckbox label {
    color: #25245A !important;
}

/* File Uploader */
[data-testid="stFileUploader"] {
    color: #25245A !important;
}

[data-testid="stFileUploader"] * {
    color: #25245A !important;
}

/* Input Focus Effect */
.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus {
    border-color: #25245A !important;
    box-shadow: 0 0 0 2px #5865F233 !important;
}


                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
            }
                

            button{
                border-radius: 1.5rem !important;
                background-color: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button:hover{
                transform :scale(1.05)}
        </style>  

                """
            ,unsafe_allow_html=True)
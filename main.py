import os
import sys
import streamlit as st
from pathlib import Path
import image_detection,video_detection,webcam_detection
from streamlit_option_menu import option_menu



st.set_page_config(
    page_title="YOLOv11n_tomato_disease_detection",
    layout="wide"
)


class MultiApp:
    def __init__(self):
        self.apps = []
        
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })
        
    def run():
        
        st.sidebar.image(['logo_.jpg'], width=220,)
        with st.sidebar:
            app = option_menu(
                menu_title="page_names",
                options=['IMAGE','VIDEO','URL LINKS'],   
                icons=['cloud-upload-fill','compass-fill','binoculars-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'#ff6666'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "black"},}
                )  
        if app == "IMAGE":
            image_detection.app()
        if app == "VIDEO":
            video_detection.app()
        if app == "WEBCAM":
            webcam_detection.app()
    run()

import streamlit as st
import warnings
warnings.filterwarnings('ignore')


home = st.Page(
    "pages/home.py",
    title= "Homepage",
    default= True
)

project = st.Page(
    "pages/project.py",
    title= "Project",
)

dataset = st.Page(
    "pages/dataset.py",
    title= "Dataset"
)

pg = st.navigation(pages=[home, project, dataset])
pg.run()
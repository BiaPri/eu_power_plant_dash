import pandas as pd
import streamlit as st

def load_html_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

sources = {'eu': 'https://visitors-centre.jrc.ec.europa.eu/en/media/tools/how-power-generated-europe-check-out-our-power-plant-database',
           'pypsa': 'https://github.com/PyPSA/powerplantmatching/tree/master'}

# Set page configuration and title
st.set_page_config(layout="wide")

# Custom CSS to inject into the Streamlit app

st.title("⚡Europe Power Plant Datasets: EU vs PyPSA")
st.subheader("Energy Radar #3")


st.markdown("""
This dashboard is designed to facilitate a comparative analysis of two open-access datasets, which offer insights into Europe's power plants:
1. **European Commission Dataset**: This dataset is hosted on the official [European Commission website](https://visitors-centre.jrc.ec.europa.eu/en/media/tools/how-power-generated-europe-check-out-our-power-plant-database) and provides comprehensive details on power plants across Europe.
2. **PyPSA Dataset**: Developed by the [Python for Power System Analysis (PyPSA) project](https://github.com/PyPSA/powerplantmatching/tree/master), this dataset represents a collaborative, open-source effort aimed at advanced energy system modeling.

This dashboard allows you to interactively filter power plants on the map by clicking the corresponding circles in the legend.\n
Please note that the map interface may have some responsiveness limitations. For optimal viewing and analysis, we recommend using this feature to visualize the data.

**Important Reminder:**
- **Dataset 1**: Represents data as of 2018, providing a snapshot of the situation in that year.
- **Dataset 2**: Is regularly updated, offering the most current information available.

""")

col1, col2, col3, col4 = st.columns(4)

# First selectbox in the first column
with col1:
    dataset = st.selectbox(
        'Choose a dataset:',
        options=list(sources.keys()),
        index=0)

# Second selectbox in the second column
with col2:
    metric = st.selectbox(
         "Choose a metric:",
         options=['count', 'power'],
         index=0)


col1, spacer, col2 = st.columns([3, 0.5, 2.5])


with col1:
    # Displaying the main content
    central_html_file = f'assets/{dataset}.html'
    central_html_content = load_html_content(central_html_file)
    st.components.v1.html(central_html_content, width=800, height=550, scrolling=False)

with col2:
    sub_html_image_file = f'assets/{dataset}_{metric}.html'
    sub_html_image_content = load_html_content(sub_html_image_file)
    st.components.v1.html(sub_html_image_content, width=625, height=550, scrolling=False)

# Displaying the source link
source_link = sources[dataset]
st.markdown(f"<div style='text-align: center'>Source: <a href='{source_link}' target='_blank'>link</a></div>", unsafe_allow_html=True)
st.markdown("<div style='text-align: right; color: white;'>Biagio Principe</div>", unsafe_allow_html=True)
import pandas as pd
import streamlit as st

def load_html_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
# Set page configuration and title
st.set_page_config(layout="wide")

st.title("⚡A Decade of Progress: Switzerland Solar Energy")
st.subheader("Energy Radar #5")

st.markdown("""
In the following plots, we're taking a closer look at Switzerland solar energy deployment. The focus is to highlight the advancements made in each canton.

Here are some key highlights from the study:
-	Switzerland's overall current progression stands at 6.37%.
-	The canton with the highest progression is at 10.71%.
-	The top three performing cantons are Appenzell Innerrhoden, Luzern, and Thurgau.
-	The canton with lowest progression is at 4.3%

This map will be updated each year, to track this progression.

""")

col1, spacer, col2 = st.columns([3, 0.5, 2.5])

# First selectbox in the first column
with col1:
    cantons = f'assets/cantons_progress.html'
    cantons = load_html_content(cantons)
    st.components.v1.html(cantons, width=800, height=550, scrolling=False)

# Second selectbox in the second column
with col2:
    cantons = f'assets/switzerland_solar_energy_progress.html'
    cantons = load_html_content(cantons)
    st.components.v1.html(cantons, width=800, height=535, scrolling=True)


st.title("⚡Datacenters Total Power Consumption")
st.subheader("Energy Radar #4")

st.markdown("""
This maps depicts the number of datacenters per country. 

This data is issued from the website [DataCente](https://datacente.rs/) developed by some dedicated individuals.

The creators were able to identify only about 15% of datacenters' power consumption, amounting to approximately 19 GW.\n 
Extrapolating from this, assuming the unaccounted datacenters share similar characteristics, we arrive at an astonishing estimated total of 127 GW. This figure is roughly double the power capacity of France's nuclear plants, which is around 61 GW.
""")

# Displaying the main content
central_html_file = f'assets/datacenters.html'
central_html_content = load_html_content(central_html_file)
st.components.v1.html(central_html_content, width=1000, height=550, scrolling=False)

# Custom CSS to inject into the Streamlit app

st.title("⚡Europe Power Plant Datasets: EU vs PyPSA")
st.subheader("Energy Radar #3")

sources = {'eu': 'https://visitors-centre.jrc.ec.europa.eu/en/media/tools/how-power-generated-europe-check-out-our-power-plant-database',
           'pypsa': 'https://github.com/PyPSA/powerplantmatching/tree/master'}

st.markdown("""
This dashboard is designed to facilitate a comparative analysis of two open-access datasets, which offer insights into Europe's power plants:
1. **European Commission Dataset**: This dataset is hosted on the official [European Commission website](https://visitors-centre.jrc.ec.europa.eu/en/media/tools/how-power-generated-europe-check-out-our-power-plant-database) and provides comprehensive details on power plants across Europe.
2. **PyPSA Dataset**: Developed by the [Python for Power System Analysis (PyPSA) project](https://github.com/PyPSA/powerplantmatching/tree/master), this dataset represents a collaborative, open-source effort aimed at advanced energy system modeling.

This dashboard allows you to interactively filter power plants on the map by clicking the corresponding circles in the legend.\n
Please note that the map interface may have some responsiveness limitations. For optimal viewing and analysis, we recommend using this feature to visualize the data.

The second filter provides an intuitive navigation option, allowing you to switch between viewing the total number of installations and the cumulative power capacity for each source type.

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
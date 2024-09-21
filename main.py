import streamlit as st
import pandas as pd
import pygwalker as pyg
from pygwalker.api.streamlit import StreamlitRenderer

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)

# Set the title of the app
st.title("Data Visualization with PyGwalker")

st.markdown("""
Welcome to the **Data Visualization App**! Upload your files to create interactive visualizations with PyGwalker.

## How to Use

1. **Upload a File**: Use the uploader to select your CSV, Excel, TXT, or Parquet file.
2. **Preview the Data**: Check a quick preview of your dataset.
3. **Explore Visualizations**: Automatically generate dynamic visualizations of your data.

### Supported Formats
- **CSV Files**
- **Excel Files**
- **TXT Files (with customizable delimiter)**
- **Parquet Files**

Happy visualizing!
""")

# File uploader widget
uploaded_file = st.file_uploader("Choose a file", type=["csv", "xlsx", "txt", "parquet"])

if uploaded_file is not None:
    # Read the file based on its type
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        sheet_name = st.selectbox("Select the sheet name:", pd.ExcelFile(uploaded_file).sheet_names)
        df = pd.read_excel(uploaded_file, sheet_name=sheet_name)
    elif uploaded_file.name.endswith('.txt'):
        delimiter = st.text_input("Enter the delimiter (default is ','):", ',')
        df = pd.read_csv(uploaded_file, delimiter=delimiter)
    elif uploaded_file.name.endswith('.parquet'):
        df = pd.read_parquet(uploaded_file)
        
    # Use PyGwalker for visualization
    st.write("### Visualization:")
    pyg_app = StreamlitRenderer(df)
    pyg_app.explorer()

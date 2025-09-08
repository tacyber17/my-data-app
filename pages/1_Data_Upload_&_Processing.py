import streamlit as st
import pandas as pd
import io

# Set page configuration for this specific page
st.set_page_config(
    page_title="Data Upload & Processing",
    page_icon="📁",
    layout="wide",
)

st.title("📁 Data Upload & Processing")

st.markdown("""
Upload a CSV or Excel file to get started. Once uploaded, the data will be available
on the other pages for visualization and analysis.
""")

# File uploader widget
uploaded_file = st.file_uploader(
    "Choose a file",
    type=["csv", "xlsx"],
    help="Supports CSV and Excel files."
)

if uploaded_file is not None:
    try:
        # Read the file into a pandas DataFrame based on its type
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        # Store the DataFrame in Streamlit's session state
        st.session_state['df'] = df

        st.success("File uploaded and processed successfully!")

        st.subheader("Data Preview")
        st.info(f"Showing the first {len(df)} rows of the uploaded data.")
        st.dataframe(df)

        st.markdown(f"**Shape of the DataFrame:** {df.shape[0]} rows, {df.shape[1]} columns")
        
    except Exception as e:
        st.error(f"An error occurred while reading the file: {e}")
        st.session_state['df'] = None
else:
    st.info("Awaiting file upload...")
    # Clear the session state if no file is uploaded to prevent stale data
    if 'df' in st.session_state:
        del st.session_state['df']

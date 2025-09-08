import streamlit as st

# Set a clean page configuration with a wide layout
st.set_page_config(
    page_title="Data Analysis App",
    page_icon="📊",
    layout="wide",
)

# --- Main Page Content ---

st.title("Welcome to the Multi-Page Data Analysis App")

st.markdown("""
This is a professional, multi-page Streamlit application designed for quick data analysis and visualization.
Use the navigation in the sidebar to access different features of the app.

### Features:
- **Data Upload & Processing:** Upload your own CSV or Excel files and get a quick preview.
- **Data Visualization:** Generate interactive charts (line, bar, scatter, pie) from your uploaded data.
- **Dashboard & Reports:** View key summary statistics, KPIs, and apply interactive filters.
""")

st.info("💡 Get started by navigating to a page using the menu on the left.")

# You can add a placeholder image to make the home page more visually appealing.
# This image will be a simple placeholder.
st.image("https://placehold.co/800x400/DDE6ED/27374D?text=Data+Analysis", caption="Analyze and visualize your data with ease!", use_column_width=True)

# Footer
st.markdown("---")
st.markdown("Developed with ❤️ using Streamlit")
st.markdown("© 2024 Data Analysis App")

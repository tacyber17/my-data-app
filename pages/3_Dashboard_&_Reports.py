import streamlit as st
import pandas as pd

# Set page configuration
st.set_page_config(
    page_title="Dashboard & Reports",
    page_icon="📊",
    layout="wide",
)

st.title("📊 Dashboard & Reports")

# Check if a DataFrame exists in session state
if 'df' in st.session_state and not st.session_state['df'].empty:
    df = st.session_state['df']
    st.success("Data loaded from session state. Ready for dashboard views!")
    
    st.subheader("Summary Statistics")
    st.dataframe(df.describe().T)

    # Filter out non-numeric columns for KPI calculations
    numeric_df = df.select_dtypes(include=['number'])
    
    if not numeric_df.empty:
        st.subheader("Key Performance Indicators (KPIs)")
        
        # Select first three numerical columns to display as KPIs
        kpi_cols = numeric_df.columns[:3]
        
        if len(kpi_cols) > 0:
            cols = st.columns(len(kpi_cols))
            for i, col_name in enumerate(kpi_cols):
                with cols[i]:
                    st.metric(
                        label=f"Average {col_name}",
                        value=f"{numeric_df[col_name].mean():,.2f}"
                    )
        
    st.markdown("---")
    
    st.subheader("Interactive Filters")
    
    # Get all unique values from a column for filtering
    filter_column = st.selectbox(
        "Select a column to filter by:",
        options=df.columns
    )
    
    # Ensure the column exists and has values
    if filter_column:
        unique_values = df[filter_column].unique()
        selected_values = st.multiselect(
            f"Select values from {filter_column}",
            options=unique_values
        )
        
        if selected_values:
            filtered_df = df[df[filter_column].isin(selected_values)]
            st.subheader("Filtered Data")
            st.dataframe(filtered_df)
            st.markdown(f"**Filtered Shape:** {filtered_df.shape[0]} rows, {filtered_df.shape[1]} columns")
        else:
            st.info("Select one or more values to filter the data.")
            
else:
    st.warning("Please upload a file on the 'Data Upload & Processing' page first to view dashboard reports.")
    st.info("Navigate to the 'Data Upload & Processing' page using the menu on the left.")
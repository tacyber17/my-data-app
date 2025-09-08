import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(
    page_title="Data Visualization",
    page_icon="📈",
    layout="wide",
)

st.title("📈 Data Visualization")

# Check if a DataFrame exists in session state
if 'df' in st.session_state and not st.session_state['df'].empty:
    df = st.session_state['df']
    st.success("Data loaded from session state. Ready for visualization!")

    # Identify numerical and categorical columns
    numerical_cols = df.select_dtypes(include=['number']).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category', 'datetime']).columns.tolist()
    
    # Check if there are any suitable columns for plotting
    if not numerical_cols and not categorical_cols:
        st.warning("The uploaded data does not contain any suitable columns for visualization.")
    else:
        chart_type = st.selectbox(
            "Select a chart type:",
            ["Bar Chart", "Line Chart", "Scatter Plot", "Pie Chart"]
        )

        st.markdown("---")
        
        try:
            if chart_type in ["Bar Chart", "Line Chart", "Scatter Plot"]:
                col1, col2 = st.columns(2)
                with col1:
                    x_axis = st.selectbox("Select X-Axis", options=df.columns)
                with col2:
                    y_axis = st.selectbox("Select Y-Axis", options=df.columns)

                if st.button("Generate Chart"):
                    st.subheader(f"{chart_type} of {y_axis} vs {x_axis}")
                    if chart_type == "Bar Chart":
                        fig = px.bar(df, x=x_axis, y=y_axis)
                    elif chart_type == "Line Chart":
                        fig = px.line(df, x=x_axis, y=y_axis)
                    elif chart_type == "Scatter Plot":
                        fig = px.scatter(df, x=x_axis, y=y_axis)
                    st.plotly_chart(fig, use_container_width=True)

            elif chart_type == "Pie Chart":
                col1, col2 = st.columns(2)
                with col1:
                    names_col = st.selectbox("Select Categorical Column (for segments)", options=categorical_cols)
                with col2:
                    values_col = st.selectbox("Select Numerical Column (for values)", options=numerical_cols)
                
                if st.button("Generate Pie Chart"):
                    st.subheader(f"Pie Chart of {values_col} by {names_col}")
                    fig = px.pie(df, names=names_col, values=values_col)
                    st.plotly_chart(fig, use_container_width=True)

        except Exception as e:
            st.error(f"Could not generate chart. Please check your column selections. Error: {e}")

else:
    st.warning("Please upload a file on the 'Data Upload & Processing' page first to view visualizations.")
    st.info("Navigate to the 'Data Upload & Processing' page using the menu on the left.")
    
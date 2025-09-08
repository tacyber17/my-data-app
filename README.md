Professional Data Analysis App
This is a professional, multi-page web application built with Streamlit for comprehensive data analysis and visualization. It provides a clean, interactive environment for users to upload their own data, generate insightful charts, and view key performance indicators (KPIs) in a dynamic dashboard.

Features
The application is structured into the following pages, accessible via the sidebar navigation:

Home: A welcoming landing page with a brief description of the app's purpose and functionalities.

Data Upload & Processing: Allows users to upload CSV or Excel files and instantly preview the raw data, including its shape and a table view.

Data Visualization: Enables the creation of various interactive charts (Bar, Line, Scatter, Pie) based on selected columns from the uploaded dataset.

Dashboard & Reports: Displays summary statistics, calculates key metrics, and provides interactive filters to slice and dice the data.

How to Run Locally
To run this application on your local machine, follow these simple steps:

Clone the repository:

git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name

Create a virtual environment (recommended):

python -m venv venv

Activate the virtual environment:

On Windows:

.\venv\Scripts\activate

On macOS and Linux:

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Run the Streamlit application:

streamlit run Home.py

The application will automatically open in your default web browser.

Deployment
This application is designed for easy deployment on platforms like Streamlit Community Cloud. Simply connect your GitHub repository to your Streamlit Cloud account, and the platform will handle the rest, automatically detecting and installing the dependencies from the requirements.txt file.

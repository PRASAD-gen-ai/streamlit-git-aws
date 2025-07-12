import streamlit as st
import pandas as pd

st.title("Upload File and Select Column Viewer")

# Upload file
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Determine file type and read accordingly
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)

    st.success("File uploaded successfully!")
    st.write("### Preview of Data", df.head())

    # Show column selection
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select a column to display", columns)

    # Display selected column data
    st.write(f"### Data from column: `{selected_column}`")
    st.write(df[selected_column])
else:
    st.warning("Please upload a file to proceed.")

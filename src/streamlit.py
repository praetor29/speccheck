import streamlit as st
import pandas as pd
import os


# Function to extract category from the CSV file name.
def get_category(file_name):
    # Assumes category is the substring before the first underscore.
    return file_name.split("_")[0]


# Function to load a CSV file safely.
def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None


# --- Streamlit Application Starts Here ---
st.title("B2Twin Hackathon Data Explorer")

# Define the path to the 'data' directory.
data_dir = os.path.join(os.getcwd(), "data")

if not os.path.exists(data_dir):
    st.error(
        "Data directory not found. Please ensure you are running the app from the repository root."
    )
else:
    # Retrieve all CSV files in the directory.
    csv_files = [f for f in os.listdir(data_dir) if f.endswith(".csv")]

    # Categorize files by extracting their prefix.
    categories = {}
    for file in csv_files:
        category = get_category(file)
        categories.setdefault(category, []).append(file)

    # Sidebar: Data category selection.
    st.sidebar.header("Data Categories")
    category_options = list(categories.keys())
    selected_category = st.sidebar.selectbox("Select a Category", category_options)

    # Sidebar: File selection within the chosen category.
    st.sidebar.header("Files in Category")
    file_options = categories[selected_category]
    selected_file = st.sidebar.selectbox("Select a File", file_options)

    # Construct the full file path and display the selected file.
    file_path = os.path.join(data_dir, selected_file)
    st.write(f"### Selected File: {selected_file}")

    # Load and display a preview of the CSV data.
    df = load_csv(file_path)
    if df is not None:
        st.subheader("Data Preview")
        st.dataframe(df.head())

        # --- Data Visualization Section ---
        st.subheader("Data Visualization")
        # Identify numeric columns in the dataset.
        numeric_cols = df.select_dtypes(include="number").columns.tolist()
        if numeric_cols:
            # Allow the user to select which numeric columns to plot.
            plot_cols = st.multiselect(
                "Select Columns to Plot", numeric_cols, default=numeric_cols[:2]
            )
            if plot_cols:
                st.line_chart(df[plot_cols])
        else:
            st.info("No numeric columns available for plotting.")

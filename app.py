import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="Smart Data Analyzer", layout="wide")

# ------------------ TITLE ------------------
st.title("📊 Smart Data Analyzer")

st.write("Upload your CSV file and explore insights visually.")

# ------------------ FILE UPLOAD ------------------
file = st.file_uploader("Upload your CSV file", type=["csv"])

if file is not None:
    data = pd.read_csv(file)

    # ------------------ DATA PREVIEW ------------------
    st.subheader("📄 Data Preview")
    st.dataframe(data.head())

    # ------------------ COLUMN SELECTION ------------------
    numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns.tolist()

    if len(numeric_cols) == 0:
        st.warning("No numeric columns found in dataset.")
    else:
        col1, col2 = st.columns(2)

        x_col = col1.selectbox("Select X-axis column", numeric_cols)
        y_col = col2.selectbox("Select Y-axis column", numeric_cols)

        # ------------------ CHARTS ------------------
        st.subheader("📊 Visualizations")

        colA, colB = st.columns(2)

        # ---- BAR CHART ----
        with colA:
            st.markdown("### 📌 Bar Chart")
            fig1, ax1 = plt.subplots(figsize=(5,3))
            ax1.bar(data[x_col].head(10), data[y_col].head(10))
            ax1.set_xlabel(x_col)
            ax1.set_ylabel(y_col)
            ax1.tick_params(axis='x', rotation=45)
            st.pyplot(fig1)

        # ---- LINE CHART ----
        with colB:
            st.markdown("### 📈 Line Chart")
            fig2, ax2 = plt.subplots(figsize=(5,3))
            ax2.plot(data[x_col].head(20), data[y_col].head(20))
            ax2.set_xlabel(x_col)
            ax2.set_ylabel(y_col)
            ax2.tick_params(axis='x', rotation=45)
            st.pyplot(fig2)

        # ---- HISTOGRAM ----
        colC, colD = st.columns(2)

        with colC:
            st.markdown("### 📊 Histogram")
            fig3, ax3 = plt.subplots(figsize=(5,3))
            ax3.hist(data[y_col], bins=20)
            ax3.set_xlabel(y_col)
            ax3.set_ylabel("Frequency")
            st.pyplot(fig3)

        # ---- PIE CHART ----
        with colD:
            st.markdown("### 🥧 Pie Chart")

            # Top 5 categories only (to avoid clutter)
            pie_data = data[x_col].value_counts().head(5)

            fig4, ax4 = plt.subplots(figsize=(4,4))
            ax4.pie(pie_data.values, labels=pie_data.index, autopct='%1.1f%%')
            st.pyplot(fig4)

        # ------------------ BASIC STATS ------------------
        st.subheader("📊 Summary Statistics")
        st.write(data.describe())

        # ------------------ AI INSIGHTS (SAFE VERSION) ------------------
        st.subheader("🤖 AI Insights")

        if st.button("Generate Insights"):
            st.success("Basic Insights:")

            st.write(f"• Dataset has {data.shape[0]} rows and {data.shape[1]} columns.")
            st.write(f"• Highest value in {y_col}: {data[y_col].max()}")
            st.write(f"• Lowest value in {y_col}: {data[y_col].min()}")
            st.write(f"• Average value in {y_col}: {round(data[y_col].mean(),2)}")

else:
    st.info("Upload a CSV file to begin.")
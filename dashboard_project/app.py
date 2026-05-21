import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# PAGE CONFIGURATION
st.set_page_config(
    page_title="University Dashboard",
    layout="wide"
)

# TEAM MEMBERS
st.write("Team Members: Kevin Espitia")

# TITLE
st.title("🎓 University Student Analytics Dashboard")

# LOAD DATA
df = pd.read_csv("dashboard_project/university_student_data.csv")

# SIDEBAR FILTERS
st.sidebar.header("Filters")

selected_year = st.sidebar.selectbox(
    "Select Year",
    sorted(df["Year"].unique())
)

selected_term = st.sidebar.selectbox(
    "Select Term",
    sorted(df["Term"].unique())
)

# FILTER DATA
filtered_df = df[
    (df["Year"] == selected_year) &
    (df["Term"] == selected_term)
]

# KPI METRICS
col1, col2, col3 = st.columns(3)

avg_retention = filtered_df["Retention Rate (%)"].mean()
avg_satisfaction = filtered_df["Student Satisfaction (%)"].mean()
total_enrolled = filtered_df["Enrolled"].sum()

col1.metric("Retention Rate", f"{avg_retention:.2f}%")
col2.metric("Student Satisfaction", f"{avg_satisfaction:.2f}%")
col3.metric("Total Enrolled", int(total_enrolled))

# GRAPH 1
st.subheader("Retention Rate")

fig1, ax1 = plt.subplots(figsize=(8,5))

ax1.plot(
    filtered_df.index,
    filtered_df["Retention Rate (%)"],
    marker='o'
)

ax1.set_title("Retention Rate")
ax1.set_xlabel("Records")
ax1.set_ylabel("Retention Rate (%)")
ax1.grid(True)

st.pyplot(fig1)

# GRAPH 2
st.subheader("Student Satisfaction")

fig2, ax2 = plt.subplots(figsize=(8,5))

ax2.bar(
    filtered_df.index,
    filtered_df["Student Satisfaction (%)"]
)

ax2.set_title("Student Satisfaction")
ax2.set_xlabel("Records")
ax2.set_ylabel("Satisfaction (%)")

st.pyplot(fig2)

# GRAPH 3
st.subheader("Enrollment")

fig3, ax3 = plt.subplots(figsize=(8,5))

ax3.bar(
    filtered_df.index,
    filtered_df["Enrolled"]
)

ax3.set_title("Enrolled Students")
ax3.set_xlabel("Records")
ax3.set_ylabel("Students")

st.pyplot(fig3)

# DATAFRAME
st.subheader("Filtered Data")

st.dataframe(filtered_df)

# FOOTER
st.caption("Data Mining - Universidad de la Costa")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# PAGE CONFIGURATION
st.set_page_config(
    page_title="University Dashboard",
    layout="wide"
    st.write("Team Members: Kevin Espitia")
)

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
    df["Term"].unique()
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
st.subheader("Retention Rate Trends")

retention_year = df.groupby("Year")["Retention Rate (%)"].mean()

fig1, ax1 = plt.subplots(figsize=(8,5))

ax1.plot(
    retention_year.index,
    retention_year.values,
    marker='o'
)

ax1.set_title("Retention Rate Over Time")
ax1.set_xlabel("Year")
ax1.set_ylabel("Retention Rate (%)")
ax1.grid(True)

st.pyplot(fig1)

# GRAPH 2
st.subheader("Student Satisfaction by Year")

satisfaction = df.groupby("Year")["Student Satisfaction (%)"].mean()

fig2, ax2 = plt.subplots(figsize=(8,5))

sns.barplot(
    x=satisfaction.index,
    y=satisfaction.values,
    ax=ax2
)

ax2.set_title("Student Satisfaction Scores")
ax2.set_xlabel("Year")
ax2.set_ylabel("Average Satisfaction (%)")

st.pyplot(fig2)

# GRAPH 3
st.subheader("Spring vs Fall Comparison")

term_compare = df.groupby("Term")["Retention Rate (%)"].mean()

fig3, ax3 = plt.subplots(figsize=(6,5))

sns.barplot(
    x=term_compare.index,
    y=term_compare.values,
    ax=ax3
)

ax3.set_title("Retention by Term")
ax3.set_ylabel("Retention Rate (%)")

st.pyplot(fig3)

# DATAFRAME
st.subheader("Filtered Data")

st.dataframe(filtered_df)

# FOOTER
st.caption("Data Mining - Universidad de la Costa")

# app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from health_data import load_data

st.set_page_config(page_title="Health Dashboard", layout="wide")

# Load data
df = load_data()

st.title("📊 Personal Health Dashboard")
st.markdown("Track your **health metrics** using simulated Huawei Watch & Scale data.")

# Show raw data
with st.expander("🔍 Show Raw Data"):
    st.dataframe(df)

# Line Charts
st.subheader("📈 Calories Burned vs Consumed")
fig, ax = plt.subplots()
ax.plot(df["date"], df["calories_burned"], label="Burned")
ax.plot(df["date"], df["calories_consumed"], label="Consumed")
ax.set_xlabel("Date")
ax.set_ylabel("Calories")
ax.legend()
st.pyplot(fig)

# Sleep Trend
st.subheader("🛌 Sleep Duration Over Time")
fig2, ax2 = plt.subplots()
sns.lineplot(data=df, x="date", y="sleep_hours", ax=ax2, marker="o", color="purple")
ax2.set_ylabel("Hours")
st.pyplot(fig2)

# Body Composition
st.subheader("💪 Body Composition Trends")
fig3, ax3 = plt.subplots()
ax3.plot(df["date"], df["body_fat_percent"], label="Body Fat %", color="orange")
ax3.plot(df["date"], df["muscle_mass_kg"], label="Muscle Mass (kg)", color="green")
ax3.set_ylabel("Value")
ax3.legend()
st.pyplot(fig3)

# Correlation Heatmap
st.subheader("🔗 Metric Correlation")
fig4, ax4 = plt.subplots(figsize=(10, 6))
corr = df.drop(columns=["date"]).corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax4)
st.pyplot(fig4)

# Daily Averages
st.subheader("📊 Daily Summary Averages")
st.dataframe(df.describe().loc[["mean", "min", "max"]].T)


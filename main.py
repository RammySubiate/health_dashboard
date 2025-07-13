import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import random
import datetime
import os

# 1. Generate Simulated Health Data
def generate_mock_health_data(days=30):
    today = datetime.date.today()
    records = []

    for i in range(days):
        date = today - datetime.timedelta(days=i)
        record = {
            "date": date.strftime("%Y-%m-%d"),
            "calories_burned": random.randint(1800, 2900),
            "calories_consumed": random.randint(1500, 2500),
            "protein_intake_g": random.randint(110, 170),
            "sleep_hours": round(random.uniform(5.5, 8.5), 1),
            "body_fat_percent": round(random.uniform(17.0, 23.0), 1),
            "muscle_mass_kg": round(random.uniform(38.0, 42.0), 1),
            "resting_heart_rate": random.randint(55, 70),
            "steps": random.randint(4000, 12000),
            "exercise_duration_min": random.randint(20, 90),
        }
        records.append(record)

    return pd.DataFrame(records)

# 2. Save and Load Data
def save_data(df, filename="mock_health_data.csv"):
    df.to_csv(filename, index=False)

def load_data(filename="mock_health_data.csv"):
    df = pd.read_csv(filename)
    df["date"] = pd.to_datetime(df["date"])
    return df.sort_values("date")

# 3. Combine All Plots into One Window
def plot_all_metrics(df):
    fig, axs = plt.subplots(2, 2, figsize=(16, 10))
    fig.suptitle("📊 Health Metrics Overview", fontsize=16)

    # Plot 1: Calories Burned vs. Consumed
    axs[0, 0].plot(df["date"], df["calories_burned"], label="Burned", color="red")
    axs[0, 0].plot(df["date"], df["calories_consumed"], label="Consumed", color="blue")
    axs[0, 0].axhline(2000, color="gray", linestyle="--", label="Reference")
    axs[0, 0].set_title("Calories Burned vs. Consumed")
    axs[0, 0].set_xlabel("Date")
    axs[0, 0].set_ylabel("Calories")
    axs[0, 0].legend()
    axs[0, 0].tick_params(axis='x', rotation=45)
    axs[0, 0].grid(True)

    # Plot 2: Sleep Trend
    sns.lineplot(x="date", y="sleep_hours", data=df, ax=axs[0, 1], color="purple", marker="o")
    axs[0, 1].set_title("Sleep Duration Over Time")
    axs[0, 1].set_xlabel("Date")
    axs[0, 1].set_ylabel("Hours")
    axs[0, 1].tick_params(axis='x', rotation=45)
    axs[0, 1].grid(True)

    # Plot 3: Body Composition
    axs[1, 0].plot(df["date"], df["body_fat_percent"], label="Body Fat %", color="orange")
    axs[1, 0].set_title("Body Composition Trends")
    axs[1, 0].set_xlabel("Date")
    axs[1, 0].set_ylabel("Value")
    axs[1, 0].legend()
    axs[1, 0].tick_params(axis='x', rotation=45)
    axs[1, 0].grid(True)

    # Plot 4: Correlation Heatmap
    corr = df.drop(columns=["date"]).corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=axs[1, 1])
    axs[1, 1].set_title("Correlation Between Health Metrics")

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

# 4. Main Function
def main():
    # Generate and save mock data if not exists
    if not os.path.exists("mock_health_data.csv"):
        df = generate_mock_health_data()
        save_data(df)

    df = load_data()

    # Display preview
    print("\n📋 Sample Data:")
    print(df.head())

    # Show all plots in one figure
    plot_all_metrics(df)

# Run script
if __name__ == "__main__":
    main()

# health_data.py
import pandas as pd
import random
import datetime
import os

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

    df = pd.DataFrame(records)
    return df.sort_values("date")

def load_data():
    filename = "mock_health_data.csv"
    if not os.path.exists(filename):
        df = generate_mock_health_data()
        df.to_csv(filename, index=False)
    df = pd.read_csv(filename)
    df["date"] = pd.to_datetime(df["date"])
    return df.sort_values("date")




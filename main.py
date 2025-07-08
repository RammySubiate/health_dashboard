import random
import datetime
import pandas as pd

def generate_mock_health_data(days=365):
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

# Example usage
df = generate_mock_health_data()
print(df.head())

# df.to_csv("mock_health_data.csv", index=False)
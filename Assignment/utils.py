import csv
import json
from datetime import datetime
import pandas as pd
import numpy as np
from tabulate import tabulate

def log_event(filename, message):
    """Log events like unsubscribe/bounce to a text file."""
    with open(filename, "a") as f:
        f.write(f"{datetime.utcnow()} - {message}\n")


def export_subscribers_csv(subscribers):
    """Export subscriber list to CSV."""
    with open("subscribers.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Email", "Status", "Joined_At"])
        for s in subscribers:
            writer.writerow([s.name, s.email, s.status, s.joined_at])
    print("✅ Subscribers exported to subscribers.csv")


def import_subscribers_json(filename):
    """Import subscribers from a JSON file."""
    with open(filename, "r") as f:
        return json.load(f)


def analyze_performance(engagements):
    """Analyze newsletter open/click rates using Pandas & NumPy."""
    data = []
    for e in engagements:
        data.append({
            "Subscriber": e.subscriber.email,
            "Newsletter": e.newsletter.title,
            "Opened": e.opened,
            "Clicked": e.clicked
        })

    df = pd.DataFrame(data)
    if df.empty:
        print("No data to analyze.")
        return

    open_rate = np.mean(df["Opened"])
    click_rate = np.mean(df["Clicked"])

    print("\n📊 Newsletter Performance:")
    print(tabulate(df, headers="keys", tablefmt="pretty"))
    print(f"\nAverage Open Rate: {open_rate*100:.2f}%")
    print(f"Average Click Rate: {click_rate*100:.2f}%")

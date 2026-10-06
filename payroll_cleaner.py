import pandas as pd

# Simulating raw, unorganized HRIS export
raw_data = {
    "emp_id": ["101", "102", "103"],
    "monthly_hours": [160, 175, 150],
    "hourly_rate": [25.0, 30.0, 22.5]
}

df = pd.DataFrame(raw_data)

# Automating total gross payroll calculation
df["gross_payroll_eur"] = df["monthly_hours"] * df["hourly_rate"]

# Export cleaned file ready for HRIS import
df.to_csv("processed_payroll_export.csv", index=False)
print("Payroll processing complete. File exported.")

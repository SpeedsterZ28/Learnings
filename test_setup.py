import pandas as pd
import sys

# 1. Verify we are using the virtual environment
print("--------------------------------------------------")
print(f"Running Python from: {sys.executable}")
print("--------------------------------------------------")

# 2. Test Pandas with some dummy data
data = {
    'ID': [101, 102, 103],
    'Department': ['Finance', 'Engineering', 'HR'],
    'Status': ['Active', 'Active', 'Pending']
}

df = pd.DataFrame(data)

print("\nSuccess! Pandas created this DataFrame:")
print(df)
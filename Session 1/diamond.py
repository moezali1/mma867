import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv("diamond.csv")

# Split the dataset into training and testing sets
train, test = train_test_split(df, test_size=0.1, random_state=42)

# Save the splits to CSV files
train.to_csv("diamond_train.csv", index=False)
test.to_csv("diamond_test.csv", index=False)

print("Dataset has been split and saved.")

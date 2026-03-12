# DAY 24 – PANDAS COMPLETE PRACTICE FILE

import pandas as pd


# 1. LOAD CSV FILE

df = pd.read_csv("day24_Employee_Data.csv")
# print("\n--- Raw Data ---")
# print(df.head())
# print("\n--- Output ---")


# print("\n--- Bootom 5 Rows ---")
# print(df.tail())


# # 2. BASIC INFORMATION

# print("\nShape:", df.shape)
# print("\nColumns:", df.columns)
# print(df.info())
# print(df.describe())


# # 3. CLEAN TEXT DATA (VERY IMPORTANT)


# Clean Employee Names
# df["Employee_Name"] = df["Employee_Name"].str.strip().str.title()
# print(df.head())

# Clean City Names
# df["City"] = df["City"].str.strip().str.title()
# print(df.head())

# # Clean Department
# df["Department"] = df["Department"].str.strip().str.title()
# print(df.head())

# print("\n--- Cleaned Text Columns ---")
# print(df[["Employee_Name", "City", "Department"]].head())



# # 4. REMOVE DUPLICATES


# print("\nDuplicate Rows:", df.duplicated().sum())
# df = df.drop_duplicates()

# print(df)

# # 5. FILTER DATA


# # Employees from Mumbai
df["City"] = df["City"].str.strip().str.title()
mumbai_emp = df[df["City"] == "Mumbai"]
print(mumbai_emp)
mumbai_emp.to_csv("Mumbai_emp.csv", index=False)











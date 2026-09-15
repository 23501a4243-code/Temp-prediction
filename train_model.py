import pandas as pd
import joblib

from sklearn.ensemble import RandomForestRegressor


# ==========================================
# 1. READ EXCEL DATASET
# ==========================================

df = pd.read_excel("100 Samples.xlsx")

print("Dataset loaded successfully!")
print("Number of samples:", len(df))


# ==========================================
# 2. CLEAN TEMPERATURE COLUMN
# ==========================================

df["Temperature"] = pd.to_numeric(
    df["Temperature"],
    errors="coerce"
)

df = df.dropna(
    subset=["Temperature"]
)


# ==========================================
# 3. SELECT FEATURES
# ==========================================

features = [
    "Age",
    "Gender",
    "Diabetes",
    "B.P",
    "Spo2",
    "Basic Health Issues",
    "Family's\nHealth Issues"
]

X = df[features].copy()

y = df["Temperature"]


# ==========================================
# 4. CLEAN GENDER
# ==========================================

X["Gender"] = (
    X["Gender"]
    .astype(str)
    .str.strip()
    .str.lower()
)

X["Gender"] = X["Gender"].replace({
    "m": "male",
    "f": "female",
    "fem ale": "female"
})


# ==========================================
# 5. HANDLE MISSING VALUES
# ==========================================

X["Age"] = X["Age"].fillna(
    X["Age"].median()
)

X["Spo2"] = X["Spo2"].fillna(
    X["Spo2"].median()
)


categorical_columns = [
    "Gender",
    "Diabetes",
    "B.P",
    "Basic Health Issues",
    "Family's\nHealth Issues"
]


for column in categorical_columns:

    X[column] = X[column].fillna(
        "Unknown"
    )


# ==========================================
# 6. CONVERT TEXT TO NUMBERS
# ==========================================

X = pd.get_dummies(
    X,
    drop_first=True
)


# ==========================================
# 7. CREATE RANDOM FOREST MODEL
# ==========================================

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


# ==========================================
# 8. TRAIN MODEL
# ==========================================

model.fit(
    X,
    y
)


# ==========================================
# 9. SAVE MODEL
# ==========================================

joblib.dump(
    model,
    "temperature_model.pkl"
)


# ==========================================
# 10. SAVE COLUMN INFORMATION
# ==========================================

joblib.dump(
    list(X.columns),
    "model_columns.pkl"
)


print()
print("====================================")
print("MODEL TRAINING COMPLETED")
print("====================================")

print()
print("Created:")
print("temperature_model.pkl")
print("model_columns.pkl")
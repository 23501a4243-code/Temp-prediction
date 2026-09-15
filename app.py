from flask import Flask, render_template, request, jsonify

import pandas as pd
import joblib


# ==========================================
# CREATE FLASK APPLICATION
# ==========================================

app = Flask(__name__)


# ==========================================
# LOAD TRAINED MODEL
# ==========================================

model = joblib.load(
    "temperature_model.pkl"
)

model_columns = joblib.load(
    "model_columns.pkl"
)


# ==========================================
# HOME PAGE
# ==========================================

@app.route("/")
def home():

    return render_template(
        "index.html"
    )


# ==========================================
# PREDICTION
# ==========================================

@app.route(
    "/predict",
    methods=["POST"]
)
def predict():

    try:

        # Get information from frontend

        data = request.get_json()


        age = float(
            data["age"]
        )

        gender = data["gender"]

        diabetes = data["diabetes"]

        bp = data["bp"]

        spo2 = float(
            data["spo2"]
        )

        basic_health = data[
            "basic_health"
        ]

        family_health = data[
            "family_health"
        ]


        # ======================================
        # CREATE DATAFRAME
        # ======================================

        input_data = pd.DataFrame({

            "Age": [age],

            "Gender": [gender],

            "Diabetes": [diabetes],

            "B.P": [bp],

            "Spo2": [spo2],

            "Basic Health Issues": [
                basic_health
            ],

            "Family's\nHealth Issues": [
                family_health
            ]

        })


        # ======================================
        # CLEAN GENDER
        # ======================================

        input_data["Gender"] = (
            input_data["Gender"]
            .astype(str)
            .str.strip()
            .str.lower()
        )


        # ======================================
        # ONE HOT ENCODING
        # ======================================

        input_data = pd.get_dummies(
            input_data,
            drop_first=True
        )


        # ======================================
        # MATCH TRAINING COLUMNS
        # ======================================

        input_data = input_data.reindex(
            columns=model_columns,
            fill_value=0
        )


        # ======================================
        # MAKE PREDICTION
        # ======================================

        prediction = model.predict(
            input_data
        )


        predicted_temperature = round(
            float(prediction[0]),
            2
        )


        # ======================================
        # RETURN RESULT
        # ======================================

        return jsonify({

            "success": True,

            "temperature":
                predicted_temperature

        })


    except Exception as e:

        return jsonify({

            "success": False,

            "error": str(e)

        })


# ==========================================
# START FLASK
# ==========================================

if __name__ == "__main__":

    app.run(
        debug=False
    )
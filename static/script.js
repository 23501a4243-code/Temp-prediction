const form =
    document.getElementById(
        "predictionForm"
    );


const result =
    document.getElementById(
        "result"
    );


const error =
    document.getElementById(
        "error"
    );


const temperature =
    document.getElementById(
        "temperature"
    );


form.addEventListener(
    "submit",
    async function(event) {

        event.preventDefault();


        // =================================
        // GET USER INPUT
        // =================================

        const age =
            document.getElementById(
                "age"
            ).value;


        const gender =
            document.getElementById(
                "gender"
            ).value;


        const diabetes =
            document.querySelector(
                'input[name="diabetes"]:checked'
            ).value;


        const bp =
            document.querySelector(
                'input[name="bp"]:checked'
            ).value;


        const spo2 =
            document.getElementById(
                "spo2"
            ).value;


        const basicHealth =
            document.querySelector(
                'input[name="basic_health"]:checked'
            ).value;


        const familyHealth =
            document.querySelector(
                'input[name="family_health"]:checked'
            ).value;


        // =================================
        // VALIDATION
        // =================================

        if (age < 0 || age > 100) {

            showError(
                "Age must be between 0 and 100."
            );

            return;

        }


       if (!spo2) {

    showError(
        "Please select an SpO2 range."
    );

    return;

}


        // =================================
        // SEND DATA TO FLASK
        // =================================

        try {

            const response =
                await fetch(
                    "/predict",
                    {

                        method: "POST",

                        headers: {

                            "Content-Type":
                                "application/json"

                        },

                        body:
                            JSON.stringify({

                                age: age,

                                gender: gender,

                                diabetes: diabetes,

                                bp: bp,

                                spo2: spo2,

                                basic_health:
                                    basicHealth,

                                family_health:
                                    familyHealth

                            })

                    }
                );


            const data =
                await response.json();


            // =================================
            // DISPLAY PREDICTION
            // =================================

            if (data.success) {

                temperature.textContent =
                    data.temperature + " °C";

                result.classList.remove(
                    "hidden"
                );

                error.classList.add(
                    "hidden"
                );

            }

            else {

                showError(
                    data.error
                );

            }


        }

        catch (err) {

            showError(
                "Could not connect to the server."
            );

        }

    }
);


// ==========================================
// ERROR FUNCTION
// ==========================================

function showError(message) {

    error.textContent =
        message;

    error.classList.remove(
        "hidden"
    );

    result.classList.add(
        "hidden"
    );

}

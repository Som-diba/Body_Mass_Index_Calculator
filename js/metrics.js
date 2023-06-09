const form = document.getElementById("bmi-form");

// get input fields
const weight = document.getElementById("weight");
const height = document.getElementById("height");

const recommendation = document.getElementById("recommendation");
const result = document.getElementById("bmi-result");

// hide recommendation element
recommendation.style.display = "none";

// listen to form submit event
form.addEventListener("submit", function (e) {
    // prevent form default behaviour ie: page refresh
    e.preventDefault();
    e.stopPropagation();

    // get form input data
    const weightValue = weight.value;
    const heightValue = height.value;

    calc_bmi(parseFloat(weightValue), parseFloat(heightValue));
    // reset form
    // form.reset();
})

// bmi calculation function
function calc_bmi(weight, height) {

    //   convert height to meters
    const height_in_m = height / 100

    let bmi = weight / Math.pow(height_in_m, 2)
    //rounding bmi to 2 decimal places
    // bmi = bmi.toFixed(2);
    bmi = Math.round(bmi * 100) / 100;
    // display bmi result
    result.textContent = bmi;
    suggest_meals(bmi);
}


function suggest_meals(bmi) {

    let recommend = ""
    if (bmi < 18.5) {
        recommend = "You are underweight. You may consider meals rich in protein and healthy fats. Examples include eggs, lean meats, fish, nuts, and avocados."
    } else if (18.5 <= bmi && bmi < 24.9) {
        recommend = "Your weight is normal. Maintain a balanced diet with a variety of fruits, vegetables, whole grains, lean proteins, and healthy fats."
    } else if (24.9 <= bmi && bmi < 29.9) {
        recommend = "You are overweight. Focus on portion control and incorporate more fruits, vegetables, whole grains, lean proteins, and low-fat dairy into your meals."
    } else {
        recommend = "You are in the obese range. It is advisable to consult a healthcare professional or nutritionist for a personalized meal plan."
    }
    // change recommendation text to recommend
    recommendation.textContent = recommend;
    // show recommendation
    recommendation.style.display = "block";
    return recommend
}

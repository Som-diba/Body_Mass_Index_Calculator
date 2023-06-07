const form = document.getElementById("bmi-form");

// get input fields
const feet = document.getElementById("feet");
const inches = document.getElementById("inches");
const pounds = document.getElementById("pounds");

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
    const feetValue = feet.value;
    const inchesValue = inches.value;
    const poundsValue = pounds.value;
    calc_bmi(parseFloat(feetValue), parseFloat(inchesValue), parseFloat(poundsValue));
    // reset form
    form.reset();
})

// bmi calculation function
function calc_bmi(feet, inches, pounds) {

    //Conversion fators
    const lbs_to_kg = 0.4536
    const in_to_m = 0.0254

    //   convert height to meters
    const height = ((feet * 12) + inches) * in_to_m

    //   convert weight to kg
    const weight = pounds * lbs_to_kg

    let bmi = weight/ Math.pow(height, 2) 
    //rounding bmi to 2 decimal places
    bmi = bmi.toFixed(2);
    // display bmi result
    result.textContent = bmi;
    suggest_meals(bmi);
}


function suggest_meals(bmi) {

    let recommend = ""
    if (bmi < 18.5) {
        recommend = "You are underweight.\nYou may consider meals rich in protein and healthy fats. Examples include eggs, lean meats, fish, nuts, and avocados."
    } else if (18.5 <= bmi < 24.9) {
        recommend = "Your weight is normal.\nMaintain a balanced diet with a variety of fruits, vegetables, whole grains, lean proteins, and healthy fats."
    } else if (24.9 <= bmi < 29.9) {
        recommend = "You are overweight.\nFocus on portion control and incorporate more fruits, vegetables, whole grains, lean proteins, and low-fat dairy into your meals."
    } else {
        recommend = "You are in the obese range.\nIt is advisable to consult a healthcare professional or nutritionist for a personalized meal plan."
    }
    // change recommendation text to recommend
    recommendation.textContent = recommend;
    // show recommendation
    recommendation.style.display = "block";
    return recommend
}

const DIABETES_TYPES = {
    '1': '1 типа',
    '2': '2 типа',
    'mody': 'Гестационный',
    'many_types': 'Несколько типов',
}

const TREATMENT_TYPES = {
    'insulin_therapy': 'Инсулинотерапия',
    'preparations': 'Препараты',
}

const GENDER = {
    'MALE': 'Мужской',
    'FEMALE': 'Женский',
}

const diabetesType = document.getElementById('diabetesType')
const treatmentType = document.getElementById('treatmentType')
const gender = document.getElementById('gender')

const replaceTextToHuman = () => {
    diabetesType.textContent = DIABETES_TYPES[diabetesType.textContent];
    gender.textContent = GENDER[gender.textContent];
    treatmentType.textContent = TREATMENT_TYPES[treatmentType.textContent];
}

const getQueryParam = (param) => {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(param);
}

const displayMessage = () => {
    const toast = document.getElementById("success-toast");

    toast.classList.remove("hidden");
    setTimeout(() => {
        toast.classList.add("opacity-100");
    }, 100);

    setTimeout(() => {
        toast.classList.remove("opacity-100");
        toast.classList.add("opacity-0");

        setTimeout(() => {
            toast.classList.add("hidden");
        }, 500);
    }, 3000);
}

document.addEventListener('DOMContentLoaded', (event) => {
    replaceTextToHuman();

    if (getQueryParam("success_change_password") === "true") {
        displayMessage();
    }
})

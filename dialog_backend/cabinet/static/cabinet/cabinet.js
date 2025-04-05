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

const INFO_MESSAGES = {
    'success_change_password': 'Пароль успешно изменен!',
    'success_edit_profile': 'Профиль успешно обновлен!',
}

const diabetesType = document.getElementById('diabetesType')
const treatmentType = document.getElementById('treatmentType')
const userName = document.getElementById('userName')
const gender = document.getElementById('gender')

const notifyMessage = document.getElementById('notifyMessage')

const replaceTextToHuman = () => {
    diabetesType.textContent = DIABETES_TYPES[diabetesType.textContent];
    gender.textContent = GENDER[gender.textContent];
    treatmentType.textContent = TREATMENT_TYPES[treatmentType.textContent];
}

const getQueryParam = (param) => {
    const urlParams = new URLSearchParams(window.location.search);
    return urlParams.get(param);
}

const displayMessage = (urlParam) => {
    const toast = document.getElementById("success-toast");
    toast.textContent = INFO_MESSAGES[urlParam]

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

const fetchDailyLogFill = async () => {
    const notifyWindow = document.getElementById('notifyWindow')

    const response = await fetch(
        `daily_log/filled/?username=${userName.textContent}`,
        {
            method: 'get',
        }
    )

    if (!response.ok) {
        notifyWindow.classList.toggle('hidden')
        notifyMessage.textContent = 'Ошибка! Дневной отчет не создан'
        return
    }

    const data = await response.json()

    if (!data['is_filled']) {
        notifyWindow.classList.toggle('hidden')
        notifyMessage.textContent = 'Дневной отчет не заполнен!'
    }
}

document.addEventListener('DOMContentLoaded', (event) => {
    replaceTextToHuman();

    if (getQueryParam("success_change_password") === "true") {
        displayMessage('success_change_password');
    }
    if (getQueryParam("success_edit_profile") === "true") {
        displayMessage('success_edit_profile');
    }

    fetchDailyLogFill();
})

const logoutForm = document.getElementById('logoutForm')
logoutForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    if (!confirm('Вы действительно хотите выйти?')) {
        return;
    }

    const form = event.target;
    const formData = new FormData(form);

    const response = await fetch(
        form.action,
        {
            method: form.method,
            body: formData,
        },
    );

    if (!response.ok) {
        alert('Ошибка выхода');
        throw new Error(`Ошибка выхода: ${response.status}`);
    }

    window.location.href = '/';

    alert('Выход успешен');
})

const pressureOpenModalBtn = document.getElementById('pressureOpenModalBtn');
const closeModalPressureBtn = document.getElementById('closeModalPressureBtn');
const modalPressure = document.getElementById('modalPressure');

pressureOpenModalBtn.addEventListener('click', () => {
modalPressure.classList.remove('hidden');
});

closeModalPressureBtn.addEventListener('click', () => {
modalPressure.classList.add('hidden');
});

modalPressure.addEventListener('click', (e) => {
if (e.target === modalPressure) {
    modalPressure.classList.add('hidden');
}
});

const glucoseOpenModalBtn = document.getElementById('glucoseOpenModalBtn');
const closeModalGlucoseBtn = document.getElementById('closeModalGlucoseBtn');
const modalGlucose = document.getElementById('modalGlucose');

glucoseOpenModalBtn.addEventListener('click', () => {
modalGlucose.classList.remove('hidden');
});

closeModalGlucoseBtn.addEventListener('click', () => {
modalGlucose.classList.add('hidden');
});

modalGlucose.addEventListener('click', (e) => {
if (e.target === modalGlucose) {
    modalGlucose.classList.add('hidden');
}
});

const temperatureOpenModalBtn = document.getElementById('temperatureOpenModalBtn');
const closeModalTemperatureBtn = document.getElementById('closeModalTemperatureBtn');
const modalTemperature = document.getElementById('modalTemperature');

temperatureOpenModalBtn.addEventListener('click', () => {
modalTemperature.classList.remove('hidden');
});

closeModalTemperatureBtn.addEventListener('click', () => {
modalTemperature.classList.add('hidden');
});

modalTemperature.addEventListener('click', (e) => {
if (e.target === modalTemperature) {
    modalTemperature.classList.add('hidden');
}
});

let ctx = document.getElementById('diabetesChart').getContext('2d');
let diabetesChart = new Chart(ctx, {
    type: 'pie',
    data: {
        datasets: [{
            label: 'Контроль диабета',
            data: [35, 25, 20, 20],
            backgroundColor: [
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(54, 162, 235, 0.2)',
            ],
            borderColor: [
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(54, 162, 235, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,  // Делаем график адаптивным
        plugins: {
            legend: {
                position: 'top',
                align: 'start',
                labels: {
                    font: {
                        size: 14,
                    },
                },
            },
            tooltip: {
                callbacks: {
                    label: function(tooltipItem) {
                        return tooltipItem.label + ': ' + tooltipItem.raw + '%';  // Отображение процентов
                    }
                }
            }
        }
    }
});

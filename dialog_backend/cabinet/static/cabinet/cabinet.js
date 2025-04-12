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
    'filled_daily_log': 'Дневной отчет успешно заполнен!',
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
    if (getQueryParam('filled_daily_log')) {
        displayMessage('filled_daily_log');
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
const formPressure = document.getElementById('formPressure');


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

formPressure.addEventListener('submit', async (e) => {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);

    const response = await fetch(
        form.action,
        {
            method: form.method,
            body: formData,
        },
    );

    if (!response.ok) {
        const glucoseError = document.getElementById('pressureError');
        glucoseError.classList.remove('hidden');
        glucoseError.textContent = await response.text()
        return
    }

    const pressureSuccess = document.getElementById('pressureSuccess');
    pressureSuccess.classList.remove('hidden');
    pressureSuccess.textContent = 'Успешно сохранено'
    setTimeout(() => {
            pressureSuccess.classList.add('hidden')
        },
        2000
    )
})

const glucoseOpenModalBtn = document.getElementById('glucoseOpenModalBtn');
const closeModalGlucoseBtn = document.getElementById('closeModalGlucoseBtn');
const modalGlucose = document.getElementById('modalGlucose');
const formGlucose = document.getElementById('formGlucose');

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
formGlucose.addEventListener('submit', async (e) => {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);

    const response = await fetch(
        form.action,
        {
            method: form.method,
            body: formData,
        },
    );

    if (!response.ok) {
        const glucoseError = document.getElementById('glucoseError');
        glucoseError.classList.remove('hidden');
        glucoseError.textContent = await response.text()
        return
    }

    const glucoseSuccess = document.getElementById('glucoseSuccess');
    glucoseSuccess.classList.remove('hidden');
    glucoseSuccess.textContent = 'Успешно сохранено'

    setTimeout(() => {
        glucoseSuccess.classList.add('hidden')
    },
    2000
    )
})

const temperatureOpenModalBtn = document.getElementById('temperatureOpenModalBtn');
const closeModalTemperatureBtn = document.getElementById('closeModalTemperatureBtn');
const modalTemperature = document.getElementById('modalTemperature');
const formTemperature = document.getElementById('formTemperature');


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
formTemperature.addEventListener('submit', async (e) => {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);

    const response = await fetch(
        form.action,
        {
            method: form.method,
            body: formData,
        },
    );

    if (!response.ok) {
        const glucoseError = document.getElementById('temperatureError');
        glucoseError.classList.remove('hidden');
        glucoseError.textContent = await response.text()
        return
    }

    const temperatureSuccess = document.getElementById('temperatureSuccess');
    temperatureSuccess.classList.remove('hidden');
    temperatureSuccess.textContent = 'Успешно сохранено'

    setTimeout(() => {
        temperatureSuccess.classList.add('hidden');
    }, 2000)
})

const getGlucoseData = async () => {
    const glucoseResponse = await fetch(
        '/data_tracking/glucose_data/'
    )
    if (!glucoseResponse.ok) {
        console.error(await glucoseResponse.text())
        return;
    }
    const {data, labels} = await glucoseResponse.json()

    return {
        data: data,
        labels: labels,
    }
}

const getTemperatureData = async () => {
    const temperatureResponse = await fetch(
        '/data_tracking/temperature_data',
    )
    if (!temperatureResponse.ok) {
        console.error(await temperatureResponse.text())
        return;
    }
    const {data, labels} = await temperatureResponse.json()
    return {
        labels: labels,
        temperatureData: data,
    }
}

const getPressureData = async () => {
    const pressureResponse = await fetch(
        '/data_tracking/pressure_data',
    )
    if (!pressureResponse.ok) {
        console.error(await pressureResponse.text())
        return;
    }
    const {labels, systolic, diastolic} = await pressureResponse.json()
    return {
        labels: labels,
        systolicData: systolic,
        diastolicData: diastolic,
    }
}

document.addEventListener('DOMContentLoaded', async () => {
    const baseOptions = {
        type: 'line',
        options: {
            responsive: true,
            plugins: {
            legend: { display: true },
        },
        scales: {
            x: { title: { display: true, text: 'Время' } },
            y: { title: { display: true, text: 'Значение' }, beginAtZero: false }
        },
    }
  };
    const glucoseChart = document.getElementById('glucoseChart')
    const glucoseLoader = document.getElementById('glucoseChart-loader')
    if (glucoseChart) {
        const {data, labels} = await getGlucoseData();
        new Chart(glucoseChart, {
        ...baseOptions,
        data: {
            labels,
            datasets: [{
                label: 'Глюкоза (ммоль/л)',
                data: data,
                borderColor: '#34d399',
                backgroundColor: '#6ee7b7',
                tension: 0.3,
                fill: false
            }]
        },
        options: {
            responsive: true,
            animation: {
                duration: 1000,
                onComplete: () => {
                    glucoseLoader.style.display = 'none'
                }
            }
        }
    });
    }
    const tempChart = document.getElementById('tempChart')
    const tempLoader = document.getElementById('tempChart-loader')
    if (tempChart) {
        const {labels, temperatureData} = await getTemperatureData();
        new Chart(tempChart, {
            ...baseOptions,
            data: {
                labels,
                datasets: [{
                    label: 'Температура (°C)',
                    data: temperatureData,
                    borderColor: '#60a5fa',
                    backgroundColor: '#bfdbfe',
                    tension: 0.3,
                    fill: false
                }]
            },
            options: {
                responsive: true,
                animation: {
                    duration: 1000,
                    onComplete: () => {
                        tempLoader.style.display = 'none'
                    }
                }
            }
        });
    }

    const pressureChart = document.getElementById('pressureChart');
    const pressureLoader = document.getElementById('pressureChart-loader')
    if (pressureChart) {
        const {labels, systolicData, diastolicData} = await getPressureData();
        new Chart(pressureChart, {
            ...baseOptions,
            data: {
                labels,
                datasets: [
                    {
                        label: 'Систолическое',
                        data: systolicData,
                        borderColor: '#f87171',
                        backgroundColor: '#fecaca',
                        tension: 0.3,
                        fill: false
                    },
                    {
                        label: 'Диастолическое',
                        data: diastolicData,
                        borderColor: '#facc15',
                        backgroundColor: '#fde68a',
                        tension: 0.3,
                        fill: false
                    }
                ]
            },
            options: {
                responsive: true,
                animation: {
                    duration: 1000,
                    onComplete: () => {
                        pressureLoader.style.display = 'none'
                    }
                }
            }
        });
    }
});

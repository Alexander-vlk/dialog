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
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

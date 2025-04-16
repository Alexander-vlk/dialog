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
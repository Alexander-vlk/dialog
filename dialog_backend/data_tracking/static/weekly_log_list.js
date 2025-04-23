const MOOD = {
  1: 'Ужасное',
  2: 'Плохое',
  3: 'Нормальное',
  4: 'Хорошее',
  5: 'Отличное',
}

const weeklyLogId = document.querySelector('#weeklyLogId').textContent

const fetchGlucoseDataPerWeek = async () => {
    const glucoseUrl = '/api/data-tracking/glucose'

    const response = await fetch(
        `${glucoseUrl}/?time_period=week&id=${weeklyLogId}`,
    )

    if (!response.ok) {
        console.error(await response.text())
        return;
    }

    return await response.json()
}

const fetchPressureDataPerWeek = async () => {
    const glucoseUrl = '/api/data-tracking/pressure'

    const response = await fetch(
        `${glucoseUrl}/?time_period=week&id=${weeklyLogId}`,
    )

    if (!response.ok) {
        console.error(await response.text())
        return;
    }

    return await response.json()
}

const getGlucoseData = async () => {
    const glucoseData = await fetchGlucoseDataPerWeek();

    const result = {
        labels: [],
        data: [],
    }

        for (const {created_at, level} of glucoseData) {
        result.labels.push(created_at)
        result.data.push(level)
    }

    return result
}

const getPressureData = async () => {
    const pressureData = await fetchPressureDataPerWeek();

    const result = {
        labels: [],
        systolicData: [],
        diastolicData: [],
    }
    for (const {created_at, systolic, diastolic} of pressureData) {
        result.labels.push(created_at)
        result.systolicData.push(systolic)
        result.diastolicData.push(diastolic)
    }
    return result
}

const createGlucosePlot = async () => {
    const glucoseCtx = document.getElementById('glucoseChart').getContext('2d');
    const {data, labels} = await getGlucoseData()
    new Chart(glucoseCtx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Глюкоза (ммоль/л)',
                data: data,
                backgroundColor: 'rgba(59, 130, 246, 0.2)',
                borderColor: 'rgba(59, 130, 246, 1)',
                borderWidth: 2,
                tension: 0.3
            }]
        },
        options: {
            scales: {
                y: { beginAtZero: false }
            }
        }
    });
}

const createPressurePlot = async () => {
    const pressureCtx = document.getElementById('pressureChart').getContext('2d');
    const {labels, systolicData, diastolicData} = await getPressureData();
    new Chart(pressureCtx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
            {
                label: 'Систолическое (мм рт. ст.)',
                data: systolicData,
                borderColor: 'rgba(34, 197, 94, 1)',
                backgroundColor: 'rgba(34, 197, 94, 0.2)',
                borderWidth: 2,
                tension: 0.3
            },
            {
                label: 'Диастолическое (мм рт. ст.)',
                data: diastolicData,
                borderColor: 'rgba(239, 68, 68, 1)',
                backgroundColor: 'rgba(239, 68, 68, 0.2)',
                borderWidth: 2,
                tension: 0.3
            }
            ]
        },
        options: {
            scales: {
                y: { beginAtZero: false }
            }
        }
    });
}

document.addEventListener('DOMContentLoaded', async () => {
    await createGlucosePlot()
    await createPressurePlot()

    const overallFeeling = document.getElementById('overall-feeling');
    const moodFloat = Math.round(parseFloat(overallFeeling.dataset.health))
    overallFeeling.textContent = MOOD[moodFloat]
})

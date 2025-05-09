const menuToggle = document.getElementById('menuToggle');
const sidebar = document.getElementById('sidebar');
const overlay = document.getElementById('overlay');

const monthlyLogId = document.getElementById('monthlyLogId').textContent;

menuToggle.addEventListener('click', () => {
    sidebar.classList.toggle('-translate-x-full');
    overlay.classList.toggle('hidden');
});

overlay.addEventListener('click', () => {
    sidebar.classList.add('-translate-x-full');
    overlay.classList.add('hidden');
});

const pressureUrl = `/api/data-tracking/pressure/?time_period=month&id=${monthlyLogId}`;

const getPressureData = async () => {
    const pressureResponse = await fetch(pressureUrl)
    if (!pressureResponse.ok) {
        console.error(await pressureResponse.text())
        return;
    }

    const pressureData = await pressureResponse.json()

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

const getHealthData = async () => {
    const healthUrl = `/api/data-tracking/health/?id=${monthlyLogId}`;
    const healthDataResponse = await fetch(healthUrl)
    if (!healthDataResponse) {
        console.error(await healthDataResponse.text())
        return;
    }

    const healthData = await healthDataResponse.json()
    const result = {
        labels: [],
        data: [],
    }
    for (const {name, count} of healthData) {
        result.labels.push(name)
        result.data.push(count)
    }
    return result
}

const createHealthPlot = async () => {
    const ctxState = document.getElementById('stateBarChart');
    const {labels, data} = await getHealthData();
    await getHealthData();
    new Chart(ctxState, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Количество',
                data: data,
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { display: false }
            }
        }
    });
}

const getAvgBjuData = async () => {
    const avgBjuUrl = `/api/data-tracking/bju/average/?id=${monthlyLogId}`;
    const avgBjuResponse = await fetch(avgBjuUrl);

    if (!avgBjuResponse.ok) {
        console.error(await avgBjuResponse.text())
        return;
    }

    const avgBjuData = await avgBjuResponse.json()
    return {
        labels: Object.keys(avgBjuData.average_bju),
        data: Object.values(avgBjuData.average_bju),
    }
}

const createAvgBjuPlot = async () => {
    const ctxBJU = document.getElementById('bjuPieChart');
    const {labels, data} = await getAvgBjuData();
    new Chart(ctxBJU, {
        type: 'pie',
        data: {
            labels: ['Белки', 'Жиры', 'Углеводы'],
            datasets: [{
                data: data,
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: { position: 'bottom' }
            }
        }
    });
}

const createPressurePlot = async () => {
    const ctxPressure = document.getElementById('pressureLineChart');
    const {labels, systolicData, diastolicData} = await getPressureData();
    new Chart(ctxPressure, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Систолическое',
                    data: systolicData,
                    borderColor: '#10b981',
                    tension: 0.3,
                    fill: false
                },
                {
                    label: 'Диастолическое',
                    data: diastolicData,
                    borderColor: '#f87171',
                    tension: 0.3,
                    fill: false
                },
            ],
        },
        options: {
            responsive: true,
            scales: {
                x: { title: { display: true, text: 'День месяца' } },
                y: { title: { display: true, text: 'мм рт. ст.' } }
            }
        }
    });
}

const glucoseUrl = `/api/data-tracking/glucose/?time_period=month&id=${monthlyLogId}`;

const getGlucosePerMonthData = async () => {
    const glucoseResponse = await fetch(glucoseUrl);
    if (!glucoseResponse.ok) {
        console.error(await glucoseResponse.text())
        return;
    }
    const glucoseData = await glucoseResponse.json()

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

const createGlucoseChart = async () => {
    const ctxGlucose = document.getElementById('glucoseLineChart');
    const {labels, data} = await getGlucosePerMonthData();
    new Chart(ctxGlucose, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Глюкоза (ммоль/л)',
                data: data,
                borderColor: '#3b82f6',
                backgroundColor: 'rgba(59, 130, 246, 0.2)',
                fill: true,
                tension: 0.3
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: { title: { display: true, text: 'День месяца' } },
                y: { title: { display: true, text: 'ммоль/л' } }
            }
        }
    });
}

document.addEventListener('DOMContentLoaded', async () => {
    await createAvgBjuPlot();
    await createHealthPlot();
    await createGlucoseChart();
    await createPressurePlot();
})

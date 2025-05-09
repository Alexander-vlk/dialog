const menuToggle = document.getElementById('menuToggle');
const sidebar = document.getElementById('sidebar');
const overlay = document.getElementById('overlay');

menuToggle.addEventListener('click', () => {
    sidebar.classList.toggle('-translate-x-full');
    overlay.classList.toggle('hidden');
});

overlay.addEventListener('click', () => {
    sidebar.classList.add('-translate-x-full');
    overlay.classList.add('hidden');
});

const ctxState = document.getElementById('stateBarChart');
new Chart(ctxState, {
    type: 'bar',
    data: {
        labels: ['Сонливость', 'Усталость', 'Раздражение', 'Бодрость', 'Апатия'],
        datasets: [{
            label: 'Количество',
            data: [12, 9, 5, 7, 4],
            backgroundColor: ['#facc15', '#94a3b8', '#f87171', '#34d399', '#c084fc']
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: { display: false }
        }
    }
});

const ctxBJU = document.getElementById('bjuPieChart');
new Chart(ctxBJU, {
type: 'pie',
data: {
labels: ['Белки', 'Жиры', 'Углеводы'],
datasets: [{
data: [15, 25, 60],
backgroundColor: ['#34d399', '#fbbf24', '#60a5fa']
}]
},
options: {
responsive: true,
plugins: {
legend: { position: 'bottom' }
}
}
});

const ctxPressure = document.getElementById('pressureLineChart');
new Chart(ctxPressure, {
type: 'line',
data: {
labels: Array.from({length: 30}, (_, i) => i + 1),
datasets: [{
label: 'Систолическое',
data: [120, 125, 130, 122, 126, 118],
borderColor: '#10b981',
tension: 0.3,
fill: false
}, {
label: 'Диастолическое',
data: [80, 83, 85, 79, 81, 78],
borderColor: '#f87171',
tension: 0.3,
fill: false
}]
},
options: {
responsive: true,
scales: {
x: { title: { display: true, text: 'День месяца' } },
y: { title: { display: true, text: 'мм рт. ст.' } }
}
}
});

const monthlyLogId = document.getElementById('monthlyLogId').textContent;
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
    await createGlucoseChart()
})

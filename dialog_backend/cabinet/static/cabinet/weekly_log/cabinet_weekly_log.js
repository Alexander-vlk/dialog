const bjuData = {
    labels: ['Белки', 'Жиры', 'Углеводы'],
    datasets: [{
        label: 'БЖУ',
        data: [30, 25, 45],
        backgroundColor: ['#34d399', '#f87171', '#60a5fa'],
        hoverOffset: 10
    }]
};

const glucoseData = {
    labels: ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'],
    datasets: [{
        label: 'Глюкоза',
        data: [5.4, 5.7, 5.3, 6.1, 5.8, 5.9, 5.6],
        fill: false,
        borderColor: '#10b981',
        tension: 0.3
    }]
};

const bpData = {
    labels: ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'],
    datasets: [{
        label: 'Давление',
        data: [120, 118, 122, 121, 119, 117, 120],
        fill: false,
        borderColor: '#3b82f6',
        tension: 0.3
    }]
};

const configBJU = { type: 'doughnut', data: bjuData };
const weeklyGlucoseConfig = { type: 'line', data: glucoseData };
const configBP = { type: 'line', data: bpData };

window.addEventListener('load', () => {
    new Chart(document.getElementById('bjuChart'), configBJU);
    new Chart(document.getElementById('weeklyGlucoseChart'), weeklyGlucoseConfig);
    new Chart(document.getElementById('bpChart'), configBP);
});
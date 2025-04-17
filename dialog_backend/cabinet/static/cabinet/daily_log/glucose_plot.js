import {baseOptions} from "./common.js";

const glucoseUrl = '../api/data-tracking/glucose/?time_period=today';

const getGlucoseData = async () => {
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

const glucoseChart = document.getElementById('glucoseChart')
const glucoseLoader = document.getElementById('glucoseChart-loader')
if (glucoseChart) {
    const {labels, data} = await getGlucoseData();
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
import {baseOptions} from "./common.js";

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
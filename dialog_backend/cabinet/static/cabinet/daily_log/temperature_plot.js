import {baseOptions} from "./common.js";

const temperatureUrl = '../api/data-tracking/body-temperature/?time_period=today';

const getTemperatureData = async () => {
    const temperatureResponse = await fetch(temperatureUrl);
    if (!temperatureResponse.ok) {
        console.error(await temperatureResponse.text())
        return;
    }
    const temperatureData = await temperatureResponse.json()
    const result = {
        labels: [],
        temperatureData: [],
    }
    for (const {created_at, temperature} of temperatureData) {
        result.labels.push(created_at)
        result.temperatureData.push(temperature)
    }

    return result
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
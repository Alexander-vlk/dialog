import {baseOptions} from "./common.js";

const getTemperatureData = async () => {
    const temperatureResponse = await fetch(
        '/data_tracking/temperature_data',
    )
    if (!temperatureResponse.ok) {
        console.error(await temperatureResponse.text())
        return;
    }
    const {data, labels} = await temperatureResponse.json()
    return {
        labels: labels,
        temperatureData: data,
    }
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
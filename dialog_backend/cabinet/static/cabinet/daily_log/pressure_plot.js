import { baseOptions } from './common.js'

const pressureUrl = '../api/data-tracking/pressure/?today=true'

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

const pressureChart = document.getElementById('pressureChart');
const pressureLoader = document.getElementById('pressureChart-loader')
if (pressureChart) {
    const {labels, systolicData, diastolicData} = await getPressureData();
    new Chart(pressureChart, {
        ...baseOptions,
        data: {
            labels,
            datasets: [
                {
                    label: 'Систолическое',
                    data: systolicData,
                    borderColor: '#f87171',
                    backgroundColor: '#fecaca',
                    tension: 0.3,
                    fill: false
                },
                {
                    label: 'Диастолическое',
                    data: diastolicData,
                    borderColor: '#facc15',
                    backgroundColor: '#fde68a',
                    tension: 0.3,
                    fill: false
                }
            ]
        },
        options: {
            responsive: true,
            animation: {
                duration: 1000,
                onComplete: () => {
                    pressureLoader.style.display = 'none'
                }
            }
        }
    });
}
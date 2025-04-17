const fetchWeeklyLogData = async () => {
    const weeklyLogUrl = '/api/data-tracking/weekly-log/'
    const weeklyLogDataResponse = await fetch(weeklyLogUrl)

    if (!weeklyLogDataResponse.ok) {
        console.error(await weeklyLogDataResponse.json())
        return
    }

    return weeklyLogDataResponse.json()
}

const getBjuData = async () => {
    const weeklyLogData = await fetchWeeklyLogData()
    const {avg_calories, avg_proteins, avg_fats, avg_carbs} = weeklyLogData.avg_data

    return [avg_proteins, avg_fats, avg_carbs]
}

const createBjuPlot = async () => {
    const bjuDiagram = document.getElementById('weeklyLogBJUChart');
    if (!bjuDiagram) {
        return
    }

    const bjuData = await getBjuData();
    new Chart(
        bjuDiagram,
        {
            type: 'doughnut',
            data: {
                labels: ['Белки', 'Жиры', 'Углеводы'],
                datasets: [{
                    label: 'БЖУ',
                    data: bjuData,
                    backgroundColor: ['#34d399', '#f87171', '#60a5fa'],
                    hoverOffset: 10
                }]
            },
        },
    );
}

const fetchCaloriesData = async () => {
    const caloriesUrl = '/api/data-tracking/calories';
    const caloriesResponse = await fetch(caloriesUrl);

    if (!caloriesResponse.ok) {
        console.error(await caloriesResponse.json())
        return
    }

    return await caloriesResponse.json()
}

const getCaloriesData = async () => {
    const caloriesData = await fetchCaloriesData();

    const result = {
        labels: [],
        calories: [],
    }
    for (const {calories, date} of caloriesData.calories_per_day) {
        result.labels.push(date)
        result.calories.push(calories)
    }
    return result
}

const createCaloriesPlot = async () => {
    const caloriesDiagram = document.getElementById('weeklyLogCaloriesChart');

    if (!caloriesDiagram) {
        return
    }

    const {labels, calories} = await getCaloriesData();
    new Chart(
        caloriesDiagram,
        {
            type: 'line',
            options: {
                responsive: true,
                plugins: {
                    legend: { display: true },
                },
                scales: {
                    x: { title: { display: true, text: 'Время' } },
                    y: { title: { display: true, text: 'Значение' }, beginAtZero: false }
                },
            },
            data: {
                labels,
                datasets: [{
                    label: 'Калории',
                    data: calories,
                    borderColor: '#60a5fa',
                    backgroundColor: '#bfdbfe',
                    tension: 0.3,
                    fill: false
                }]
            },
        },
    );
}

const fetchGlucoseData = async () => {
    const glucoseUrl = '/api/data-tracking/average-glucose/'
    const glucoseResponse = await fetch(glucoseUrl)

    if (!glucoseResponse.ok) {
        console.error(await glucoseResponse.json())
        return
    }

    return await glucoseResponse.json()
}

const getGlucoseData = async () => {
    const glucoseData = await fetchGlucoseData();

    const result = {
        labels: [],
        glucoses: [],
    }

    for (const {date, level} of glucoseData.average_glucose_per_day) {
        result.labels.push(date)
        result.glucoses.push(level)
    }

    return result
}

const createGlucosePlot = async () => {
    const glucoseDiagram = document.getElementById('weeklyGlucoseChart');

    if (!glucoseDiagram) {
        return
    }

        const {labels, glucoses} = await getGlucoseData();
    new Chart(
        glucoseDiagram,
        {
            type: 'line',
            options: {
                responsive: true,
                plugins: {
                    legend: { display: true },
                },
                scales: {
                    x: { title: { display: true, text: 'Время' } },
                    y: { title: { display: true, text: 'Значение' }, beginAtZero: false }
                },
            },
            data: {
                labels,
                datasets: [{
                    label: 'Средний уровень глюкозы',
                    data: glucoses,
                    borderColor: '#f87171',
                    backgroundColor: '#fecaca',
                    tension: 0.3,
                    fill: false
                }]
            },
        },
    );
}

const fillAvgCalories = async () => {
    const weeklyLogData = await fetchWeeklyLogData()
    document.getElementById('averageCalories').textContent = weeklyLogData.avg_data.avg_calories
}

document.addEventListener('DOMContentLoaded', async () => {
    await fillAvgCalories()

    await createBjuPlot()
    await createCaloriesPlot()
    await createGlucosePlot()
})

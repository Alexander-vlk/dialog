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

document.addEventListener('DOMContentLoaded', async () => {
    const bjuDiagram = document.getElementById('weeklyLogBJUChart');
if (bjuDiagram) {
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
            }
        }
    );
}
})

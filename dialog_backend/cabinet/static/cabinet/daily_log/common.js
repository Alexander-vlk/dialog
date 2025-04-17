export const baseOptions = {
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
    }
};

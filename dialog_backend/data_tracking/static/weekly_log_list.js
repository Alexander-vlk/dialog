  const glucoseCtx = document.getElementById('glucoseChart').getContext('2d');
  const glucoseChart = new Chart(glucoseCtx, {
    type: 'line',
    data: {
      labels: ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'],
      datasets: [{
        label: 'Глюкоза (ммоль/л)',
        data: [5.2, 6.0, 5.5, 6.1, 5.8, 6.3, 5.9],
        backgroundColor: 'rgba(59, 130, 246, 0.2)',
        borderColor: 'rgba(59, 130, 246, 1)',
        borderWidth: 2,
        tension: 0.3
      }]
    },
    options: {
      scales: {
        y: { beginAtZero: false }
      }
    }
  });

  const pressureCtx = document.getElementById('pressureChart').getContext('2d');
  const pressureChart = new Chart(pressureCtx, {
    type: 'line',
    data: {
      labels: ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'],
      datasets: [
        {
          label: 'Систолическое (мм рт. ст.)',
          data: [120, 122, 121, 119, 118, 120, 121],
          borderColor: 'rgba(34, 197, 94, 1)',
          backgroundColor: 'rgba(34, 197, 94, 0.2)',
          borderWidth: 2,
          tension: 0.3
        },
        {
          label: 'Диастолическое (мм рт. ст.)',
          data: [80, 82, 79, 78, 77, 79, 80],
          borderColor: 'rgba(239, 68, 68, 1)',
          backgroundColor: 'rgba(239, 68, 68, 0.2)',
          borderWidth: 2,
          tension: 0.3
        }
      ]
    },
    options: {
      scales: {
        y: { beginAtZero: false }
      }
    }
  });
const healthTypes = {
    'Ужасное': ['bg-red-100', 'text-red-800'],
    'Плохое': ['bg-red-100', 'text-red-800'],
    'Нормальное': ['bg-gray-100', 'text-gray-800'],
    'Хорошее': ['bg-green-100', 'text-green-800'],
    'Отличное': ['bg-green-100', 'text-green-800'],
}

const generalHealths = document.getElementsByClassName("generalHealth");

document.addEventListener('DOMContentLoaded', () => {
    Array.from(generalHealths).forEach(health => {
        let healthType = healthTypes[health.textContent.trim()]
        health.classList.add(...healthType);
    })
})

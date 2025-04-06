const healthTypes = {
    'bad': ['Плохое', 'bg-red-100', 'text-red-800'],
    'normal': ['Нормальное', 'bg-gray-100', 'text-gray-800'],
    'great': ['Отличное', 'bg-green-100', 'text-green-800'],
    'tiredness': ['Усталость', 'bg-yellow-100', 'text-yellow-800'],
    'weakness': ['Слабость', 'bg-orange-100', 'text-orange-800'],
    'drowsiness': ['Сонливость', 'bg-indigo-100', 'text-indigo-800'],
    'dizziness': ['Головокружение', 'bg-purple-100', 'text-purple-800'],
    'nausea': ['Тошнота', 'bg-pink-100', 'text-pink-800'],
    'another': ['Другое', 'bg-blue-100', 'text-blue-800'],
}

const generalHealths = document.getElementsByClassName("generalHealth");

document.addEventListener('DOMContentLoaded', () => {

    Array.from(generalHealths).forEach(health => {
        let healthType = healthTypes[health.textContent.trim()]
        health.textContent = healthType[0];
        health.classList.add(healthType[1], healthType[2]);
    })
})

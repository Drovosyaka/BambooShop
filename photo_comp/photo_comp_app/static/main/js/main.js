// Подтверждение возраста
function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));
    var expires = "expires="+ d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
    var name = cname + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

jQuery(document).ready(function($) {
    var ageCookie = getCookie('age');
    if (ageCookie) {
        $(".overlayyy").hide();
    }

    $("#yesButtonnn").click(function () {
        setCookie('age', 'yes', 3);
        $(".overlayyy").hide();
    });

    $("#noButtonnn").click(function () {
        setCookie('age', 'no', 3);
    });
});

fetch('api/v1/photocomp/')
    .then(response => {
        // Проверяем, что запрос был успешным
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        // Возвращаем JSON из ответа
        return response.json();
    })
    .then(data => {
        // Создаем таблицу и добавляем данные из JSON
        const table = document.createElement('table');
        const thead = document.createElement('thead');
        const tbody = document.createElement('tbody');
        // Создаем заголовки таблицы
        const headerRow = document.createElement('tr');
        const idHeader = document.createElement('th');
        idHeader.textContent = 'ID';
        const titleHeader = document.createElement('th');
        titleHeader.textContent = 'Имя';
        const contentHeader = document.createElement('th');
        contentHeader.textContent = 'Резюме';
        const timeCreateHeader = document.createElement('th');
        timeCreateHeader.textContent = 'Время создания';
        const timeUpdateHeader = document.createElement('th');
        timeUpdateHeader.textContent = 'Время обновления';
        const isPublishedHeader = document.createElement('th');
        isPublishedHeader.textContent = 'Статус публикации';
        const catHeader = document.createElement('th');
        catHeader.textContent = 'Категория';
        // Добавляем заголовки в заголовок таблицы
        headerRow.appendChild(idHeader);
        headerRow.appendChild(titleHeader);
        headerRow.appendChild(contentHeader);
        headerRow.appendChild(timeCreateHeader);
        headerRow.appendChild(timeUpdateHeader);
        headerRow.appendChild(isPublishedHeader);
        headerRow.appendChild(catHeader);
        thead.appendChild(headerRow);
        // Добавляем данные из JSON в таблицу
        data.forEach(function(item) {
            const dataRow = document.createElement('tr');
            const idData = document.createElement('td');
            idData.textContent = item.id;
            const titleData = document.createElement('td');
            titleData.textContent = item.title;
            const contentData = document.createElement('td');
            contentData.textContent = item.content;
            const timeCreateData = document.createElement('td');
            timeCreateData.textContent = item.time_create;
            const timeUpdateData = document.createElement('td');
            timeUpdateData.textContent = item.time_update;
            const isPublishedData = document.createElement('td');
            isPublishedData.textContent = item.is_published;
            const catData = document.createElement('td');
            catData.textContent = item.cat;
            // Добавляем данные в строку
            dataRow.appendChild(idData);
            dataRow.appendChild(titleData);
            dataRow.appendChild(contentData);
            dataRow.appendChild(timeCreateData);
            dataRow.appendChild(timeUpdateData);
            dataRow.appendChild(isPublishedData);
            dataRow.appendChild(catData);
            // Добавляем строку в тело таблицы
            tbody.appendChild(dataRow);
        });
        // Добавляем тело таблицы в таблицу
        table.appendChild(thead);
        table.appendChild(tbody);
        // Отображаем таблицу на странице
        document.getElementById('myTable').appendChild(table);
        table.style.display = 'block';
    })
    .catch(e => {
        // Обрабатываем ошибку
        console.log('Произошла ошибка при получении данных: ' + e.message);
    });
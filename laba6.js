let tg = window.Telegram.WebApp;
tg.expand();  // Расширяем веб-приложение для Telegram
tg.MainButton.textColor = "#FFFFFF";
tg.MainButton.color = "#2cab37";

let item = "";  // Переменная для хранения выбранной игры

// Получаем ссылки на кнопки
let btn1 = document.getElementById("btn1");
let btn2 = document.getElementById("btn2");
let btn3 = document.getElementById("btn3");
let btn4 = document.getElementById("btn4");
let btn5 = document.getElementById("btn5");
let btn6 = document.getElementById("btn6");
let btn7 = document.getElementById("btn7");
let btn8 = document.getElementById("btn8");
let btn9 = document.getElementById("btn9");
let btn10 = document.getElementById("btn10");

// Массив с обновлениями для каждой игры
const updates = {
    "1": "2024-11-27: Исправления ошибок и улучшения производительности.",
    "2": "2024-11-26: Добавлен новый герой и изменения на картах.",
    "3": "2024-11-25: Изменения баланса оружия.",
    "4": "2024-11-22: Добавлены новые обои и исправления ошибок.",
    "5": "2024-11-20: Улучшения геймплея и исправления ошибок.",
    "6": "2024-11-18: Новый игровой режим и изменения баланса.",
    "7": "2024-11-27: Сезонное событие и введение нового персонажа.",
    "8": "2024-11-26: Добавлены новые транспортные средства и миссии.",
    "9": "2024-11-24: Исправления ошибок и новые функции для многопользовательского режима.",
    "10": "2024-11-27: Введены новые танки и самолеты."
};

// Обработчики для кнопок
btn1.addEventListener("click", function () {
    item = "1";
    tg.MainButton.setText("Вывести обновления для Counter-Strike 2");
    tg.MainButton.show();
});

btn2.addEventListener("click", function () {
    item = "2";
    tg.MainButton.setText("Вывести обновления для Dota 2");
    tg.MainButton.show();
});

btn3.addEventListener("click", function () {
    item = "3";
    tg.MainButton.setText("Вывести обновления для PUBG");
    tg.MainButton.show();
});

btn4.addEventListener("click", function () {
    item = "4";
    tg.MainButton.setText("Вывести обновления для Wallpaper Engine");
    tg.MainButton.show();
});

btn5.addEventListener("click", function () {
    item = "5";
    tg.MainButton.setText("Вывести обновления для Wukong");
    tg.MainButton.show();
});

btn6.addEventListener("click", function () {
    item = "6";
    tg.MainButton.setText("Вывести обновления для Naraka: Bladepoint");
    tg.MainButton.show();
});

btn7.addEventListener("click", function () {
    item = "7";
    tg.MainButton.setText("Вывести обновления для Apex Legends");
    tg.MainButton.show();
});

btn8.addEventListener("click", function () {
    item = "8";
    tg.MainButton.setText("Вывести обновления для GTA V");
    tg.MainButton.show();
});

btn9.addEventListener("click", function () {
    item = "9";
    tg.MainButton.setText("Вывести обновления для Deadlock");
    tg.MainButton.show();
});

btn10.addEventListener("click", function () {
    item = "10";
    tg.MainButton.setText("Вывести обновления для War Thunder");
    tg.MainButton.show();
});

// Отправка данных в Telegram-бот при нажатии на MainButton
Telegram.WebApp.onEvent("mainButtonClicked", function () {
    tg.sendData(updates[item]);  // Отправляем информацию об обновлении
});

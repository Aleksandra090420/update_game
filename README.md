<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Game Updates</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333;
        }
        .button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            margin: 5px;
        }
        .button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Обновления игр</h1>
        <p>Выберите игру, чтобы получить обновления:</p>
        <!-- Кнопки для взаимодействия -->
        <button class="button" id="game1">Обновления для Counter-Strike 2</button>
        <button class="button" id="game2">Обновления для Dota 2</button>
        <button class="button" id="game3">Обновления для PUBG</button>
        <button class="button" id="game4">Обновления для Wallpaper Engine</button>
        <button class="button" id="game5">Обновления для Wukong</button>
        <button class="button" id="game6">Обновления для Naraka: Bladepoint</button>
        <button class="button" id="game7">Обновления для Apex Legends</button>
        <button class="button" id="game8">Обновления для GTA V</button>
        <button class="button" id="game9">Обновления для Deadlock</button>
        <button class="button" id="game10">Обновления для War Thunder</button>
    </div>

    <script>
        // При нажатии на кнопку отправляется информация через WebApp
        document.getElementById('game1').addEventListener('click', function() {
            window.Telegram.WebApp.sendData("1");  // отправка данных о Counter-Strike 2
        });

        document.getElementById('game2').addEventListener('click', function() {
            window.Telegram.WebApp.sendData("2");  // отправка данных о Dota 2
        });

        document.getElementById('game3').addEventListener('click', function() {
            window.Telegram.WebApp.sendData("3");  // отправка данных о PUBG
        });

        document.getElementById('game4').addEventListener('click', function() {
            window.Telegram.WebApp.sendData("4");  // отправка данных о Wallpaper Engine
        });

        document.getElementById('game5').addEventListener('click', function() {
            window.Telegram.WebApp.sendData("5");  // отправка данных о Wukong
        });

        document.getElementById('game6').addEventListener('click', function() {
            window.Telegram.WebApp.sendData("6");  // отправка данных о Naraka: Bladepoint
        });

        document.getElementById('game7').addEventListener('click', function() {
            window.Telegram.WebApp.sendData("7");  // отправка данных о Apex Legends
        });

        document.getElementById('game8').addEventListener('click', function() {
            window.Telegram.WebApp.sendData("8");  // отправка данных о GTA V
        });

        document.getElementById('game9').addEventListener('click', function() {
            window.Telegram.WebApp.sendData("9");  // отправка данных о Deadlock
        });

        document.getElementById('game10').addEventListener('click', function() {
            window.Telegram.WebApp.sendData("10");  // отправка данных о War Thunder
        });
    </script>
</body>
</html>

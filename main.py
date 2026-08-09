from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="tg">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SafarAvia - Сервиси саёҳат</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Inter', sans-serif; }
        body { background-color: #f8fafc; color: #0f172a; padding-bottom: 90px; }
        
        header { 
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); 
            color: white; 
            padding: 16px 20px 25px; 
            text-align: center;
        }

        .top-tools {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 500px;
            margin: 0 auto 15px auto;
            gap: 10px;
        }
        .select-wrapper {
            background: rgba(255, 255, 255, 0.12);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 12px;
            padding: 4px 10px;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .select-wrapper select {
            background: transparent;
            color: white;
            border: none;
            outline: none;
            font-size: 12px;
            font-weight: 600;
            cursor: pointer;
        }
        .select-wrapper select option {
            background: #1e293b;
            color: white;
        }

        .logo-wrapper {
            display: inline-flex;
            align-items: center;
            gap: 10px;
            background: rgba(255, 255, 255, 0.1);
            padding: 8px 20px;
            border-radius: 30px;
            border: 1px solid rgba(255,255,255,0.15);
        }
        .logo-text { 
            font-size: 22px; 
            font-weight: 800; 
            background: linear-gradient(90deg, #38bdf8, #818cf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .subtitle { font-size: 12px; color: #cbd5e1; margin-top: 8px; }
        
        .container { padding: 20px 16px; max-width: 500px; margin: auto; }
        
        .nav-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 10px;
            background: white;
            padding: 16px 10px;
            border-radius: 20px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.04);
            border: 1px solid #e2e8f0;
            margin-bottom: 20px;
        }
        .nav-item {
            display: flex;
            flex-direction: column;
            align-items: center;
            cursor: pointer;
        }
        .circle-icon {
            width: 54px;
            height: 54px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 22px;
            margin-bottom: 6px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.06);
            color: white;
        }
        .nav-label { font-size: 11px; font-weight: 700; color: #334155; text-align: center; }

        .bg-aviasales { background: linear-gradient(135deg, #0284c7, #38bdf8); }
        .bg-avito { background: linear-gradient(135deg, #10b981, #34d399); }
        .bg-airhelp { background: linear-gradient(135deg, #f97316, #fb923c); }
        .bg-klook { background: linear-gradient(135deg, #8b5cf6, #a78bfa); }

        .section-title {
            font-size: 13px;
            font-weight: 700;
            color: #64748b;
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        .card { 
            background: white; 
            border-radius: 16px; 
            margin-bottom: 12px; 
            box-shadow: 0 2px 8px rgba(0,0,0,0.03); 
            border: 1px solid #e2e8f0;
            overflow: hidden;
            transition: all 0.3s ease;
        }
        .card-header {
            padding: 16px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            cursor: pointer;
            user-select: none;
        }
        .card-left { display: flex; align-items: center; gap: 12px; }
        .card-small-icon {
            width: 42px;
            height: 42px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            color: white;
        }
        .card-info h4 { font-size: 15px; font-weight: 700; color: #0f172a; }
        .card-info p { font-size: 12px; color: #64748b; }
        .arrow-icon { 
            font-size: 14px; 
            color: #94a3b8; 
            transition: transform 0.3s ease; 
            font-weight: bold;
        }

        .card-body {
            display: none;
            padding: 0 16px 16px 16px;
            border-top: 1px solid #f1f5f9;
            background: #fafafa;
        }
        .card-body p {
            font-size: 13px;
            color: #334155;
            line-height: 1.5;
            margin-top: 12px;
        }
        .bullet-list {
            margin: 10px 0 14px 0;
            padding-left: 18px;
            font-size: 12px;
            color: #475569;
            line-height: 1.6;
        }
        .btn-action {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            width: 100%;
            padding: 12px;
            border-radius: 10px;
            color: white;
            text-decoration: none;
            font-weight: 700;
            font-size: 14px;
            text-align: center;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        }

        .card.active .card-body { display: block; }
        .card.active .arrow-icon { transform: rotate(90deg); color: #0284c7; }

        .support-box {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 16px;
            padding: 16px;
            text-align: center;
            margin-top: 20px;
        }
        .support-box h3 { font-size: 14px; color: #0f172a; margin-bottom: 4px; }
        .support-box p { font-size: 12px; color: #64748b; margin-bottom: 10px; }
        .btn-tg {
            display: inline-block;
            background: #0284c7;
            color: white;
            padding: 10px 18px;
            border-radius: 10px;
            text-decoration: none;
            font-size: 13px;
            font-weight: 600;
        }

        /* --- LIVE CHAT WIDGET --- */
        .chat-btn {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: linear-gradient(135deg, #0284c7, #38bdf8);
            color: white;
            width: 56px;
            height: 56px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 26px;
            box-shadow: 0 4px 15px rgba(2, 132, 199, 0.4);
            cursor: pointer;
            z-index: 1000;
            transition: transform 0.2s ease;
        }
        .chat-btn:active { transform: scale(0.9); }

        .chat-box {
            position: fixed;
            bottom: 85px;
            right: 20px;
            width: 320px;
            max-width: calc(100vw - 40px);
            height: 400px;
            background: white;
            border-radius: 16px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            border: 1px solid #e2e8f0;
            display: none;
            flex-direction: column;
            overflow: hidden;
            z-index: 1000;
        }
        .chat-header {
            background: #0f172a;
            color: white;
            padding: 12px 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-weight: 700;
            font-size: 14px;
        }
        .chat-close { cursor: pointer; font-size: 18px; opacity: 0.8; }
        .chat-messages {
            flex: 1;
            padding: 12px;
            overflow-y: auto;
            background: #f8fafc;
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        .msg {
            max-width: 80%;
            padding: 8px 12px;
            border-radius: 12px;
            font-size: 13px;
            line-height: 1.4;
        }
        .msg-operator {
            background: white;
            border: 1px solid #e2e8f0;
            align-self: flex-start;
            color: #0f172a;
        }
        .msg-user {
            background: #0284c7;
            color: white;
            align-self: flex-end;
        }
        .chat-input-area {
            display: flex;
            padding: 10px;
            border-top: 1px solid #e2e8f0;
            background: white;
            gap: 6px;
        }
        .chat-input-area input {
            flex: 1;
            border: 1px solid #cbd5e1;
            border-radius: 8px;
            padding: 8px 10px;
            font-size: 13px;
            outline: none;
        }
        .chat-input-area button {
            background: #0284c7;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 8px 12px;
            font-weight: 600;
            cursor: pointer;
        }
    </style>
</head>
<body>

<header>
    <div class="top-tools">
        <div class="select-wrapper">
            <span>🌐</span>
            <select id="langSelect" onchange="changeLanguage(this.value)">
                <option value="tg">Тоҷикӣ</option>
                <option value="ru">Русский</option>
                <option value="en">English</option>
                <option value="tr">Türkçe</option>
                <option value="ar">العربية</option>
                <option value="de">Deutsch</option>
                <option value="fr">Français</option>
                <option value="es">Español</option>
                <option value="zh">中文</option>
                <option value="uz">Ўзбекча</option>
            </select>
        </div>

        <div class="select-wrapper">
            <span>🔲</span>
            <select id="currencySelect" onchange="changeCurrency(this.value)"></select>
        </div>
    </div>

    <div class="logo-wrapper">
        <span style="font-size: 22px;">✈️</span>
        <span class="logo-text">SafarAvia</span>
    </div>
    <p class="subtitle" id="txt-subtitle">Барои маълумот ва гузариш рӯи категория пахш кунед</p>
</header>

<div class="container">

    <div class="nav-grid">
        <div class="nav-item" onclick="openCard('card-aviasales')">
            <div class="circle-icon bg-aviasales">✈️</div>
            <span class="nav-label">Aviasales</span>
        </div>
        <div class="nav-item" onclick="openCard('card-avito')">
            <div class="circle-icon bg-avito">🏨</div>
            <span class="nav-label">Avito</span>
        </div>
        <div class="nav-item" onclick="openCard('card-airhelp')">
            <div class="circle-icon bg-airhelp">⚖️</div>
            <span class="nav-label">AirHelp</span>
        </div>
        <div class="nav-item" onclick="openCard('card-klook')">
            <div class="circle-icon bg-klook">🎟️</div>
            <span class="nav-label">Klook</span>
        </div>
    </div>

    <div class="section-title" id="txt-categories">Категорияҳо (Пахш кунед)</div>

    <!-- 1. Aviasales Card -->
    <div class="card" id="card-aviasales">
        <div class="card-header" onclick="toggleCard('card-aviasales')">
            <div class="card-left">
                <div class="card-small-icon bg-aviasales">✈️</div>
                <div class="card-info">
                    <h4>Aviasales</h4>
                    <p id="aviasales-short">Ҷустуҷӯ ва муқоисаи чиптаҳо</p>
                </div>
            </div>
            <span class="arrow-icon">➔</span>
        </div>
        <div class="card-body">
            <p><strong id="aviasales-why-title">Барои чӣ лозим аст?</strong><br>
            <span id="aviasales-desc">Aviasales бузургтарин сервиси ҷустуҷӯи чиптаҳои ҳавопаймоӣ мебошад. Он нархи чиптаҳоро аз садҳо авиакомпанияҳо муқоиса карда, арзонтаринашро меёбад.</span></p>
            <ul class="bullet-list">
                <li id="aviasales-b1">✅ Нархҳо мустақиман аз сайти расмии авиакомпанияҳо</li>
                <li id="aviasales-b2">✅ Бе комиссия ва пардохти иловагӣ</li>
                <li id="aviasales-b3">✅ Интихоби парвозҳои мустақим ва арзон</li>
            </ul>
            <a href="https://aviasales.tpo.lu/uvx5sy8B" class="btn-action bg-aviasales" id="aviasales-btn" target="_blank">Гузаштан ба Aviasales ➔</a>
        </div>
    </div>

    <!-- 2. Avito Card -->
    <div class="card" id="card-avito">
        <div class="card-header" onclick="toggleCard('card-avito')">
            <div class="card-left">
                <div class="card-small-icon bg-avito">🏨</div>
                <div class="card-info">
                    <h4>Avito Путешествия</h4>
                    <p id="avito-short">Иҷораи хона ва меҳмонхонаҳо</p>
                </div>
            </div>
            <span class="arrow-icon">➔</span>
        </div>
        <div class="card-body">
            <p><strong id="avito-why-title">Барои чӣ лозим аст?</strong><br>
            <span id="avito-desc">Сервиси қулай барои пайдо ва брон кардани ҷои зист ҳангоми сафар ба Россия ва кишварҳои СНГ.</span></p>
            <ul class="bullet-list">
                <li id="avito-b1">✅ Иҷораи квартираҳои суткавӣ ва отелҳо</li>
                <li id="avito-b2">✅ Аксҳои ҳақиқӣ ва шарҳи мизоҷон</li>
                <li id="avito-b3">✅ Бронкунии бехатар бо кафолат</li>
            </ul>
            <a href="https://avito.tpo.lu/EetgCxYO" class="btn-action bg-avito" id="avito-btn" target="_blank">Гузаштан ба Avito ➔</a>
        </div>
    </div>

    <!-- 3. AirHelp Card -->
    <div class="card" id="card-airhelp">
        <div class="card-header" onclick="toggleCard('card-airhelp')">
            <div class="card-left">
                <div class="card-small-icon bg-airhelp">⚖️</div>
                <div class="card-info">
                    <h4>AirHelp</h4>
                    <p id="airhelp-short">Ҷуброни пули парвозҳои дермонда</p>
                </div>
            </div>
            <span class="arrow-icon">➔</span>
        </div>
        <div class="card-body">
            <p><strong id="airhelp-why-title">Барои чӣ лозим аст?</strong><br>
            <span id="airhelp-desc">Агар парвози шумо беш аз 3 соат дер монда бошад, бекор шуда бошад ё ҷои нишаст нарасида бошад, AirHelp ба шумо кӯмак мекунад, то аз авиакомпания ҷубронпулӣ гиред.</span></p>
            <ul class="bullet-list">
                <li id="airhelp-b1">✅ Санҷиши ройгони ҳуқуқи ҷуброн</li>
                <li id="airhelp-b2">✅ Ҳама кори ҳуқуқиро мутахассисон иҷро мекунанд</li>
                <li id="airhelp-b3">✅ Танҳо ҳангоми гирифтани пул комиссия медиҳед</li>
            </ul>
            <a href="https://airhelp.tpo.lu/ui184ihg" class="btn-action bg-airhelp" id="airhelp-btn" target="_blank">Санҷиши ҷубронпулӣ ➔</a>
        </div>
    </div>

    <!-- 4. Klook Card -->
    <div class="card" id="card-klook">
        <div class="card-header" onclick="toggleCard('card-klook')">
            <div class="card-left">
                <div class="card-small-icon bg-klook">🎟️</div>
                <div class="card-info">
                    <h4>Klook</h4>
                    <p id="klook-short">Экскурсия ва билетҳо дар хориҷа</p>
                </div>
            </div>
            <span class="arrow-icon">➔</span>
        </div>
        <div class="card-body">
            <p><strong id="klook-why-title">Барои чӣ лозим аст?</strong><br>
            <span id="klook-desc">Платформа барои харидани билетҳои парки аттракционҳо, музейҳо, экскурсияҳо ва eSIM (интернет) дар саросари ҷаҳон.</span></p>
            <ul class="bullet-list">
                <li id="klook-b1">✅ Хариди чиптаҳо бе навбатпайпоӣ дар касса</li>
                <li id="klook-b2">✅ Нархҳои арзон ва чегирмаҳои махсус</li>
                <li id="klook-b3">✅ Тасдиқи фаврӣ дар телефон</li>
            </ul>
            <a href="https://klook.tpo.lu/ZseFdLJw" class="btn-action bg-klook" id="klook-btn" target="_blank">Гузаштан ба Klook ➔</a>
        </div>
    </div>

    <!-- Support Box -->
    <div class="support-box">
        <h3 id="support-title">💬 Маркази кумак</h3>
        <p id="support-desc">Савол ё мушкилие доред?</p>
        <a href="https://t.me/your_telegram" class="btn-tg" id="support-btn" target="_blank">Оператор (Telegram)</a>
    </div>

</div>

<!-- LIVE CHAT WIDGET -->
<div class="chat-btn" onclick="toggleChat()">💬</div>

<div class="chat-box" id="chatBox">
    <div class="chat-header">
        <span id="chat-title">💬 Чат бо оператор</span>
        <span class="chat-close" onclick="toggleChat()">✖</span>
    </div>
    <div class="chat-messages" id="chatMessages">
        <div class="msg msg-operator" id="chat-welcome">
            Салом! Чӣ мушкилӣ ё савол доред? Нависед, мо ба шумо кӯмак мерасонем.
        </div>
    </div>
    <div class="chat-input-area">
        <input type="text" id="chatInput" placeholder="Паёми худро нависед..." onkeypress="handleKeyPress(event)">
        <button onclick="sendMessage()">➔</button>
    </div>
</div>

<script>
    const translations = {
        tg: {
            subtitle: "Барои маълумот ва гузариш рӯи категория пахш кунед",
            categories: "Категорияҳо (Пахш кунед)",
            whyTitle: "Барои чӣ лозим аст?",
            aviasalesShort: "Ҷустуҷӯ ва муқоисаи чиптаҳо",
            aviasalesDesc: "Aviasales бузургтарин сервиси ҷустуҷӯи чиптаҳои ҳавопаймоӣ мебошад. Он нархи чиптаҳоро аз садҳо авиакомпанияҳо муқоиса карда, арзонтаринашро меёбад.",
            aviasalesB1: "✅ Нархҳо мустақиман аз сайти расмии авиакомпанияҳо",
            aviasalesB2: "✅ Бе комиссия ва пардохти иловагӣ",
            aviasalesB3: "✅ Интихоби парвозҳои мустақим ва арзон",
            aviasalesBtn: "Гузаштан ба Aviasales ➔",
            avitoShort: "Иҷораи хона ва меҳмонхонаҳо",
            avitoDesc: "Сервиси қулай барои пайдо ва брон кардани ҷои зист ҳангоми сафар ба Россия ва кишварҳои СНГ.",
            avitoB1: "✅ Иҷораи квартираҳои суткавӣ ва отелҳо",
            avitoB2: "✅ Аксҳои ҳақиқӣ ва шарҳи мизоҷон",
            avitoB3: "✅ Бронкунии бехатар бо кафолат",
            avitoBtn: "Гузаштан ба Avito ➔",
            airhelpShort: "Ҷуброни пули парвозҳои дермонда",
            airhelpDesc: "Агар парвози шумо беш аз 3 соат дер монда бошад, бекор шуда бошад ё ҷои нишаст нарасида бошад, AirHelp ба шумо кӯмак мекунад, то аз авиакомпания ҷубронпулӣ гиред.",
            airhelpB1: "✅ Санҷиши ройгони ҳуқуқи ҷуброн",
            airhelpB2: "✅ Ҳама кори ҳуқуқиро мутахассисон иҷро мекунанд",
            airhelpB3: "✅ Танҳо ҳангоми гирифтани пул комиссия медиҳед",
            airhelpBtn: "Санҷиши ҷубронпулӣ ➔",
            klookShort: "Экскурсия ва билетҳо дар хориҷа",
            klookDesc: "Платформа барои харидани билетҳои парки аттракционҳо, музейҳо, экскурсияҳо ва eSIM (интернет) дар саросари ҷаҳон.",
            klookB1: "✅ Хариди чиптаҳо бе навбатпайпоӣ дар касса",
            klookB2: "✅ Нархҳои арзон ва чегирмаҳои махсус",
            klookB3: "✅ Тасдиқи фаврӣ дар телефон",
            klookBtn: "Гузаштан ба Klook ➔",
            supportTitle: "💬 Маркази кумак",
            supportDesc: "Савол ё мушкилие доред?",
            supportBtn: "Оператор (Telegram)"
        },
        ru: {
            subtitle: "Нажмите на категорию для подробностей и перехода",
            categories: "Категории (Нажмите)",
            whyTitle: "Зачем это нужно?",
            aviasalesShort: "Поиск и сравнение авиабилетов",
            aviasalesDesc: "Aviasales — крупнейший сервис поиска авиабилетов. Он сравнивает цены сотен авиакомпаний и находит самые дешевые варианты.",
            aviasalesB1: "✅ Цены напрямую от официальных авиакомпаний",
            aviasalesB2: "✅ Без комиссий и скрытых наценок",
            aviasalesB3: "✅ Удобный выбор прямых и дешевых рейсов",
            aviasalesBtn: "Перейти в Aviasales ➔",
            avitoShort: "Аренда жилья и отелей",
            avitoDesc: "Удобный сервис для поиска и бронирования жилья во время поездок по России и СНГ.",
            avitoB1: "✅ Посуточная аренда квартир и отелей",
            avitoB2: "✅ Реальные фото и отзывы гостей",
            avitoB3: "✅ Безопасное бронирование с гарантией",
            avitoBtn: "Перейти в Avito ➔",
            airhelpShort: "Компенсация за задержку рейса",
            airhelpDesc: "Если ваш рейс задержали более чем на 3 часа, отменили или отказали в посадке, AirHelp поможет получить компенсацию до 600€.",
            airhelpB1: "✅ Бесплатная проверка права на компенсацию",
            airhelpB2: "✅ Всю юридическую работу делают специалисты",
            airhelpB3: "✅ Комиссия только в случае успеха",
            airhelpBtn: "Проверить компенсацию ➔",
            klookShort: "Экскурсии и билеты за границей",
            klookDesc: "Платформа для покупки билетов в парки развлечений, музеи, экскурсии и eSIM по всему миру.",
            klookB1: "✅ Покупка билетов без очередей в кассу",
            klookB2: "✅ Выгодные цены и специальные скидки",
            klookB3: "✅ Мгновенный ваучер прямо в телефоне",
            klookBtn: "Перейти в Klook ➔",
            supportTitle: "💬 Центр поддержки",
            supportDesc: "Есть вопросы или проблемы?",
            supportBtn: "Оператор (Telegram)"
        },
        en: {
            subtitle: "Click on a category for details and redirect",
            categories: "Categories (Click)",
            whyTitle: "Why do you need this?",
            aviasalesShort: "Search and compare flight tickets",
            aviasalesDesc: "Aviasales is the largest flight search service. It compares ticket prices across hundreds of airlines to find the cheapest options.",
            aviasalesB1: "✅ Prices directly from official airlines",
            aviasalesB2: "✅ No hidden fees or extra commissions",
            aviasalesB3: "✅ Easy selection of direct and cheap flights",
            aviasalesBtn: "Go to Aviasales ➔",
            avitoShort: "Apartment and hotel rentals",
            avitoDesc: "Convenient service for finding and booking accommodations when traveling across Russia and CIS countries.",
            avitoB1: "✅ Daily apartment and hotel rentals",
            avitoB2: "✅ Real photos and guest reviews",
            avitoB3: "✅ Secure booking with guarantees",
            avitoBtn: "Go to Avito ➔",
            airhelpShort: "Compensation for delayed flights",
            airhelpDesc: "If your flight was delayed over 3 hours, canceled, or overbooked, AirHelp helps you claim up to 600€ in compensation.",
            airhelpB1: "✅ Free compensation claim check",
            airhelpB2: "✅ Full legal work handled by experts",
            airhelpB3: "✅ Fee is charged only if you win",
            airhelpBtn: "Check Compensation ➔",
            klookShort: "Tours and attractions abroad",
            klookDesc: "Platform to book tickets for theme parks, museums, tours, activities, and travel eSIMs worldwide.",
            klookB1: "✅ Skip-the-line tickets for attractions",
            klookB2: "✅ Great prices and exclusive discounts",
            klookB3: "✅ Instant confirmation on your phone",
            klookBtn: "Go to Klook ➔",
            supportTitle: "💬 Support Center",
            supportDesc: "Have questions or need help?",
            supportBtn: "Operator (Telegram)"
        }
    };

    function changeLanguage(lang) {
        localStorage.setItem('selectedLang', lang);

        const t = translations[lang] || translations['tg'];

        document.getElementById('txt-subtitle').textContent = t.subtitle;
        document.getElementById('txt-categories').textContent = t.categories;

        document.getElementById('aviasales-why-title').textContent = t.whyTitle;
        document.getElementById('avito-why-title').textContent = t.whyTitle;
        document.getElementById('airhelp-why-title').textContent = t.whyTitle;
        document.getElementById('klook-why-title').textContent = t.whyTitle;

        // Aviasales
        document.getElementById('aviasales-short').textContent = t.aviasalesShort;
        document.getElementById('aviasales-desc').textContent = t.aviasalesDesc;
        document.getElementById('aviasales-b1').textContent = t.aviasalesB1;
        document.getElementById('aviasales-b2').textContent = t.aviasalesB2;
        document.getElementById('aviasales-b3').textContent = t.aviasalesB3;
        document.getElementById('aviasales-btn').textContent = t.aviasalesBtn;

        // Avito
        document.getElementById('avito-short').textContent = t.avitoShort;
        document.getElementById('avito-desc').textContent = t.avitoDesc;
        document.getElementById('avito-b1').textContent = t.avitoB1;
        document.getElementById('avito-b2').textContent = t.avitoB2;
        document.getElementById('avito-b3').textContent = t.avitoB3;
        document.getElementById('avito-btn').textContent = t.avitoBtn;

        // AirHelp
        document.getElementById('airhelp-short').textContent = t.airhelpShort;
        document.getElementById('airhelp-desc').textContent = t.airhelpDesc;
        document.getElementById('airhelp-b1').textContent = t.airhelpB1;
        document.getElementById('airhelp-b2').textContent = t.airhelpB2;
        document.getElementById('airhelp-b3').textContent = t.airhelpB3;
        document.getElementById('airhelp-btn').textContent = t.airhelpBtn;

        // Klook
        document.getElementById('klook-short').textContent = t.klookShort;
        document.getElementById('klook-desc').textContent = t.klookDesc;
        document.getElementById('klook-b1').textContent = t.klookB1;
        document.getElementById('klook-b2').textContent = t.klookB2;
        document.getElementById('klook-b3').textContent = t.klookB3;
        document.getElementById('klook-btn').textContent = t.klookBtn;

        // Support
        document.getElementById('support-title').textContent = t.supportTitle;
        document.getElementById('support-desc').textContent = t.supportDesc;
        document.getElementById('support-btn').textContent = t.supportBtn;
    }

    function changeCurrency(curr) {
        localStorage.setItem('selectedCurrency', curr);
    }

    document.addEventListener("DOMContentLoaded", function() {
        const currencyList = [
            "TJS (Сомонӣ)", "RUB (Рубль)", "USD (Dollar)", "EUR (Euro)", "KZT (Тенге)", 
            "UZS (Сум)", "TRY (Lira)", "AED (Dirham)", "GBP (Pound)", "CNY (Yuan)"
        ];

        const currSelect = document.getElementById('currencySelect');
        currencyList.forEach(curr => {
            const opt = document.createElement('option');
            opt.value = curr.split(' ')[0];
            opt.textContent = curr;
            currSelect.appendChild(opt);
        });

        const savedLang = localStorage.getItem('selectedLang') || 'tg';
        document.getElementById('langSelect').value = savedLang;
        changeLanguage(savedLang);

        const savedCurr = localStorage.getItem('selectedCurrency') || 'TJS';
        document.getElementById('currencySelect').value = savedCurr;
    });

    function toggleCard(cardId) {
        document.getElementById(cardId).classList.toggle('active');
    }

    function openCard(cardId) {
        const card = document.getElementById(cardId);
        if (!card.classList.contains('active')) card.classList.add('active');
        card.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }

    /* --- CHAT FUNCTIONS --- */
    function toggleChat() {
        const chat = document.getElementById('chatBox');
        chat.style.display = (chat.style.display === 'flex') ? 'none' : 'flex';
    }

    function sendMessage() {
        const input = document.getElementById('chatInput');
        const text = input.value.trim();
        if (!text) return;

        const messagesBox = document.getElementById('chatMessages');

        const userMsg = document.createElement('div');
        userMsg.className = 'msg msg-user';
        userMsg.textContent = text;
        messagesBox.appendChild(userMsg);

        input.value = '';
        messagesBox.scrollTop = messagesBox.scrollHeight;

        setTimeout(() => {
            const opMsg = document.createElement('div');
            opMsg.className = 'msg msg-operator';
            opMsg.textContent = "Ташаккур! Паёми шумо ба оператор фиристода шуд. Ба наздикӣ ҷавоб медиҳем.";
            messagesBox.appendChild(opMsg);
            messagesBox.scrollTop = messagesBox.scrollHeight;
        }, 1000);
    }

    function handleKeyPress(e) {
        if (e.key === 'Enter') sendMessage();
    }
</script>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

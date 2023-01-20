# Создаем шаблон заполнения словаря с пользователями cur = валюта
FXrates_database_template: dict = {'currency_sell': {'settle': list()}, 'currency_buy': {'settle': list()}}
# list_values=(RUB/cur, cur/USDT, RUB/USD, USDT/USD, time)
# cur = (Тайский бат, Индонезийская рупия, Вьетнамский донг, Грузинский лари, Дирхам ОАЭ)
# Инициализируем "базу данных"
FXrates_db: dict = {}

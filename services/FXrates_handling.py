# Заполняем базу данных с курсами FXrates_database.py
from database.FXrates_database import FXrates_db
from database.FXrates_database import FXrates_db
from lexicon.lexicon import LEXICON

fx_rates = ('RUB/USD', 'USDT/USD', 'THB/USD', 'RUB/THB')
fx_settle = ['cash', 'atm', 'account']
for cur in fx_rates:
    FXrates_db[cur] = {f'{settle} buy, sell': (1.0, 1.0) for settle in fx_settle}
'''for k, v in FXrates_db.items():
    print(k, v)
print(FXrates_db)'''
FXrates_db = {'RUB/USD': {'cash': (68.705, 73.715), 'atm': (68.705, 73.715),
                          'account': (68.705, 73.715)},
              'USDT/USD': {'cash': (1.02, 0.97), 'atm': (1.02, 0.97),
                           'account': (1.02, 0.97)},
              'THB/USD': {'cash': (29.23, 30.98), 'atm': (29.23, 30.98),
                          'account': (29.23, 30.98)},
              'RUB/THB': {'cash': (2.034, 2.284), 'atm': (2.034, 2.284),
                          'account': (2.034, 2.284)}}


# функция подготовки вывода сообщения с курсами валютной пары и контактом в телегу
def FXrates_db_print(fx_rate):
    output = f'Валютная пара <b>{fx_rate}</b>\n'
    for settle in fx_settle:
        output += f'<b>{LEXICON[settle]}</b>: покупка <b>{ FXrates_db[fx_rate][settle][0]}</b> продажа ' \
                  f'<b>{FXrates_db[fx_rate][settle][1]}</b>\n'
    output += f'Для обмена по этим курсам пишите сюда {LEXICON["CONTACT"]}'
    return output


print(FXrates_db_print('RUB/USD'))

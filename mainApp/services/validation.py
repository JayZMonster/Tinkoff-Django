from tinkoff.invest import Client
from ..models import Setting
# TODO Import Tinkoff creds model

VALIDATION_PASS = '123'


def check_settings():
    """
    Пытаестся создать тестовый ордер для проверки наличия API ключей Tinkoff,
    путем получения баланса
    :return:
    """
    # TODO Дописать проверку
    try:
        t_info = Setting.query.all()
        last_info = t_info[-1]
    except:
        key_status = stop_status = 'Отсутствует'
        return key_status, stop_status
    try:
        with Client(last_info.api_key) as actual_client:
            from tinkoff_funcs import get_free_money
            ping = get_free_money(actual_client, int(last_info.account_id))
            print("Tinkoff Client check: ", ping)
        key_status = 'Предоставлен'
        stop = str(last_info.stop_loss)
        return key_status, stop
    except:
        print(f'<Tinkoff> У вас отсутствуют или неверно введены API-ключи!')
        key_status = 'Введены неверно'
        stop = str(last_info.stop_loss)
        return key_status, stop
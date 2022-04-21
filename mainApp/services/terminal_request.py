import tinkoff_funcs as t
import validation


def check_if_valid(data):
    """
    Проверяет правильный ли пароль был отправлен вместе с вебхуком
    :param data:
    :return:
    """
    if data['pass'] != validation.VALIDATION_PASS:
        return False
    else:
        return True


def proceed_request(request):
    # TODO доделать процесс торговли
    tinkoff_credentials = get_info(TINKOFF)
    try:
        data = request.POST
        if not check_if_valid(data):
            print('Password error')
            return {
                'code': 'error'
            }
        else:
            print(t.get_timestamp(), "Alert Received & Sent!")
            order_response, msg = t.make_order_tick(data, last.api_key)

        if order_response:
            deal(data, last_info.tg_token, last_info.chat_id, TINKOFF)
            return {
                'response': order_response
            }
        else:
            return {
                'response': False
            }

    except Exception as e:
        print("[X]", t.get_timestamp(), "Error:\n>", e)
        return "Error", 400
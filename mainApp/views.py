from django.shortcuts import render, redirect
from django.views import View
from .services.validation import check_settings
from django.http.response import JsonResponse

# Create your views here.


class MainPage(View):

    @staticmethod
    def get(request):
        tinkoff_status, stop = check_settings()
        print(tinkoff_status)
        context = {
            'tinkoff': {
                't_status': tinkoff_status,
                'stop': stop,
            },

        }
        return render(request, 'mainApp/main_page.html', context)


class Settings(View):

    @staticmethod
    def get(request):
        return render(request, 'mainApp/tinkoff_info.html')

    @staticmethod
    def post(request):
        return redirect(to='mainApp/main_page.html')


class Terminal(View):

    @staticmethod
    def get(request):
        return render(request, 'mainApp/terminal.html')

    @staticmethod
    def post(request):
        from services.terminal_request import proceed_request
        proceed_request(request)
        # TODO Сделать запись истории сделок и расчет сводки
        return redirect(to='mainApp/terminal.html')


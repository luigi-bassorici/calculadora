import flet as ft
from flet import colors
from decimal import Decimal

botoes = [
    {'operador': 'C', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '±', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '%', 'fonte': colors.BLACK, 'fundo': colors.BLUE_GREY_100},
    {'operador': '/', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '7', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '8', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '9', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '*', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '4', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '5', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '6', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '-', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '1', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '2', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '3', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '+', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
    {'operador': '0', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '.', 'fonte': colors.WHITE, 'fundo': colors.WHITE24},
    {'operador': '=', 'fonte': colors.WHITE, 'fundo': colors.ORANGE},
]


def main(page: ft.page):
    page.title="Calculadora"
    page.bgcolor='#000000'
    page.window_width=300
    page.window_height=450
    page.window_resizable=False
    page.window_always_on_top = True

    result = ft.Text(value='0', color=colors.WHITE, size=32)
    
    def calculate(operador, value_at):
        try:
            value = eval(value_at)
            if operador == '%':
                value /= 100
            elif operador == '±':
                value = -value
        except:
            return 'error'
        digits = min(abs(Decimal(value).as_tuple().exponent), 5)
        return format(value, f'.{digits}f')


    def select(e):
        value_at= result.value if result.value not in ['0', 'error'] else ''
        value = e.control.content.value

        if value.isdigit():
            value = value_at + value
        elif value =='C':
            value = '0'
        else:
            if value_at and value_at[-1] in ('+', '-', '/', '*', '.'):
                value_at = value_at[-1]
            
            value = value_at + value

            if value[-1] in ['=','%','±']:
                value = calculate(operador = value[-1], value_at = value_at)

        result.value = value
        result.update()

    display = ft.Row(width=300, controls=[result], alignment='end')
    
    btns = [

        ft.Container(
        content=ft.Text(value=btn['operador'], color=btn['fonte']),
        width=60,
        height=60,
        bgcolor=btn['fundo'],
        border_radius=100,
        alignment=ft.alignment.center,
        on_click=select
        )
        
        for btn in botoes
        
        ]

    keyboard = ft.Row(
        width=300,
        wrap=True,
        controls=btns,
        alignment='end'
    )
    
    page.add(display)
    page.add(keyboard)


ft.app(target = main)
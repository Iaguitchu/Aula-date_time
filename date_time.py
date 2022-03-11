from datetime import *

def trabalhando_com_o_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%H:%M:%S'))
    print(data_atual.strftime('%d/%m/%y'))
    print(data_atual.strftime('%c'))
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2035, 6, 20, 15, 30, 20)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2022'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(data_convertida)
    print(type(data_convertida))

    nova_data = data_convertida - timedelta(days = 365, hours = 2, minutes = 10)
    print(nova_data)

def trabalhando_com_o_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%Y')) # data formatada para o calendario brasileiro
    print(data_atual.strftime('%A/%B/%Y')) # data no formato escrita para o calendario brasileiro

def trabalhando_com_o_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)
    horario_str =horario.strftime('%H:%M:%S')
    print(horario_str)
    print(type(horario_str))


if __name__ == '__main__':
     trabalhando_com_o_datetime()
     trabalhando_com_o_date()
     trabalhando_com_o_time()


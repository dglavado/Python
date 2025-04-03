from datetime import date, datetime, timedelta #bibliotecas standard

from dateutil.relativedelta import relativedelta #necessário baixar essa
#comando para instalar
#pip install python-dateutil

#atualiza o pip
# python.exe -m pip install --upgrade pip

#desinstala
#pip uninstall python-dateutil

hoje = date.today()

#daqui30dias = hoje + 30 #erro

daqui30dias = hoje + timedelta(days=30)
daqui3meses = hoje + relativedelta(month=3)
daqui1ano = hoje + relativedelta(years=1)
daqui3semanas = hoje + relativedelta(weeks=3)

print(daqui1ano) #2026-02-19

primeiroDia = hoje + relativedelta(day=1)  #define o dia para 1 - days faria a soma dos dias

ultimoDia = hoje + relativedelta(day=31) #

ultimoDiaNov = date(2023, 11, 1) + relativedelta(day=31) #último dia não importa quantos dias tem o mês
ultimoDiaFev = date(2024, 2, 15) + relativedelta(day=31) #datetime.date(2024, 2, 29)

print(hoje.year, hoje.month, hoje.day, hoje.weekday()) #2025 2 19 2
#weekday retorna o dia da semana. Segunda = 0 e domingo = 6

print(primeiroDia.strftime('%d.%m.%Y')) #%Y - ano 4 dígitos, %y ano 2 dígitos
print(primeiroDia.strftime('%d/%m/%Y'))
print(primeiroDia.strftime('%m/%d/%Y'))

primeiroDia = primeiroDia.strftime('%d/%m/%Y') #converte para texto a variável

#print(primeiroDia + relativedelta(days=5)) #erro pois a variável foi convertida
      
primeiroDia = datetime.strptime(primeiroDia, '%d/%m/%Y') #converte de volta a variável para datetime

print(primeiroDia + relativedelta(days=5))

diasCorridosNoAno = hoje - date(hoje.year, 1, 1)

print(diasCorridosNoAno) #49 days, 0:00:00

print(diasCorridosNoAno.days)

diasCorridosNoAno = relativedelta(hoje, date(hoje.year, 1, 1))

print(diasCorridosNoAno) #relativedelta(months=+1, days=+18)

print(diasCorridosNoAno.months, diasCorridosNoAno.days) #1 18

print(f'Passados {diasCorridosNoAno.months} meses e {diasCorridosNoAno.days} dias') #Passados 1 meses e 18 dias

idadeMR = relativedelta(hoje, date(1984, 4, 5))
print(f'Passados {idadeMR.years} anos, {idadeMR.months} meses e {idadeMR.days} dias') #Passados 40 anos, 10 meses e 14 dias

agora = datetime.now()

print('fim')

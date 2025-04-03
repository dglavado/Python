#para instalar 
#pip install workadays
from datetime import date
from workadays.workdays import workdays, networkdays, is_workday
from dateutil.relativedelta import relativedelta

hoje = date.today() #19/02/2025

#somar n dias úteis a uma data
print(workdays(hoje, 10, country="BR", state="SP")) #2025-03-07 - pulando os fins de semana e Carnaval (segunda e terça)
#dá pra incluir o país (default BR), estado
print(workdays(hoje, 10, country="US", state="NY")) #2025-03-05

#Primeiro dia útil do mês
def firstWorkDay(deRef: date):
    dt = dtRef + relativedelta(day=1)
    while not is_workday(dt):
        dt += relativedelta(days=1)
    return dt

#Último dia útil do mês
def lastWorkDay(dtRef: date):
    dt = dtRef + relativedelta(day=31)
    while not is_workday(dt):
        dt -= relativedelta(days=1)
    return dt

#próximo dia útil de uma data específica
def nextWorkDay(dtRef: date):
    while not is_workday(dtRef):
        dtRef += relativedelta(days=1)
    return dtRef


def firstN_WorkDay(dtRef: date, nDay: int = 1): # = 1 (default = 1 - parâmetro não obrigatório)
    dt = dtRef + relativedelta(day=1)
    cont = 1
    while cont < nDay:
        while not is_workday(dt):
            dt += relativedelta(days=1)

        dt += relativedelta(days=1)
        cont += 1
    return dt

dtRef = date(2023, 10, 20)
#print(firstN_WorkDay(dtRef, 5)) #2023-11-08

print(firstWorkDay(dtRef)) #2023-10-02
print(lastWorkDay(dtRef)) #2023-10-31

print(lastWorkDay(date(2023, 4, 20))) #2023-04-28

print(nextWorkDay(date(2023, 10, 14))) #2023-10-16


#Quinto dia útil do mês (ou nº dia útil)
#somar n dias úteis a uma data



print('Fim')


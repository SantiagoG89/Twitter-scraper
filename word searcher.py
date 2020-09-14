import twint
import datetime
import pandas
import time
from dateutil.relativedelta import *

start_date = datetime.date(2020, 3, 1)

number_of_months = 4


meses = []

for month in range(number_of_months):

  a_date = (start_date + relativedelta(months=month))

  meses.append(a_date)


def calcular_mes(mes):
    c = twint.Config()
    c.Search = "infectadura"
    c.Since = str(mes)
    c.Until = str(mes + relativedelta(day=31))
    c.Lang = "es"
    c.Pandas = True
    twint.run.Search(c)
    listadetweets = twint.storage.panda.Tweets_df
    time.sleep(180)

    return listadetweets[["date", "tweet"]]


resultadostotales = pandas.DataFrame(columns=['date', 'tweet'])

for mes in meses:
    try:
        resultadosparciales = calcular_mes(mes)
        resultadostotales = resultadostotales.append(resultadosparciales)

    except KeyError:
        print('IndexError')

print(resultadostotales)

resultadostotales.to_csv("C:/Users/user/Documents/infectadura.csv")



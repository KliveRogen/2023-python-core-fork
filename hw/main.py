from hw.date_util import parse_date
from wine import Wine
from beer import Beer
from market import Market

"""
TODO: Доработать заготовки классов вина (Wine), пива (Beer) и магазина (Market) таким образом, чтобы через класс Market можно было:

    * получить список всех напитков (вина и пива) отсортированный по наименованию
    * проверить наличие напитка в магазине (за время О(1))
    * получить список напитков (вина и пива) в указанном диапазоне даты производства
    * (*) написать свой декоратор, который бы логировал начало выполнения метода и выводил время выполнения
"""

beers = [
    Beer("Budweiser", parse_date("2022-01-02")),
    Beer("Heineken", parse_date("2023-02-12")),
    Beer("Guinness", parse_date("2022-03-10")),
    Beer("Stella Artois", parse_date("2022-04-22")),
    Beer("Corona", parse_date("2022-05-05")),
    Beer("Leffe Blonde", parse_date("2021-08-24")),
    Beer("Kronenbourg 1664", parse_date("2020-09-15")),
    Beer("Krušovice", parse_date("2021-05-15"))
]

wines = [
    Wine("Chateau Margaux", parse_date("2005-01-01")),
    Wine("Brunello di Montalcino", parse_date("2010-02-15")),
    Wine("Barolo", parse_date("2012-03-10")),
    Wine("Napa Valley Cabernet Sauvignon", parse_date("2015-04-22")),
    Wine("Bordeaux Grand Cru Classé", parse_date("2018-05-05")),
    Wine("Chardonnay", parse_date("2019-08-25")),
    Wine("Sauternes", parse_date("2008-09-15")),
    Wine("Mosel Riesling", parse_date("2016-10-01"))
]

market = Market(wines, beers)

print("\n\nПолучение списка всех напитков (вина и пива), отсортированный по наименованию:\n|\n|")
sorted_drinks = market.get_drinks_sorted_by_title()
for sorted_drink in sorted_drinks:
    print(sorted_drink.title)

print("\n\nПроверка наличия напитка в магазине (за время О(1)):\n|\n|")
print(f"Напиток Sauternes имеется? : {market.has_drink_with_title('Sauternes')}")


print("\n\nПолучение списка напитков (вина и пива) в указанном диапазоне даты производства:\n|\n|")
filtered_drinks = market.get_drinks_by_production_date(parse_date("2008-09-15"), parse_date("2015-09-18"))
for sorted_drink in filtered_drinks:
    print(sorted_drink.title)

from hw.logger import time_log
from datetime import datetime


class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.wines = {} if wines is None else {wine.title: wine for wine in wines}
        self.beers = {} if beers is None else {beer.title: beer for beer in beers}

    @time_log
    def has_drink_with_title(self, title=None) -> bool:
        """
        Проверяет наличие напитка в магазине за О(1)

        :param title:
        :return: True|False
        """
        return title in self.wines or title in self.beers

    @time_log
    def get_drinks_sorted_by_title(self) -> list:
        """
        Метод получения списка напитков (вина и пива) отсортированных по title

        :return: list
        """
        drinks = list(self.wines.values()) + list(self.beers.values())
        return sorted(drinks, key=lambda drink: drink.title)

    @time_log
    def get_drinks_by_production_date(self, from_date: datetime, to_date: datetime) -> list:
        """
        Метод получения списка напитков в указанном диапазоне дат: с from_date по to_date

        :return: list
        """
        filtered_drinks = []
        drinks = list(self.wines.values()) + list(self.beers.values())
        for drink in drinks:
            if from_date <= drink.production_date <= to_date:
                filtered_drinks.append(drink)
        return filtered_drinks

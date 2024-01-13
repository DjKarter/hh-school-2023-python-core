from datetime import date
from decorator import logger


class Market:
    def __init__(self, wines: list = None, beers: list = None) -> None:
        self.wines = {}
        self.beers = {}
        for elem in wines:
            self.wines[elem.title] = elem
        for elem in beers:
            self.beers[elem.title] = elem

    @logger
    def has_drink_with_title(self, title=None) -> bool:
        return (title in self.wines) or (title in self.beers)

    @logger
    def get_drinks_sorted_by_title(self) -> list:
        return sorted(list(self.wines.values()) + list(self.beers.values()), key=lambda x: x.title)

    @logger
    def get_drinks_by_production_date(self, from_date=None, to_date=None) -> list:
        drinks = []

        f_date = date(int(from_date[from_date.rfind('.') + 1:]),
                      int(from_date[3:5]),
                      int(from_date[:2]))
        t_date = date(int(to_date[to_date.rfind('.') + 1:]),
                      int(to_date[3:5]),
                      int(to_date[:2]))

        for elem in (list(self.wines.values()) + list(self.beers.values())):
            elem_date = date(int(elem.production_date[elem.production_date.rfind('.') + 1:]),
                             int(elem.production_date[3:5]),
                             int(elem.production_date[:2]))
            if f_date < elem_date < t_date:
                drinks.append(elem)

        return drinks

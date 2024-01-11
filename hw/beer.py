from hw.drink import Drink


class Beer(Drink):
    def __init__(self, title, production_date) -> None:
        super().__init__(title, production_date)


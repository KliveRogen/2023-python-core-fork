from datetime import datetime


class Drink:
    def __init__(self, title, production_date: datetime):
        self.title = title
        self.production_date = production_date

from datetime import datetime


class Drink:
    def __init__(self, title=None, production_date: datetime = None):
        self.title = title
        self.production_date = production_date

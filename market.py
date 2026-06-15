import json
import os


class StockMarket:

    def __init__(self):

        self.file_name = "market.json"

        self.market = {}

        self.load()

    def load(self):

        if os.path.exists(
            self.file_name
        ):

            with open(
                self.file_name,
                "r"
            ) as file:

                self.market = json.load(
                    file
                )

    def save(self):

        with open(
            self.file_name,
            "w"
        ) as file:

            json.dump(
                self.market,
                file,
                indent=4
            )

    def create_company(
        self,
        name,
        price
    ):

        self.market[name] = {

            "price": price,

            "volume": 0
        }

        self.save()

    def get_company(
        self,
        name
    ):

        return self.market.get(
            name
        )

    def get_market(self):

        return self.market
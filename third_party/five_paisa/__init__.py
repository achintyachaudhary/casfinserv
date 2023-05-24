import requests


class StockOpening:
    def opening_price(self, stock_id):
        url = f"https://www.5paisa.com/update-stock-info/{stock_id}"
        response = requests.request("GET", url)
        return response

import inspect
import json
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'casfinserv.settings')
import django

django.setup()

from core.models import BTSTStock, Stock
from third_party.chartink.btst import BTST


def btst_cron():
    response = BTST().btst_15_min()
    print(response.text)
    stock_list = json.loads(response.text)["data"]
    for stock in stock_list:
        obj, created = Stock.objects.get_or_create(
            name=stock["name"],
            price=stock["close"],
            nse_code=stock["nsecode"],
            bse_code=stock["bsecode"]
        )
        btst_stock = BTSTStock(
            stock=obj,
            closing_price=stock["close"],
            percentage_change=stock["per_chg"],
            volume=stock["volume"],
        )
        btst_stock.save()


if __name__ == "__main__":
    print("hello world")
    btst_cron()

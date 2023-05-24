import inspect
import os
import sys
from datetime import datetime, timedelta

from core.models import BTSTStock
from third_party.five_paisa import StockOpening

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'casfinserv.settings')
import django

django.setup()


def stock_opening_price():
    current_datetime = datetime.now()
    yesterday = current_datetime - timedelta(days=1)
    target_datetime = datetime(yesterday.year, yesterday.month, yesterday.day, 9, 27)
    btst_stock = BTSTStock.objects.filter(created_at=target_datetime)
    for stock in btst_stock:
        stock_price = StockOpening().opening_price(stock.stock.nse_code)
        stock.next_day_opening = stock_price
        stock.save()


if __name__ == "__main__":
    print("Stock Opening Price Script")
    stock_opening_price()

import inspect
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'casfinserv.settings')
import django

django.setup()
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from core.models import BTSTStock
from third_party.five_paisa import StockOpening


def stock_opening_price():
    from datetime import datetime, timedelta

    # Get the current UTC datetime
    current_datetime_utc = datetime.utcnow()

    # Subtract one day using timedelta
    one_day = timedelta(days=1)
    yesterday_datetime_utc = current_datetime_utc - one_day

    # Set the time to 9:27 AM
    yesterday_927_am_utc = yesterday_datetime_utc.replace(hour=9, minute=27, second=0, microsecond=0)

    print(yesterday_927_am_utc)

    btst_stock = BTSTStock.objects.filter(created_at__gt=yesterday_927_am_utc)
    for stock in btst_stock:
        stock_price = StockOpening().opening_price(stock.stock.nse_code)
        import json
        x = json.loads(stock_price.text)
        x = x['stocks']
        stock.next_day_opening = float(x['price'] + '.' + x['d_price'])
        stock.save()


if __name__ == "__main__":
    print("Stock Opening Price Script")
    stock_opening_price()

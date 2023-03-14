import sys
from datetime import date
from datetime import datetime
from datetime import timedelta
import pytest
import rooms


right_date_format = datetime.now().strftime("%Y-%m-%d %H:%m")

d = datetime.now() - timedelta(days=7)
past_date = d.strftime("%Y-%m-%d %H:%m")

d = datetime.now() - timedelta(days=7)
future_date = d.strftime("%Y-%m-%d %H:%m")


def test_is_date():
    
    
    right_date_format = str(date.today())
    wrong_date_format = str(date.today()).replace("-",".")
    
    rooms.is_date(right_date_format) == True
    
    # will fail: Wrong date format
    with pytest.raises(ValueError):
        rooms.is_date(wrong_date_format)

def test_validate_date_time():

    
    # will fail: 'From Date' is in the past.
    with pytest.raises(ValueError):
        rooms.validate_date_time(past_date)
    








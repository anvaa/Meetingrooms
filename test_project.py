
from datetime import date
from datetime import datetime
from datetime import timedelta
import pytest
#from project import is_date, validate_date_time
import project

# right_date_format = datetime.now().strftime("%Y-%m-%d %H:%M")

d = datetime.now() - timedelta(days=1)
past_date = d.strftime("%Y-%-%d %H:%M")

d = datetime.now() + timedelta(days=1)
future_date = d.strftime("%Y-%m-%d %H:%M")

def test_isdate():
    
    test_res = str(future_date) + ":00"
    assert project.isdate(future_date) == test_res
    
    # will fail: Wrong date/time format. Try yyyy-mm-dd hh:mm
    wrong_date_format = str(future_date).replace("-",".")
    with pytest.raises(ValueError):
        project.is_date(wrong_date_format)

def test_validate_datetime():

    # will fail: 'Date is in the past.
    with pytest.raises(ValueError):
        project.validate_datetime(past_date)
   
    








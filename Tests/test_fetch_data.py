from fetch_data import fetch_data, parse_data_for_temperature, get_current_date


def test_fetch_data():
    assert type(fetch_data()) == dict
    
def test_parse_data_for_temperature_type():
    
    
    data = {"main":{
        "temp": 25.7
    }}
    ret = parse_data_for_temperature(data)
    assert ret == 25.7

def test_date_length():
    date = get_current_date()
    assert len(date) == 10
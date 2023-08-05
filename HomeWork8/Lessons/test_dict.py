empty_dict = {}

def test_empty_dict():
    value = empty_dict["key"]
    assert value == None

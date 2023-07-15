from string_utils import StringUtils

string_utils = StringUtils()

def test_trim_positive():
    string_utils = StringUtils()
    res = string_utils.trim('   Anton')
    assert res == 'Anton'
def test_trim_negative():
    string_utils = StringUtils()
    res = string_utils.trim('   Anton')
    assert res == '  Anton'
    
def test_capitilize():
    string_utils = StringUtils()
    res = string_utils.capitilize('anton')
    assert res == 'Anton'

def test_to_list():
    string_utils = StringUtils()
    res = string_utils.to_list("A, n, t, o")
    assert res == ["A","n","t","o"]

def test_contains():
    string_utils = StringUtils()
    res = string_utils.contains("Anton", "t")
    assert res == True

def test_delete_symbol():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("Anton", "A")
    assert res == "nton"

def test_starts_with():
    string_utils = StringUtils()
    res = string_utils.starts_with("Anton", "A")
    assert res == True

def test_end_with():
    string_utils = StringUtils()
    res = string_utils.end_with("Anton", "n")
    assert res == True

def test_is_empty():
    string_utils = StringUtils()
    res = string_utils.is_empty("")
    assert res == True

def test_list_to_string():
    string_utils = StringUtils()
    res = string_utils.list_to_string(["A","n","t","o","n"])
    assert res == ("A, n, t, o, n")
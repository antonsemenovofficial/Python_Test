from string_utils import StringUtils

string_utils = StringUtils()

def test_string_with_space():
    string_utils = StringUtils()
    res = string_utils.trim('   Anton')
    assert res == 'Anton'
    
def test_capitilize():
    string_utils = StringUtils()
    res = string_utils.capitilize('anton')
    assert res == 'anton'
import pytest
from string_utils import StringUtils

string_utils = StringUtils()

## Убираем пробелы перед словом
def test_trim_positive():
    string_utils = StringUtils()
    res = string_utils.trim('  Anton')
    assert res == 'Anton'
def test_trim_positive_two():
    string_utils = StringUtils()
    res = string_utils.trim('  4 april 2023')
    assert res == '4 april 2023'

@pytest.mark.xfail(strict=True)
def test_trim_negative():
    string_utils = StringUtils()
    res = string_utils.trim('   Anton')
    assert res == '  Anton'

## Выводим слово с заглавной  
def test_capitilize():
    string_utils = StringUtils()
    res = string_utils.capitilize('anton')
    assert res == 'Anton'
@pytest.mark.xfail(strict=True)
def test_capitilize_negative():
    string_utils = StringUtils()
    res = string_utils.capitilize('anton')
    assert res == 'anton'

## Превращаем значения в список
def test_to_list():
    string_utils = StringUtils()
    res = string_utils.to_list('Ark')
    assert res == ['Ark']
@pytest.mark.xfail(strict=True)
def test_to_list_negative():
    string_utils = StringUtils()
    res = string_utils.to_list('Ark')
    assert res == 'Ark'
def test_to_list_two():
    string_utils = StringUtils()
    res = string_utils.to_list("")
    assert res == []

## Поиск буквы в слове
def test_contains():
    string_utils = StringUtils()
    res = string_utils.contains("Anton", "t")
    assert res == True
@pytest.mark.xfail(strict=True)
def test_contains_negative():
    string_utils = StringUtils()
    res = string_utils.contains("Anton", "s")
    assert res == True
@pytest.mark.xfail(strict=True)
def test_contains_negative_two():
    string_utils = StringUtils()
    res = string_utils.contains("Anton", "o")
    assert res == False

## Удаление символов
def test_delete_symbol():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("Anton", "A")
    assert res == "nton"
@pytest.mark.xfail(strict=True)
def test_delete_symbol_negative():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("Anton", "A")
    assert res == "Aton"
@pytest.mark.xfail(strict=True)
def test_delete_symbol_negative_two():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("Anton", "A")
    assert res == "Anton"


## Проверка буквы начала слова
def test_starts_with():
    string_utils = StringUtils()
    res = string_utils.starts_with("Anton", "A")
    assert res == True
@pytest.mark.xfail(strict=False)
def test_starts_with_negative():
    string_utils = StringUtils()
    res = string_utils.starts_with("Anton", "n")
    assert res == False



## Проверка буквы окончания слова
def test_end_with():
    string_utils = StringUtils()
    res = string_utils.end_with("Anton", "n")
    assert res == True
@pytest.mark.xfail(strict=True)
def test_end_with_negative():
    string_utils = StringUtils()
    res = string_utils.end_with("Anton", "A")
    assert res == True

## Проверка пустой строки
def test_is_empty():
    string_utils = StringUtils()
    res = string_utils.is_empty("")
    assert res == True
@pytest.mark.xfail(strict=True)
def test_is_empty_negative():
    string_utils = StringUtils()
    res = string_utils.is_empty(123)
    assert res == False
@pytest.mark.xfail(strict=True)
def test_is_empty_negative_two():
    string_utils = StringUtils()
    res = string_utils.is_empty("Антон")
    assert res == True

## Перевод списка в строку
def test_list_to_string():
    string_utils = StringUtils()
    res = string_utils.list_to_string(["A","n","t","o","n"])
    assert res == ("A, n, t, o, n")
@pytest.mark.xfail(strict=True)
def test_list_to_string_negative():
    string_utils = StringUtils()
    res = string_utils.list_to_string(["A","n","t","o","n"])
    assert res == ["A, n, t, o, n"]
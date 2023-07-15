import pytest
from string_utils import StringUtils

string_utils = StringUtils()

## Убираем пробелы перед словом
@pytest.mark.parametrize(str, 'result',[
("  Anton", "Anton"), 
("  4 april 2023", "4 april 2023")
])
def test_trim_positive(str, result):
    string_utils = StringUtils()
    res = string_utils.trim(str, result)
    assert res == result
def test_trim_negative():
    string_utils = StringUtils()
    res = string_utils.trim('   Anton')
    assert res == '  Anton'

## Выводим слово с заглавной  
def test_capitilize():
    string_utils = StringUtils()
    res = string_utils.capitilize('anton')
    assert res == 'Anton'
def test_capitilize_negative():
    string_utils = StringUtils()
    res = string_utils.capitilize('anton')
    assert res == 'anton'

## Превращаем значения в список
def test_to_list():
    string_utils = StringUtils()
    res = string_utils.to_list('Ark')
    assert res == ['Ark']
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
def test_contains_negative():
    string_utils = StringUtils()
    res = string_utils.contains("Anton", "s")
    assert res == True
def test_contains_negative_two():
    string_utils = StringUtils()
    res = string_utils.contains("Anton", "o")
    assert res == False

## Удаление символов
def test_delete_symbol():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("Anton", "A")
    assert res == "nton"
def test_delete_symbol_negative():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("Anton", "A")
    assert res == "Aton"
def test_delete_symbol_negative_two():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("Anton", "A")
    assert res == "Anton"


## Проверка буквы начала слова
def test_starts_with():
    string_utils = StringUtils()
    res = string_utils.starts_with("Anton", "A")
    assert res == True
def test_starts_with_negative():
    string_utils = StringUtils()
    res = string_utils.starts_with("Anton", "n")
    assert res == False



## Проверка буквы окончания слова
def test_end_with():
    string_utils = StringUtils()
    res = string_utils.end_with("Anton", "n")
    assert res == True
def test_end_with_negative():
    string_utils = StringUtils()
    res = string_utils.end_with("Anton", "A")
    assert res == False

## Проверка пустой строки
def test_is_empty():
    string_utils = StringUtils()
    res = string_utils.is_empty("")
    assert res == True
def test_is_empty_negative():
    string_utils = StringUtils()
    res = string_utils.is_empty(123)
    assert res == False
def test_is_empty_negative_two():
    string_utils = StringUtils()
    res = string_utils.is_empty("Антон")
    assert res == False

## Перевод списка в строку
def test_list_to_string():
    string_utils = StringUtils()
    res = string_utils.list_to_string(["A","n","t","o","n"])
    assert res == ("A, n, t, o, n")
def test_list_to_string_negative():
    string_utils = StringUtils()
    res = string_utils.list_to_string(["A","n","t","o","n"])
    assert res == ["A, n, t, o, n"]
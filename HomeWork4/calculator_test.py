from calculator import Calculator

calculator = Calculator()

def test_sum_positive_nums():
    calculator = Calculator()
    res = calculator.sum(4,5)
    assert res == 9
def test_sum_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-4,-5)
    assert res == -9
def test_sum_positive_and_negative_nums():
    calculator = Calculator()
    res = calculator.sum(-5,5)
    assert res == 1


#res = calculator.sum(4, 5)
#assert (res == 9)

#res = calculator.sum (-6, -10)
#assert res == -16

#res = calculator.sum (-5, 10)
#assert res == 5

#res = calculator.sum (5.6, 4.3)
#res = round(res, 1)
#assert res == 9.9

#res = calculator.sum (10, 0)
#assert res == 10

#res =calculator.div(10, 2)
#assert res == 5

#numbers = []
#res = calculator.avg(numbers)
#assert res == 0

#numbers = [1,2,3]
#res = calculator.avg(numbers)
#assert res == 2

#res = calculator.div(5, 0)
#assert res == None
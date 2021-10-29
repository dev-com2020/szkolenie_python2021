from kalkulator import BasicCalculator

def test_add():
    object = BasicCalculator()
    object.provide_number(10)
    object.provide_operand('+')
    object.provide_number(5)
    assert object.show_result()[0] == 15

def test_subs():
    object = BasicCalculator()
    object.provide_number(13)
    object.provide_operand('-')
    object.provide_number(21)
    assert object.show_result()[0] == -8
import model
import view
import get_mult

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    model.init(value_a, value_b)
    get_mult.init(value_a, value_b)
    result = model.sum()
    result_2 = get_mult.mult()
    view.view_data(result, 'summ')
    view.view_data(result_2, 'mult')
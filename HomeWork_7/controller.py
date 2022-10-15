import logger
import model
import view

def button_click():
    value_string = view.get_value()     
    model.init_equation(value_string)     
    result = model.decision(model.transform(value_string))   
    view.view_data(result, 'result') 
    logger.logger(f'{value_string} = {result}')


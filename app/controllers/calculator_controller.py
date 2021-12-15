from app.controllers.controller import ControllerBase
from calc.calculator import Calculator
from flask import render_template, request


class CalculatorController(ControllerBase):
    @staticmethod
    def post():
        # get the values out of the form
        value1 = request.form['value1']
        value2 = request.form['value2']
        operation = request.form['operation']

        # make the tuple
        my_tuple = (value1, value2)
        # this will call the correct operation
        getattr(Calculator, operation)(my_tuple)
        result = str(Calculator.get_last_result_value())
        return render_template('result.html', value1=value1, value2=value2, operation=operation, result=result)

    @staticmethod
    def get():
        return render_template('basicform.html')

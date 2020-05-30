from fractions import Fraction

from flask import Flask, request

app = Flask(__name__)


def inputs():
    if request.method == 'POST':
        value1 = request.values.get('A', default=0, type=str)
    else:
        value1 = request.args.get('A', default=0, type=str)
    try:
        value1 = Fraction(value1)
    except ZeroDivisionError:
        return "A's denominator shouldn't be 0! \n"
    except ValueError:
        return "A should be number(includes integers, rationals, float)! \n"
    if request.method == 'GET':
        value2 = request.args.get('B', default=0, type=str)
    else:
        value2 = request.args.get('B', default=0, type=str)
    try:
        value2 = Fraction(value2)
    except ValueError:
        return "B should be number(includes integers, rationals, float)! \n"
    except ZeroDivisionError:
        return "B's denominator shouldn't be 0! \n"
    return value1, value2


@app.route('/div',methods=['GET','POST'])
def division():
    try:
        value1, value2 = inputs()
        try:
            result = ((value1) / (value2))
        except ZeroDivisionError:
            error_msg = "B's value shouldn't be zero! \n"
            return error_msg
    except ValueError:
        warning_msg = inputs()
        return warning_msg
    else:
        return str(round(float(result),4)) + '\n'


if __name__ == "__main__":
    app.run()

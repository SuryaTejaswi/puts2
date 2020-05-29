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


@app.route('/')
def index():
    return 'Usage;\n<Operation>?A=<Value1>&B=<Value2>\n'


if __name__ == "__main__":
    app.run()

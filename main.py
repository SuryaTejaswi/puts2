
from flask import Flask, request
from fractions import Fraction
import statistics

app = Flask(__name__)


def input():
    if request.method != 'GET':
        a = request.values.get('X', default=0, type=str)

    else:

        a = request.args.get('X', default=0, type=str)
    try:
        nw = []
        for val in a.split(','):
            nw.append(Fraction(val))

    except ValueError:
        warning = "Enter a valid input. "
        return warning

    return nw


@app.route('/max', methods=['GET', 'POST'])
def maximum():
    try:
        nw = input()
        r = max(nw)
    except ValueError:
        warning = input()
        return warning
    else:
        if float(r).is_integer():
            answer = int(r)
            return "%d \n" % answer
        else:
            
            return str(float(round(r, 4))) + " \n"
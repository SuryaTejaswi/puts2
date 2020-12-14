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
        warning = "Enter a valid input vector. "
        return warning
    return nw


@app.route('/', methods=['GET', 'POST'])
def empty_route():
    return 'Usage: <operation>?<X1, X2, X3, ..., XN>\n'


@app.route('/min', methods=['GET', 'POST'])
def minimum():
    try:
        nw = input()
        r = min(nw)
    except ValueError:
        warning = input()
        return warning
    else:
        if float(r).is_integer():
            answer = int(r)
            return "%d\n" % answer
        else:
            return str(float(round(r, 3))) + "\n"


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
            return "%d\n" % answer
        else:

            return str(float(round(r, 3))) + "\n"


@app.route('/mean', methods=['GET', 'POST'])
@app.route('/average', methods=['GET', 'POST'])
@app.route('/avg', methods=['GET', 'POST'])
def mean():
    try:
        nw = input()
        r = statistics.mean(nw)
    except ValueError:
        warning = input()
        return warning
    else:
        if float(r).is_integer():
            answer = int(r)
            return "%d\n" % answer
        else:

            return str(float(round(r, 3))) + "\n"


@app.route('/median', methods=['GET', 'POST'])
def median():
    try:
        list = input()
        r = statistics.median(list)
    except ValueError:
        warning = in_take()
        return warning
    else:
        if float(r).is_integer():
            r = int(r)
            return "%d \n" % r
        else:

            return str(float(round(r, 3))) + " \n"


if __name__ == "__main__":
    app.run(debug=False)


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


@app.route('/median', methods=['GET', 'POST'])
def median():
    try:
        list = input()
        r = statistics.median(list)
    except ValueError:
        warning = input()
        return warning
    else:
        if float(r).is_integer():
            r = int(r)
            return "%d \n" % r
        else:

            return str(float(round(r, 4))) + " \n"


if __name__ == "__main__":
    app.run(debug=False)
    




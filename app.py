from flask import Flask, request

app = Flask(__name__)

def lcm(a, b):
    import math
    return abs(a * b) // math.gcd(a, b)

@app.route("/adekarimov_gmail_com")
def compute():
    x = request.args.get("x")
    y = request.args.get("y")

    try:
        x = int(x)
        y = int(y)

        if x < 0 or y < 0:
            return "NaN"

        return str(lcm(x, y))

    except:
        return "NaN"

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# redeploy

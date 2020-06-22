from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # TODO: add url to database and return shortened url (shortening logic)
        return
    else:
        return render_template('index.html')


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def route(path):
    # TODO: go to database and find correct url to redirect to
    return


if __name__ == "__main__":
    app.run(debug=True)

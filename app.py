import ssl
from flask import Flask, render_template, request, redirect
from flask_pymongo import pymongo

app = Flask(__name__, template_folder='templates')

client = pymongo.MongoClient("mongodb+srv://dbAdmin:ZUYONlfCtQC5WiBu@cluster0-d16zl.mongodb.net/url-shortener?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
# db = client["urls-shortener"]
# col = db["example"]
# mydict = {"name": "John", "address": "Highway 37" }
#
# x = col.insert_one(mydict)


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

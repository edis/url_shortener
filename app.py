import ssl
from flask import Flask, render_template, request, redirect
from flask_pymongo import pymongo
from gen_slug import base62_slug

app = Flask(__name__, template_folder='templates')

client = pymongo.MongoClient("mongodb+srv://dbAdmin:ZUYONlfCtQC5WiBu@cluster0-d16zl.mongodb.net/urls-redirects?retryWrites=true&w=majority", ssl_cert_reqs=ssl.CERT_NONE)
db = client["urls-redirects"]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['init-url']

        # TODO: implement counter

        slug = base62_slug(100000000001)

        col = db[slug]
        url_dict = {"url": url}
        col.insert(url_dict)

        # TODO: render page with url

    return render_template('index.html')


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def route(path):
    try:
        redirect_url = db[path].find_one()["url"]
        return redirect(redirect_url)
    except TypeError:
        # TODO: render 404 page
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

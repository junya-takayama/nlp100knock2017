from flask import Flask, render_template, url_for, request
from c7utils import MongoSearch
import pandas as pd

app = Flask(__name__)

template = """
<div class="section">
    <table class="tableA">
        <tbody>
            <tr>
                <th>NAME</th>
                <td>%s</td>
            </tr>
            <tr>
                <th>ALIASES</th>
                <td>%s</td>
            </tr>
            <tr>
                <th>TAGS</th>
                <td>%s</td>
            </tr>
            <tr>
                <th>TYPE</th>
                <td>%s</td>
            </tr>
            <tr>
                <th>GID</th>
                <td>%s</td>
            </tr>
            <tr>
                <th>GENDER</th>
                <td>%s</td>
            </tr>
        </tbody>
    </table>
</div>
"""

def tableGenerater(results):
    text = ""
    for data in results:
        name = data.get("name","unknown")
        if "aliases" in data.keys():
            aliases = ", ".join([alias["name"] for alias in data["aliases"]])
        else:
            aliases = ""
        if "tags" in data.keys():
            tags = ", ".join([tag["value"] for tag in data["tags"]])
        else:
            tags = ""
        atype = data.get("type","unknown")
        gid = data.get("gid","unknown")
        gender = data.get("gender","unknown")
        text += template%(name,aliases,tags,atype,gid,gender)
    return text
            
            

@app.route('/')
def index():
    return render_template('index.html',keyword='',tags='')

@app.route('/search')
def search():
    
    keyword = request.args.get('keyword')
    tags = request.args.get('tags')
    mode = request.args.get('mode')
    n = 2
    descending = not(mode == "ngram")
    search = MongoSearch()
    results = search.search(keyword,tags,mode,n,descending)
    search.close()
    results = tableGenerater(results)
    
    return render_template('index.html', keyword=keyword,tags=tags,results=results)

if __name__ == "__main__":
    app.run(debug=True)
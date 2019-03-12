from flask import Flask, render_template, request
from generateMap import generateMap

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/', methods=['POST', 'GET'])
def index():
    filename = request.args.get('filename') or 'stats.csv'
    graphtitle = request.args.get('graphtitle') or 'Gun Crimes'

    return render_template('index.html',
        graph_map=generateMap(filename, graphtitle)
    )

if __name__ == "__main__":
    app.run(debug=True)

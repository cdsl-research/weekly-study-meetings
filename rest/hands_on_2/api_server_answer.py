from flask import Flask, render_template, make_response, jsonify

fruits_list = {"apple":{"price":100, "stock":50}, "orange":{"price":130, "stock":30}, 
    "grapes":{"price":220, "stock":55}, "banana":{"price":140, "stock":60}}

app = Flask(__name__)

@app.route('/')
def index():
    return "TEST API!"

@app.route('/api/fruits/')
def fruits():
    return jsonify(fruits_list)

@app.route('/api/fruits/<string:name>')
def fruits_once(name=None):
    if name in fruits_list:
        return jsonify(fruits_list[name])
    else:
        return jsonify({"error":{"status":404, "comment":name + " is not found"}})

@app.route('/api/fruits/<string:name>/stock/<int:count>')
def fruits_stock(name=None, count=None):
    if name in fruits_list:
        fruits_list[name]['stock'] += int(count)
        return jsonify(fruits_list[name])
    else:
        return jsonify({"error":{"status":404, "comment":name + " is not found"}})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

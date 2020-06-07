from flask import Flask, render_template, make_response, jsonify

fruits_list = {"apple":{"price":100, "stock":50}, "orange":{"price":130, "stock":30}, 
    "grapes":{"price":220, "stock":55}, "banana":{"price":140, "stock":60}}

app = Flask(__name__)


# app.routeの引数にアクセスするとその下にあるメソッドが実行される
@app.route('/')
def index():
    return "TEST API!"


@app.route('/api/適したurlにしてみてください/')
def fruits():
    return jsonify(fruits_list)


# /<string:name>　とするとurlからstringのnameが引数に取れます
@app.route('/適したurlにしてみてください')
def fruits_once(name=None):
    if name in fruits_list:
        # nameで指定された果物の情報を返す
    else:
        return jsonify({"error":{"status":404, "comment":name + " is not found"}})


# 指定された果物の在庫を増やしたり減らしたりするメソッド
@app.route('/api/fruits/<string:name>/stock/<int:count>')
def fruits_stock(name=None, count=None):
    if name in fruits_list:
       # 指定された果物の在庫を増やしたり減らしたりする(ヒント: countは負の値も入っている可能性がある)
        return jsonify(fruits_list[name])
    else:s
        return jsonify({"error":{"status":404, "comment":name + " is not found"}})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

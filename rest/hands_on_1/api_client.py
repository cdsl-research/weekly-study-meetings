import requests
import sys
import json


def main():
    post_number = input("郵便番号を入力してください。(ハイフン無し)")
    # **************ここに実装*************
    # urlにpost_numberをいい感じにくっつけてrequests.getメソッドでリクエストを送る
    # requests
    # 返ってきた値を変数responseに入れる
    out_put(response)
    
    
def out_put(response):
    try:
        if sys.argv[1] == "-json":
            print(response.text)
    except:
        parsed_obj = json.loads(response.text)
        print(parsed_obj["results"][0]["address1"] + parsed_obj["results"][0]["address2"] + parsed_obj["results"][0]["address3"])


if __name__ == '__main__':
    main()

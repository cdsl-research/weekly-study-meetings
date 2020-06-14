import requests
import sys
import json


def main():
    post_number = input("郵便番号を入力してください。(ハイフン無し)")
    base_url = "http://zipcloud.ibsnet.co.jp"
    response = requests.get(base_url + "/api/search?zipcode=" + post_number)
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

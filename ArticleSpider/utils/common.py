# encoding: utf-8
__author__ = 'mtianyan'
__date__ = '2018/1/18 0018 03:52'
import hashlib


def get_md5(url):
    # str就是unicode了.Python3中的str对应2中的Unicode
    if isinstance(url, str):
        url = url.encode("utf-8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()


if __name__ == "__main__":
    print(get_md5("http://jobbole.com".encode("utf-8")))
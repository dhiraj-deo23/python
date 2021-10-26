import requests
import hashlib
import sys


def get_api_req(first, tail):
    url = 'https://api.pwnedpasswords.com/range/' + first
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching API. status code: {res.status_code} Check your API config details')
    for tails in res.text.splitlines():
        x = tails.split(":")
        if x[0] == tail:
            print(
                f'the password is compromised {x[1]} times. Choose another password')
            return
    print('sab changa ji, carry on!')


def check_res(password):
    hashed = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    (first_5, tail) = (hashed[:5], hashed[5:])
    return get_api_req(first_5, tail)


def main(args):
    for password in args:
        check_res(password)


main(sys.argv[1:])

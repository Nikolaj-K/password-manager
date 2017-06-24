import os
import sys
import json
from base64 import urlsafe_b64decode as from_base64
from base64 import urlsafe_b64encode as to_base64

FILENAME = "public.json" # you can rename this filename any way you please
PROMT = ['Enter your private key: ','Enter the application: ','Enter your password: ']

def symmetric_crypt(priv, pw, mode="encode"):
    if mode == "decode":
        dop = lambda pw_char, displace: (pw_char + displace) % 256 # displacement operation
        pw = from_base64(str(pw))
    else: # else do an encoding
        dop = lambda pw_char, displace: (pw_char - displace) % 256
    # The next line is the Vignere cypher. I saw something like this on StackOverflow
    ns = [dop(ord(pw[i]), ord(priv[i % len(priv)])) for i in range(len(pw))]
    result = "".join([chr(abs(n)) for n in ns])
    if mode == "decode":
        return result
    else: # return encoded string
        return to_base64(result) # urlsafe_b64encode doesn't work here in Python 3

def main(private_key, app, password):
    try:
        with open(FILENAME, "r") as infile:
            public = json.load(infile)
    except (ValueError, IOError):
        public = {}
        with open(FILENAME, "w") as outfile:
            json.dump(public, outfile)
    try:
        if password == "decode":
            plaintext = symmetric_crypt(private_key, public[app], "decode")
            print('    Your password for {0} is {1}'.format(app, plaintext))
        else:
            public_key = symmetric_crypt(private_key, password)
            public.update({app: public_key})
            with open(FILENAME, "w") as outfile:
                json.dump(public, outfile)
            print('    Generated public key {0} for {1}'.format(public_key, app))
    except (ValueError, KeyError):
        print('    Check if "{0}" has an entry for {1}.'.format(FILENAME, app))

if __name__ == '__main__':
    args = [raw_input(p) for p in PROMT] # In Python 3, use input ofr raw_input
    main(args[0], args[1], args[2])

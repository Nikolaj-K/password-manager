# Password manager
Authored by Nikolaj Kuntner

Created on 16. June 2017

## Overview
This short Python 2 script encrypts and decrypts any number of passwords using a private key (a single master password you choose) with a basic
[Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher).

## Usage
Using the terminal/shell/command prompt, go to the folder with the python file and run it via
```python
python Vigenere.py
```

You are asked to enter a private key, an application name and a password for it. Then it creates and writes the encrypted password to a .json file. You can look up the application names at any time. If you run the code again and write "decode" instead of a password, your password is revealed.

![password_manager_in_use](http://i.imgur.com/tgZgsV7.png)

Let me know if you're motivated to extend this with a popup-window to display the decoded password.
Note that there are open software available which protects your passwords much better, although the code might not be as simple to read :)

# Password manager
Authored by Nikolaj Kuntner

Created on 16. June 2017

<br />

## Overview
This short Python 2 script decrypts and encrypts any number of passwords using a single master password (private key) using a basic
[Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher).

## Usage
Using the terminal/shell/command propmt, go to the folder with the python file and run it via

```python
python Vignrere.py
```

You are then asked to enter a master key, an application and a password, and then it creates writes the encrypted password to a .json file. You can look up the application names any time. If you run the code again and write "decode" instead of a password, your password is revealed.

![password_manager_in_use](http://i.imgur.com/tgZgsV7.png)

Let me know if you're motivated to extend this with a popup-window to display the decoded password.
Note that there are open software available which protects your passwords much better, although the code might not be as simple to read :)

<p align="center">
  <img src="https://github.com/Itsmmdoha/d0ppelganger/assets/70005698/68636dab-16dd-4bfe-980e-1658d2e835d3" alt="GIF">
</p>

d0ppelganger is a url masking tool that can make a fishy url look like it's from
a well known domain. The purpose of making this tool is not to promote phishing.
Rather it's about learnig how it works and spoting a phishing url right away if
it's using url masking.

## Usage/Examples

**Method 01:**

_For linu users only(tested on debian based distros)_ If you want the fastest
way possible, just execute the below command in a linux shell

```bash
wget "https://github.com/Itsmmdoha/d0ppelganger/releases/download/v1.0.1/d0ppelganger_linux_exe_v1.0.1" -q && chmod +x d0ppelganger_linux_exe_v1 && ./d0ppelganger_linux_exe_v1
```

**Method 02:** Run it from source

1. clone the repository

```bash
git clone https://github.com/Itsmmdoha/d0ppelganger
```

2. change directory

```bash
cd d0ppelganger
```

3. install dependencies

```bash
pip3 install -r requirements.txt
```

4. run the main file

```bash
python3 main.py
```

## How it Works

![Screenshot from 2023-07-31 16-15-05](https://github.com/Itsmmdoha/d0ppelganger/assets/70005698/aa5760d6-8f56-4918-82ff-a6a460b22589)

The above diagram explaines the things this tool does to a url.

URL masking is a technique used to make a link's destination appear different
from its actual target. d0ppelganger employs the character "@" to manipulate the
appearance of a URL and trick the browser into ignoring the text before the
character "@".

In the past, the `username:password@site.com` pattern was commonly used to embed
login credentials directly into the URL. Back in the day, if you typed
`username:password@site.com` in the address bar, the browser would've translated
it into a HTTP request like this:

```http
GET / HTTP/1.1
Host: site.com
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
```

In this example, the username is "username" and the password is "password". The
Authorization header contains the Base64-encoded representation of the
credentials in the format "username:password". This method of embedding
credentials directly in the URL is known as "Basic Authentication".

However, this method was inherently insecure and posed a security risk since the
credentials would be exposed in server logs and could be easily accessed by
unauthorized individuals. Due to these security concerns, modern browsers have
deprecated and removed support for this syntax. In modern browsers, the
credentials part "username:password@" is simply ignored. The browser will
instead make a regular HTTP request to the host specified in the URL without
including the credentials. The request would look like this:

```http
GET / HTTP/1.1
Host: site.com
```

## This tool uses the is.gd API

To know more about the api, refer to the
[API Reference](https://is.gd/apishorteningreference.php). By leveraging the
is.gd API, d0ppelganger can shorten URLs, thereby making them look more
trustworthy. However, it's crucial to note that such behavior can be misused for
malicious purposes like phishing. The intention behind d0ppelganger is to raise
awareness about URL masking and help users recognize and avoid potential
phishing attacks.

## Disclaimer

Use this tool responsibly and ethically. d0ppelganger is intended for
educational and awareness purposes only. I will not be responsible for any
misuse or malicious activities conducted using this tool. Always exercise
caution and verify URLs before clicking on them.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use,
modify, and distribute it according to the terms of the license.

## 🚀 About Me

I'm an enthusiast. I have a youtube channel named
[HoundSec](https://youtube.com/@HoundSec)

contact me at: the_doha@protonmail.com

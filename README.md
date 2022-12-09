<h1><img src="https://github.com/santinilorenzo/orc/blob/master/orc.png?raw=true"> ORC</h1>
<h3>What is?</h3>
Quick and dirty email forensic tool.

<h3>Usage</h3>
From help menu

```
usage: orc.py [-h] [-H] [-p] [-a] [-u] email_path

Email forensic tool

positional arguments:
  email_path            Path of the email to analyze

optional arguments:
  -h, --help            show this help message and exit
  -H, --headers         Print email headers in a friendly way (default: False)
  -p, --print-payload   Print email payloads as they are (default: False)
  -a, --payload-analysis
                        Payload analysis (default: False)
  -u, --find-urls       Search for URLs (default: False)
```

<h3>Notes</h3>
Just like an Orc, this script is ugly. Probably it won't have unit tests, unless parse operation becomes difficult: only trying to parse many mails (and time) will tell.
Purpose of this tool is to have an automatic help to perform phishing/spam mail analysis looking at headers and body content. What I want to do is automatically decode base64 (and other types of encodings) mail content to verify if it is legit or not. I also want to extract URLs, eventually decode them (phishing mails often contains 'strange' URLs) and IPs, then do some automatic query on the web to find reputation etc.

<h3>Security</h3>
Opening mail with this tool should be safe enough, because EML files are read and interpreted as text files, so nothing will be executed and nothing malicious should be triggered unless Python itself contains vulnerable code in the file read method (very unlikely, but nothing is impossible).

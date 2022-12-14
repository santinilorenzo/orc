import hashlib
import re


class Utils:
    def __init__(self, logger, find_urls_enabled):
        self.logger = logger
        self.find_urls_enabled = find_urls_enabled

    def hashes_of(self, obj):
        print("____HASHES____")
        md5 = hashlib.md5(obj).hexdigest()
        sha1 = hashlib.sha1(obj).hexdigest()
        sha256 = hashlib.sha256(obj).hexdigest()
        print("md5sum: {:80} -> PIVOT TO VT: https://www.virustotal.com/gui/search/{:}".format(md5, md5))
        print("sha1sum: {:79} -> PIVOT TO VT: https://www.virustotal.com/gui/search/{:}".format(sha1, sha1))
        print("sha256sum: {:77} -> PIVOT TO VT: https://www.virustotal.com/gui/search/{:}".format(sha256, sha256))
        print("__END_HASHES__")

    def find_urls(self, string_to_check):
        if self.find_urls_enabled:
            urls = re.findall(
                r"((http|https)?:\/\/[www]?\.?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b[-a-zA-Z0-9()@:%_\+.~#?&//=]*)",
                string_to_check)
            if urls is not None and len(urls) > 0:
                print("____URLs____")
                for url in urls:
                    print(url[0].replace(".", "[.]").replace(":", ": "))
                print("__END_URLs__")

#!/usr/bin/env python3
import glob
import sys 
import os
import re
import urllib.parse
import socket

root_dir = sys.argv[1]
pattern = re.compile(r"((http|https|ajp|ws|wss):\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,10}\b([-a-zA-Z0-9@:%_\+.~#?&\/\/=]*))")
rx_blanks = re.compile(r"\W+")

for filename in glob.iglob(root_dir + '**/**', recursive=True):
    print("file:", filename)
    if os.path.isfile(filename):
        try:
            for i, line in enumerate(open(filename)):
                for url in re.findall(pattern, line):
                    url_parsed = urllib.parse.urlparse(url[0])
                    try:
                        get_ip = socket.gethostbyname_ex(url_parsed.hostname)
                        if url_parsed.port is None:
                            my_port = 443
                        else:
                            my_port = url_parsed.port
                        print("URL:", url_parsed.hostname, "PORT:", my_port, "IP:", get_ip[2])
                    except:
                        print(url_parsed.hostname, "failed to resolve IP")
        except:
            print("can't read file")

import glob
import sys 
import os
import re
import urllib.parse
import socket

root_dir = '/home/umesh/scripts/httpd'
patterrn = re.compile(r"((http|https|ajp|ws|wss):\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,10}\b([-a-zA-Z0-9@:%_\+.~#?&\/\/=]*))")

rx_blanks=re.compile(r"\W+") # to remove blanks and newlines

for filename in glob.iglob(root_dir + '**/**',recursive=True):
    #print("file: ",filename)
    if os.path.isfile(filename):
        # file exists
        try:
            for i, line in enumerate(open(filename)):
                #print(line)
                for url in re.findall(patterrn, line):
                    #print(url[0])
                    url_parsed = urllib.parse.urlparse(url[0])
                    #scheme= 'scheme://netloc/path;parameters? query#fragment', allow_fragments=True
                    #print (url_parsed.port)
                    #print (url_parsed.hostname)
                    try:
                        get_ip = socket.gethostbyname_ex(url_parsed.hostname)
                    except:
                        print(url_parsed.hostname,"failed to resolve iP")
                        
                    get_ip = socket.gethostbyname_ex(url_parsed.hostname)
                    print(get_ip[2])
                    if url_parsed.port == None:
                        my_port = 443
                    else:
                        my_port = url_parsed.port
                    print("URL: ",url_parsed.hostname,"PORT: ",my_port,"IP: ",get_ip[2])
        except:
            print("can't read file")                    
                    
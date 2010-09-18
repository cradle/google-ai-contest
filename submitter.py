#!/usr/bin/env python
import urllib, urllib2, cookielib, getpass
 
class WebForm:
    def __init__(self):
        pass
    def Opener(self,ref):
        """Creats an opener to store cookies,
        and keep a referer to the site
        Added user-agent to spoof browser"""
        self.refrence = ref
        cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        self.opener.addheaders.append(('User-agent', 'Mozilla/4.0'))
        self.opener.addheaders.append(('Referer',ref))
        return self.opener
 
    def GET(self,opnr,url):
        """HBH GET method, notice to data option"""
        get_req = opnr.open(url)
        return get_req.read()
 
    def POST(self,opnr,url,data):
        """data is a dictinary type like login_data"""
        enData = urllib.urlencode(data)
        get_req = opnr.open(url,enData)
        return get_req.read()
 
def main():
    #Example
    s = WebForm()
    username = 'metonymous'#raw_input("username: ")
    password = 'pa55word'#getpass.getpass("password: ")
    postData = {'username':username,'password':password}

    url_open = s.Opener('http://ai-contest.com/login.php')
    request = s.POST(url_open,'http://ai-contest.com/check_login.php', postData)
    print request
    print dir(s)
    #f = open('check_login.php','w')
    #f.write(request)
 
if __name__ == "__main__":
    main()

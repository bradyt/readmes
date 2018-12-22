
import subprocess
import urllib.request

url = 'https://raw.githubusercontent.com/Malabarba/smart-mode-line/master/README.org'

response = urllib.request.urlopen(url)
data = response.read()
text = data.decode('utf-8')

subprocess.run(["pandoc", text, "-o", "README.org", "--columns=70"])

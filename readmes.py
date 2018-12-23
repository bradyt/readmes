import os.path
import subprocess
import urllib.request

urls = [
    "https://raw.githubusercontent.com/Malabarba/smart-mode-line/master/README.org",
    "https://raw.githubusercontent.com/bbatsov/projectile/master/README.md",
    "https://raw.githubusercontent.com/purcell/exec-path-from-shell/master/README.md",
    "https://raw.githubusercontent.com/wasamasa/dotemacs/master/init.org",
]


def construct_filename(url):
    u = url.split("/")
    name = u[3]
    repo = u[4]
    filename = u[6]
    return "-".join((name, repo, filename))


def ensure_download(url, filename):
    if not os.path.isfile(filename):
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode("utf-8")
        with open(os.path.join("responses", filename), "w") as f:
            f.write(text)


def replace_extension(filename):
    return os.path.splitext(filename)[0] + ".org"


def ensure_conversion(filename):
    target = os.path.join("readmes", replace_extension(filename))
    if not os.path.isfile(target):
        download = os.path.join("responses", filename)
        subprocess.run(["pandoc", download, "--output", target, "--columns=70"])


for url in urls:
    filename = construct_filename(url)
    ensure_download(url, filename)
    ensure_conversion(filename)

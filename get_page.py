import requests

page = requests.get("https://raw.githubusercontent.com/ChloeLiShang/CMPUT404-lab1/master/get_page.py")

print(page.content)

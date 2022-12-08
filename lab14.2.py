import requests

p = requests.get("http://ukr.net")
out = open("D:\Git\Repos\VKN\photo.jpeg", "wb")
out.write(p.content)
out.close()
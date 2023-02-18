import requests as req
from bs4 import BeautifulSoup as BS


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.51 Safari/537.36',
    "cookie": "__cf_bm=ZTlCq7g0bYAINpmyQ9IhqphXeYLj9.Hqgq0.oWO93Dg-1676747609-0-Ab4D44d/MKp4+XZ/TZaONO0mCXYkpWuAPm4N/utvBcKIAOdoO+XcomK8l/Zvk2gxBcqy+GwwDOQYrmzGgqEoO+fQv/QDixzK+JwRHivVap5/"
}

link = "https://www.chess.com/chess-themes/pieces/neo/300/{}{}.png"
for color in 'wb':
    for figure in 'prnbqk':
        print(link.format(color, figure))
        image = req.get(link.format(color, figure), headers=headers).content
        with open(f"./src/img/{color}{figure}.png", 'wb') as file:
            file.write(image)

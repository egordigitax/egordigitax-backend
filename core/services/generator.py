from io import BytesIO

from PIL import Image
import requests

def generate_square(id, bearer):
    url = f"https://api.pnchh.com/api/v1/punchember/leaderboard?limit=5&offset=0&userId={id}"
    headers = {"Authorization": f"Bearer {bearer}"}
    res = requests.get(url, headers=headers).json()
    character = res["currentUserRow"]["character"]

    char_urls = []
    for url in list(character.keys())[1:]:
        char_urls.append(character[url])
    char_urls.reverse()

    char_img = Image.new("RGBA", (36,36), (0,0,0,0))

    for url in char_urls:
        res = requests.get(url)
        img = Image.open(BytesIO(res.content))
        char_img.alpha_composite(img)

    char_img = char_img.resize((1300,1310), Image.NEAREST)

    back = Image.open("core/services/background.png")

    back.paste(char_img, (150, 150), char_img)

    back.save("sources/temp.png")
    return "sources/temp.png"

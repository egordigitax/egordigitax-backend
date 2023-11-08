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

    def append_element(img, element):
        _elem = requests.get(character[element])
        element_img = Image.open(BytesIO(_elem.content))
        img.alpha_composite(element_img)

    def append_element_if_exist(elem):
        if elem in character.keys():
            append_element(char_img, elem)

    append_element_if_exist("body")
    append_element_if_exist("shoes")
    append_element_if_exist("pants")
    append_element_if_exist("cloth")
    append_element_if_exist("face")
    append_element_if_exist("hair")
    append_element_if_exist("headphones")
    append_element_if_exist("glasses")
    append_element_if_exist("sunglasses")
    append_element_if_exist("glass")
    append_element_if_exist("accessories")

    char_img = char_img.resize((1300,1310), Image.NEAREST)

    back = Image.open("core/services/background.png")

    back.paste(char_img, (150, 150), char_img)

    back.save("sources/temp.png")
    return "sources/temp.png"

import requests
from urllib import parse

def get_ocid(character_name):
    parsed_character_name = parse.quote(character_name)

    ocid_request_url = f"https://open.api.nexon.com/maplestory/v1/id?character_name={parsed_character_name}"
    ocid_request_headers = {
        "accept": "application/json",
        "x-nxopen-api-key": "test_2e7d86996071c7dee732b698edaadf67478876df15052177cbd63a9f76ef6207e4cb2054f341b79305fa2dc30fea1b21"
    }
    get_ocid_response = requests.get(ocid_request_url, headers=ocid_request_headers)

    if get_ocid_response.status_code == 200:
        character_data = get_ocid_response.json()
        print(character_data)
        return character_data['ocid']
    else:
        print(f"Error: {get_ocid_response.status_code}")
        return False


def get_character_status(ocid, date):
    url = f"https://open.api.nexon.com/maplestory/v1/character/basic?ocid={ocid}&?date={date}"
    request_headers = {
        "accept": "application/json",
        "x-nxopen-api-key": "test_2e7d86996071c7dee732b698edaadf67478876df15052177cbd63a9f76ef6207e4cb2054f341b79305fa2dc30fea1b21"
    }
    response = requests.get(url, headers=request_headers)
    if response.status_code == 200:
        response_data = response.json()
        print(response_data)
        return response_data
    else:
        print(f"Error: {response.status_code}")
        return False


def download_image(image_url, save_path):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Image downloaded: {save_path}")
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    image_download_cnt = 1
    ocid = get_ocid("아델")
    if ocid:
        response_data = get_character_status(ocid, '2024-05-15')
        if response_data:
            image_url = response_data["character_image"]
            download_image(image_url, f"./images/character_image_{image_download_cnt}.png")
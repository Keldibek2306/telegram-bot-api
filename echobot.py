from time import sleep
import requests
from settings import TOKEN

BASE_URL = f'https://api.telegram.org/bot{TOKEN}'


def get_updates(offset: int | None):
    params = {
        'offset': offset
    }
    getupdates_url = f'{BASE_URL}/getUpdates'
    response = requests.get(getupdates_url, params=params)
    return response.json()["result"]


def send_message(chat_id: int, text: str):
    params = {
        'chat_id': chat_id,
        'text': text
    }
    requests.get(f'{BASE_URL}/sendMessage', params=params)


def send_contact(chat_id: int, first_name: str, phone_number: str):
    params = {
        'chat_id': chat_id,
        'first_name': first_name,
        'phone_number': phone_number,
    }
    requests.get(f'{BASE_URL}/sendContact', params=params)


def send_photo(chat_id: int, photo: str):
    params = {
        'chat_id': chat_id,
        'photo': photo,
    }
    requests.get(f'{BASE_URL}/sendPhoto', params=params)


def send_audio(chat_id: int, audio: str):
    params = {
        'chat_id': chat_id,
        'audio': audio
    }
    requests.get(f'{BASE_URL}/sendAudio', params=params)


def send_document(chat_id: int, document: str):
    params = {
        'chat_id': chat_id,
        'document': document
    }
    requests.get(f'{BASE_URL}/sendDocument', params=params)


def send_video(chat_id: int, video: str):
    params = {
        'chat_id': chat_id,
        'video': video
    }
    requests.get(f'{BASE_URL}/sendVideo', params=params)


def send_voice(chat_id: int, voice: str):
    params = {
        'chat_id': chat_id,
        'voice': voice
    }
    requests.get(f'{BASE_URL}/sendVoice', params=params)


def send_video_note(chat_id: int, video_note: str):
    params = {
        'chat_id': chat_id,
        'video_note': video_note
    }
    requests.get(f'{BASE_URL}/sendVideoNote', params=params)


def send_paid_media(chat_id: int, media: list):
    params = {
        'chat_id': chat_id,
        'media': media
    }
    requests.post(f'{BASE_URL}/sendPaidMedia', json=params)


def send_media_group(chat_id: int, media: list):
    params = {
        'chat_id': chat_id,
        'media': media
    }
    requests.post(f'{BASE_URL}/sendMediaGroup', json=params)


def send_location(chat_id: int, latitude: float, longitude: float):
    params = {
        'chat_id': chat_id,
        'latitude': latitude,
        'longitude': longitude
    }
    requests.get(f'{BASE_URL}/sendLocation', params=params)


def send_venue(chat_id: int, latitude: float, longitude: float, title: str, address: str):
    params = {
        'chat_id': chat_id,
        'latitude': latitude,
        'longitude': longitude,
        'title': title,
        'address': address
    }
    requests.get(f'{BASE_URL}/sendVenue', params=params)


def send_poll(chat_id: int, question: str, options: list):
    params = {
        'chat_id': chat_id,
        'question': question,
        'options': options
    }
    requests.post(f'{BASE_URL}/sendPoll', json=params)


def send_contact(chat_id: int, first_name: str, phone_number: str):
    params = {
        'chat_id': chat_id,
        'first_name': first_name,
        'phone_number': phone_number,
    }

    sendmessage_url = f'{BASE_URL}/sendContact'
    requests.get(sendmessage_url, params=params)


def send_photo(chat_id: int, photo: str):
    params = {
        'chat_id': chat_id,
        'photo': photo,
    }

    sendmessage_url = f'{BASE_URL}/sendPhoto'
    requests.get(sendmessage_url, params=params)


def updater(token: str):
    offset = None

    while True:
        updates = get_updates(offset)
        for update in updates:
            
            if 'message' in update and 'text' in update['message']:
                user = update['message']['from']
                
                send_message(user['id'], update['message']['text'])

            offset = update['update_id'] + 1

        sleep(1)


if __name__ == '__main__':
    updater(TOKEN)

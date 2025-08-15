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


def updater(token: str):
    offset = None

    while True:
        updates = get_updates(offset)
        for update in updates:
            if 'message' in update:
                message = update['message']
                user = message['from']

                if 'text' in message:
                    text = message['text']
                    send_message(user['id'], text)

                elif 'contact' in message:
                    contact = message['contact']
                    send_contact(user['id'], contact['first_name'], contact['phone_number'])

                elif 'photo' in message:
                    photo = message['photo'][0]
                    send_photo(user['id'], photo['file_id'])

                elif 'audio' in message:
                    audio = message['audio']
                    send_audio(user['id'], audio['file_id'])

                elif 'document' in message:
                    document = message['document']
                    send_document(user['id'], document['file_id'])

                elif 'video' in message:
                    video = message['video']
                    send_video(user['id'], video['file_id'])

                elif 'voice' in message:
                    voice = message['voice']
                    send_voice(user['id'], voice['file_id'])

                elif 'video_note' in message:
                    video_note = message['video_note']
                    send_video_note(user['id'], video_note['file_id'])

                elif 'location' in message:
                    location = message['location']
                    send_location(user['id'], location['latitude'], location['longitude'])

                elif 'venue' in message:
                    venue = message['venue']
                    send_venue(user['id'], venue['location']['latitude'],
                               venue['location']['longitude'], venue['title'], venue['address'])

                elif 'poll' in message:
                    poll = message['poll']
                    send_poll(user['id'], poll['question'], poll['options'])

            offset = update['update_id'] + 1

        sleep(1)


if __name__ == '__main__':
    updater(TOKEN)

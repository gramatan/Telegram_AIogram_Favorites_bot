import asyncio
import logging
import os
import requests
from datetime import datetime
from aiogram import types

from config.config import ADMIN

logger = logging.getLogger(__name__)

IMAGE_URL = 'https://www.calend.ru/img/export/informer.png'
LOCAL_IMAGE_PATH = 'cached_calendar.png'


def download_image():
    try:
        response = requests.get(IMAGE_URL)
        response.raise_for_status()

        with open(LOCAL_IMAGE_PATH, 'wb') as f:
            f.write(response.content)
        logger.info('New calendar image has been downloaded and saved.')

    except requests.exceptions.RequestException as e:
        logger.warning(f'Error occurred while updating calendar image: {e}')
        return False

    return True

def is_image_stale():
    if not os.path.exists(LOCAL_IMAGE_PATH):
        return True

    file_mod_time = datetime.fromtimestamp(os.path.getmtime(LOCAL_IMAGE_PATH))
    return file_mod_time.date() != datetime.now().date()


async def send_calendar_sticker(message: types.Message):
    if is_image_stale():
        if not download_image():
            await message.answer('Failed to load the image. Please try again later.')
            await message.delete()
            return
        logger.info('Image was downloaded and sent.')
    else:
        logger.info('Image was sent from cache.')

    with open(LOCAL_IMAGE_PATH, 'rb') as f:
        await message.answer_sticker(f)


async def refresh_image(message: types.Message):
    if message.from_id != ADMIN:
        update_message = await message.answer('Hold on! Only the chosen ones can update the calendar.')
        await asyncio.sleep(5)
        await update_message.delete()
        return

    if download_image():
        update_message = await message.answer('The calendar image has been updated.')
        logger.info('Image was downloaded and updated upon user request.')
    else:
        update_message = await message.answer('Failed to update the image. Please try again later.')
        logger.info('Failed to download image upon user request.')

    await message.delete()

    await asyncio.sleep(5)
    await update_message.delete()

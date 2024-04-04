import json
import disnake
import aiohttp
import asyncio


async def check_attachments(message):
    '''
    Check message attachments to ensure that
    there is an attachment and that the attachment is
    the sample.json file for updating embed
    '''
    # if len(message.attachments) == 1:
    #     attachment = message.attachments[0]
    #     channel = message.channel

    #     # Confirm uploaded file is the sample.json
    #     if attachment.filename == "sample.json":
    #         url = attachment.url

    #         # Create a async client session and download the json from discord attachment url
    #         async with aiohttp.ClientSession() as session:
    #             async with session.get(url) as response:
    #                 response = await response.json()
    # Указываем путь к файлу JSON
    file_path = 'sam'

    # Открываем файл в режиме чтения
    with open(file_path, 'r') as file:
        # Загружаем содержимое файла JSON в переменную
        json_content = json.load(file)

    # Преобразуем содержимое JSON в текстовый формат
    json_text = json.dumps(json_content)
    embed = json_text

    # Create the embed object for discord, if fails, return error
    try:
        embed = disnake.Embed.from_dict(embed)
        return embed
    except:
        return "Error"



async def check_message(message):
    '''
    check that the upload message has content
    content should only be the message ID to be updated
    '''
    msg_id = message.content.strip()

    # check the the ID found in the message content is a valid message within the channel.
    try:
        msg = await message.channel.fetch_message(int(msg_id))
        return msg
    except:
        return "Error"

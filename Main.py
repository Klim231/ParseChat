from telethon import TelegramClient, sync, events




api_id = 8019680
api_hash = 'a70c14318d7fbd747502ae9228a9d2fc'

client = TelegramClient('Crypto_session', api_id, api_hash)


@client.on(events.NewMessage(chats=['🏆Wall Street Crypto 5 поток 🌴']))
async def normal_handler(event):
#    print(event.message)
    msg_dict = event.message.to_dict()
    chats_id = [-1001545927249, -1001541061595]
    for chat_id in chats_id:
        try:
            if msg_dict['media'] == None:
                await client.send_message(chat_id, event.message.to_dict()['message'])
            else:
                chat = await event.get_input_chat()
                msg = await client.get_messages(chat.channel_id, limit=1)
                await client.forward_messages(chat_id, msg)
        except:
            pass

client.start()
client.run_until_disconnected()

# @client.on(events.NewMessage(chats=['Admins']))
# async def normal_handler(event):
# #    print(event.message)
#     msg_dict = event.message.to_dict()
#     print(msg_dict)
#     print(msg_dict['message'])
#     if msg_dict['media'] == None:
#         await client.send_message(-1001473454951, event.message.to_dict()['message'])
#     else:
#         chat = await event.get_input_chat()
#         msg = await client.get_messages(chat.channel_id, limit=1)
#         await client.forward_messages(-1001473454951, msg)
#
#
# client.start()
# client.run_until_disconnected()

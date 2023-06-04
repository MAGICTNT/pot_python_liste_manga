import random


async def send_message_priver(username, message, user_message, is_private):
    try:
        print("?.1")
        response = get_response_priver(username, user_message)
        print("?.2")
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)
        
def get_response_priver(user: str, message: str) ->  tuple[str, str] | tuple[str, str, str, str] | str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Hey ', user

    if p_message == 'roll':
        return 'Salut ', user, ' ', str(random.randint(1, 6))

    if p_message == '!hello':
        return '`need help you too`'

    return 'J\'ai pas compris '
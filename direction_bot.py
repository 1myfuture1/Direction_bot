from textblob import TextBlob
import discord 

client = discord.Client()

read_chann_dict = {
    '#rules': ['what are rules?', 'is it in channel rules?', 'is it rules?', 'what rules?', 'where can I see rules?', 'show me rules', 'server rules', 'channel rules'],
    '#directory': ["i'm new here", 'where can i start?', 'can you give me a guide?', 'where is channel?', 'what channels do?'],
    '#twitter': ["what's your social medias?", 'do you have twitter?', 'where can i find your sm?']
}

write_chann_dict = {
    '#welcome': ['hi!', 'hey!', 'hi', 'hey', 'hello', 'hello!'],
    '#quantum-community-program-qa channels': ['my work', "here's my work", 'my meme', 'my article', 'my art', 'my video'],
    '#testnet-signup-qa': ['testnet', 'how can i get into testnet?', 'i need a help with testnet', 'i want to do a testnet', 'your testnet is good'],
}

language_channels = {
    'zh-CN': '#chinese-community-🇨🇳',
    'fr': '#french-community-🇫🇷',
    'ko': '#korean-community-🇰🇷',
    'th': '#thai-community-🇹🇭',
    'tr': '#turkish-community-🇹🇷',
    'ru': '#russian-community-🇷🇺 '
}

@client.event
async def on_ready():
    print("Hey bud, it's me! {0.user}".format(client))

@client.event
async def on_message(message):
    '''This function will take a message and direct user to a right channel if needed'''
    
    # We won't give directions in channels for languages. 
    if 1:#any(chann == str(message.channel) for chann in write_chann_dict.keys()):  # I couldn't figure out how to access channel's name
        if len(message.content) < 3: 
            message.content += '  ' # We need it fo TextBlob to work.

        word_len = TextBlob(message.content)
        language = word_len.detect_language()

        if language in language_channels.keys():
            # Directing people to their language channels.
            await message.reply(f'Please, only speak English here. Go to {language_channels[language]} to chat in your language :)')
        elif language != 'en':
            # If we don't have a channel for language that user uses, he'll get this message.
            await message.reply("Sorry, we don't have a channel for your language yet, but please, only speak English here.")
        else:
            # Bot gives directions based on users' messages.
            for channel in write_chann_dict.keys():
                for phrase in write_chann_dict[channel]:
                    if message.content.lower() == phrase:
                        await message.reply(f'Please, go to {channel}')

            for r_channel in read_chann_dict.keys():
                for r_phrase in read_chann_dict[r_channel]:
                    if message.content.lower() == r_phrase:
                        await message.reply(f'Please, go to {r_channel}')
            

client.run('TOKEN')

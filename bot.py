from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

from configbot import TOKEN_BOT, NEEUS_CHANNEL, GITHUB_PROFILE
from locate import *

bot = Bot(TOKEN_BOT)
dp = Dispatcher(bot)

ButtonChannel = InlineKeyboardButton(text='Neeus Channel 🫂', callback_data='channel_neeus')
ButtonGitHub = InlineKeyboardButton(text='My GitHub 👾', callback_data='profile_github')
ButtonHelp = InlineKeyboardButton(text='Help 👨🏽‍🏫', callback_data='help')
Buttons = InlineKeyboardMarkup().add(ButtonHelp, ButtonChannel, ButtonGitHub)

@dp.message_handler(commands=[COMMANDS['/start']])
async def welcome(message: types.message):
    await message.answer(ES.WELCOME_BOT_USER.format(message.from_user.full_name), reply_markup = Buttons)
    
@dp.callback_query_handler(text=['channel_neeus', 'profile_github', 'help'])
async def buttons_bot(call: types.CallbackQuery):
    if call.data == 'channel_neeus':
        await call.message.answer(NEEUS_CHANNEL)
    elif call.data == 'donate_for_bot':
        await call.message.answer(ES.DONATE_FOR_THE_BOT)
    elif call.data == 'profile_github':
        await call.message.answer(GITHUB_PROFILE)
    elif call.data == 'help':
        await call.message.answer_photo('https://github.com/fcoagz/NeeusBot/blob/main/assets/example.png?raw=true', ES.HELP)

@dp.message_handler(commands=[COMMANDS['/donate']])
async def echo(message: types.message):
    await message.reply(ES.DONATE_FOR_THE_BOT)  

@dp.message_handler(content_types=['text'])
async def echo(message: types.message):

    message.text = message.text.upper()
    message.text = message.text.lower()

    if message.text == SONG[1]:
        await message.answer_audio('{}/5'.format(NEEUS_CHANNEL))
    elif message.text == SONG[2]:
        await message.answer_audio('{}/6'.format(NEEUS_CHANNEL))
    elif message.text == SONG[3]:
        await message.answer_audio('{}/7'.format(NEEUS_CHANNEL))
    elif message.text == SONG[4]:
        await message.answer_audio('{}/8'.format(NEEUS_CHANNEL))
    elif message.text == SONG[5]:
        await message.answer_audio('{}/9'.format(NEEUS_CHANNEL))
    elif message.text == SONG[6]:
        await message.answer_audio('{}/10'.format(NEEUS_CHANNEL))
    elif message.text == SONG[7]:
        await message.answer_audio('{}/12'.format(NEEUS_CHANNEL))
    elif message.text <= SONG[8]:
        await message.answer_audio('{}/13'.format(NEEUS_CHANNEL))
    elif message.text == SONG[9]:
        await message.answer_audio('{}/15'.format(NEEUS_CHANNEL))
    elif message.text == SONG[10]:
        await message.answer_audio('{}/16'.format(NEEUS_CHANNEL))
    elif message.text == SONG[11]:
        await message.answer_audio('{}/17'.format(NEEUS_CHANNEL))
    elif message.text == SONG[12]:
        await message.answer_audio('{}/18'.format(NEEUS_CHANNEL))
    elif message.text == SONG[13]:
        await message.answer_audio('{}/19'.format(NEEUS_CHANNEL))
    elif message.text == SONG[14]:
        await message.answer_audio('{}/20'.format(NEEUS_CHANNEL))
    elif message.text == SONG[15]:
        await message.answer_audio('{}/21'.format(NEEUS_CHANNEL))
    elif message.text == SONG[18]: # te recorde
        await message.answer_audio('{}/21'.format(NEEUS_CHANNEL))
    elif message.text == SONG[16]:
        await message.answer_audio('{}/27'.format(NEEUS_CHANNEL))
    elif message.text == SONG[17]:
        await message.answer_audio('{}/33'.format(NEEUS_CHANNEL))

executor.start_polling(dp)

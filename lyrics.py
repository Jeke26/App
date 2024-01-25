import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Fungsi untuk mencari lirik
def search_lyrics(artist, title):
    api_url = f'https://api.lyrics.ovh/v1/{artist}/{title}'
    response = requests.get(api_url)

    if response.status_code == 200:
        lyrics = response.json().get('lyrics', 'Lirik tidak ditemukan.')
    else:
        lyrics = 'Terjadi kesalahan dalam mencari lirik.'

    return lyrics

# Fungsi untuk menangani perintah /lyrics
def lyrics(update: Update, context: CallbackContext) -> None:
    args = context.args
    if len(args) < 2:
        update.message.reply_text('Gunakan perintah /lyrics [artis] [judul] untuk mencari lirik lagu.')
        return

    artist = args[0]
    title = ' '.join(args[1:])
    result = search_lyrics(artist, title)

    update.message.reply_text(result)

def main():
    updater = Updater(token='6394509655:AAGDcW87avQzWD66Fxcv8U-i2M_l9cB79V0', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('lyrics', lyrics))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import requests

# Fungsi untuk menangani perintah /search
def search_spotify(query, access_token):
    api_url = 'https://api.spotify.com/v1/search'
    headers = {'Authorization': f'Bearer {access_token}'}
    params = {'q': query, 'type': 'track'}

    response = requests.get(api_url, headers=headers, params=params)
    results = response.json().get('tracks', {}).get('items', [])

    return results

    # Kirim hasil pencarian ke pengguna dengan tombol unduh
    if results:
        result_text = "\n".join([f"{index + 1}. {track['title']}" for index, track in enumerate(results)])
        keyboard = [
            [InlineKeyboardButton("Unduh", url=track['link'])] for track in results
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
    else:
        result_text = "Tidak ada hasil ditemukan."
        reply_markup = None

    update.message.reply_text(result_text, reply_markup=reply_markup)

# Konfigurasi token bot dan inisialisasi Updater
updater = Updater(token='6578195199:AAGMG0exVKHtttBReBtJusgbIE0R57av-G8', use_context=True)

# Daftarkan handler untuk perintah /search
updater.dispatcher.add_handler(CommandHandler('search', search))

# Jalankan bot
updater.start_polling()
updater.idle()
  

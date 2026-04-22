import discord
from discord.ext import commands
import os

# Setup bot dengan prefix '!'
intents = discord.Intents.default()
intents.message_content = True  # Diperlukan untuk membaca pesan

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} siap digunakan!')

# Command sederhana: Salam
@bot.command()
async def hello(ctx):
    await ctx.send('Halo! Saya adalah bot untuk Soul Land News World. Apa yang bisa saya bantu?')

# Command untuk info game (simulasi berita)
@bot.command()
async def news(ctx):
    news_message = """
    **Berita Terbaru Soul Land News World:**
    - Update patch 1.5: Karakter baru tersedia!
    - Event mingguan: Raid boss aktif hingga 25 April.
    - Tips: Tingkatkan level dengan quest harian.
    """
    await ctx.send(news_message)

# Command untuk info karakter (contoh sederhana)
@bot.command()
async def info(ctx, *, nama: str = None):
    if not nama:
        await ctx.send('Silakan sebutkan nama karakter, contoh: !info Tang San')
        return
    
    # Simulasi data karakter (bisa diganti dengan database nanti)
    karakter_data = {
        'tang san': 'Karakter utama dengan spirit blue silver grass. Level max: 100.',
        'xiao wu': 'Karakter pendukung dengan spirit soft bone rabbit. Spesialisasi: Agility.'
    }
    
    info = karakter_data.get(nama.lower(), 'Karakter tidak ditemukan. Coba nama lain.')
    await ctx.send(f'**Info {nama.title()}:** {info}')

# Jalankan bot dengan token dari environment variable (untuk keamanan)
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
if TOKEN:
    bot.run(TOKEN)
else:
    print('Error: DISCORD_BOT_TOKEN tidak ditemukan. Set variabel environment terlebih dahulu.')
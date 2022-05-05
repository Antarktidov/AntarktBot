# -*- coding: utf-8 -*-
import discord #импортируем библиотеки
from discord import Client, Intents, Embed
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
import requests
import random
import datetime as DT
import time
import calendar
import os
import sys
import wikitextparser as wtp

settings = {#параметры бота
    'token': 'вставьте сюда ваш токен',
    'bot': 'ДивноГорьеБот',
    'id': вставьте сюда id бота вез кавычек,
    'prefix': 'див!'
}

bot = commands.Bot(command_prefix = "див!")
@bot.command()
async def погода(ctx, *, city): # Погода
    url = 'https://wttr.in/' + city

    weather_parameters = {
    '0': '',
    'T': '',
    'M': '',
    }

    request_headers = {
    'Accept-Language': 'ru'
    }
    response = requests.get(url, headers=request_headers, params=weather_parameters)
    await ctx.send(response.text)
@bot.command()
async def царевны(ctx): #Царевны
    await ctx.send('''<https://tsarevny.ru> - сайт
<https://www.youtube.com/tsarevny> - YouTube
<https://vk.com/tsarevny.official> - VK
<https://tsarevny.fandom.com/ru> - вики
<https://vk.com/tsarevna_ask> - ASK Царевны''')
@bot.command()
async def инфо(ctx): #Информация о боте
    await ctx.send('Автор бота - Антаркт#5225. Версия Питона - 3.9.7. Использована библиотека discord.py. Отдельное спасибо kotenok gav#8521 и Fluttershy#7152 (Strangedude123/Снежок Сказочника/TerribleEditor/StarlightGlimmer) за помощь в установке библиотеки и исправлении багов. А также спасибо Black Spaceship за то, что вдохновил автора на написание бота и Ядекс. Практикуму за обучение автора. Также спасибо папиному знакомому Максиму за помощь в установке питона на другой компьютер. Ещё спасибо всем неравнодушным людям со stackowerflow, хабра и прочих рессрсов и атору и переводчику книги "Байт оф Пайтон"')
@bot.command()
async def сервер(ctx): #Сервер поддержки бота
    await ctx.send('Вставьте сюда ссылку на ваш сервер')
@bot.command()
async def код(ctx): #Код бота
    await ctx.send('<https://github.com/Antarktidov/AntarktBot/blob/main/AntarkBot.py>')
@bot.command()
async def утка(ctx): #Утки
    ducks = ['https://cdn.pixabay.com/photo/2017/02/01/00/31/duck-2028587_1280.jpg', 'https://s.go31.ru/section/catalogpagesintext/upload/images/catalog/intext/000/052/452/kupit-utku_5f435b652c525.jpg', 'https://masslandlords.net/wp-content/uploads/sex-based-discrimination-image-licensed-Pixabay-1536x826.jpg', 'https://stroy-podskazka.ru/images/article/orig/2019/04/skolko-zhivut-utki-i-ot-chego-eto-zavisit.jpg', 'https://mota.ru/upload/resize/1280/1024/upload/wallpapers/source/2016/06/16/20/01/48977/mota.ru_2016061628-b17.jpg', 'https://i.ytimg.com/vi/hJLaqQLVKhw/maxresdefault.jpg', 'https://moydom.moscow/wp-content/uploads/2020/05/2020-05-15-13-43-35.jpg', 'https://cdn.pixabay.com/photo/2021/06/16/21/46/ducklings-6342270_1280.jpg', 'https://cdn.fishki.net/upload/post/2017/05/04/2282681/dffed465d0896b77c479704c2abe7da6.jpg', 'https://avatars.mds.yandex.net/get-zen_doc/1921148/pub_5f8df42b75135c199900abf2_5f8df43975135c199900bde4/scale_1200', 'https://avatars.mds.yandex.net/get-zen_doc/1712062/pub_5fe600850d0c7759ac79521f_5fe600a9e5cdbc6a96b5b214/scale_1200', 'https://img-fotki.yandex.ru/get/6104/127683550.1d/0_116c81_cf72adf1_XXXL.jpg']
    duckimage = random.choice(ducks)
    await ctx.send(duckimage)
@bot.command()
async def пригласить(ctx): #Пригласить бота
    await ctx.send('Используйте эту ссылку, чтобы пригласить меня на ваш сервер <Вставьте сюда ссылку-приглашение бота>')
@bot.command()
async def цитата(ctx): #Цитаты
    quotes = ['Есть только один русский сотрудник, Kuzura - TokihikoH11', 'Engslish please in #general. - MisterWoodhause', 'Создавать вики для вандалов - это как покупать шубу для моли. ParaNormanBates', 'Шв - крутая вики - Липчанин', 'Тсоре над нами, мы - швиане']
    randomquote = random.choice(quotes)
    await ctx.send(randomquote)

@bot.command()
async def печенье(ctx): #Печенье
    eda = ['Ты искал печенье, но ничего не нашёл', 'Ты искал печенье и нашёл юбилейное https://choco-opt.ru/upload/iblock/163/1638803371a06e5ca39c368889b6b43b.jpeg', 'Ты искал печенье и нашёл посиделкино https://avatars.mds.yandex.net/get-mpic/5159019/img_id5076932055298017294.jpeg/orig', 'Ты искал печенье и нашёл юбилейное с шоколадом https://static.beloris.ru/content/products/458645/947684/tmp/1280_128062335dc6ec68d916fa620b6c681fdbe6_xl.jpg', 'Ты искал печенье, но ничего не нашёл', 'Ты нашёл печенье, но его съела собака', 'Ты нашёл печенье, но его съела кошка', 'Ты искал печенье, но нашёл оливье https://ne-dieta.ru/wp-content/uploads/2017/12/final_1200-7.jpg', 'Ты пытался найти хоть-какую-то еду, но нашёл печенье', 'Ты искал печеньеб но нашёл подарок на новый год']
    randomeda = random.choice(eda)
    await ctx.send(randomeda)
@bot.command()
async def пожелание(ctx): #Пожелания
    wishlist = ['лечь спать пораньше', 'сидеть всю ночь в дискорде', 'получить глобальный статус на Фэндоме', '100 000 правок на Фэндоме', 'стать админом русской Википедиии', 'всю ночь играть в акинатора', 'стать разработчиком Фэндома', 'стать сотрудником Яндекса или Microsoft', 'спокойной ночи']
    testwish = random.choice(wishlist)
    await ctx.send('Желаем вам ' + testwish)
@bot.event
async def on_ready():
    #Статус
     await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Царевны, Сказочный Патруль"))
     #Залогинен
     print('Бот вошёл в систему как {0.user}'.format(bot))
#реакция бота на сообщения
@bot.event
async def on_message(message):
    string = message.content.lower()
    wstring = message.content
    if message.author == bot.user or string.find("`") != -1 or string.find("> ") != -1 or string.find("||") != -1:
        return
    #if string.find("да") != -1:
    w = "да"
    if string.startswith(f"{w} ") or string.startswith(f"{w}!") or string.startswith(f"{w},") or string.startswith(f"{w}?") or string.startswith(f"{w}.") or string.endswith(f" {w}") or string.find(f" {w} ") != -1 or string.find(f" {w}.") != -1 or string.find(f" {w}!") != -1 or string.find(f" {w}?") != -1 or string.find(f" {w},") != -1 or string == w:
        await message.channel.send('А у тебя есть борода?')
    w = "нет"
    if string.startswith(f"{w} ") or string.startswith(f"{w}!") or string.startswith(f"{w},") or string.startswith(f"{w}?") or string.startswith(f"{w}.") or string.endswith(f" {w}") or string.find(f" {w} ") != -1 or string.find(f" {w}.") != -1 or string.find(f" {w}!") != -1 or string.find(f" {w}?") != -1 or string.find(f" {w},") != -1 or string == w:
        netanswers = ['Ты мне достался на обед!', 'Откуда взялся интернет!']
        netanswer = random.choice(netanswers)
        await message.channel.send(netanswer)
    w = "yes"
    if string.startswith(f"{w} ") or string.startswith(f"{w}!") or string.startswith(f"{w},") or string.startswith(f"{w}?") or string.startswith(f"{w}.") or string.endswith(f" {w}") or string.find(f" {w} ") != -1 or string.find(f" {w}.") != -1 or string.find(f" {w}!") != -1 or string.find(f" {w}?") != -1 or string.find(f" {w},") != -1 or string == w:
        await message.channel.send('Yes, yes... ОБХСС! - Джентельмены у\д\ачи')
    if string.find("609078741775155211") != -1:
        await message.channel.send('Мой преффикс - див!')
    w = "бот"
    if string.startswith(f"{w} ") or string.startswith(f"{w}!") or string.startswith(f"{w},") or string.startswith(f"{w}?") or string.startswith(f"{w}.") or string.endswith(f" {w}") or string.find(f" {w} ") != -1 or string.find(f" {w}.") != -1 or string.find(f" {w}!") != -1 or string.find(f" {w}?") != -1 or string.find(f" {w},") != -1 or string == w:
        whatbotanswers = ['Чего?', 'А кто же ещё', 'Да, я бот', 'приём, приём, как слышно']
        whatbotanswer = random.choice(whatbotanswers)
        await message.channel.send(whatbotanswer)
    w = "привет"
    if string.startswith(f"{w} ") or string.startswith(f"{w}!") or string.startswith(f"{w},") or string.startswith(f"{w}?") or string.startswith(f"{w}.") or string.endswith(f" {w}") or string.find(f" {w} ") != -1 or string.find(f" {w}.") != -1 or string.find(f" {w}!") != -1 or string.find(f" {w}?") != -1 or string.find(f" {w},") != -1 or string == w:   
        author = message.author # Объявляем переменную author и записываем туда информацию об авторе.
        answers = [f'Привет, {author.mention}!', 'Денег нет!']
        answer = random.choice(answers)
        await message.channel.send(answer)
    if wstring.isupper() == True:
        answers = ['CAPSLOCK DETECTED', 'Еээээ! Капсовая вечеринка :tada:!']
        answer = random.choice(answers)
        await message.channel.send(answer)
    #вики-ссылки
    if string.find("[[") != -1 and message.content.find("]]") != -1:
        result = wstring[wstring.find('[[')+1:wstring.find(']]')]
        result = result.replace('[', '')
        result = result.replace(' ', '_')
        result = result.replace('?', '%3F')
        #фэндом
        if result.startswith('w:c:'):
            components = result.split(':')
            print(components)
            print(components[2].find('.') != -1)
            #неанглийские вики
            if components[2].find('.') != -1:
                print(components[2])
                lurl = components[2].split('.') #lurl - lang и url
                lang = lurl[0]
                url = lurl[1]
                slash = '/'
            #английские вики
            else:
                lang = ''
                url = components[2]
                slash = ''
            #удаление w:c:ru.wiki: из массива и сборка оставшихся частей
            a = components.pop(2)
            a = components.pop(1)
            a = components.pop(0)
            #(components)
            page = ':'.join(components) 
            #print(page)
            if result.endswith('?'):
                page = page + '%3F'
            if result.endswith(')'):
                page = page + '_'
            await message.channel.send(f'<https://{url}.fandom.com/{lang}{slash}wiki/{page}>')
        #русская википедия
        elif result.startswith('ruwikipedia:'):
            page = result.replace('ruwikipedia:', '')
            if result.endswith('?'):
                page = page + '%3F'
            if result.endswith(')'):
                page = page + '_'
            await message.channel.send(f'<https://ru.wikipedia.org/wiki/{page}>')
        #Библиотека Лосяша - вики поуполчанию
        else:
            if result.endswith('?'):
                result = result + '%3F'
            if result.endswith(')'):
                result = result + '_'
            await message.channel.send(f'<https://losyash-library.fandom.com/ru/wiki/{result}>')
    #шаблоны
    if string.find("{{") != -1 and message.content.find("}}") != -1:
        result = wstring[wstring.find('{{')+1:wstring.find('}}')]
        result = result.replace('{', '')
        result = result.replace(' ', '_')
        result = result.replace('?', '%3F')
        #фэндом
        #русские вики
        if result.startswith('w:c:ru.'):
            Template = "Шаблон:"
        else:
            Template = "Template:"
        if result.startswith('w:c:'):
            components = result.split(':')
            print(components)
            print(components[2].find('.') != -1)
            #неанглийские вики
            if components[2].find('.') != -1:
                print(components[2])
                lurl = components[2].split('.') #lurl - lang и url
                lang = lurl[0]
                url = lurl[1]
                slash = '/'
            #английские вики
            else:
                lang = ''
                url = components[2]
                slash = ''
            #удаление w:c:ru.wiki: из массива и сборка оставшихся частей
            a = components.pop(2)
            a = components.pop(1)
            a = components.pop(0)
            #(components)
            page = ':'.join(components) 
            #print(page)
            if result.endswith('?'):
                page = page + '%3F'
            if result.endswith(')'):
                page = page + '_'
            await message.channel.send(f'<https://{url}.fandom.com/{lang}{slash}wiki/{Template}{page}>')
        #русская википедия
        elif result.startswith('ruwikipedia:'):
            page = result.replace('ruwikipedia:', '')
            if result.endswith('?'):
                page = page + '%3F'
            if result.endswith(')'):
                page = page + '_'
            await message.channel.send(f'<https://ru.wikipedia.org/wiki/Шаблон:{page}>')
        #Библиотека Лосяша - вики поуполчанию
        else:
            if result.endswith('?'):
                result = result + '%3F'
            if result.endswith(')'):
                result = result + '_'
            await message.channel.send(f'<https://losyash-library.fandom.com/ru/wiki/Шаблон:{result}>')
        
        #устранение конфликта между этим событием и командами
    await bot.process_commands(message)
@bot.command()
async def факты(ctx): #Факт
    await ctx.send('''Интересные факты о программмировании:
- Если скачать сразу два питона, то библиотека может не установится
- Если скачать питон через визуал студио - тоже самое
- Слишком новый или старый питон - опять тоже самое
- Ну и вообще тоже самое если неправильно установить питон
- Если кодить в визуал студио, то питон не будет поддерживать кириллицу
- Невозможно создать команду bot.
- Невозможно создать две одинаковые команды
- Библиотека discord.py не поддерживает слэш-команды
- При установке питона могут не установится некоторые стандартные библиотеки''')
@bot.command()
async def тест(ctx): #Тест
    await ctx.send('Бот подключён к интернету и соединён с дискордом')
@bot.command() # Основной
async def основной(ctx):
    await ctx.send('Эта беседа должна быть продолжена в <#923622413068038187>')
@bot.command() # НГ
async def нг(ctx):
    now = DT.datetime.today()
    new_year = DT.datetime(2022, 1, 1)
    print(now)
    print(new_year)
    if now < new_year:
        await ctx.send('С наступающим Новым годом!')
    else:
        await ctx.send('С наступившим Новым годом!')
    photos = ['http://shop.rpkgr.ru/wa-data/public/shop/products/57/53/5357/images/23882/23882.700.jpg', 'https://tdpodarkov.ru/800/600/https/kofe.ru/images/thumbnails/2445/2000/detailed/32/7278.40.jpg', 'https://images.ru.prom.st/682835621_w640_h640_podarochnyj-nabor-schelkunchik.jpg', 'https://7960777a-2fd1-4b07-8bbb-896e98c4659c.selcdn.net/upload/resize_cache/iblock/cce/400_400_140cd750bba9870f18aada2478b24840a/cce7a262f93d9591e1dfdd3b5f0026d5.jpg', 'https://ftea.ru/wp-content/uploads/2019/04/45.2.jpg', 'https://avatars.mds.yandex.net/get-zen_doc/2746214/pub_5fe7fbc7dba1eb4af8e7739d_5fe7fdcedba1eb4af8e80e1f/scale_1200', 'https://serovodorod-okt.ru/800/600/https/avatars.mds.yandex.net/get-zen_doc/1880383/pub_5e9e11d44292883111a14819_5e9eddd9175b6f71c45ae3d7/scale_1200', 'https://static.1000.menu/img/content/20917/-salat-stolichnyi-salat-stolichnyi-olive_1498161313_1_og.jpg', 'https://avatars.mds.yandex.net/get-zen_doc/3396902/pub_5fc26e684c127965db076658_5fc26f404c127965db08f651/scale_1200']
    randomphoto = random.choice(photos)
    await ctx.send(randomphoto)
@bot.command()
async def kuzura(ctx): #Kuzura
    await ctx.send('https://thumbnailer.mixcloud.com/unsafe/900x900/extaudio/3/9/f/d/188e-cf7a-43d9-ad47-9aeab297e2f8.jpg')
@bot.command()
async def мышеловка(ctx): #мышеловка
    text = input()
    await ctx.send(text)
@bot.command()
async def мем(ctx): #Мемы
    memes = ['https://sun9-16.userapi.com/impg/p0_aG8X-nbQf9nniAEdW1ej3KbCff-PT_lt4ew/QlOWMPCh5TA.jpg?size=555x669&quality=96&sign=07dd41dcda4e87d14dbee6bcf8d01605&type=album https://sun9-32.userapi.com/impg/YtwMqzLei5lXp-zuTp1WTutgSMAQYpFyNuAOJg/4zDvMfz4a4k.jpg?size=564x666&quality=96&sign=1eb190a6c474250025ff4cb873ff60bf&type=album источник -Такая себе Учёба', 'https://sun9-39.userapi.com/impg/rt6OheLsYVIIrrlQEmBgf6Ainqqq8f957Enm3w/9cTlI19HuDw.jpg?size=570x726&quality=96&sign=bb792a097adfddc777e665e3c990f637&type=album https://sun9-68.userapi.com/impg/iw4y2sRreRs-qATN7fDoWQJx8gFMmj0I9KatSQ/G7ZxXxdNvsM.jpg?size=572x727&quality=96&sign=0d3a74c1ee8100568909038d64556f76&type=album источник - Такая себе учёба']
    randommeme = random.choice(memes)
    await ctx.send(randommeme)
@bot.command()
async def животноевидео(ctx): #животные
    animals = ['https://m.youtube.com/watch?v=L2BrWJ-UlzY', 'https://vk.com/video-198644058_456239936', 'https://m.youtube.com/watch?v=lApSdmMpst8', 'https://m.youtube.com/watch?v=lApSdmMpst8', 'https://m.youtube.com/watch?v=2Pa-eOU-ID0', 'https://m.youtube.com/watch?v=lo6sMZq4jvw', 'https://m.youtube.com/watch?v=6BQMU9fqLV4', 'https://m.youtube.com/watch?v=WaJuvuVARQs', 'https://m.youtube.com/watch?v=uD1YheEBORs', 'https://m.youtube.com/watch?v=0g0Ct2JHdgM', 'https://m.youtube.com/watch?v=nft43wL3vgA']
    randomanimal = random.choice(animals)
    await ctx.send(randomanimal)
@bot.command()
async def галерея(ctx):#галерея
    await ctx.send('''https://\\cdn.dribbble.com/users/974337/screenshots/2631759/pato_dribbble.gif
https://\\\\cdn.dribbble.com/users/974337/screenshots/2631759/pato_dribbble.gif
https://\\\\\\cdn.dribbble.com/users/974337/screenshots/2631759/pato_dribbble.gif
https://\\\\\\\\cdn.dribbble.com/users/974337/screenshots/2631759/pato_dribbble.gif''')
@bot.command()
async def кнопки(ctx):
    msg = await ctx.send(
        embed = discord.Embed(title = 'Это просто кнопки. Они не работают', timestamp = ctx.message.created_at),
        components = [
            Button(style = ButtonStyle.green, label = 'Зелёная'),
            Button(style = ButtonStyle.red, label = 'Красная'),
            Button(style = ButtonStyle.blue, label = 'Синяя'),
            Button(label = 'Серая')
        ])
    responce = await bot.wait_for('button_click', check = lambda message: message.author == ctx.author)
    if responce.component.label == 'Зелёная':
        await responce.respond(content = 'Тестзел')
    else:
        await responce.respond(content = 'Тесткрасн')
@bot.command() # указываем боту на то, что это его команда
async def вики(ctx, *, text):
    if text.find("@") != -1:
        await ctx.send('Пытаться пингануть кого-то с помощью бота запрещено')
    else:
        text = text.split(" ")
        print(text)
        wiki = text[0]
        print(wiki)
        page = text[1]
        print(page)
        if wiki == 'спв':
            wikiurl = 'https://fabulous-patrol.fandom.com/ru/wiki/'
        if wiki == 'цв':
            wikiurl = 'https://tsarevny.fandom.com/ru/wiki/'
        if wiki == 'щпв':
            wikiurl = 'https://paw-patrol.fandom.com/ru/wiki/'
        if wiki == 'бл':
            wikiurl = 'https://losyash-library.fandom.com/ru/wiki/'
        if wiki == 'лв':
            wikiurl = 'https://luntik.fandom.com/ru/wiki/'
        if wiki == 'лфв':
            wikiurl = 'https://luntikfanon.fandom.com/ru/wiki/'
        if wiki == 'вв':
            wikiurl = 'https://wikies.fandom.com/wiki/'
        if wiki == 'сообщ':
            wikiurl = 'https://c.fandom.com/ru/wiki/'
        if wiki == 'мыло':
            wikiurl = 'https://soap.fandom.com/wiki/'
        if wiki == 'дев':
            wikiurl = 'https://dev.fandom.com/wiki/'
        if wiki == 'тест':
            wikiurl = 'https://test.fandom.com/ru/wiki/'
        if wiki == 'бв':
            wikiurl = 'https://barboskiny.fandom.com/ru/wiki/'
        if wiki == 'пв':
            wikiurl = 'https://prostokvashino.fandom.com/ru/wiki/'
        if wiki == 'вп':
            wikiurl = 'https://ru.wikipedia.org/wiki/'
        if wiki == 'мета':
            wikiurl = 'https://meta.wikimedia.org/wiki/'
        if wiki == 'медиа':
            wikiurl = 'https://www.mediawiki.org/wiki/'
        if wiki == 'пбв':
            wikiurl = 'https://polandballru.miraheze.org/wiki/'
        if wiki == 'ншв':
            wikiurl = 'https://peopleshararam.fandom.com/ru/wiki/'
        if wiki == 'шв':
            wikiurl = 'https://shararam.fandom.com/wiki/'
        await ctx.send('<' + wikiurl + page + '>')
@bot.command() #
async def напомни(ctx, *, text):
    text = text.split(",")
    print(text)
    answer = text[0]
    print(answer)
    local_time = float(text[1])
    print(local_time)
    local_time = local_time * 60
    try:
        #time.sleep(local_time)
        # Показываем текст напоминания
        author = ctx.message.author
        #await ctx.send(author.mention + ', ' + answer)
        await ctx.send('Команда временно (то есть неизвестно сколько, может быть вечно) не работает')
    except:
        await ctx.send('Слишком большое число')
@bot.command() #
async def дзен(ctx):
    await ctx.send('''Красивое лучше, чем уродливое.
Явное лучше, чем неявное.
Простое лучше, чем сложное.
Сложное лучше, чем запутанное.
Плоское лучше, чем вложенное.
Разреженное лучше, чем плотное.
Читаемость имеет значение.
Особые случаи не настолько особые, чтобы нарушать правила.
При этом практичность важнее безупречности.
Ошибка никогда не должна замалчиваться.
Если только вы сами этого не захотите.
Встретив двусмысленность, отбрось искушение угадать.
Должен существовать один и, желательно, только один очевидный способ сделать что-то.
Хотя он поначалу может быть и не очевиден, если вы не голландец.
Сейчас лучше, чем никогда.
Хотя никогда зачастую лучше, чем прямо сейчас.
Если реализацию сложно объяснить — идея плоха.
Если реализацию легко объяснить — идея, возможно, хороша.
Пространства имён — отличная штука! Будем делать их больше!
Источник https://practicum.yandex.ru/trainer/backend-developer/lesson/ee71d9c9-bfe5-41c0-a093-12b380880136/''')
@bot.command() # указываем боту на то, что это его команда
async def фэндом(ctx, *, text):
    if text.find("@") != -1:
        await ctx.send('Пытаться пингануть кого-то с помощью бота запрещено')
    else:
        text = text.split(" ")
        print(text)
        lang = text[0]
        print(lang)
        wiki = text[1]
        print(wiki)
        page = text[2]
        print(page)
        if lang == 'en':
            lang = ''
            slash = ''
        else:
            slash = '/'
        await ctx.send(f'<https://{wiki}.fandom.com/{lang}{slash}wiki/{page}>')
@bot.command() # указываем боту на то, что это его команда
async def gamepedia(ctx, *, text):
    if text.find("@") != -1:
        await ctx.send('Пытаться пингануть кого-то с помощью бота запрещено')
    else:
        text = text.split(" ")
        print(text)
        lang = text[0]
        print(lang)
        wiki = text[1]
        print(wiki)
        page = text[2]
        print(page)
        if lang == 'en':
            lang = ''
        else:
            lang = '-' +lang
        await ctx.send(f'<https://{wiki}{lang}.gamepedia.com/{page}>')
@bot.command() # указываем боту на то, что это его команда
async def викия(ctx, *, text):
    if text.find("@") != -1:
        await ctx.send('Пытаться пингануть кого-то с помощью бота запрещено')
    else:
        text = text.split(" ")
        print(text)
        lang = text[0]
        print(lang)
        wiki = text[1]
        print(wiki)
        page = text[2]
        print(page)
        if lang == 'en':
            lang = ''
            slash = ''
        else:
            slash = '/'
        await ctx.send(f'<https://{wiki}.wikia.org/{lang}{slash}wiki/{page}>')
@bot.command() # указываем боту на то, что это его команда
async def мирахез(ctx, *, text):
    if text.find("@") != -1:
        await ctx.send('Пытаться пингануть кого-то с помощью бота запрещено')
    else:
        text = text.split(" ")
        print(text)
        wiki = text[0]
        print(wiki)
        page = text[1]
        print(page)
        await ctx.send(f'<https://{wiki}.miraheze.org/wiki/{page}>')
@bot.command() # указываем боту на то, что это его команда
async def shoutwiki(ctx, *, text):
    if text.find("@") != -1:
        await ctx.send('Пытаться пингануть кого-то с помощью бота запрещено')
    else:
        text = text.split(" ")
        print(text)
        wiki = text[0]
        print(wiki)
        page = text[1]
        print(page)
        await ctx.send(f'<https://{wiki}.shoutwiki.com/wiki/{page}>')
@bot.command() # указываем боту на то, что это его команда
async def поиск(ctx, *, text):
    text = text.split(" ")
    lang =  text[0]
    print(lang)
    url = text[1]
    print(url)
    query = text[2]
    print(query)
    if lang == "en":
        lang = ''
        slash = ''
    else:
        slash = '/'
    await ctx.send(f'<https://{url}.fandom.com/{lang}{slash}wiki/Special:Search?query={query}&scope=internal>')
@bot.command() # указываем боту на то, что это его команда
async def поискобс(ctx, *, text):
    text = text.split(" ")
    lang =  text[0]
    print(lang)
    url = text[1]
    print(url)
    query = text[2]
    print(query)
    if lang == "en":
        lang = ''
        slash = ''
    else:
        slash = '/'
    await ctx.send(f'<https://{url}.fandom.com/{lang}{slash}wiki/Special:Search?scope=internal&query={query}&contentType=posts>')
@bot.command() # указываем боту на то, что это его команда
async def календарь(ctx, *, text):
    text = text.split(",")
    print(text)
    year = int(text[0])
    print(year)
    month = int(text[1])
    print(month)
    await ctx.send(calendar.month(year, month))
    #сейчас
@bot.command() # указываем боту на то, что это его команда
async def сейчас(ctx):
    dt = DT.datetime.now()
    print(dt)
    print(dt.timestamp())
    await ctx.send(f'<t:{int(dt.timestamp())}>')
@bot.command() # указываем боту на то, что это его команда
async def время(ctx, *, text):
    if text.find("@") != -1:
        await ctx.send('Пытаться пингануть кого-то с помощью бота запрещено')
    else:
        text = text.split("/")
        print(text)
        time = text[0]
        print(time)
        zone = int(text[1])
        zone = zone - 3
        try:
            dt = DT.datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
            print(dt)
            dt = dt.timestamp()
            print(dt)
            dt = dt + zone * 3600
            await ctx.send(f'<t:{int(dt)}>')
        except:
            await ctx.send('Поздравляю, вы чуть не сломали бота! Но мой програмист предусмотрел это!')
@bot.command() # указываем боту на то, что это его команда
async def спойлер(ctx, *, text):
    if text.find("@") != -1:
        await ctx.send('Пытаться пингануть кого-то с помощью бота запрещено')
    else:
        await ctx.send(f'||{text}||')
@bot.command() # указываем боту на то, что это его команда
async def кодполе(ctx, *, text):
    if text.find("@") != -1:
        await ctx.send('Пытаться пингануть кого-то с помощью бота запрещено')
    else:
        text = text.split("/")
        print(text)
        lang = text[0]
        print(lang)
        code = text[1]
        print(code)
        await ctx.send(f'''```{lang}
{code}```''')
        await ctx.send('Внимание, команда может работать некорректно!')
@bot.command() # указываем боту на то, что это его команда
async def курсив(ctx, *, text):
    if text.find("@") != -1:
        await ctx.send('Пытаться пингануть кого-то с помощью бота запрещено')
    else:
        await ctx.send(f'*{text}*')
@bot.command() # указываем боту на то, что это его команда
async def зачёркнутый(ctx, *, text):
    if text.find("@") != -1:
        await ctx.send('Пытаться пингануть кого-то с помощью бота запрещено')
    else:
        await ctx.send(f'~~{text}~~')
@bot.command() # указываем боту на то, что это его команда
async def подчёркнутый(ctx, *, text):
    if text.find("@") != -1:
        await ctx.send('Пытаться пингануть кого-то с помощью бота запрещено')
    else:
        await ctx.send(f'__{text}__')
@bot.command() # указываем боту на то, что это его команда
async def число(ctx, *, num):
    num = int(num)
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    randomnum = random.choice(nums)
    if num == randomnum:
        await ctx.send('Правильно, вы угадали!')
    else:
        await ctx.send(f'А вот и нет, я загадал число {randomnum}')
@bot.command() # указываем боту на то, что это его команда
async def кнб(ctx):
    items = ['Камень', 'Ножницы', 'Бумага']
    useritem = random.choice(items)
    botitem = random.choice(items)
    if useritem == 'Камень':
        if botitem == 'Камень':
            await ctx.send('У меня камень и у тебя камень! Ничья!')
        if botitem == 'Ножницы':
            await ctx.send('У меня ножницы, а у тебя камень! Ты победил!')
        if botitem == 'Бумага':
            await ctx.send('У меня бумага, а у тебя камень! Я победил!')
    if useritem == 'Ножницы':
        if botitem == 'Камень':
            await ctx.send('У меня камень, а у тебя ножницы! Я победил!')
        if botitem == 'Ножницы':
            await ctx.send('У меня ножницы и у тебя ножницы! Ничья!')
        if botitem == 'Бумага':
            await ctx.send('У меня бумага, а у тебя ножницы! Ты победил!')
    if useritem == 'Бумага':
        if botitem == 'Камень':
            await ctx.send('У меня камень, а у тебя бумага! Ты победил!')
        if botitem == 'Ножницы':
            await ctx.send('У меня ножницы, а у тебя бумага! Я победил!')
        if botitem == 'Бумага':
            await ctx.send('У меня бумага и у тебя бумага! Ничья!')
@bot.command() # указываем боту на то, что это его команда
async def питон(ctx):
    pythons = ['https://proprikol.ru/wp-content/uploads/2020/11/kartinki-pitony-42.jpg', 'https://web-zoopark.ru/wp-content/uploads/2018/06/8-123.jpg', 'https://techrocks.ru/wp-content/uploads/2020/01/animal-wildlife-portrait-green-botany-reptile-771261-pxhere.com-min.jpg', 'https://studychinese.ru/content/dictionary/pictures/26/13309.jpg', 'https://irecommend.ru/sites/default/files/product-images/529225/lxlDWbQMyzdDPMKf5nQ.jpg', 'https://avatars.mds.yandex.net/get-zen_doc/2993437/pub_60003582dc0ac42b28a7db7b_6000365e4e913f1758296a6c/scale_1200', 'https://avatars.mds.yandex.net/get-zen_doc/112297/pub_60fd3f43caa93609b6079429_60fd3f52237ef804672bc967/scale_1200', 'https://proprikol.ru/wp-content/uploads/2020/11/kartinki-pitony-10.jpg']
    randompython = random.choice(pythons)
    embed = discord.Embed(title = 'Питон', description = '''
Если вы питонист, вы можете поставить этого питона в свою командную строку, а точнее в эмулятор командной строки conemu.
Скачать conemu ||<https://www.fosshub.com/ConEmu.html?dwl=ConEmuSetup.210912.exe>||
Если вы не питонист, вы можете попробовать бесплатные вводные курсы от Яндекс. Практикума ||<https://practicum.yandex.ru/profile/backend-developer/>||
Ну или посмотреть обучающее видео от Хауди Хо ||<https://www.youtube.com/watch?v=fp5-XQFr_nk>||
Впрочем, если вам не даётся Питон, не расстраивайтесь. Есть много интересных профессий, как в айти (дизайнеры) так и не в айти.''')
    embed.set_image(url = randompython)
    await ctx.send(embed = embed)
@bot.command() # указываем боту на то, что это его команда
async def жаба(ctx):
    toads = ['https://attuale.ru/wp-content/uploads/2018/07/6320.jpg', 'https://krasivosti.pro/uploads/posts/2021-09/1631067050_33-krasivosti-pro-p-zhaba-v-stringakh-zhivotnie-krasivo-foto-35.jpg', 'https://a.d-cd.net/e4AAAgCw3OA-1920.jpg', 'https://imya-sonnik.ru/wp-content/uploads/2019/10/s1200-2020-06-03t094632.632.jpg', 'https://animalreader.ru/wp-content/uploads/2015/12/seraja-zhaba-ili-obyknovennaja-samaja-krupnaja-sredi-evropejskih-zhab-animal-reader.ru-.jpg', 'https://get.pxhere.com/photo/nature-wildlife-macro-frog-toad-amphibian-fauna-close-up-animals-vertebrate-naturaleza-ggl1-gaby1-animales-bufobufo-canon550d-sapocom-n-bullfrog-ranidae-408011.jpg']
    randomtoad = random.choice(toads)
    embed = discord.Embed(title = 'Жаба', description = '''
Это - жаба. Точнее жабаскрипт! (Шутка!)
Жабаскипт, это шуточное завание языка программирования javascript (джаваскрипт).
Этот язык в соновном используют во фронтенд-веб разработке. Но его можно использовать и для бэкенда - в Node.js
Если вы жабаскиптер, вы можете поставить эту жабу в свою командную строку, а точнее в эмулятор командной строки conemu.
Скачать conemu ||<https://www.fosshub.com/ConEmu.html?dwl=ConEmuSetup.210912.exe>||
Если вы не джаваскриптер, не расстраивайтесь - вот учебник от Ильи Кантора ||<https://learn.javascript.ru/>||
Впрочем, если вам не даётся Жабаскипт, не расстраивайтесь. Есть много интересных профессий, как в айти (дизайнеры) так и не в айти.''')
    embed.set_image(url = randomtoad)
    await ctx.send(embed = embed)
@bot.command()
async def слон(ctx):
    elephants = ['https://web-zoopark.ru/wp-content/uploads/2018/11/1-108.jpg', 'https://vsezhivoe.ru/wp-content/uploads/2017/09/maxresdefault-6.jpg', 'https://static.360tv.ru/media/article_media/da8c564405db404cb515901435aab39c_201702111927.jpg', 'https://fb.ru/misc/i/gallery/54934/2490533.jpg', 'https://cepia.ru/images/u/pages/1412/5.jpg', 'https://kipmu.ru/wp-content/uploads/slnprvtstv-scaled.jpg', 'https://kot-pes.com/wp-content/uploads/2018/11/post_5be870b5c338c.jpg']
    randomelephant = random.choice(elephants)
    embed = discord.Embed(title = 'Слон', description = '''
Это - слон. Символ языка програмирования PHP.
Именно но PHP написаны такие сайты, как Википедия, ФЭНДОМ (все знают про Фэндом?), Абсурдопедия и Вордпресс.
Если вы PHP-ер, вы можете поставить этого слона в свою командную строку, а точнее в эмулятор командной строки conemu.
Скачать conemu ||<https://www.fosshub.com/ConEmu.html?dwl=ConEmuSetup.210912.exe>||
Если вы не PHP-ер, не расстраивайтесь, изучать PHP можно на сайте ||<https://www.php.net/tutorial>||
Впрочем, если вам не даётся PHP, не расстраивайтесь. Есть много интересных профессий, как в айти (дизайнеры) так и не в айти.''')
    embed.set_image(url = randomelephant)
    await ctx.send(embed = embed)
@bot.command() # указываем боту на то, что это его команда
async def ява(ctx):
    java = ['island', 'coffe', 'bike', 'kotlin', 'js']
    randomitem = random.choice(java)
    if randomitem == 'island':
        embed = discord.Embed(title = 'Остров Ява', description = '''
Это - остров ява, в честь которого было названо кофе в честь котрого назван язык программирования джава.
Если вы программируете на яве, то есть на джваве, вы можете поставить эту фотку в свою командную строку, а точнее в эмулятор командной строки conemu.
Скачать conemu ||<https://www.fosshub.com/ConEmu.html?dwl=ConEmuSetup.210912.exe>||''')
        islands = ['https://toursbali.ru/wp-content/uploads/2021/04/ostrov-yava.jpg', 'https://www.tripsoul.ru/Destinations/IMG_Asia/Indonesia/The-Beaches-Of-Java/TheBeachesOfJava_02.jpg', 'http://safari-tour.su/wp-content/uploads/2017/11/YAva-ostrov.jpg', 'https://indonesia.su/wp-content/uploads/2021/01/vulkan.jpg']
        randomisland = random.choice(islands)
        embed.set_image(url = randomisland)
    if randomitem == 'coffe':
        embed = discord.Embed(title = 'Кофе Ява', description = '''
Это - кофе ява, в честь которого назван язык программирования джава.
Если вы программируете на яве, то есть на джваве, вы можете поставить эту фотку в свою командную строку, а точнее в эмулятор командной строки conemu.
Скачать conemu ||<https://www.fosshub.com/ConEmu.html?dwl=ConEmuSetup.210912.exe>||''')
        embed.set_image(url = 'https://about-tea.ru/wp-content/uploads/9/6/6/966cabf494fbdc244ae0a465de40f308.jpeg')
    if randomitem == 'js':
        embed = discord.Embed(title = 'Джава', description = '''
А это вовсе не джава, а джаваскрипт. На нём в соновном пишут веб-страницы вместе с html и css. Смотри не перепутай :wink:''')
        embed.set_image(url = 'https://software.3metas.com/wp-content/uploads/2014/04/javascript6-compressed.jpg')
    if randomitem == 'bike':
        embed = discord.Embed(title = 'Мотоцикл Ява', description = '''
Это - мотоцикл ява, который назван в честь острова ява, в честь которого названо кофе ява, в в честь котрого назван язык программирования джава.
Если вы программируете на яве, то есть на джваве, вы можете поставить эту фотку в свою командную строку, а точнее в эмулятор командной строки conemu.
Скачать conemu ||<https://www.fosshub.com/ConEmu.html?dwl=ConEmuSetup.210912.exe>||''')
        embed.set_image(url = 'https://s2.usedcars.ru/photos/2018/10/1280x1024/15400302044358.jpg')
    if randomitem == 'kotlin':
        embed = discord.Embed(title = 'Джава', description = '''
А это вовсе не джава, а котлин. На нём в соновном разрабатывают под андроид. Смотри не перепутай :wink:
Кстати, язык программирования kotlin назван в честь острова котлин в Санкт-Петербурге, который на картинке.
Если вы программируете на яве, то есть на джваве, то есть на котлине, вы можете поставить эту фотку в свою командную строку, а точнее в эмулятор командной строки conemu.
Скачать conemu ||<https://www.fosshub.com/ConEmu.html?dwl=ConEmuSetup.210912.exe>||''')
        kotlins = ['https://avatars.mds.yandex.net/get-zen_doc/34175/pub_5cb390045d901500b31a69e5_5cb4ba13eb4c5d00b3cb323d/scale_1200', 'https://avatars.mds.yandex.net/get-zen_doc/1584427/pub_5e59b4dbf9af6a13103b30b0_5e59b54b669c1f78da921bb0/scale_1200', 'https://avatars.mds.yandex.net/get-zen_doc/3855260/pub_5f6363f06f388e770c91d1ca_5f64910361cbe322d96a80cd/scale_1200', 'https://img-fotki.yandex.ru/get/6519/47953450.5a/0_a139e_d77704c3_XXXL.jpg']
        randomkotlin = random.choice(kotlins)
        embed.set_image(url = randomkotlin)
    await ctx.send(embed = embed)
@bot.command()
async def смешарики(ctx):
    await ctx.send('''<https://losyash-library.fandom.com/ru/wiki/Служебная:Случайная_страница/Файл>
Поскольку из-за Кэша дискорд выдаёт всё время одну и туже картинку, вам придётся перейти по ссылке, чтобы каждый раз видеть разные картинки''')
@bot.command()
async def рептилоид(ctx): #рептилии
    reptilias = ['https://cdn.pixabay.com/photo/2017/05/29/20/44/reptile-2354834_1280.jpg', 'https://cherepah.ru/wp-content/uploads/9/d/9/9d9edf475db6e1708c3380bf79791a44.jpeg', 'https://www.1zoom.ru/big2/412/292436-alexfas01.jpg', 'https://aquariumsystems.su/images/osv-3.jpg', 'https://cdn.pixabay.com/photo/2019/09/28/21/43/lizard-4511852_960_720.jpg', 'https://krasivosti.pro/uploads/posts/2021-09/1630953184_8-krasivosti-pro-p-mini-yashcheritsi-zhivotnie-krasivo-foto-9.jpg', 'https://i.pinimg.com/originals/03/66/33/036633c918aadf2b9d017cb877391d3a.jpg', 'https://krasivosti.pro/uploads/posts/2021-06/1623373690_24-krasivosti_pro-p-reptilii-zhivotnie-krasivo-foto-27.jpg']
    reptilia = random.choice(reptilias)
    await ctx.send(reptilia)
@bot.command() # указываем боту на то, что это его команда
async def выбрать(ctx, *, text):
    if text.find("@") != -1:
        await ctx.send('Пытаться пингануть кого-то с помощью бота запрещено')
    else:
        text = text.split(",")#всё равно получаем массив, даже если элемент всего один
        print(text)
        if len(text)  != 1: #проверка, состоит ли массив из одного элемента
            await ctx.send( random.choice (text) )
        else:
            text = text[0].split(" ")#Если массив состоит из одного элемента, то обращаемся к первому ([0]) элементу
            print(text)
            if len(text)  != 1:
                await ctx.send( random.choice (text) )
            else:
                await ctx.send('Введите минимум два элемента, разделённых пробелом или запятой')
@bot.command()
async def монетка(ctx):
    coins = ['орёл', 'решка']
    coin = random.choice(coins)
    await ctx.send(coin)
#сообщения об ошибках
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(f'{ctx.author.mention}, данной команды не существует.')
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Введите один или несколько аргуметов")
    else:
        raise error
@bot.command()
async def стоп(ctx):
    await ctx.send('Выключаюсь')
    print('Выключаюсь')
    exit()
@bot.command()
async def сообщить(ctx, *, text):
    text = text.split(" ")
    print(text)
    print(len(text))
    if len(text) == 1:
        link = text[0]
        reason = "Отсутсвует"
    elif len(text) == 2:
        reason = text[0]
        print(reason)
        link = text[1]
    else:
        await ctx.send('Ошибка1')
    link = link.split("/")
    print(link)
    #https://fanonsmesh.fandom.com/ru/wiki/Служебная:Вклад/Ekulabukhova
    domain = link[2]
    print(domain)
    domain = domain.split('.')
    wikiurl = domain[0]
    print(wikiurl)
    lang = link[3]
    if lang == 'wiki':
        lang = 'en'
    if lang == 'f':
        await ctx.send('Ошибка2')
    print(lang)
    userinfo = link[len(link)-1]
    print(userinfo)
    if userinfo.find(":") != -1:
        userinfo = userinfo.split(':')
        user = userinfo[1]
    else:
        user = userinfo
    print(user)
    await ctx.send(f'''Причина сообщения: {reason}
    Nameofwiki: {wikiurl}
    Язык: {lang}
    Имя участника: {user}''')
'''@bot.command() # указываем боту на то, что это его команда
async def викитекст(ctx, *, text):
    if text.find("@") != -1:
        await ctx.send('Пытаться пингануть кого-то с помощью бота запрещено')
    else:
        parsed = wtp.parse(text)
        await ctx.send(parsed)'''
bot.run('вставье сюда ваш токен') # Обращаемся к словарю settings с ключом token, для получения токена

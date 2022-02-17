# -*- coding: utf-8 -*-
import discord #импортируем библиотеки
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle
import requests
import random
import datetime as DT
import time
import calendar

settings = {#параметры бота
    'token': 'вставьте сюда ваш токен',
    'bot': 'ДивноГорьеБот',
    'id': вставьте сюда id бота вез кавычек,
    'prefix': 'див!'
}

bot = commands.Bot(command_prefix = "див!")

@bot.command() # Привет
async def привет(ctx): # Создаём функцию и передаём аргумент ctx.
    author = ctx.message.author # Объявляем переменную author и записываем туда информацию об авторе.
    await ctx.send(f'Привет, {author.mention}!') # Выводим сообщение с упоминанием автора, обращаясь к переменной author.
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
async def помощники(ctx):#Русские помощники
    await ctx.send('Kuzura (сотрудник), Natalya-ru (Дизайн, css), Arhhhat (ARC, js, css), Katuwa (Аниме), Cryosleep')
@bot.command()
async def русотр(ctx):#Русские сотрудники
    await ctx.send('Kuzura (помощник), Vlazovskiy (раньше)')
@bot.command()#Бывшие русские помощники
async def бывшпомощники(ctx):
    await ctx.send('PavelShepard, Kopcap94 (VSTF, council, vanguard), Idel sea Qatarhael, Fiona of Amber (Эскадра), Новак и другие')
@bot.command() #Википроекты, шде зарегистрирован Антаркт
async def анатрктвики(ctx):
    await ctx.send('Википедия, Фэндом, Викиреальность и Мирахез')
@bot.command() #Вики, где Антаркт админ
async def анатрктадмин(ctx):
    await ctx.send('''<https://tsarevny.fandom.com/ru> _- Царевны вики
<https://paw-patrol.fandom.com/ru> - Щенячий Патруль вики (-ru)
<https://test.fandom.com/ru> - тест вики
и другие''')
@bot.command()
async def мир(ctx): #Мир вам, добрые люди
    print('Мир вам, добрые люди')
@bot.command()
async def fandomkuzura(ctx): #Фэндом, Кузура и поддержка
    await ctx.send('''<https://ru.fandom.com> - главная страница
<https://c.fandom.com/ru> - Вики Сообщества
<https://c.fandom.com/ru/wiki/Участник:Kuzura> - Kuzura
<https://c.fandom.com/ru/wiki/Стена_обсуждения:Kuzura> - Стена Кузуры
<https://support.fandom.com/hc/ru> - поддержка''')
@bot.command()
async def gamepedianotkuzura(ctx): #Gamepedia
    await ctx.send('Геймпедии больше нет, её купил Фэндом')
@bot.command()
async def wikiakuzurza(ctx): #Wikia.org
    await ctx.send('Викии.орг больше нет, её перенесли на Фэндом')
@bot.command()
async def царевны(ctx): #Царевны
    await ctx.send('''<https://tsarevny.ru> - сайт
<https://www.youtube.com/tsarevny> - YouTube
<https://vk.com/tsarevny.official> - VK
<https://tsarevny.fandom.com/ru> - вики
<https://vk.com/tsarevna_ask> - ASK Царевны''')
@bot.command()
async def антартктпроекты(ctx):#Проекты Антаркта
    await ctx.send('''<https://test.fandom.com/ru/wiki/MediaWiki:FayryNetMobile.css>
<https://test.fandom.com/ru/wiki/MediaWiki:MinecraftRevived.css>
<https://test.fandom.com/ru/wiki/MediaWiki:Wikia.orgFandomMobileColors.css>
<https://test.fandom.com/ru/wiki/MediaWiki:DiscordCosmos.css>
<https://test.fandom.com/ru/wiki/MediaWiki:NewFandomColorsCosmos.css>
<https://test.fandom.com/ru/wiki/MediaWiki:OldFandomColorsCosmos.css>
<https://test.fandom.com/ru/wiki/MediaWiki:NedoUCXCosmos.css>
<https://test.fandom.com/ru/wiki/MediaWiki:UCXDiscussions.css>
<https://test.fandom.com/ru/wiki/MediaWiki:VectorDiscord.css>
<https://test.fandom.com/ru/wiki/MediaWiki:DiscordMobileTheme.css>
<https://test.fandom.com/ru/wiki/MediaWiki:OldGlobalNavMobile.css>
<https://test.fandom.com/ru/wiki/MediaWiki:OldGamepediaGlobalNavMobile.css>
<https://tsarevny.fandom.com/ru/wiki/MediaWiki:DarkMobile.css>
<https://tsarevny.fandom.com/ru/wiki/MediaWiki:LightMobile.css>
<https://fabulous-patrol.fandom.com/ru/wiki/MediaWiki:DarkMobile.css>
<https://fabulous-patrol.fandom.com/ru/wiki/MediaWiki:LightMobile.css>''')
@bot.command()
async def инфо(ctx): #Информация о боте
    await ctx.send('Автор бота - Антаркт#5225. Версия Питона - 3.9.7. Использована библиотека discord.py. Отдельное спасибо kotenok gav#8521 и Fluttershy#7152 (Strangedude123/Снежок Сказочника) за помощь в установке библиотеки и исправлении багов. А также спасибо Black Spaceship за то, что вдохновил автора на написание бота и Ядекс. Практикуму за обучение автора. Также спасибо папиному знакомому Максиму за помощь в установке питона на другой компьютер')
@bot.command()
async def анекдот(ctx): #Мама, можно мне питон?
    await ctx.send(''' - Moom, can we have python?
- No, we have python at home
At home: Пшшшшшшш''')
@bot.command()
async def сервер(ctx): #Сервер поддержки бота
    await ctx.send('вставьте сюда ссылку на сервер бота')
@bot.command()
async def код(ctx): #Код бота
    await ctx.send('<https://github.com/Antarktidov/AntarktBot/blob/main/AntarkBot.py>')
@bot.command()
async def бот(ctx): #Чего
    whatbotanswers = ['Чего?', 'А кто же ещё', 'Да, я бот', 'А вот щас обидно было', 'приём, приём, как слышно']
    whatbotanswer = random.choice(whatbotanswers)
    await ctx.send(whatbotanswer)
@bot.command()
async def утка(ctx): #Утки
    ducks = ['https://cdn.pixabay.com/photo/2017/02/01/00/31/duck-2028587_1280.jpg', 'https://s.go31.ru/section/catalogpagesintext/upload/images/catalog/intext/000/052/452/kupit-utku_5f435b652c525.jpg', 'https://masslandlords.net/wp-content/uploads/sex-based-discrimination-image-licensed-Pixabay-1536x826.jpg', 'https://stroy-podskazka.ru/images/article/orig/2019/04/skolko-zhivut-utki-i-ot-chego-eto-zavisit.jpg', 'https://mota.ru/upload/resize/1280/1024/upload/wallpapers/source/2016/06/16/20/01/48977/mota.ru_2016061628-b17.jpg', 'https://i.ytimg.com/vi/hJLaqQLVKhw/maxresdefault.jpg', 'https://moydom.moscow/wp-content/uploads/2020/05/2020-05-15-13-43-35.jpg', 'https://cdn.pixabay.com/photo/2021/06/16/21/46/ducklings-6342270_1280.jpg', 'https://cdn.fishki.net/upload/post/2017/05/04/2282681/dffed465d0896b77c479704c2abe7da6.jpg', 'https://avatars.mds.yandex.net/get-zen_doc/1921148/pub_5f8df42b75135c199900abf2_5f8df43975135c199900bde4/scale_1200', 'https://avatars.mds.yandex.net/get-zen_doc/1712062/pub_5fe600850d0c7759ac79521f_5fe600a9e5cdbc6a96b5b214/scale_1200', 'https://img-fotki.yandex.ru/get/6104/127683550.1d/0_116c81_cf72adf1_XXXL.jpg']
    duckimage = random.choice(ducks)
    await ctx.send(duckimage)
@bot.command()
async def пригласить(ctx): #Пригласить бота
    await ctx.send('Используйте эту ссылку, чтобы пригласить меня на ваш сервер <вставьте сюда приглашение бота>')
@bot.command()
async def да(ctx): #Да
    await ctx.send('А у тебя есть борода?')
@bot.command()
async def нет(ctx): #Нет
    netanswers = ['Ты мне достался на обед!', 'Откуда взялся интернет!']
    netanswer = random.choice(netanswers)
    await ctx.send(netanswer)
@bot.command()
async def yes(ctx): #Yes
    await ctx.send('Yes, yes... ОБХСС! - Джентельмены удачи')
@bot.command()
async def цитата(ctx): #Цитаты
    quotes = ['Есть только один русский сотрудник, Kuzura - TokihikoH11', 'Engslish please in #general. - MisterWoodhause', 'Создавать вики для вандалов - это как покупать шубу для моли. ParaNormanBates', 'Шв - крутая вики - Липчанин', 'Тсоре над нами, мы -швиане']
    randomquote = random.choice(quotes)
    await ctx.send(randomquote)
@bot.command()
async def скин(ctx): #Скин
    skins = ['FandomDesktop', 'FandomMobile', 'Vector', 'DarkVector', 'Oasis', 'Wikia', 'WIkiaMobile', 'Minerva', 'Hydra', 'HydaraDark']
    randomskin = random.choice(skins)
    await ctx.send(randomskin)
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
async def on_ready(): #Статус
     await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Царевны, Сказочный Патруль"))
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
    await ctx.send('Поверье мне, я полностью работоспособен!')
@bot.command()
async def викиаккаунт(ctx): #вики
    await ctx.send('''Мой аккаунт на вики:
<https://tsarevny.fandom.com/ru/wiki/Участник:ДивноГорьеБот> - Царевны вики. Имею статус бота и администратора, но на самом деле мной управляет Антаркт. Руками. Именно мне выпала честь однажны поздравить всех с первым апреля.
<https://fabulous-patrol.fandom.com/ru/wiki/Участник:ДивноГорьеБот> - Сказочный Патруль вики. Имею только заполненный профайл.
<https://feerinki.fandom.com/ru/wiki/Участник:ДивноГорьеБот> - Фееринки вики. С помощью меня Антаркт руками проставлял шаблон.
<https://test.fandom.com/ru/wiki/Участник:ДивноГорьеБот> - тестовый аккаунт Антарта. Имею права бюрократа и администратора.''')
@bot.command()
async def практикум(ctx): #Курсы
    await ctx.send('''Курсы Антарта на Яндекс. Практикуме:
Веб-разработчик (бесплатная часть пройдена)
Дизайнер интерфейсов (бесплатная часть пройдена)
Питон-разработчик (бесплатная часть пройдена)
C ++ разработчик (в процессе)''')
@bot.command() # Основной
async def основной(ctx):
    await ctx.send('Эта беседа должна быть продолжена в #основной')
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
#языки программирования и не только
@bot.command()
async def русский(ctx): #русский
    await ctx.send('Да,а разговариваю по-русски')
@bot.command()
async def english(ctx): #english
    await ctx.send('Извините,я не разговариваю по-английски. Почти')
@bot.command()
async def python(ctx): #python
    await ctx.send('Да, я разговариваю на питоне')
@bot.command()
async def сиплюсплюс(ctx): #C++
    await ctx.send('Извините, я не разговариваю на C++')
@bot.command()
async def php(ctx): #php
    await ctx.send('Извините, я не разговариваю на php')
@bot.command()
async def java(ctx): #java
    await ctx.send('Это вам не javascript')
@bot.command()
async def javascript(ctx): #javascript
    await ctx.send('Это вам не java')
@bot.command()
async def мышеловка(ctx): #мышеловка
    text = input()
    await ctx.send(text)
@bot.command()
async def кодеры(ctx):#Кодеры
    await ctx.send('''Александр III(также известен как Hummel009) - CSS, Java (minecfraft), Kopcap94(CSS, JavaScript, Ruby), BlackSpaceship (Питон), Не кочан (Также известен как IvanovVN, Vonavy) (JavaScript), Natalya-ru (CSS), Arhhhat (раньше был ник на санскрите), (CSS, Javascript), Kotgav (html, CSS, JavaScript, php, Python)
Если кого-то нет в списке, напишите владельцу бота - добавлю.''')
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
    if responce.component.label == 'Да':
        await responce.respond(content = 'Тестда')
    else:
        await responce.respond(content = 'Тестнет')
@bot.command() # указываем боту на то, что это его команда
async def вики(ctx, *, text):
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
        time.sleep(local_time)
        # Показываем текст напоминания
        author = ctx.message.author
        await ctx.send(author.mention + ', ' + answer)
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
    text = text.split(" ")
    print(text)
    wiki = text[0]
    print(wiki)
    page = text[1]
    print(page)
    await ctx.send(f'<https://{wiki}.miraheze.org/wiki/{page}>')
@bot.command() # указываем боту на то, что это его команда
async def shoutwiki(ctx, *, text):
    text = text.split(" ")
    print(text)
    wiki = text[0]
    print(wiki)
    page = text[1]
    print(page)
    await ctx.send(f'<https://{wiki}.shoutwiki.com/wiki/{page}>')
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
bot.run('вставье сюда ваш токен') # Обращаемся к словарю settings с ключом token, для получения токена

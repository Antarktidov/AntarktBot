# -*- coding: utf-8 -*-
import discord #импортируем библиотеки
from discord.ext import commands
import requests
import random
#Погода
url = 'https://wttr.in'

weather_parameters = {
    '0': '',
    'T': '',
    'M': '',
}

request_headers = {
    'Accept-Language': 'ru'
}
response = requests.get(url, headers=request_headers, params=weather_parameters)#Погода в командную строку
print(response.text)
settings = {#параметры бота
    'token': 'вставьте сюда ваш токе',
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
async def погода(ctx): # Погода
    response = requests.get(url, headers=request_headers, params=weather_parameters)
    await ctx.send(response.text)
@bot.command()
async def помощники(ctx):#Русские помощники
    await ctx.send('Kuzura (сотрудник), Natalya-ru (Дизай, css), Arhhhat (ARC, js, css), Katuwa (Аниме), Cryosleep')
@bot.command()
async def русотр(ctx):#Русские сотрудники
    await ctx.send('Kuzura (помощник), Vlazovskiy (раньше)')
@bot.command()#Бывшие русские помощники
async def бывшпомощники(ctx):
    await ctx.send('PavelShepard, Kopcap94 (VSTF, council, vanguard), Idel sea Qatarhael и другие')
@bot.command() #Википроекты, шде зарегистрирован Антаркт
async def анатрктвики(ctx):
    await ctx.send('Википедия, Фэндом, Викиреальность и Мирахез')
@bot.command() #Вики, где Антаркт админ
async def анатрктадмин(ctx):
    await ctx.send('''<https://tsarevny.fandom.com/ru> _- Царевны вики
<https://fabulous-patrol.fandom.com/ru> - Сказочный Патруль вики
<https://paw-patrol.fandom.com/ru> - Щенячий Патруль вики (-ru)
<https://test.fandom.com/ru> - тест вики
и другие''')
@bot.command()
async def мир(ctx): #Мир вам, добрые люди
    print('Мир вам, добрые люди')
@bot.command()
async def fandom(ctx): #Фэндом, Кузура и поддержка
    await ctx.send('''<https://ru.fandom.com> - главная страница
<https://c.fandom.com/ru> - Вики Сообщества
<https://c.fandom.com/ru/wiki/Участник:Kuzura> - Kuzura
<https://c.fandom.com/ru/wiki/Стена_обсуждения:Kuzura> - Стена Кузуры
<https://support.fandom.com/hc/ru> - поддержка''')
@bot.command()
async def gamepedia(ctx): #Gamepedia
    await ctx.send('Геймпедии больше нет, её купил Фэндом')
@bot.command()
async def wikia(ctx): #Wikia.org
    await ctx.send('Скоро викиюорг объеденят с Фэндомом')
@bot.command()
async def царевны(ctx): #Царевны
    await ctx.send('''<https://tsarevny.ru> - сайт
<https://www.youtube.com/tsarevny> - YouTube
<https://vk.com/tsarevny.official> - VK
<https://tsarevny.fandom.com/ru> - вики
<https://vk.com/tsarevna_ask> - ASK Царевны''')
@bot.command()
async def антартктпроекты(ctx):#Проекты Антпаркта
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
    await ctx.send('Автор бота - Антаркт#5225. Версия Питона - 3.9.7. Использована библиотека discord.py. Отдельное спасибо kotenok gav#8521 и Fluttershy#7152 (Strangedude123/Снежок Сказочника) за помощь в установке библиотеки и исправлении багов. А также спасибо Black Spaceship за то, что вдохновил автора на написание бота и Ядекс. Практикуму за обучение автора')
@bot.command()
async def анекдот(ctx): #Мама, можно мне питон?
    await ctx.send(''' - Moom, can we have python?
 - No, we have python at home
At home: Пшшшшшшш''')
@bot.command()
async def сервер(ctx): #Сервер поддержки бота
    await ctx.send('вставьте сбда ссылку на ваш сервер')
@bot.command()
async def код(ctx): #Код бота
    await ctx.send('<https://test.fandom.com/ru/wiki/AntarktBot.py>')
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
    await ctx.send('Используйте эту ссылку, чтобы пригласить меня на ваш сервер <вставьте сюда ссылку-приглашение бота>')
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
async def печенье(ctx): #Это на Новый год, не трогайте!
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
- Если кодить в визуал студио, то питон не будет поддерживать кириллицу
- Невозможно создать команду bot.
- Библиотека discord.py не поддерживает слэш-команды''')
@bot.command()
async def тест(ctx): #Тест
    await ctx.send('Поверье мне, я полностью работоспособен!')
@bot.command()
async def вики(ctx): #вики
    await ctx.send('''Мой аккаунт на вики:
<https://tsarevny.fandom.com/ru/wiki/Участник:ДивноГорьеБот> - Царевны вики. Имею статус бота и администратора, но на самом деле мной управляет Антаркт. Руками. Именно мне выпала честь однажны поздравить всех с первым апреля.
<https://fabulous-patrol.fandom.com/ru/wiki/Участник:ДивноГорьеБот> - Сказочный Патруль вики. Имею только заполненный профайл.
<https://feerinki.fandom.com/ru/wiki/Участник:ДивноГорьеБот> - Фееринки вики. С помощью меня Антаркт руками прпоставлял шаблон.
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

bot.run('вставье сюда ваш токен') # Обращаемся к словарю settings с ключом token, для получения токена

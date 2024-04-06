from writing9.band import Band

band_list = [0.5*i for i in range(1, 19)]
pages = 10 #2

with open('./data/links2.txt', 'a') as f:
    for band in band_list:
        for page in range(2, pages):
            with Band() as bot:
                try:
                    bot.land_page(band, page)
                    res = bot.pull_all_essay_on_page()
                    for link in res:
                        f.write(link+'\n')
                except:
                    bot.quit()
                    continue
print('done')
    
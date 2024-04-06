from writing9.essay import Essay
import pandas as pd
from tqdm import tqdm

with open('./data/links.txt', 'r') as f:
    links =[link[:-1] for link in f.readlines()]
    
data = []
for link in tqdm(links[489:]):
    with Essay(link=link) as bot:
        try:
            bot.land_page()
            res = bot.essay_details()
            data.append(res)
            pd.DataFrame(data).to_csv('data/ielts2.csv')
        except:
            bot.quit()
            continue
# pd.DataFrame(data).to_csv('data/ielts.csv')
print('done')

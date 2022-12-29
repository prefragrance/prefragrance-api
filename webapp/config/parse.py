import pandas as pd
import os, sys
import django

sys.path.append('/Users/hoyeon/dev/취향/prefragrance-api/webapp') # add path to project root dir
os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"

django.setup()

#Importing Models
from product.models import Product, Category, ProductCode, Code

# 향수 데이터를 판다스 데이터프레임을 이용해 DB에 넣기 편하게 전처리 해주는 로직
perfumes = pd.read_json('/Users/hoyeon/dev/취향/prefragrance-api/webapp/config/perfume_data_combined.json')
perfumes.insert(loc = 3, column = 'category', value = 'perfume')
perfumes.rename(columns = {'main accords' : 'main_accords'}, inplace = True)

# code(a.k.a notes) 또한 향수와 마찬가지로 전처리 해주기.
all_codes = pd.read_csv('/Users/hoyeon/dev/취향/prefragrance-api/webapp/config/all_notes.csv')
all_codes.rename(columns = {'Note Name':'note_name'}, inplace = True)

#결측치 전처리
perfumes['rating'] = perfumes['rating'].replace('NA', 0)
# idx = perfumes[perfumes['rating'] == 'NA'].index
# print(perfumes['rating'][idx])

for perfume in perfumes.itertuples():
    prd = Product()
    ctgry = Category()
    
    ctgry.name = perfume.category
    ctgry.save()
    
    prd.name = perfume.name
    prd.producer = perfume.company
    prd.category = ctgry
    prd.thumbnail_url = perfume.image
    prd.rate = perfume.rating
    prd.save()
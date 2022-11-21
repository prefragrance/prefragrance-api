import pandas as pd
import os, sys
import django

sys.path.append('/Users/hoyeon/dev/취향/prefragrance-api/webapp') # add path to project root dir
os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"

django.setup()

from product.models import Product, Category

perfumes = pd.read_json('/Users/hoyeon/dev/취향/prefragrance-api/webapp/config/perfume_data_combined.json')
perfumes.insert(loc = 3, column = 'category', value = 'perfume')

for perfume in perfumes.itertuples():
    perfume_product = Product.objects.create(
        name = perfume.name,
        producer = perfume.company,
        thumbnail_url = perfume.image,
        rate = perfume.rating
        )
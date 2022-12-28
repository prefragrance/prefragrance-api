import pandas as pd
import os, sys
import django

sys.path.append('/Users/hoyeon/dev/취향/prefragrance-api/webapp') # add path to project root dir
os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"

django.setup()

from product.models import Product, Category, ProductCode, Code

perfumes = pd.read_json('/Users/hoyeon/dev/취향/prefragrance-api/webapp/config/perfume_data_combined.json')
perfumes.insert(loc = 3, column = 'category', value = 'perfume')
perfumes.rename(columns = {'main accords' : 'main_accords'}, inplace = True)

print(perfumes.head())

for perfume in perfumes.itertuples():
    # perfume_product = Product.objects.create(
    #     name = perfume.name,
    #     category = Category.objects.create(name = perfume.category), #Foreign Key Referenced Feature는 어떻게 다뤄야하는가? 이 라인 다시 살펴볼 것.)
    #     producer = perfume.company,
    #     thumbnail_url = perfume.image,
    #     rate = perfume.rating,
    #     )
    print(perfume.main_accords)
    print(type(perfume.main_accords))
        # print(cd)
        # print(type(cd))
'''

    code = ProductCode.objects.create(cd)

    return getattr(self.get_queryset(), name)(*args, **kwargs)
TypeError: QuerySet.create() takes 1 positional argument but 2 were given
'''

# notes = pd.read_csv('/Users/hoyeon/dev/취향/prefragrance-api/webapp/config/all_notes.csv')
# notes.rename(columns = {'Note Name' : 'name'}, inplace = True)
# notes.drop_duplicates(['name'])
# print(notes.head())

# for note in notes.itertuples():
#     note = Code.objects.create(
#         name = note.name
#     )

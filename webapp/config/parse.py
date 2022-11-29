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
    perfume_product = Product.objects.create(
        name = perfume.name,
        category = Category.objects.create(name = perfume.category), #Foreign Key Referenced Feature는 어떻게 다뤄야하는가? 이 라인 다시 살펴볼 것.)
        producer = perfume.company,
        thumbnail_url = perfume.image,
        rate = perfume.rating,
        )
    for cd in perfume.main_accords:
        perfume_code = ProductCode.objects.create(
            product = perfume.name,
            code = ProductCode.objects.create(cd)
        )

# notes = pd.read_csv('/Users/hoyeon/dev/취향/prefragrance-api/webapp/config/all_notes.csv')
# notes.rename(columns = {'Note Name' : 'name'}, inplace = True)
# notes.drop_duplicates(['name'])
# print(notes.head())

# for note in notes.itertuples():
#     note = Code.objects.create(
#         name = note.name
#     )
'''    
class Product(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)  # primary key
    category = models.ForeignKey(
        "product.Category", null=True, blank=True, on_delete=models.CASCADE
    )
    thumbnail_url = models.URLField(null=True, blank=True)
    name = models.CharField(max_length=400, null=False, blank=False)
    producer = models.CharField(max_length=400, null=False, blank=False)
    tags = TaggableManager(blank=True)
    codes = models.ManyToManyField(
        "product.Code",
        related_name="codes",
        through="product.ProductCode",
    )
    
    ###NULL OK
    feedback_cnt = models.IntegerField(default=0)
    review_cnt = models.IntegerField(default=0)
    visit_cnt = models.IntegerField(default=0)
    
    rate_sum = models.FloatField(null=True, blank=True)
    rate = models.FloatField(default=0)
    liked_users = models.ManyToManyField(
        "accounts.User",
        through="product.ProductFeedback",
        related_name="liked_products",
    )
'''
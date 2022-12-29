# 메달에 해당하는 리뷰의 개수 구하기
from review.models import Review, ReviewCount

from config.celery import app

#ReviewCount에서 가장 최근의 데이터를 뽑아 비교하면 됨.
#유저마다 리뷰의 개수를 세고, 몇개를 작성해야 상위 0.3% 인지 확인
@app.task
def find_medal_standard():
    result = count_reivew_of_users()
    ReviewCount.objects.create(gold_medal = result[int(len(result)*0.03)], silver_medal = result[int(len(result)*0.05)], bronze_medal = result[int(len(result)*0.1)])

@app.task
def count_reivew_of_users():
    result = {}
    for review in Review.objects.all():
        if review.user in result:
            result[review.user]+=1
        else:
            result[review.user] = 1

    return sorted(result.values(),reverse=True)

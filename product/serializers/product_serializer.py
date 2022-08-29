from rest_framework import serializers
from product.models import Product, ProductFeedback
from review.serializers import ReviewSerializer

class ProductSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = [
            "id",
            "feedback_cnt",
            "review_cnt",
            "visit_cnt",
            "rate_sum",
            "rate"
        ]
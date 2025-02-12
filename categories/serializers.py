from rest_framework import serializers
from .models import UserCategory

class UserCategorySerializer(serializers.ModelSerializer):
    id_user = serializers.CharField(source='user.id', read_only=True)
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = UserCategory
        fields = ['points','category_name', 'id_user', 'first_name', 'last_name']
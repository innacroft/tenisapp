from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserCategory
from .serializers import UserCategorySerializer

class UserRankingView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        user_categories = UserCategory.objects.order_by('-points')
        serializer = UserCategorySerializer(user_categories, many=True)
        ranked_users = [
            {'rank': index + 1, **data}
            for index, data in enumerate(serializer.data)
        ]
        return Response(ranked_users)
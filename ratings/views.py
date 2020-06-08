# pylint: disable=no-member, no-self-use
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_422_UNPROCESSABLE_ENTITY,HTTP_200_OK
from rest_framework.exceptions import NotFound
from django.db.models import Avg, Sum
import math

from .serializers import RatingSerializer,PopulatedRatingSerializer
from jwt_auth.serializers import UserSerializer
from jwt_auth.models import User
from .models import Ratings
from postRatings.models import PostRatings


class RatingListView(APIView):

    
    def post(self, request, pk):
        if not request.POST._mutable:
            request.POST._mutable = True
        request.data['rated'] = pk
        request.data['owner'] = request.user.id
        print(request.data)
        created_rating = RatingSerializer(data=request.data)
        if created_rating.is_valid():
            created_rating.save()
            return Response(created_rating.data,status=HTTP_201_CREATED)
        return Response( created_rating.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)


    #GET ALL A USERS PAST RATINGS 
    #.. GET ALL ONE USERS POSTS- RATINGS
    #GET ALL ONE USERS PROFILE RATINGS 
    #FIND SUM OF BOTH 
    # FIND AVERAGE OF BOTH 
    def get(self, request, pk):
        user_profile_ratings = Ratings.objects.filter(rated=pk).aggregate(Avg('rating'))
        user_post_ratings = PostRatings.objects.filter(post_owner=pk).aggregate(Avg('rating'))
        user_rating_score = (user_profile_ratings['rating__avg'] + user_post_ratings['rating__avg']) / 2
        users_ratings = Ratings.objects.filter(owner_id=pk)
        serailized_ratings = PopulatedRatingSerializer(users_ratings, many=True)
        return Response(({'ratings':serailized_ratings.data, 'avg':user_rating_score }), status=HTTP_200_OK)
    

    



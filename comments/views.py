# pylint: disable=no-member, no-self-use

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound,PermissionDenied
from rest_framework.status import HTTP_201_CREATED,HTTP_422_UNPROCESSABLE_ENTITY, HTTP_200_OK,HTTP_204_NO_CONTENT

from .models import Comments
from posts.models import Post
from .serializers import CommentSerializer,PopulatedCommentSerializer
from posts.serializers import PopulatedPostSerializer


class CommentDetailView(APIView):

    # POST A COMMENT, POST REQUEST, /api/comment
    def post(self, request, pk,id):
        request.data['comment_owner'] = request.user.id
        request.data['post_owner'] = pk
        request.data['post'] = id
        created_comment = CommentSerializer(data=request.data)
        if created_comment.is_valid():
            created_comment.save()
            return Response(created_comment.data, status=HTTP_201_CREATED)
        return Response(created_comment.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)

#GET ALL COMMENTS ON ONE POST 
    def get(self,request, pk):
        posts_comments = Post.objects.filter(id=pk)
        serailized_comments = PopulatedPostSerializer(posts_comments, many=True)
        return Response(serailized_comments.data, status=HTTP_200_OK)


    def is_comment_owner(self, comment, user):
        if comment.comment_owner.id != user.id:
            raise PermissionDenied()



class CommentView(APIView):
#GET ALL COMMENTS FROM ONE USER
    # def get(self,request, pk):
    #     all_comments = Comments.objects.filter(comment_owner=pk)
    #     serailized_comments = PopulatedCommentSerializer(all_comments, many=True)
    #     return Response(serailized_comments.data, status=HTTP_200_OK)

    def delete(self, request, pk):
        comment_to_delete = Comments.objects.get(pk=pk)
        print(comment_to_delete.comment_owner.id )
        print(request.user.id)
        if comment_to_delete.comment_owner.id != request.user.id:
            raise PermissionDenied()
        comment_to_delete.delete()
        return Response(status=HTTP_204_NO_CONTENT)




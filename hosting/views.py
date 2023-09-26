from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import GitLink


# Create your views here.

@api_view(['POST'])
@permission_classes([])
def receive_git_link(request):
    if request.method == 'POST':
        link = request.data.get('link')

        if link:
            git_link = GitLink(link=link)
            git_link.save()
            return Response({'message': 'ลิงค์ Git ถูกบันทึกแล้ว'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message': 'กรุณาส่งลิงค์ Git'}, status=status.HTTP_400_BAD_REQUEST)
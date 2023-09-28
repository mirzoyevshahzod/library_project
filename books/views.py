from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics


class BookListApiView(generics.ListAPIView):
     queryset = Book.objects.all()
     serializer_class = BookSerializer


#APIView ni aslida yaratiliwi tepadagisi tayyor view

# class BookListApiView(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         serializer_data = BookSerializer(books , many=True).data
#         data = {
#             "status": f"Returned {len(books)} books",
#             "books": serializer_data
#         }
#
#         return Response(data)




class BookDetailApiView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateApiView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateApiView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


#APIView ni aslida yaratiliwi tepadagisi tayyor view

# class BookCreateApiView(APIView):
#     def post(self,request):
#         data = request.data
#         serializer = BookSerializer(data)
#         if serializer.is_valid():
#             serializer.save()
#             data = {'status': f"{len(data)} books are saved to the database"}
#             return Response()



class BookListCreateApiView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
from rest_framework import views, response


class BlogView(views.APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        return response.Response({"blog": "get"}, 200)

    def post(self, request):
        return response.Response({"blog": "post"}, 200)

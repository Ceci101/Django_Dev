import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View


# Create your views here.


# def index(request):
#     return HttpResponse("Welcome!")


# def get_project_1(request):
#     return HttpResponse("<h1>This is the first project!</h1>")


# def get_projects(request, pk):
#     return HttpResponse(f"<h1>Get num {pk} project!</h1>")
#
#
# def get_project(request):
#     return HttpResponse("<h1>Get a project!</h1>")
#
#
# def create_project(request):
#     return HttpResponse("<h1>Create a project!</h1>")
#
#
# def put_project(request):
#     return HttpResponse("<h1>Update a project!</h1>")
#
#
# def delete_project(request):
#     return HttpResponse("<h1>Delete a project!</h1>")


def projects(request):
    """
    试图函数
    :param request:WSGIRequest对象（<class 'django.core.handlers.wsgi.WSGIRequest'>,
    <class 'django.http.request.HttpRequest'>, <class 'object'>）
    :return:HttpRsponse对象或其子类对象
    """
    print(request)
    print(type(request))
    print(type(request).__mro__)
    return HttpResponse(f"<h1>A project!</h1>")


class ProjectsView(View):

    def get(self, request, pk):
        # project_data ={
        #         'id': pk,
        #         'name': 'xxx项目',
        #         'leader': 'A'
        # }
        project_data_list = [
            {
                'id': pk,
                'name': 'xxx项目',
                'leader': 'A'
            },
            {
                'id': pk+1,
                'name': 'xxx项目',
                'leader': 'B'
            },
        ]
        # return HttpResponse(f"<h1>Get project {pk}!</h1>")

        # ensure_ascii: False，让中文在前端正常显示，不会转换成Ascii码
        # json_str = json.dumps(project_data, ensure_ascii=False)
        # return HttpResponse(json_str, content_type='application/json', status=201)
        # return JsonResponse(project_data, json_dumps_params={"ensure_ascii": False}, status=200)
        return JsonResponse(project_data_list, json_dumps_params={"ensure_ascii": False}, safe=False)

    def post(self, request, pk):
        # 前段参数解析

        return HttpResponse(f"<h1>Create a project!</h1>")

    def put(self, request):
        return HttpResponse(f"<h1>Update a project!</h1>")

    def patch(self, request):
        return HttpResponse(f"<h1>Update a project!</h1>")

    def delete(self, request):
        return HttpResponse(f"<h1>Delete a project!</h1>")

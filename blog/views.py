from django.shortcuts import render

#refere em blog/urls

def post_list(request):
    return render(request, 'blog/post_list.html')

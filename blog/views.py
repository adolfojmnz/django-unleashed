from django.shortcuts import render, get_object_or_404


def post_list(request):
    tmplate_name = 'blog/post_list.html'
    context = {'post_list': Post.objects.all()}
    return render(request, template_name, context)

def post_detail(request):
    template_name = 'blog/post_detail.html'
    context = {'post_detail': get_object_or_404(Post,
        pub_date__year=year,
        pub_date__month=month,
        slug__iexact=slug)}
    return render(request, template_name, context)


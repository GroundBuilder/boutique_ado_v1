from django.shortcuts import render

# Create your views here.


def all_products(request):
    """ A view to return the index page.  """

    return render(request, 'home/index.html')

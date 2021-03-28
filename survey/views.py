from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,'form.html')

def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['dojo_location']
    request.session['fav_lang'] = request.POST['fav_lang']
    request.session['comment'] = request.POST['comment']
    return redirect('/submit_page')

def submit_page(request):
    context = {
        'name' : request.session['name'],
        'location' : request.session['location'],
        'fav_lang' : request.session['fav_lang'],
        'comment' : request.session['comment']
    }
    return render(request, 'submit_page.html', context)

    # if request.method == "POST":
    #     print(request.method)
    #     # context = {
    #     #     'name': request.POST['name'],
    #     #     'lang': request.POST['fav_lang'],
    #     #     'location': request.POST['dojo_location'],
    #     #     'comment': request.POST['comment']
    #     # }
    #     return redirect('submint_page.html')
    # # return render(request, 'submit_page.html')
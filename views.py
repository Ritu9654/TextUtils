# I have Created this page
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    param={'name': 'ritu', 'place': 'delhi'}
    return render(request, 'index.html')

def analyze(request):
    djtext= request.POST.get('text','default')

    removepunc= request.POST.get('removepunc','off')
    fullcaps= request.POST.get('fullcaps','off')
    removespace= request.POST.get('removespace','off')
    removenextline= request.POST.get('removenextline','off')
    charcount= request.POST.get('charcount','off')

    print(removepunc)
    print(djtext)

    punctuations = '''!()=[]{};:'"\,<>./?@#$%^&*_~'''

    if removepunc == "on":
        analysed = ""
        for char in djtext:
                if char not in punctuations:
                    analysed = analysed + char

        params = {'purpose': 'removed punctuations', 'analysed_text': analysed}
        djtext = analysed

    if fullcaps == "on":
        analysed = ""
        for char in djtext:
            analysed = analysed + char.upper()

        params = {'purpose': 'full capitalization', 'analysed_text': analysed}
        djtext = analysed

    if removespace == "on":
        analysed = ""
        for char in djtext:
            if char != " ":
                analysed = analysed + char

        params = {'purpose': 'Remove space', 'analysed_text': analysed}
        djtext = analysed

    if removenextline == "on":
        analysed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analysed = analysed + char

        params = {'purpose': 'Remove next line', 'analysed_text': analysed}
        djtext = analysed

    if charcount == "on":
        count=0
        for char in djtext:
            count = count+1
        analysed=count
        params = {'purpose': 'character count', 'analysed_text': analysed}


    if (charcount != "on" and  removenextline != "on" and removespace != "on" and removepunc != "on" and fullcaps != "on"):
        return HttpResponse('Please select any operation and try again...')

    return render(request, 'analyse.html', params)

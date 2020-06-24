from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html',{'msg':'suren'})

def removepunc(request):
    
    djtext=request.POST.get('removepunc','off')
    text=request.POST.get('text','off')
    capfirst=request.POST.get('capfirst','off')
    newlineremove=request.POST.get('newlineremove','off')
    spaceremove=request.POST.get('spaceremove','off')
    charcount=request.POST.get('charcount','off')
    if djtext=="on":
       punc= '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
       analized=""
       for char in text:
              if char not in punc:
                     analized=analized+char
       params= {'remove':'remove punctuations','textremove':analized}   
       text=analized       
       
    
    if capfirst=='on':
       analized=""     
       for char in text:             
            analized=analized + char.upper()
       params={'remove':'Changed to Uppercase','textremove':analized}
       text=analized    

 
    if newlineremove=='on':
       analized=""   
       for char in text:
              if char !="\n" and char!="\r":
                  analized=analized + char
       params={'remove':'remove new line','textremove':analized}           
       text=analized    

    
    if spaceremove=='on':
       analized=""   
       for index,char in enumerate(text):
              if not(text[index]==" " and text[index+1]==" "):
                  analized=analized + char
       params={'remove':'remove Space','textremove':analized}
       text=analized

    if charcount=='on':
       analized=""    
       analized=analized+str(len(text))
       params={'remove':'counting the char','textremove':analized}
       text=analized
       
    if djtext!="on" and newlineremove!="on" and spaceremove!="on" and capfirst!="on" and charcount!="on":
           return HttpResponse('error please fill up the text and try again')

    return render(request,'remove.html',params)       
# def capfirst(request):
#        return HttpResponse("capitalized first")   
 
# def newlineremove(request):
#        return HttpResponse("newline remove first")   

# def spaceremove(request):
#        return HttpResponse("space remover")      

# def charcount(request):
#     return HttpResponse("charcount")           


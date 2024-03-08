from django.shortcuts import render
from translate import Translator

# Create your views here. 
  
def translator_view(request):
    if request.method == 'POST':

        text = request.POST['translate']
        to_lang = request.POST['tolanguage']
        from_lang = request.POST["fromlanguage"]
        translator = Translator(to_lang=to_lang, from_lang=from_lang)
        translation = translator.translate(text)
        
        context = {
            'translation': translation,
            
        }
        return render(request,'translator.html', context)
    return render(request, 'translator.html')
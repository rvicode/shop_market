from django.shortcuts import render
from .forms import ContactUsForm
from .models import ContactUs


def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            instance = form.save()
            print('confirm')
    else:
        print('again')
        form = ContactUsForm()
    return render(request, 'contact_us/contact_us.html', {'form': form})

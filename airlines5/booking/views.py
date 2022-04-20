
from cgitb import html
from django.shortcuts import redirect, render
from airlines5.settings import EMAIL_HOST_USER
from .forms import SearchForm, BookingForm
from .models import Booking, Fly, Search
from views_stuff.models import Underbanner

from django.core.mail import send_mail

# Create your views here.
def home_view(request):
    underbanners = Underbanner.objects.all()
    flyForm = SearchForm()
    context = {
        'flyForm':flyForm,
        'underbanners':underbanners,
        'iterator' : range(1, 11)
    }
    if request.method == 'POST':
        try:
            f_search = Search.objects.latest('id')
            if f_search.id == 1:
                flyForm = SearchForm(request.POST, instance=f_search)
        except:
            print('non esiste una ricerca')
            f_search = False
            flyForm = SearchForm(request.POST)
        if flyForm.is_valid():
            try:
                querySet = Fly.objects.filter(start = request.POST['start'], arrive=request.POST['arrive'], date=request.POST['date'], free_seats__gte = request.POST['person'])
                if querySet[0] and f_search:
                    flyForm.save()
                    return redirect('/search/')
                elif querySet[0]:
                    flyForm.save()
                    return redirect('/search/')
            except:
                context['nullSearch'] = True
    return render(request, 'home.html', context)


def search_view(request):
    underbanners = Underbanner.objects.all()
    search = Search.objects.latest('id')
    querySet= Fly.objects.filter(start=search.start, arrive=search.arrive, date=search.date, free_seats__gte = search.person)
    context = {
        'underbanners':underbanners,
        'search':search,
        'querySet':querySet,
    }
    return render(request, 'search.html', context)


def flyDetailView(request, id):
    fly = Fly.objects.get(id=id)
    saved_booking = Booking.objects.filter(fly=fly)
    booking = BookingForm()
    person = Search.objects.get(id=1)
    context = {
        'querySet':fly,
        'booking':booking,
        'saved_booking':saved_booking,
        'person':person.person,
    }
    if request.method == 'POST':
        booking = BookingForm(request.POST)
        if booking.is_valid():
            message_name = request.POST['name']
            message_email_to_send = request.POST['email']
            ticket = request.POST['unique_id']
            seat = request.POST['airC_seat']
            send_mail(
                'Grazie '+ message_name +' per la fiducia!, ecco a lei il suo ticket', #subject
                'Ticket: '+ ticket + '\nposto a sedere ' + seat, # message
                EMAIL_HOST_USER, 
                [message_email_to_send],
            ) 

            booking.fields['status'].initial = 'pending' #non fa nulla
            booking.save()
            person.person = int(person.person) - 1
            fly.free_seats = fly.free_seats - 1
            fly.save()
            if int(person.person) > 0:
                person.save()
                return redirect('fly_detail', fly.id)
            return redirect('/success/')
        else:
            context['nullSearch'] = True

    return render(request, 'detail.html', context)


def success_view(request):
    return render(request, 'success.html', {})

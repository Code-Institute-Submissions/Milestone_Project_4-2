from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Poster, Genre
from .forms import PosterForm
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.db.models import Q

def all_posters(request):

    posters = Poster.objects.all()
    query = None
    genres = ['test1', 'test2', 'test3', 'test4']
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                posters = posters.annotate(lower_name=Lower('name'))
            if sortkey == 'genre':
                sortkey = 'genre__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            posters = posters.order_by(sortkey)

        if 'genre' in request.GET:
            genres = request.GET['genre'].split(',')
            posters = posters.filter(genre__name__in=genres)
            genres = Genre.objects.filter(name__in=genres)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a keyword or ISBN to search.")
                return redirect(reverse('posters'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(description_full__icontains=query) | Q(isbn10__icontains=query) | Q(isbn13__icontains=query) | Q(genre__friendly_name__icontains=query)

            posters = posters.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'posters': posters,
        'search_term': query,
        'current_genres': genres,
        'current_sorting': current_sorting,
    }

    return render(request, 'posters/posters.html', context)

def poster_detail(request, poster_id):

    poster = get_object_or_404(Poster, pk=poster_id)

    if poster.disc_price:
        points = int(poster.disc_price * 100)
    else:
        points = int(poster.price * 100)

    context = {
        'poster': poster,
        'points': points,
    }

    return render(request, 'posters/poster_detail.html', context)

@login_required
def add_poster(request):
  
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PosterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Added poster!')
            return redirect(reverse('add_poster'))
        else:
            messages.error(request, 'Failed to add poster')
    else:
        form = PosterForm()
        
    template = 'posters/add_poster.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_poster(request, poster_id):

    if not request.user.is_superuser:
        messages.error(request, 'Can not do that, sorry')
        return redirect(reverse('home'))

    poster = get_object_or_404(Poster, pk=poster_id)
    if request.method == 'POST':
        form = PosterForm(request.POST, request.FILES, instance=poster)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated poster!')
            return redirect(reverse('poster_detail', args=[poster.id]))
        else:
            messages.error(request, 'Failed to update poster')
    else:
        form = PosterForm(instance=poster)
        messages.info(request, f'You are editing {poster.name}')

    template = 'posters/edit_poster.html'
    context = {
        'form': form,
        'poster': poster,
    }

    return render(request, template, context)

@login_required
def delete_poster(request, poster_id):

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    poster = get_object_or_404(Poster, pk=poster_id)
    poster.delete()
    messages.success(request, 'Poster deleted!')
    return redirect(reverse('posters'))
from django.shortcuts import render
from django.http import HttpResponse
from .models import Memorial, Fund, Donation
from .forms import MemorialForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

def index(request):
    return HttpResponse("Hello, world. You're at the memorials index.")

class MemorialList(LoginRequiredMixin, ListView):
    model = Memorial
    paginate_by = 10

    def get_queryset(self):
        queryset = super(MemorialList, self).get_queryset()
        queryset = queryset.filter(hospital=self.request.user.profile.hospital)
        return queryset

class MemorialCreate(LoginRequiredMixin, CreateView):
    model = Memorial
    fields = ['owner_name','owner_address_one','owner_address_two', 'owner_city', 'owner_state', 'owner_zipcode', 'pet_name', 'pet_species']
    success_url = '/memorials/memorial/list'

    def form_valid(self,form):
        form.instance.hospital_id = self.request.user.profile.hospital.id
        return super().form_valid(form)

class MemorialUpdate(LoginRequiredMixin, UpdateView):
    model = Memorial
    fields = ['hospital','owner_name','owner_address_one','owner_address_two', 'owner_city', 'owner_state', 'owner_zipcode', 'pet_name', 'pet_species']
    success_url = '/memorials/memorial/list'

    def get_queryset(self):
        queryset = super(MemorialUpdate, self).get_queryset()
        queryset = queryset.filter(hospital=self.request.user.profile.hospital)
        return queryset

    def form_valid(self,form):
        form.instance.hospital_id = self.request.user.profile.hospital.id
        return super().form_valid(form)

class MemorialDelete(LoginRequiredMixin, DeleteView):
    model = Memorial
    success_url = reverse_lazy('memorial-list')

    def get_queryset(self):
        queryset = super(MemorialDelete, self).get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def form_valid(self,form):
        form.instance.hospital_id = self.request.user.profile.hospital.id
        return super().form_valid(form)

class MemorialDetail(LoginRequiredMixin, DetailView):
    model = Memorial
    fields = ['hospital','owner_name','owner_address_one','owner_address_two', 'owner_city', 'owner_state', 'owner_zipcode', 'pet_name', 'pet_species']


@login_required    
def process_donation(request):
    funds = Fund.objects.all()
    memorials = Memorial.objects.filter(
                hospital=request.user.profile.hospital.id, status="New"
                                        )
    return render(request, 'memorials/process_donation.html', {'funds': funds, 'memorials': memorials})

def payment(request):
    pass

@login_required    
def past_donations(request):
    donations = Donation.objects.filter(
                hospital=request.user.profile.hospital.id, status="Paid"
    )

    return render(request, 'memorials/past_donations.html', {'donations': donations})

def payment(request):
    pass
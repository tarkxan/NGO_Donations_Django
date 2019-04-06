from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, reverse_lazy

from donation.views import DonationList, UserList, UserEdit, \
    DonationCreate, DonationTypeList, IndexView, UserRemove, UserListEdit, DonationTypeRemove

from . import views
app_name = 'donation'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('users/', UserList.as_view(), name='user_list'),
    path('users/<int:pk>/edit/', UserEdit.as_view(), name='user_edit'),
    path('donations/', DonationList.as_view(), name='donation_list'),
    path('donations/new', DonationCreate.as_view(), name='donation_create'),
    path('dtypes/', DonationTypeList.as_view(), name='dtype_list'),
    path('dtypes/<int:pk>/remove/', DonationTypeRemove.as_view(), name='dtype_remove'),
    path('login/', LoginView.as_view(extra_context={'next': reverse_lazy('donation:index')}), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('donation:index')), name='logout'),
    path('users/<int:pk>/remove/', UserRemove.as_view(), name='user_remove'),
    path('users/<int:pk>/edit_user/', UserListEdit.as_view(), name='user_line_edit'),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('users/new/', views.add_user, name='add_user'),
]
# from django.contrib import admin
# from django.urls import path
# from accounts.views import home  # Update this based on where your home view is located

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', home, name='home'),  # Add this line to handle the root URL
#     path('accounts/', include('accounts.urls')),  # Include your app URLs
#     path('content/', include('content.urls')),
#     path('shop/', include('shop.urls')),
# ]
from django.contrib import admin
from django.urls import path, include  # Include the 'include' function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),  # Include accounts URLs
    path('api/content/', include('content.urls')),    # Include content URLs
    path('api/shop/', include('shop.urls')),          # Include shop URLs
]

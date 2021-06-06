from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token  
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve

urlpatterns =[
  #ApI URLs
    path("api/v1.0/register/", views.RegisterUser, name="RegisterUser"),
    path("api/v1.0/retrieve_pin/", views.Retrieve_pin, name="retrieve_pin"),
    path('api/v1.0/login/', views.C_Login.as_view()),
    #path('api/v1.0/subscribe/', views.Subscribe_user, name="subscribe"),
    path('api/v1.0/video/', views.Show_video, name="video"),
    path('api/v1.0/article/', views.Show_article, name="article"),
    path("getuser/", views.Get_all_users ),
    path("example/", views.example ),
    path('api/v1.0/cancel/', views.Api_Cancel),
    path("mail/", views.mail ), 
    path("staffing/", views.Make_user_admin ),
    #stripe configuration and website url
    path('', views.Home, name='home'),
    path("webregister/", views.WebRegister, name='webregister' ),
    path("weblogin/", views.WebLogin, name='weblogin'),  
    path("weblogout/", views.WebLogout, name='weblogout'),  #
    path("postvideo/", views.Post_video, name='postvideo'),
    path("postarticle/", views.Post_article, name='postarticle'), 
    path("showarticle/", views.Display_article, name='showarticle'), #
    path("showvideo/", views.Display_video, name='showvideo'), #
    path('retreivepin/', views.WebRetrieve_pin, name="retreivepin"),
    path('saving/', views.Saving, name="saving"),
    path('funnel/', views.Funnel, name="funnel"),
    path('payment/', views.Stripe_config_pay),
    path('success/', views.success),
    path('cancel/', views.cancel),
    path('webhook/', views.stripe_webhook),
    path("create-checkout-session/", views.Create_checkout_session, name="create_checkout_session"),
    
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path("",views.home,name='home'),
    path("about",views.AboutView.as_view(),name='about'),
    path("contact",views.ContactView.as_view(),name='contact'),
    path('devis/', views.devis, name='devis'),
    path('blog/',views.PostListView.as_view(),name='post_list'),
    path('blog/<int:pk>/',views.PostDetailView.as_view(),name='post_detail'),
    path('blog/create/', views.CreatePostView.as_view(), name='create_post'),
    path('blog/<int:id>/delete_post/', views.delete_post, name='delete_post'),
    path('blog/<int:id>/delete_partner/', views.delete_partner, name='delete_partner'),
    path('blog/<int:id>/delete_doc/', views.delete_doc, name='delete_doc'),
    path('blog/update_post/<int:pk>', views.UpdatePostView.as_view(), name='update_post'),
    path('blog/update_partner/<int:pk>', views.UpdatePartnerView.as_view(), name='update_partner'),
    path('blog/update_doc/<int:pk>', views.UpdateDocView.as_view(), name='update_doc'),
    path('blog/add_categorie/', views.AddCategorieView.as_view(), name='add_categorie'),
    path('blog/add_doc/', views.AddDocsView.as_view(), name='add_doc'),
    path('blog/add_partner/', views.AddPartnerView.as_view(), name='add_partner'),
    path('blog/categorie/<str:cats>/', views.sameCategorieList, name='same_categorie_list'),
    path('activite/', views.activiteListView, name='activite'),
    path('etudes_au_niger/', views.etudesListView, name='etudes'),
    path('partnaires/', views.PartnerListView.as_view(), name='partners'),
    path('documents/', views.DocsListView.as_view(), name='documents'),
    path('blog/categorie_list/', views.categorieListView, name='categorie_list'),
    path('blog/like/<int:pk>', views.like_view, name='like_view'),
    path('blog/<int:pk>/add_comment/',views.AddCommentView.as_view(), name ='add_comment_section'),
    path('blog/<int:pk>/author_profile', views.showProfileView.as_view(), name='showProfileView')
    


]
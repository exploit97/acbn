from django.shortcuts import reverse
from .models import Post,Categorie,Comment
from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase,client

# Create your tests here.

class PostListViewPageTestCase(TestCase):
    # test that index returns a 200
    def test_PostListView_page(self):
        response = self.client.get(reverse('blogs:home'))
        self.assertEqual(response.status_code,200)


class PostDetailViewPageTestCase(TestCase):
    # test that postDetail page returns a 200 if post exists
    def setUp(self):
      
        self.user = User.objects.create_user(username='jacob', email='jacob@...', password='top_secret')
    
    def test_post_detail_page_returns_a_200(self) :
        author = self.user
        
        
        post_1 = Post.objects.create(title='Mon post de test',author = author)
        
        post_1_id=Post.objects.get(title='Mon post de test').id
        response = self.client.get(reverse('blogs:post_detail', args=(post_1_id,)))
        self.assertEqual(response.status_code,200)

    

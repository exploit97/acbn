from django import forms
from blog.models import Post, Categorie,Comment,Documents,Partner

class PostForm(forms.ModelForm):

    class Meta:
        model= Post
        fields = ['title','text','post_image','categorie','snippet']
        widgets = {
            'title': forms.TextInput(attrs={"class":'form-control' ,'name':'title'}),
        'text' : forms.Textarea(attrs={'class':"form-control", 'name':"text", 'cols':"30" ,'rows':"10" }),
        'snippet' : forms.Textarea(attrs={'class':"form-control", 'name':"snippet", 'cols':"30" ,'rows':"5" }),
        'categorie' : forms.Select(attrs={'class':"form-control", 'name':"categorie" }),
        'pos_image' : forms.FileInput(attrs={'class':"form-control", 'name':"image" }),
        } 

class PartnerForm(forms.ModelForm):

    class Meta:
        model= Partner
        fields = ['name','image']
        widgets = {
            'name': forms.TextInput(attrs={"class":'form-control' ,'name':'nom'}),
            'image' : forms.FileInput(attrs={'class':"form-control", 'name':"image" }),
        } 

class DocForm(forms.ModelForm):

    class Meta:
        model= Documents
        fields = ['title','description','doc_file']
        widgets = {
            'title': forms.TextInput(attrs={"class":'form-control' ,'name':'title'}),
            'description' : forms.Textarea(attrs={'class':"form-control", 'name':"description", 'cols':"30" ,'rows':"10" }),
            'doc_file' : forms.FileInput(attrs={'class':"form-control", 'name':"fichier" }),
        } 
class AddCommentForm(forms.ModelForm):

    class Meta:
        model= Comment
        fields = ['name','text']
        widgets = {
            'name': forms.TextInput(attrs={"class":'form-control' ,'name':'name'}),
        'text' : forms.Textarea(attrs={'class':"form-control", 'name':"text", 'cols':"30" ,'rows':"10" }),
        
        } 

class AddCategorieForm(forms.ModelForm):

    class Meta:
        model= Categorie
        fields = ['name',]
        widgets = {
            'name': forms.TextInput(attrs={"class":'form-control' ,'name':'name'}),
            
        
        
        } 
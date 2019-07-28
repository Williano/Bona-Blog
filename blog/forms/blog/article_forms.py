# Django imports
from django import forms

# Blog app imports
from blog.models.article_models import Article
from blog.models.category_models import Category


class ArticleCreateForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.filter(
                                      approved=True),
                                      empty_label="Select Category")

    class Meta:
        model = Article
        fields = ["title", "category", "image", "body", "tags", "status"]

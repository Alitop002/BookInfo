from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    CATEGORY_CHOICES = [
        ('Uzbek Literature', 'Uzbek Literature'),
        ('Russian Literature', 'Russian Literature'),
        ('English Literature', 'English Literature'),
    ]
    
    name = models.CharField(max_length=100, choices=CATEGORY_CHOICES, unique=True)
    image = models.ImageField(upload_to='category_images/')

    def __str__(self):
        return self.name
    
class Books(models.Model):
    LANGUAGE_CHOICES = [
    ('uz', 'Uzbek'),
    ('ru', 'Russian'),
    ('en', 'English'),
    ]
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    title = models.CharField(max_length=200)
    year = models.PositiveIntegerField()
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, default='uz')
    pages = models.PositiveIntegerField()
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='book_images/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class Comments(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user', 'book')

    def __str__(self):
        return f"{self.user.username} - {self.book.title}"


    

from django.db import models


# define blog post 
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="blog_image",blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to="product/")
    created_at = models.DateTimeField(auto_now_add=True)
    # blog post 
    blog_url = models.URLField(blank=True,null=True) # direct link  

    def __str__(self):
        return self.title
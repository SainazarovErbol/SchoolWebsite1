from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='GalleryImages')
    image = models.ImageField(upload_to='gallery_images/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image in {self.gallery.title}"


class Video(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, related_name='GalleryVideos')
    video_file = models.FileField(upload_to='video_gallery/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Video in {self.gallery.title}"

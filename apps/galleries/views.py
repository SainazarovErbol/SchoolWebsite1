from django.forms import inlineformset_factory
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from apps.galleries.forms import GalleryForm, ImageForm, VideoForm
from .models import Gallery, Image, Video

from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required, permission_required

# Gallery Views
class GalleryListView(ListView):
    model = Gallery
    template_name = 'gallery/gallery_list.html'
    context_object_name = 'galleries'


class GalleryDetailView(DetailView):
    model = Gallery
    template_name = 'gallery/gallery_detail.html'
    context_object_name = 'gallery'


# VideoGallery Views

class CustomPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser or \
               (self.request.user.role == 'content_maker' and
                self.request.user.has_perm('galleries.can_manage_gallery'))


class GalleryCreateView(CustomPermissionMixin, CreateView):
    model = Gallery
    form_class = GalleryForm
    template_name ='gallery/gallery_form.html'
    success_url = reverse_lazy('gallery_list')
    extra = 3

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = inlineformset_factory(Gallery, Image, form=ImageForm, extra=self.extra)(
                self.request.POST, self.request.FILES, instance=self.object
            )
        else:
            data['formset'] = inlineformset_factory(Gallery, Image, form=ImageForm, extra=self.extra)()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            form.instance.owner = self.request.user
            self.object = form.save()
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class GalleryUpdateView(CustomPermissionMixin, UpdateView):
    model = Gallery
    form_class = GalleryForm
    template_name = 'gallery/gallery_form.html'
    success_url = reverse_lazy('gallery_list')

    extra = 3

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = inlineformset_factory(Gallery, Image, form=ImageForm, extra=self.extra)(
                self.request.POST, self.request.FILES, instance=self.object
            )
        else:
            data['formset'] = inlineformset_factory(Gallery, Image, form=ImageForm, extra=self.extra)()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            form.instance.owner = self.request.user
            self.object = form.save()
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)


class GalleryDeleteView(CustomPermissionMixin, DeleteView):
    model = Gallery
    template_name = 'gallery/gallery_confirm_delete.html'
    success_url = reverse_lazy('gallery_list')




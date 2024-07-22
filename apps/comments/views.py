from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DeleteView

from .models import Comment
from .forms import CommentForm


class CommentUpdateView(View):
    form_class = CommentForm
    template_name = 'comments/update_comment.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_object(self):
        comment = get_object_or_404(Comment, id=self.kwargs['pk'], user=self.request.user)
        return comment

    def get(self, request, *args, **kwargs):
        comment = self.get_object()
        form = self.form_class(instance=comment)
        return render(request, self.template_name, locals())

    def post(self, request, *args, **kwargs):
        comment = self.get_object()
        form = self.form_class(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.pk)
        return render(request, self.template_name, locals())





class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comments/delete_comment.html'
    success_url = reverse_lazy('post_list')  # Redirect to a different URL after deletion

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_object(self):
        # Ensure the comment belongs to the user, if necessary
        comment = get_object_or_404(Comment, pk=self.kwargs['pk'])
        if comment.user != self.request.user and not self.request.user.is_superuser:
            raise PermissionDenied("You do not have permission to delete this comment.")
        return comment

    def post(self, request, *args, **kwargs):
        comment = self.get_object()
        post_id = comment.post.pk
        comment.delete()
        return redirect('post_detail', pk=post_id)

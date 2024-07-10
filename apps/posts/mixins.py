from django_filters.views import FilterView
from .services import PostFilter


class FilteredPostListView(FilterView):
    filterset_class = PostFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        return context

    def get_paginate_by(self, queryset):
        return self.paginate_by

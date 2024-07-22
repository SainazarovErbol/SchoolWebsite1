from django.http import JsonResponse
from django.template.loader import render_to_string
from django_filters.views import FilterView
from .services import PostFilter

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

class FilteredPostListView(FilterView):
    filterset_class = PostFilter
    template_name = 'post/filtered_posts.html'  # Replace with your template name
    paginate_by = 10  # Adjust as needed

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

    def get(self, request, *args, **kwargs):
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            self.object_list = self.get_queryset()
            context = self.get_context_data()
            html = render_to_string('post/filtered_posts.html', context, request=request)
            return JsonResponse({'html': html})
        return super().get(request, *args, **kwargs)



class PaginationMixin:
    paginate_by = 3

    def paginate_queryset(self, queryset, page_kwarg):
        paginator = Paginator(queryset, self.paginate_by)
        page = self.request.GET.get(page_kwarg)
        try:
            page_obj = paginator.page(page)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        return {
            'paginator': paginator,
            'page_obj': page_obj,
            'is_paginated': page_obj.has_other_pages(),
        }

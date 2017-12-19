from django.shortcuts import render


from django.views.generic import View
from django.views.generic.base import TemplateView, TemplateResponseMixin, ContextMixin

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Book

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.views.generic.edit import CreateView, UpdateView, DeleteView, ModelFormMixin

from .forms import BookForm

from django.core.urlresolvers import reverse

from django.http import Http404

from django.contrib.messages.views import SuccessMessageMixin


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **kwargs):
        view = super(LoginRequiredMixin, cls).as_view(**kwargs)
        return login_required(view)


class TempView(TemplateView):
    template_name = 'cbv/template.html'

    def get_context_data(self, **kwargs):
        context = super(TempView, self).get_context_data(**kwargs)
        context['title'] = 'THIS IS A TEMPLATE VIEW.'
        return context


# class AnotherTempView(ContextMixin, TemplateResponseMixin, View):
#     template_name = 'cbv/template.html'
#
#     def get(self, *args, **kwargs):
#         context = self.get_context_data(**kwargs)
#         context['title'] = 'THIS IS ANOTHER TEMPLATE VIEW.'
#         return self.render_to_response(context)
#
#     def post(self):
#         pass
#
#     """當服務端使用cbv模式的時候,使用者發給服務端的請求包含url和method,這兩個資訊都是字串型別,服務端通過
#     路由對映表匹配成功後會自動去找dispatch方法,然後Django會通過dispatch反射的方式找到類中對應的方法並執行
#     類中的方法執行完畢之後,會把客戶端想要的資料返回給dispatch方法,由dispatch方法把資料返回經客戶端
#     """
#     @method_decorator(login_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super(AnotherTempView, self).dispatch(request, *args, **kwargs)

class AnotherTempView(ContextMixin, TemplateResponseMixin, LoginRequiredMixin, View):
    template_name = 'cbv/template.html'

    def get(self, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['title'] = 'THIS IS ANOTHER TEMPLATE VIEW.'
        return self.render_to_response(context)

    def post(self):
        pass


# def book_detail(request, slug):
#     book = Book.objects.get(slug=slug)
#     template = ''
#     context = {
#         'book': book
#     }
#     return render(request, template, context)

class BookDetail(ModelFormMixin, DetailView):
    template_name = 'cbv/detail.html'
    model = Book
    form_class = BookForm

    def get_context_data(self, *args, **kwargs):
        context = super(BookDetail, self).get_context_data(*args, **kwargs)
        context['form'] = self.get_form()
        context['btn_title'] = 'Update Book'
        return context

    def post(self, request, *args, **kwargs):
        # self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class BookList(ListView):
    template_name = 'cbv/list.html'
    model = Book

    def get_queryset(self, *args, **kwargs):
        qs = super(BookList, self).get_queryset(*args, **kwargs).order_by('id')
        return qs


class BookCreate(SuccessMessageMixin, CreateView):
    template_name = 'cbv/form.html'
    model = Book
    form_class = BookForm
    # fields = [
    #     'title',
    #     'description'
    # ]

    def form_valid(self, form):
        print(form.instance)
        form.instance.added_by = self.request.user
        return super(BookCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('cbv:book_list')

    success_message = "%(title)s was created at %(created_at)s"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            created_at=self.object.timestamp
        )

class BookUpdate(UpdateView):
    template_name = 'cbv/form.html'
    model = Book
    form_class = BookForm

    def get_object(self, queryset=None):
        pass


class BookDelete(DeleteView):
    template_name = 'cbv/delete.html'
    model = Book
    form_class = BookForm

    def get_success_url(self):
        return reverse('cbv:book_list')


class MultipleObjectMixin(object):
    def get_object(self, queryset=None, *args, **kwargs):
        slug = self.kwargs.get('slug')
        if slug:
            try:
                obj = self.model.objects.get(slug=slug)
            except self.model.MultipleObjectReturned:
                obj = self.get_queryset().first()
            except:
                raise Http404
            return obj
        return None


from django.shortcuts import render


from django.views.generic import View
from django.views.generic.base import TemplateView, TemplateResponseMixin, ContextMixin

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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


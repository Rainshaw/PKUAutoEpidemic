from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.generic import View, CreateView, UpdateView
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadData
from django.conf import settings


# Create your views here.
from epidemic.forms import InfoCreateForm
from epidemic.models import Info
from epidemic.tasks import send_detail_url_email


class NoIndexView(View):
    def get(self, request):
        return HttpResponseRedirect(reverse('epidemic:index'))


class IndexView(View):
    def get(self, request):
        return render(request, template_name='index.html')


class InfoCreateView(CreateView):
    model = Info
    template_name = 'epidemic/info_create.html'
    form_class = InfoCreateForm

    def get_success_url(self):
        return reverse('epidemic:create-success')

    def form_valid(self, form):
        response = super().form_valid(form)
        domain = self.request.get_host()
        send_detail_url_email.delay(self.object.id, domain)
        return response


class InfoCreateSuccessView(View):
    def get(self, request):
        return render(request, template_name='epidemic/create-success.html')


class InfoDetailView(View):
    def get(self, request, token):
        serializer = Serializer(settings.SECRET_KEY, 60 * 60 * 24 * 7)
        try:
            tokens = serializer.loads(token)
            # 获取id
            info_id = tokens['info_id']

            # 根据id获取信息
            info = Info.objects.get(id=info_id)
            ctx = {
                "info": info,
                "token": token,
            }
            return TemplateResponse(request, template='epidemic/info-detail.html', context=ctx)
        except SignatureExpired:
            raise PermissionDenied('激活链接已过期！ 请登录或联系管理员获取新的激活链接')
        except BadData:
            raise PermissionDenied('激活链接错误！ 请复制粘贴完整的激活链接')


class InfoUpdateView(UpdateView):
    model = Info
    template_name = 'epidemic/info_update.html'
    form_class = InfoCreateForm

    def get_object(self, queryset=None):
        serializer = Serializer(settings.SECRET_KEY, 60 * 60 * 24 * 365)
        token = self.kwargs.get('token')
        try:
            token = serializer.loads(token)
            # 获取id
            info_id = token['info_id']

            # 根据id获取信息
            info = Info.objects.get(id=info_id)
            return info
        except SignatureExpired:
            raise PermissionDenied('激活链接已过期！ 请登录或联系管理员获取新的激活链接')
        except BadData:
            raise PermissionDenied('激活链接错误！ 请复制粘贴完整的激活链接')

    def get_success_url(self):
        return reverse('epidemic:info-detail', kwargs={'token': self.kwargs.get('token')})



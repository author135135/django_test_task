from django.views.generic import RedirectView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from students_base_app.models import Student, Group
from students_base_app.forms import StudentForm, GroupForm, LoginForm


# Create your views here.
class Home(ListView):
    template_name = 'students_base_app/home.html'
    model = Group
    context_object_name = 'groups'

home = login_required(Home.as_view())


class GroupView(DetailView):
    template_name = 'students_base_app/group/view.html'
    model = Group
    context_object_name = 'group'
    pk_url_kwarg = 'group_id'

group_view = login_required(GroupView.as_view())


class GroupAdd(SuccessMessageMixin, CreateView):
    template_name = 'students_base_app/group/add.html'
    form_class = GroupForm
    success_url = reverse_lazy('students_app:home')
    success_message = 'New group was added.'

group_add = login_required(GroupAdd.as_view())


class GroupEdit(SuccessMessageMixin, UpdateView):
    template_name = 'students_base_app/group/edit.html'
    form_class = GroupForm
    model = Group
    pk_url_kwarg = 'group_id'
    context_object_name = 'group'
    success_message = 'Group was updated.'

    def get_success_url(self):
        return reverse('students_app:group_view', kwargs={'group_id': self.object.id})

group_edit = login_required(GroupEdit.as_view())


class GroupDelete(SuccessMessageMixin, DeleteView):
    template_name = 'students_base_app/delete_confirm.html'
    model = Group
    pk_url_kwarg = 'group_id'
    success_url = reverse_lazy('students_app:home')
    success_message = 'Group was deleted.'

group_delete = login_required(GroupDelete.as_view())


class StudentAdd(SuccessMessageMixin, CreateView):
    template_name = 'students_base_app/student/add.html'
    form_class = StudentForm
    success_message = 'New student was added.'

    def get_success_url(self):
        return reverse('students_app:group_view', kwargs={'group_id': self.object.group.id})

student_add = login_required(StudentAdd.as_view())


class StudentEdit(SuccessMessageMixin, UpdateView):
    template_name = 'students_base_app/student/edit.html'
    form_class = StudentForm
    model = Student
    pk_url_kwarg = 'student_id'
    success_message = 'Student profile updated.'

    def get_success_url(self):
        return reverse('students_app:group_view', kwargs={'group_id': self.object.group.id})

student_edit = login_required(StudentEdit.as_view())


class StudentDelete(SuccessMessageMixin, DeleteView):
    template_name = 'students_base_app/delete_confirm.html'
    model = Student
    pk_url_kwarg = 'student_id'
    success_message = 'Student was deleted.'

    def get_success_url(self):
        return reverse('students_app:group_view', kwargs={'group_id': self.object.group.id})

student_delete = login_required(StudentDelete.as_view())


class AccountLogin(SuccessMessageMixin, FormView):
    template_name = 'students_base_app/account/login.html'
    form_class = LoginForm
    success_message = 'You logged now.'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(username=username, password=password)

        if user and user.is_active:
            login(self.request, user)
        else:
            form.add_error('password', 'Login or password incorrect.')

            return super(AccountLogin, self).form_invalid(form)

        return super(AccountLogin, self).form_valid(form)

    def get_success_url(self):
        return self.request.GET.get('next', reverse('students_app:home'))

account_login = AccountLogin.as_view()


class AccountLogout(RedirectView):
    url = reverse_lazy('students_app:home')
    permanent = False

    def get(self, request, *args, **kwargs):
        logout(request)

        return super(AccountLogout, self).get(request, *args, **kwargs)

account_logout = login_required(AccountLogout.as_view())

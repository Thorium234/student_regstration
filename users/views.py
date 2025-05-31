from django.shortcuts import redirect, render
from .forms import RegisterForm
# Create your views here.
def register(request):
    form=RegisterForm()
    if request.method == 'POST':
            form=RegisterForm(request.POST or None)
            if form.is_valid():
                 form.save()
            return redirect('student_list')
    else:
        form=RegisterForm()
        return render(request,'registration/register.html',{'form':form})
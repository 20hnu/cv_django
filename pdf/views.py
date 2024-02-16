from django.shortcuts import render,get_object_or_404
from .models import Profile
from django.http import HttpResponse
from django.template import loader
import pdfkit
import io
# Create your views here.
def accept(request):
    if request.method == 'POST':
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        phone = request.POST.get('phone',"")
        degree = request.POST.get('degree',"")
        university = request.POST.get('university',"")
        school = request.POST.get('school',"")
        skill = request.POST.get('skills',"")
        about_you = request.POST.get('about',"")
        previous_work = request.POST.get('previous_work',"")
              
        profile  = Profile(name=name,email=email,phone=phone,school=school,university=university,about_you=about_you,previous_work = previous_work,skill=skill,degree=degree)
        profile.save()
        return render(request,'success.html')
    return render(request,'accept.html')

def resume(request,id):
    user_profile = get_object_or_404(Profile,pk=id)
    template = loader.get_template('resume.html')
    html = template.render({'user_profile':user_profile})
    options = {
        'page-size':'Letter',
        'encoding':'UTF-8'
    }
    config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
    pdf = pdfkit.from_string(html,False,configuration = config,options = options)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename = "resume.pdf"'
    return response
    
    
def list(request):
    profiles = Profile.objects.all()
    return render(request, 'list.html', {'profiles': profiles})
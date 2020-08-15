from django.shortcuts import render
from .models import Profile, Project, Contact, SkillLevel, Blog
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import get_template


# Create your views here.
def Home(request):
    form_class = ContactForm
    profile = Profile.objects.first()
    contact = Contact.objects.first()
    projects = Project.objects.all()
    skills = SkillLevel.objects.all()
    blogs = Blog.objects.all()

    if request.method == 'POST':
        form = form_class(data=request.POST)
        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template =get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['youremail@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            
            return redirect('home')

    return render(request, 'portfolio/index.html',{'profile': profile,'contact':contact,'skills':skills,'projects':projects,'form': form_class, 'blogs': blogs})
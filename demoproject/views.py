from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect
from .forms import usersForm
from demoapp.models import Service
from news.models import News
from django.core.paginator import Paginator

def homePage(request):
    newsData = News.objects.all();
    servicesData = Service.objects.all().order_by('-service_title')[2:5]
    # for a in servicesData:
    #     print(a.service_icon)
    # print(services)
    data={
        'servicesData':servicesData,
        'newsData':newsData
    }

    # data ={
    #     'title' : 'Home Page',
    #     'bdata':'study with me.',
    #     'clist':['Java',' Python','Django','PHP'],
    #     'numbers':[10,20,30,40,50],
    #     'student_details':[
    #         {'name': 'pradeep', 'phone':9876543210},
    #         {'name':'testing', 'phone':8765413290}
    #     ]
    # }
    return render(request, "index.html",data)

def newsDetails(request,slug):
   
    newsDetails=News.objects.get(news_slug=slug)
    data = {
        'newsDetails': newsDetails
    }
    return render(request,"newsdetails.html",data)

def service(request):
       # __icontains
        servicesData = Service.objects.all()
        paginator=Paginator(servicesData,2)
        page_number = request.GET.get('page')
        ServiceDatafinal=paginator.get_page(page_number)
        if request.method == "GET":
            st=request.GET.get('servicename')
            if st != None:
                servicesData = Service.objects.filter(service_title__icontains=st)

        data={
            'servicesData':ServiceDatafinal,
            
        }
        return render(request, "services.html",data)

def submitform(request):
    try:
        if request.method=="POST":
        # n1 = int(request.GET['num1'])
        # n2 = int(request.GET['num2'])
        # n3 = int(request.GET['num3'])
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            n3 = int(request.POST.get('num3'))
            finalans=n1+n2+n3
            data={
                'n1':n1,
                'n2':n2,
                'n3':n3,

                'output':finalans
            }
            url='/about-us/?output={}'.format(finalans)
            # return HttpResponseRedirect(url)
            return HttpResponse(finalans)
    except:
        pass

def aboutUs(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request,"newsdetails.html")

def products(request):
    return render(request,"Products.html")

def contactus(request):
    return render(request,"ContactUs.html")

def Course(request):
    return HttpResponse("<b>Hello, world. This is the index view of Demoapp.</b>")


def courseDetails(request,courseid):
    return HttpResponse(courseid)

def calculator(request):
    c=""
    try:
        if request.method =="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr == "+":
                c = n1+n2
            elif opr == "-":
                c = n1-n2
            elif opr == "*":
                c = n1*n2
            else:
                c = n1/n2

    except:
        c = "Invalid operator......"
    print(c)

    return render(request,"calculator.html", {"c":c})

def saveevenodd(request):
    c=''
    if request.method=="POST":
        if request.POST.get('num1') == "":
            return render(request,"evenodd.html", {'error':True})

        n=eval(request.POST.get('num1'))
        if n%2==0:
            c="Even Number"
        else:
            c="Odd Number"
    return render(request,"evenodd.html", {"c":c})

def marksheet(request):
    data = {}
    if request.method == "POST": 
        s1 = eval(request.POST.get('subject1'))
        s2 = eval(request.POST.get('subject2'))
        s3 = eval(request.POST.get('subject3'))
        s4 = eval(request.POST.get('subject4'))
        s5 = eval(request.POST.get('subject5'))
        t = s1+s2+s3+s4+s5
        p = (t*100)/500
        if p >= 60:
            d="First Div"
        elif p>=48:
            d = "Second Div"
        elif p>=48:
            d = "Third Div"
        else:
            d="Fail"
        
        data={
            'total':t,
            'per':p,
            'div':d
        }
        print(t)
    return render(request,"marksheet.html",data)

def userForm(request):
    finalans = 0
    fn =  usersForm()
    data={'form':fn}
    try:
        if request.method=="POST":
        # n1 = int(request.GET['num1'])
        # n2 = int(request.GET['num2'])
        # n3 = int(request.GET['num3'])
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalans=n1+n2
            data={
                'form':fn,
                'output':finalans
            }
            url='/about-us/?output={}'.format(finalans)
            # return HttpResponseRedirect(url)
            return redirect(url)
    except:
        pass
    return render(request,"userform.html", data)







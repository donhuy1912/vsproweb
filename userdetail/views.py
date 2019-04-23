from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from django.contrib import messages
from homepage.myfunction import *
from adminpage import templates
import re
import string

# from accounttype.models import AccountType
# from account.models import Account

# Create your views here.

def index(request):
    userdetails = UserDetail.objects.all()
    enviromentcates = EnviromentCate.objects.all()
    accounttypes = AccountType.objects.all()
    accounts = Account.objects.all()
    subjects = Subject.objects.all()
    subjectparts = SubjectPart.objects.all()
    chapters = Chapter.objects.all()
    lessons = Lesson.objects.all()
    items = Item.objects.all()
    activitytypes = ActivityType.objects.all()
    activitys = Activity.objects.all()
    activitysubmittions = ActivitySubmittion.objects.all()
    forums = Forum.objects.all()
    newss = News.objects.all()
    projectshares = ProjectShare.objects.all()
    competitions = Competition.objects.all()
    competitionsubmittions = CompetitionSubmittion.objects.all()
    subjectlikes = SubjectLike.objects.all()
    subjectteachers = SubjectTeacher.objects.all()
    

    for userdetail in userdetails:
        userdetail.birthday = userdetail.birthday.strftime("%Y-%m-%d")

    for accounttype in accounttypes:
        accounttype.createdate = accounttype.createdate
        accounttype.editdate = accounttype.editdate

    for account in accounts:
        account.createdate = account.createdate
        account.editdate = account.editdate

    for enviromentcate in enviromentcates:
        #enviromentcate.createdate = enviromentcate.createdate.strftime("%Y-%m-%d")
        enviromentcate.createdate = enviromentcate.createdate
        enviromentcate.editdate = enviromentcate.editdate

    for subjectteacher in subjectteachers:
        subjectteacher.createdate = subjectteacher.createdate
        subjectteacher.editdate = subjectteacher.editdate

    for subject in subjects:
        subject.createdate = subject.createdate
        subject.editdate = subject.editdate

    for subjectpart in subjectparts:
        subjectpart.createdate = subjectpart.createdate
        subjectpart.editdate = subjectpart.editdate

    for chapter in chapters:
        chapter.createdate = chapter.createdate
        chapter.editdate = chapter.editdate

    for lesson in lessons:
        lesson.createdate = lesson.createdate
        lesson.editdate = lesson.editdate

    for item in items:
        item.createdate = item.createdate
        item.editdate = item.editdate

    for activitytype in activitytypes:
        activitytype.createdate = activitytype.createdate
        activitytype.editdate = activitytype.editdate

    for activity in activitys:
        activity.createdate = activity.createdate
        activity.editdate = activity.editdate


    for activitysubmittion in activitysubmittions:
        activitysubmittion.createdate = activitysubmittion.createdate
        activitysubmittion.editdate = activitysubmittion.editdate

    for forum in forums:
        forum.createdate = forum.createdate
        forum.editdate = forum.editdate

    for news in newss:
        news.createdate = news.createdate
        news.editdate = news.editdate

    for projectshare in projectshares:
        projectshare.createdate = projectshare.createdate
        projectshare.editdate = projectshare.editdate

    for competition in competitions:
        competition.createdate = competition.createdate
        competition.editdate = competition.editdate
        competition.opendate = competition.opendate.strftime("%Y-%m-%d %H:%M:%S")
        competition.enddate = competition.enddate.strftime("%Y-%m-%d %H:%M:%S")

    for competitionsubmittion in competitionsubmittions:
        competitionsubmittion.createdate = competitionsubmittion.createdate
        competitionsubmittion.editdate = competitionsubmittion.editdate
    context = {'userdetails': userdetails,
                'accounttypes': accounttypes,
                'accounts': accounts,
                'subjects': subjects,
                'subjectparts': subjectparts,
                'chapters': chapters,
                'lessons': lessons,
                'items': items,
                'activitytypes': activitytypes,
                'activitys': activitys,
                'activitysubmittions': activitysubmittions,
                'forums': forums,
                'newss': newss,
                'projectshares': projectshares,
                'competitions': competitions,
                'competitionsubmittions': competitionsubmittions,
                'subjectteachers': subjectteachers,
                'enviromentcates': enviromentcates,
            
    }
   
    return render(request, 'adminpage/tables_object.html', context)

def create(request):
    accounts = Account.objects.all()
    for account in accounts:
        account.createdate = account.createdate
        account.editdate = account.editdate
    context = {
        'accounts':accounts
    }

    if request.method == "POST":
        accountid = request.POST.get('accountid')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        birthday = request.POST.get('birthday')
        address = request.POST.get('address')
        phonenumber = request.POST.get('phonenumber')
        email = request.POST.get('email')
        isenable = request.POST.get('isenable')
        note = request.POST.get('note')

        if (firstname == '' or lastname =='' or email =='' or phonenumber == '' or accountid == '' or birthday == '' or address == ''):
            messages.error(request, 'Vui lòng điền đầy đủ các thông tin dấu *')
            return render(request, 'userdetail/userdetail_create.html', context)
        elif (not isEmail(email)):
            messages.error(request, 'Email không hợp lệ')
            return render(request, 'userdetail/userdetail_create.html', context)
        elif (not boolcheckphoneNumber(phonenumber)):
            messages.error(request, 'Số điện thoại không hợp lệ')
            return render(request, 'userdetail/userdetail_create.html', context)
        # elif (boolcheckEmail(email)):
        #     messages.error(request, 'Email này đã được sử dụng cho tài khoản khác')
        #     return render(request, 'userdetail/userdetail_create.html', context)
        else:
            if request.method == 'POST':
                userdetail = UserDetail( 
                                            accountid = Account.objects.get(accountid = accountid),
                                            firstname = firstname, 
                                            lastname = lastname, 
                                            birthday =  birthday,
                                            address = address, 
                                            phonenumber = phonenumber, 
                                            email = email, 
                                            isenable = isenable,
                                            note = note)
                userdetail.save()
                return redirect('/tables_object/')
    
    return render(request, 'userdetail/userdetail_create.html', context)

def edit(request, id):
    userdetail = UserDetail.objects.get(userdetailid = id)
    userdetail.birthday = userdetail.birthday.strftime("%Y-%m-%d")

    accounts = Account.objects.all()
    for account in accounts:
        account.createdate = account.createdate
        account.editdate = account.editdate
    context = {
        'userdetail': userdetail,
        'accounts': accounts
    }

    return render(request, 'userdetail/userdetail_edit.html', context)

def getNum(x):
    return int(''.join(ele for ele in x if ele.isdigit()))
    
def update(request, id):
    userdetail = UserDetail.objects.get(userdetailid = id)
    userdetail.birthday = userdetail.birthday.strftime("%Y-%m-%d")

    accounts = Account.objects.all()
    for account in accounts:
        account.createdate = account.createdate
        account.editdate = account.editdate
    context = {
        'userdetail': userdetail,
        'accounts': accounts
    }

    if request.method == "POST":
        accountid = request.POST.get('accountid')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        birthday = request.POST.get('birthday')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')
        isenable = request.POST.get('isenable')
        note = request.POST.get('note')
    
        if (firstname == '' or lastname =='' or email =='' or phonenumber == ''):
            messages.error(request, 'Vui lòng điền đầy đủ các thông tin dấu *')
            return redirect('/tables_object/userdetail/edit/'+id)
        elif (not isEmail(email)):
            messages.error(request, 'Email không hợp lệ')
            return redirect('/tables_object/userdetail/edit/'+id)
        elif (not boolcheckphoneNumber(phonenumber)):
            messages.error(request, 'Số điện thoại không hợp lệ')
            # return render(request, 'userdetail/userdetail_edit.html', context)
            # x= '/userdetail/edit/'+id
            return redirect('/tables_object/userdetail/edit/'+id)
        else:
            userdetail = UserDetail.objects.filter(userdetailid = id).update(accountid = Account.objects.get(accountid = getNum(accountid)))
            userdetail = UserDetail.objects.get(userdetailid = id)
            userdetail.firstname = firstname
            userdetail.lastname = lastname
            userdetail.birthday = birthday
            userdetail.address = address
            userdetail.phonenumber = phonenumber
            userdetail.email = email
            userdetail.isenable = isenable
            userdetail.note = note
            userdetail.save()
            return redirect('/tables_object/')
    return render(request, 'userdetail/userdetail_edit.html', context)


def delete(request, id):
    userdetail = UserDetail.objects.get(userdetailid =  id)
    userdetail.delete()
    return redirect('/tables_object/')

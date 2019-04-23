from django.shortcuts import render, redirect
from homepage.models import *
# Create your views here.

def admin1 (request):
    if request.session.has_key('username'):
        username = request.session['username']
        account = Account.objects.get(username=username)
        if account.accounttypeid.accounttypeid == 1:
            accounts=Account.objects.all()
            countaccount=len(accounts)
            userdetail=UserDetail.objects.get(accountid=account)
            countadmin=len(Account.objects.filter(accounttypeid=1))
            countteacher=len(Account.objects.filter(accounttypeid=2))
            countstudent=len(Account.objects.filter(accounttypeid=3))
            countenvir=len(EnviromentCate.objects.all())
            countdcourse=len(Subject.objects.all())

            context={
                'countaccount':countaccount,
                'userdetail':userdetail,
                'countenvir':countenvir,
                'countcourse':countdcourse,
                'countadmin':countadmin,
                'countteacher':countteacher,
                'countstudent':countstudent,
                'account':account,
            }
            return render(request, 'adminpage/admin1.html',context)    
        else:
           return redirect('homepage:index') 
    else:
        return redirect('homepage:index')
    

def admin2 (request):
    if request.session.has_key('username'):
        account = Account.objects.get(username = request.session['username'])
        if account.accounttypeid.accounttypeid == 1:
            return render(request, 'adminpage/admin2.html')
        else:
            return redirect('homepage:index')
    else:
        return redirect('homepage:index')

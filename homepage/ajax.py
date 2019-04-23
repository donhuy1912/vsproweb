from django.shortcuts import render, redirect
from django.contrib import messages
from homepage.models import *
from homepage.myfunction import *
from django.core.mail import send_mail
from homepage.myclass import *
from django.http import JsonResponse
from datetime import datetime, timedelta
 
def ajaxsentmes(request):
    
    if request.session.has_key('username'):
        account = Account.objects.get(username=request.session['username'])
        content=request.GET.get('content')
        try:
            chatrooms=ChatRoom.objects.get(accountid=account)
        except:
            chatroomnew=ChatRoom(
                supportid=None,
                accountid=account,
                createdate =  datetime.now(),
            )
            chatroomnew.save()
            chatrooms=ChatRoom.objects.get(accountid=account)
        chat=Chat(
            chatroomid=chatrooms,
            accountid=account,
            createdate =  datetime.now(),
            content=content
        )
        chatrooms.createdate=datetime.now()
        chatrooms.save()
        chat.save()
        data={
            's':True
        }
        return JsonResponse(data)
    else:
        data={
            's':False
        }
        return JsonResponse(data)

def getallmes(request):
    s=''
    if request.session.has_key('username'):
        account = Account.objects.get(username=request.session['username'])
        try:
            chatrooms=ChatRoom.objects.get(accountid=account)
        except:
            chatroomnew=ChatRoom(
                supportid=None,
                accountid=account,
                createdate =  datetime.now(),
            )
            chatroomnew.save()
            chatrooms=ChatRoom.objects.get(accountid=account)
        time_threshold = datetime.now() - timedelta(hours=5)

        chats=Chat.objects.filter(chatroomid=chatrooms).filter(createdate__gte=time_threshold).order_by('createdate')
       
        for chat in chats:
            
            temp='''<div class="chat-message clearfix">
					
					<img src=''' + chat.accountid.avatar +''' alt="" width="32" height="32">

					<div class="chat-message-content clearfix">
						
						<span class="chat-time">'''+ str(chat.createdate.hour) + ''':''' + str(chat.createdate.minute)  +'''</span>
                        <strong>'''+chat.accountid.username+'''</strong>
						<p> '''+ chat.content +''' </p>

					</div> 
					<hr>
				</div>'''
            s=s+temp
        if len(chats) > 0:
            lastid= chats[len(chats)-1].chatid 
        else: 
            lastid=0
        data={

            'flag':True,
            'lastid':lastid,
            's':s
        }
        return JsonResponse(data)
    else:
        data={
            'flag':False,
            's':s
        }
        return JsonResponse(data)

def getmes(request):
    try:
        lastidold=int(request.GET.get('lastid'))
    except:
        lastidold=0
    
    s=''
    if request.session.has_key('username'):
        account = Account.objects.get(username=request.session['username'])
        chatrooms=ChatRoom.objects.get(accountid=account)
        time_threshold = datetime.now() - timedelta(hours=5)
        chats=Chat.objects.filter(chatroomid=chatrooms).filter(createdate__gte=time_threshold).filter(chatid__gt=lastidold).order_by('chatid')
        alllchat=Chat.objects.filter(chatroomid=chatrooms).order_by('chatid')
        
        
        for chat in chats:
            temp='''<div class="chat-message clearfix">
					
					<img src=''' + chat.accountid.avatar +''' alt="" width="32" height="32">

					<div class="chat-message-content clearfix">
						
						<span class="chat-time">'''+ str(chat.createdate.hour) + ''':''' + str(chat.createdate.minute)  +'''</span>
                        <strong>'''+chat.accountid.username+'''</strong>
						<p> '''+ chat.content +''' </p>

					</div> 
					<hr>
				</div>'''
            s=s+temp
        if len(alllchat) > 0:
            lastid= alllchat[len(alllchat)-1].chatid
 
        else: 
            lastid=0
        
        count=lastid-lastidold
        data={
            'count':count,
            'lastid':lastid,
            'flag':True,
            's':s
        }
        return JsonResponse(data)
    else:
        data={
            'flag':False,
            's':s
        }
        return JsonResponse(data)
#admin chat
def getallroomchat(request):
    searoom=request.GET.get('searoom')
    # Nếu == '' thì pass, ngược lại thì tìm
    if searoom != '':
        # tìm chatroom name == search
        accounts = Account.objects.filter(username__icontains=searoom)
        arracc=[]
        for account in accounts:
            arracc.append(account.accountid)
        chatrooms=ChatRoom.objects.filter(accountid__in=arracc).order_by('-createdate')
        
    if searoom == '':
        chatrooms=ChatRoom.objects.order_by('-createdate')
    # else:
    #     # 
    #     chatrooms=[]
    #     tempchatroom=ChatRoom.objects.order_by('-createdate')
    #     for tem in tempchatroom:
    #         if tem.accountid.username__icontains==searoom:
    #             chatrooms.append(tem)
    s=''
    for chatroom in chatrooms:
        chat=Chat.objects.filter(chatroomid=chatroom.chatroomid).order_by("-chatid")[0]
        temp=''' <a id='chatroomlist' href="#"  onclick="changeroom('''+ str(chatroom.chatroomid) +''')">
                                <div class="mail_list">
                                  <div class="left">
                                   
                                  </div>
                                  <div class="right">
                                    <h3 style="color:green">'''+ str(chatroom.accountid.username) +''' <small>'''+ str(chatroom.createdate.hour) + ''':''' + str(chatroom.createdate.minute)  +'''</small></h3>
                                    <p>'''+ chat.content[0:29] +'''</p>
                                  </div>
                                </div>
                              </a>'''
        s=s+temp
    data={
        's':s
    }
    return JsonResponse(data)
def getallmesadmin(request):
    idroom=int(request.GET.get('idroom'))
    s=''
    if request.session.has_key('username'):
        account = Account.objects.get(username=request.session['username'])

        chatrooms=ChatRoom.objects.get(chatroomid=idroom)
        
   
        chats=Chat.objects.filter(chatroomid=chatrooms).order_by('createdate')
        
        for chat in chats:
            temp='''<div class="sender-info">
                            <div class="row">
                              <div class="col-md-12">
                                <strong style='color:green'>''' + chat.accountid.username+ '''</strong>
                                
                                
                              </div>
                            </div>
                          </div>
                          <div class="view-mail">
                            <p>'''+ chat.content +''' </p>
                              <hr>
                                                          
                          </div>'''
            s=s+temp
        if len(chats) > 0:
            lastid= chats[len(chats)-1].chatid 
        else: 
            lastid=0
        data={

            'flag':True,
            'lastid':lastid,
            's':s
        }
        return JsonResponse(data)
    else:
        data={
            'flag':False,
            's':s
        }
        return JsonResponse(data)

def getmesadmin(request):
    idroom=int(request.GET.get('idroom'))
    try:
        lastidold=int(request.GET.get('lastid'))
    except:
        lastidold=0
    
    s=''
    if request.session.has_key('username'):
        account = Account.objects.get(username=request.session['username'])
        chatrooms=ChatRoom.objects.get(chatroomid=idroom)

        chats=Chat.objects.filter(chatroomid=chatrooms).filter(chatid__gt=lastidold).order_by('chatid')
        alllchat=Chat.objects.filter(chatroomid=chatrooms).order_by('chatid')
        for chat in chats:
            temp='''<div class="sender-info">
                            <div class="row">
                              <div class="col-md-12">
                                <strong style='color:green'>''' + chat.accountid.username+ '''</strong>
                                
                                
                              </div>
                            </div>
                          </div>
                          <div class="view-mail">
                            <p>'''+ chat.content +''' </p>
                              <hr>
                                                          
                          </div>'''
            s=s+temp
        if len(alllchat) > 0:
            lastid= alllchat[len(alllchat)-1].chatid
        else: 
            lastid=0
        
        count=lastid-lastidold
        data={
            'count':count,
            'lastid':lastid,
            'flag':True,
            's':s
        }
        return JsonResponse(data)
    else:
        data={
            'flag':False,
            's':s
        }
        return JsonResponse(data)

def sentmesadmin(request):
    
    if request.session.has_key('username'):
        account = Account.objects.get(username=request.session['username'])
        content=request.GET.get('content')
        idroom=int(request.GET.get('idroom'))
        
        chatrooms=ChatRoom.objects.get(chatroomid=idroom)
        
        chat=Chat(
            chatroomid=chatrooms,
            accountid=account,
            createdate =  datetime.now(),
            content=content
        )
        chatrooms.createdate=datetime.now()
        chatrooms.save()
        chat.save()
        data={
            's':True
        }
        return JsonResponse(data)
    else:
        data={
            's':False
        }
        return JsonResponse(data)
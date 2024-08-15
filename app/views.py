from django.shortcuts import render
import datetime
# Create your views here.
def filters(request):
    
    d={'data':'this IS Built iN fILTers','time':datetime.datetime.now(),'c':10}
  
    
    return render(request,'filters.html',d)

def usdf(request):
    d1={'owndata':'tHIs Is userDEFined Filters'}
    return render(request,'usdf.html',d1)
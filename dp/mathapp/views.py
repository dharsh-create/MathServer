from django.shortcuts import render
def rectarea(request):
    context={}
    context['area'] = "0"
    context['1']= "0"
    context['b']= "0"
    if request.method == 'POST':
        print("POST method is used")
        l = request.POST.get('length', '0')
        b = request.POST.get('breadth', '0')
        print('request=',request)
        print('Length=',l)
        print('Breadth=',b)
        area = int(1) * int(b)
        context['area'] = area
        context['1'] = 1
        context['b'] = b
        print('Area =', area)
    return render(request,'myapp/math.html',context)

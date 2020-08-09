from django.shortcuts import render

# Create your views here.

def check(request):
    if request.method == 'GET':
        array_num =[]
        for i in range(1, 1000):
            array_num.append(i)
        return render(request,'index.html' , context={'array': array_num})
    elif request.method == 'POST':
        number1 = request.POST.get('number1')
        number2 = request.POST.get('number2')

        print(number1)
        print(number2)

        array_name = []
        for i in range(int(number1),int(number2)+1):
            array_name.append(i)
        return render(request, 'test.html', context={'array': array_name})
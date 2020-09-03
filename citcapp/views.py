from django.shortcuts import render,redirect
from django.views.generic import View
from citcapp.models import CustomerModel,CityModel
from citcapp.forms import CustomerForm, CityForm

class ShowIndex(View):
    def post(self, request):
        cf = request.POST["b1"]
        if cf == "city":
            cty = CityForm(request.POST)
            if cty.is_valid():
                cty.save()
                return redirect("index")
            else:
                return render(request, "index.html",{"ctf": cty, "cuf": CustomerForm()})
        else:
            cus = CustomerForm(request.POST)
            if cus.is_valid():
                cus.save()
                return redirect("index")
            else:
                return render(request, "index.html", {"cus": cus, "ctf": CityForm()})
    def get(self, request):
        ct_all = CityModel.objects.all()
        cu_all = CustomerModel.objects.all()
        return render(request, "index.html",{"ctf": CityForm(), "cuf": CustomerForm(),"call": ct_all, "cuall":cu_all})


class Delete(View):
    def get(self, request):
        d = request.GET['did']
        CityModel.objects.filter(pin_code=d).delete()
        return redirect("index")

from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import make_password
from store.models import Customer

class Updateprofile(View):

    def get(self, request):
        return render(request, 'store/profile.html')

    def post(self, request):
        customor = request.POST
        customorId = request.session["customer"]
        # validate
        error = self.validateData(customor)
        if error:
            return render(request, 'store/profile.html', {"error": error, "customor": customor})
        else:
            emails=[]
            exist = False
            customors=Customer.objects.all()
            for c in customors:
                if c.id != customorId:
                    emails.append(Customer.objects.get(id=customorId))
            for e in emails:
                if e.email == customor['email']:
                    exist=True

            if not exist:
                error["emailExits_error"] = "Email Already Exits"
                return render(request, 'store/profile.html', {"error": error, "customor": customor})
            else:

                Customer.objects.filter(id=customorId).update(name=customor['name'],
                    email=customor['email'],
                    phone=customor['phone'],
                    password=make_password(customor['password']),)


                return redirect('store')

    # Validate form method
    def validateData(self, customor):
        error = {}
        if not customor['name'] or not customor['email'] or not customor['phone'] or not customor['password'] or not \
        customor['confirm_password']:
            error["field_error"] = "All field must be required"
        elif len(customor['password']) < 8 and len(customor['confirm_password']) < 8:
            error['minPass_error'] = "Password must be 8 char"
        elif len(customor['name']) > 25 or len(customor['name']) < 3:
            error["name_error"] = "Name must be 3-25 charecter"
        elif len(customor['phone']) != 10:
            error["phoneNumber_error"] = "Phone number must be 10 charecter."
        elif customor['password'] != customor['confirm_password']:
            error["notMatch_error"] = "Password doesn't match"

        return error
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Hospital.models import patient
import json

# Function used for getting patient information using "GET"
# Function used for creating patient information using "POST"
@csrf_exempt
def view_get_post_patient(request):
    print("What's the request => ",request.method)
    if request.method == "GET":
        patients=patient.objects.all()
        print("QuerySet objects => ",patients)
        list_of_patients = list(patients.values("patientName",
        "patientAddress","patientPhoneNo","patientAge","patientSex"))
        # list_of_patient=patient.objects.all()
        print("List of Patient objects => ",list_of_patients)
        dictionary_name = {
        "patients":list_of_patients
    }
        return JsonResponse(dictionary_name)
    elif request.method == "POST":
        print("Request body content =>", request.body)
        print("Request body type =>", type(request.body))
        python_dictionary_object = json.loads(request.body)
        print("Python dictionary contents=>",python_dictionary_object)
        print("Python dictionary type=>",type(python_dictionary_object))
        print(python_dictionary_object['patientName'])
        print(python_dictionary_object['patientAddress'])
        print(python_dictionary_object['patientPhoneNo'])
        print(python_dictionary_object['patientAge'])
        print(python_dictionary_object['patientSex'])
        patient.objects.create(patientName=python_dictionary_object['patientName']
        ,patientAddress=python_dictionary_object['patientAddress'],
        patientPhoneNo=python_dictionary_object['patientPhoneNo'],
        patientAge=python_dictionary_object['patientAge'],
        patientSex=python_dictionary_object['patientSex'])
        
        return JsonResponse({
            "message":"Successfully posted!!"
        })    
    else:
        return HttpResponse("Other HTTP verbs testing")

# Function used for getting patient information through ID "GET"
@csrf_exempt
def view_getByID_updateByID_deleteByID(request,ID):
    print("What's the request =>",request.method)
    if request.method == "GET":
        patients=patient.objects.get(id=ID)
        # print(type(patient.code))
        return JsonResponse({
            "id":patients.id,
            "patientName":patients.patientName,
            "patientAddress":patients.patientAddress,
            "patientPhone":patients.patientPhoneNo,
            "patientAge":patients.patientAge,
            "patientSex":patients.patientSex
        })
        return JsonResponse({
        "message":" Other htpp verbs Testing"
        }) 

from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Hospital.models import patient
import json


# Function for getting patients information using "GET"
# Function for Creating patients information using "POST"

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

# Function for getting patients information through ID
# Function for updating patients information through ID
# Function for deleting patients information through ID
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
    # Deletion
    elif request.method =="DELETE":
        patients = patient.objects.get(id = ID)
        patients.delete()
        return JsonResponse({
            "message":"Successfully deleted!!"
        })
    # Updating
    elif request.method == "PUT":
        update = json.loads(request.body)
        patients = patient.objects.get(id = ID)
        patients.patientName = update['patientName']
        patients.patientAddress = update['patientAddress']
        patients.patientPhoneNo = update['patientPhoneNo']
        patients.patientAge = update['patientAge']
        patients.patientSex = update['patientSex']
        patients.save()
        return JsonResponse({
            "message":"Successfully Updated!!"})

    else:
        return JsonResponse({
        "message":" Other htpp verbs Testing"
        })

# Function for pagination

@csrf_exempt
def view_patient_pagination(request,CONTENT_NUMBER, PAGENO):
    if request.method == 'GET':
        first = ((PAGENO -1)* CONTENT_NUMBER)# determine which is the first content that is required to show in page
        last = first + CONTENT_NUMBER#determine the last content that is required to show in page
        patients=patient.objects.values()[first:last]#rent and assign all data(objects) of patient model and only show data between first and last
        return JsonResponse({
        "patients":list(patients.values("patientName","patientAddress","patientPhoneNo","patientAge","patientSex"))
        })#return or output json object of patient with help of json responce which work as dums() methon
    else:
        return JsonResponse({
            "message":"There is not enough data for pagination, please store more data for pagination"
        })#error message if there is not enough data to paginate


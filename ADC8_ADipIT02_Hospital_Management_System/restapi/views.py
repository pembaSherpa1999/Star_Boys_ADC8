from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Hospital.models import patient
import json


@csrf_exempt
#pagination to show number of file according to pagenumber
def view_patient_pagination(request,CONTENT_NUMBER,PAGENO):
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


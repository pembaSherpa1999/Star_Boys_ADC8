from django.shortcuts import render

# Create your views here.
        #views.py file
def index(request):
#gets all patients
    patients = patient.objects.all()
    context = {
        'patients': patients
    }
# pass the context object to be rendered in the index file
    return render(request, 'index.html', context)

          #index.html file
{#loop through the patient db and display individual records#}
    {% for patient in patients %}
        <li> {{ patientt.first_name }} {{ patientt.last_name }} {{ patient.major }}  patient.year }}</li>
    {% endfor %}

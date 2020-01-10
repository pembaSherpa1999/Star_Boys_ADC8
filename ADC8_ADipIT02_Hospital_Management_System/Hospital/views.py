from django.shortcuts import render

# View function file for Update functionality

def update_record(request,id):
    instance = Hospital.objects.get(id=id)

    # Update the form with the data obtained above

    form = HospitalForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'update.html', {'form': form})



# ...index.html file(Use this code in index.html page)

# {#This is the loop through the Hospital db and display individual records#}
    {% for hospital in hospitals %}
        <li> {{ hospital.patient_first_name }} {{ hospital.patient_middle_name }} {{ hospital.patient_last_name }}  {{ hospital.patient_age }}</li>

# {#this add the line below#}
<a href="{% url 'delete' Hospital.id %}">Delete Record</a>

# ...views.py file(View function for Delete)
def delete_record(request,id):
    # this get the object from the Hospital db
    record = Hospital.objects.get(id=id)
    record.delete()
    return redirect('index')
    
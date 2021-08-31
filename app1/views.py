from django.shortcuts import render
from .models import StudentDB, Attendance
from pprint import pprint

# Create your views here.
def index(request):
    '''
    d = {
        'name': 'tarun',
        'class':'13th', 
        'DOB': '4327498327424',
        'arr': [ 2*i for i in range(1,11) ],
        'di': {'name': 'Akash Omar', 'class': '13','college': 'BCA'}
    }
    return render(request, 'index.html', d)
    '''
    return render(request, 'index.html')
    
    
def submit(request):
    err = []
    
    st_name = request.POST.get('name')
    if(st_name == ''):
        err.append('name')
        
    st_address = request.POST.get('address')
    if(st_address == ''):
        err.append('address')
        
    st_class = request.POST.get('class')
    if(st_class == ''):
        err.append('class')
        
    st_phone = request.POST.get('phone')
    if(st_phone == ''):
        err.append('phone')
        
    st_gender = request.POST.get('gender')
    if(st_gender == ''):
        err.append('gender')
        
    if(err):
        return render( request, 'details.html', {'error': ', '.join(err)} )
    else:
        st_DB_Obj = StudentDB(Name=st_name, Address=st_address, Class=st_class, Phone=st_phone, Gender=st_gender)
        st_DB_Obj.save()
        return render( request, 'details.html', {'success': 'Details Saved Successfully'} )
        
def getStudents(request):
    studentDetailsObj = StudentDB.objects.all()
    #studentDetailsObj = StudentDB.objects.filter(Name='Tarun')

    details = []
    if(studentDetailsObj):
        for i in studentDetailsObj:
            details.append({
                'rollno': i.RollNo,
                'name': i.Name,
                'address': i.Address,
                'class': i.Class,
                'phone': i.Phone,
                'gender': i.Gender,
            })
    return render( request, 'showStudentDetails.html', {'details': details} )
    
def add_attendance(request, rollno):
    studentDetailsObj = StudentDB.objects.get(RollNo=rollno)
    if(request.POST.get('attendance') != None):
        date = request.POST.get('date')
        attend = request.POST.get('attendance')

        attendance_obj = Attendance(RollNo=studentDetailsObj, Date=date, Attendance=attend)
        attendance_obj.save()
        return render(request, 'addattendance.html', { 'status': "Attendance saved successfully" })
    else:
        return render(request, 'addattendance.html', {'rollno': rollno, 'name': studentDetailsObj.Name})
    

def show_attendance(request, rollno):
    studentDetailsObj = StudentDB.objects.get(RollNo=rollno)
    attendance_obj = Attendance.objects.filter(RollNo=studentDetailsObj)
    details = []
    if(attendance_obj):
        for i in attendance_obj:
            rollno = i.RollNo.RollNo
            name = i.RollNo.Name
            date = i.Date
            attendance = i.Attendance
            
            details.append({
                'rollno': rollno,
                'name': name,
                'date': date,
                'attendance': attendance,
            })
        return render(request, 'showattendance.html', {'details': details})
    else:
        return render(request, 'showattendance.html', {'status': f"No Attendance found for Roll No: {rollno}"})
    
    
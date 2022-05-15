from flask import *
from DbPackage.dbconnection import Db

app=Flask(__name__)

app.secret_key="hi"

db = Db()

@app.route('/')
def load_login():
    return render_template('login.html')

@app.route('/action_log',methods=['get','post'])
def acion_log():
    username=request.form['username']
    password=request.form['password']
    qry="SELECT * FROM `login` WHERE (`email`='"+username+"' AND`password`='"+password+"') "
    print(qry)
    res=db.selectone(qry)
    if res is not None:
        utype=res['usertype']
        lid=res['log_id']
        session['lid']=lid
        session['utype']=utype
        if utype=='admin':
            return redirect(url_for('load_adminhome'))
        elif utype=='health':
            return redirect(url_for('load_healthHome'))
        else:
            return redirect(url_for('load_login'))
    else:
        return redirect(url_for('load_login'))

@app.route('/adminhome')
def load_adminhome():
    return render_template('admin.html')

@app.route('/healthHome')
def load_healthHome():
    return render_template('health department.html')



@app.route('/add_health_page_load')
def add_health_page_load():
    return render_template('add health.html')

@app.route('/add_health',methods=['get','post'])
def add_health():
    name=request.form['name']
    address=request.form['address']
    license=request.form['license']
    phone=request.form['phone']
    email=request.form['email']
    password=request.form['Password']
    q="insert into login(email,password,usertype) values ('"+email+"','"+password+"','health')"
    lid=db.insert(q)
    qry="insert into health_reg(health_name,health_login_id,address,phone,license,email)values('"+name+"','"+str(lid)+"','"+address+"','"+phone+"','"+license+"','"+email+"')"
    res=db.insert(qry)
    if res>0:
        return redirect(url_for('add_health_page_load'))
    else:
        return "Error..."


@app.route('/view_health')
def view_health():
    qry="SELECT * FROM `health_reg`"
    res=db.select(qry)
    return render_template('view H D name.html',data=res)


@app.route('/edit_health_details/<id>')
def edit_health_details(id):
    qwa="SELECT * FROM `health_reg` where health_department_id='"+str(id)+"'"
    res = db.selectone(qwa)
    print(res)
    return render_template('edit healthdept.html',data=res)


@app.route('/health_edit',methods=['get','post'])
def health_edit():
    id=request.form['id']
    name = request.form['name']
    address = request.form['address']
    license = request.form['license']
    phone = request.form['phone']
    email = request.form['email']
    q="UPDATE `health_reg`SET `health_name`='"+name+"',address='"+address+"',`phone`='"+phone+"',`license`='"+license+"',`email`='"+email+"' WHERE health_department_id='"+str(id)+"'"
    result=db.update(q)
    if result>0:
        return redirect(url_for('view_health'))
    else:
        return redirect(url_for('view_health'))

@app.route('/delete_health/<id>')
def delete_health(id):
    qsd="delete from health_reg where health_department_id='"+str(id)+"'"
    db.delete(qsd)
    return redirect(url_for('view_health'))

@app.route('/viewPages')
def viewpages():
    q="select * from health_reg"
    result=db.select(q)
    return render_template('AdminViewPages.html',data=result)

@app.route('/SelectPage',methods=['get','post'])
def selectpage():
    hlid=request.form['hlid']
    select=request.form['select']
    session['lid']=hlid
    if select=="Asha Workers":
        return redirect(url_for('view_ashaworker'))
    elif select=="Volunteers":
        return redirect(url_for('view_volunteer'))
    else:
        return redirect(url_for('view_quarantineHouse'))

@app.route('/add_emergencyoption_page_load')
def add_emergencyoption_page_load():
    return render_template('emergncy option.html')

@app.route('/add_emergencyoption',methods=['get','post'])
def add_emergencyoption():
    option=request.form['emergency']
    q="INSERT INTO`emergency_option`(`emergency_option`) VALUES('"+option+"')"
    result=db.insert(q)
    return render_template('emergncy option.html')

@app.route('/view_emergencyoption')
def view_emergencyoption():
    q="SELECT * FROM`emergency_option` "
    result=db.select(q)
    return render_template('view emergency.html',data=result)

@app.route('/delete_emergency/<id>')
def delete_emergency(id):
    q="delete from emergency_option where `emergency_id`='"+str(id)+"'"
    db.delete(q)
    return redirect(url_for('view_emergencyoption'))

@app.route('/add_ashaworker_page_load')
def add_ashaworker_page_load():
    return render_template('add ashaworker.html')

@app.route('/add_ashaworker',methods=['get','post'])
def add_ashaworker():

    name=request.form['name']
    photo=request.files['photo']
    address=request.form['address']
    phone=request.form['phone']
    email=request.form['email']
    pin=request.form['pin']
    gender=request.form['radio']
    aadharno=request.form['aadharno']
    password=request.form['pwd']
    hlid=session['lid']
    print(email,password)
    q="insert into login(email,password,usertype) values ('"+email+"','"+password+"','ashaworker')"
    lid=db.insert(q)
    ext = str.split(photo.filename, '.')
    ext1 = ext[len(ext) - 1]
    filename = str(lid) + "." + ext1
    path = "C:\\Users\\UNAIS\\PycharmProjects\\covi care\\src\\static\\ashaworkerPics\\" + filename
    photo.save(path)
    q1="INSERT INTO `asha_worker`(health_login_id,asha_worker_name,asha_worker_login_id,photo,address,phone,email,pin,gender,aadhar_no)VALUES('"+str(hlid)+"','"+name+"','"+str(lid)+"','"+filename+"','"+address+"','"+phone+"','"+email+"','"+pin+"','"+gender+"','"+aadharno+"')"
    res=db.insert(q1)
    return render_template('add ashaworker.html')

@app.route('/view_ashaworker')
def view_ashaworker():
    hlid=session['lid']
    q="select * from asha_worker where health_login_id='"+str(hlid)+"'"
    res=db.select(q)
    return render_template('view ashaworker.html',data=res)

@app.route('/add_volunteer_page_load')
def add_volunteer_page_load():
    return render_template('add volunteer.html')

@app.route('/add_volunteer',methods=['get','post'])
def add_volunteer():
    name=request.form['name']
    address=request.form['address']
    phone=request.form['phone']
    email=request.form['email']
    photo=request.files['photo']
    age=request.form['age']
    password=request.form['password']
    hlid=session['lid']
    q="insert into login(email,password,usertype) values ('"+email+"','"+password+"','volunteer')"
    lid=db.insert(q)
    ext = str.split(photo.filename, '.')
    ext1 = ext[len(ext) - 1]
    filename = str(lid) + "." + ext1
    path = "C:\\Users\\UNAIS\\PycharmProjects\\covi care\\src\\static\\volunteerPics\\" + filename
    photo.save(path)
    q1="insert into volunter_reg(user_name,volunteer_login_id,health_login_id,address,phone,email,photo,age) values('"+name+"','"+str(lid)+"','"+str(hlid)+"','"+address+"','"+phone+"','"+email+"','"+filename+"','"+age+"')"
    res=db.insert(q1)
    return render_template('add volunteer.html')

@app.route('/view_volunteer')
def view_volunteer():
    hlid=session['lid']
    q="select * from volunter_reg where health_login_id='"+str(hlid)+"'"
    res=db.select(q)
    return render_template('view volunteer.html',data=res)


@app.route('/view_quarantineHouse')
def view_quarantineHouse():
    hlid=session['lid']
    q="select house.*,asha_worker.asha_worker_name from house,asha_worker where house.ashaworker_login_id=asha_worker.asha_worker_login_id and asha_worker.health_login_id='"+str(hlid)+"'"
    res=db.select(q)
    return render_template('HouseDetails.html',data=res)

@app.route('/view_HouseMembers/<id>')
def view_housemembers(id):
    q="select * from house where house_id='"+id+"'"
    res=db.selectone(q)
    print(q)
    print(res)
    q1="select house_members.*,health_status.* from house_members,health_status where health_status.member_login_id=house_members.member_login_id and house_members.house_id='"+id+"'"
    result=db.select(q1)
    print(result)
    return render_template('members list.html',data=res,data1=result)

@app.route('/view_medicineRequest')
def view_medicineRequest():
    hlid=session['lid']
    q="select house_members.*,house.*,medicine_request.* from medicine_request,house_members,house,asha_worker where medicine_request.member_lid=house_members.member_login_id and house_members.house_id=house.house_id and house.ashaworker_login_id=asha_worker.asha_worker_login_id and asha_worker.health_login_id='"+str(hlid)+"'"
    res=db.select(q)
    return render_template('approval.html',data=res)

@app.route('/update_statusApprove/<id>')
def update_statusApprove(id):
    q="update medicine_request set status='Approved' where request_id='"+str(id)+"'"
    res = db.update(q)
    if res>0:
        return redirect(url_for('view_medicineRequest'))
    else:
        return redirect(url_for('view_medicineRequest'))

@app.route('/update_statusReject/<id>')
def update_statusReject(id):
    q="update medicine_request set status='Rejected' where request_id='"+str(id)+"'"
    res = db.update(q)
    if res>0:
        return redirect(url_for('view_medicineRequest'))
    else:
        return redirect(url_for('view_medicineRequest'))

if __name__=='__main__':

    app.run(debug=True)





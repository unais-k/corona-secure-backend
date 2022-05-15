import base64

import datetime as DT
from flask import *
import demjson
from DbPackage.dbconnection import Db


app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"


@app.route('/Login',methods=['POST'])
def login():
    r = {}
    db = Db()
    email=request.form['email']
    pwd=request.form['pwd']

    q1="delete from quarantine_duration where dateout=curdate()"
    res=db.delete(q1)
    q = "SELECT * FROM `login` WHERE email='"+email+"' AND `password`='"+pwd+"'"
    result = db.selectone(q)
    if result!=None:
        r['status'] = "success"
        r['lid'] = result['log_id']
        r['usertype'] = result['usertype']
    else:
        r['status'] = "failed"
    print(demjson.encode(r))
    return demjson.encode(r)


@app.route('/ViewAshaWorkerProfile',methods=['POST'])
def viewAshaWorkerProfile():
    r = {}
    db = Db()
    lid=request.form['lid']
    utype=request.form['utype']
    if utype=="ashaworker":
        q = "select asha_worker.*,health_reg.health_name from asha_worker,health_reg where health_reg.health_login_id=asha_worker.health_login_id and asha_worker.asha_worker_login_id='"+lid+"'"
    else:
        q="select asha_worker.*,health_reg.health_name from asha_worker,health_reg,house,house_members where health_reg.health_login_id=asha_worker.health_login_id and asha_worker.asha_worker_login_id=house.ashaworker_login_id and house.house_id=house_members.house_id and house_members.member_login_id='"+lid+"'"
    result = db.selectone(q)
    if result!=None:
        r['status'] = "success"
        r['name'] = result['asha_worker_name']
        r['photo'] = result['photo']
        r['phone'] = result['phone']
        r['address'] = result['address']
        r['pin'] = result['pin']
        r['gender'] = result['gender']
        r['aadhar_no'] = result['aadhar_no']
        r['email'] = result['email']
        r['healthName'] = result['health_name']
    else:
        r['status'] = "failed"
    print(demjson.encode(r))
    return demjson.encode(r)

@app.route('/ViewVolunteerProfile',methods=['POST'])
def viewVounteerProfile():
    r = {}
    db = Db()
    lid=request.form['lid']
    q="select volunter_reg.*,health_reg.health_name from volunter_reg,health_reg where health_reg.health_login_id=volunter_reg.health_login_id and volunter_reg.volunteer_login_id='"+lid+"'"
    result = db.selectone(q)
    if result!=None:
        r['status'] = "success"
        r['name'] = result['user_name']
        r['photo'] = result['photo']
        r['phone'] = result['phone']
        r['age'] = result['age']
        r['email'] = result['email']
        r['address'] = result['address']
        r['healthName'] = result['health_name']
    else:
        r['status'] = "failed"
    print(demjson.encode(r))
    return demjson.encode(r)

@app.route('/AddFamily',methods=['POST'])
def addFamily():
    r = {}
    db = Db()
    lid = request.form['lid']
    hname = request.form['hname']
    hno = request.form['hno']
    rno = request.form['rno']

    address = request.form['address']
    q="insert into house(house_name,house_no,address,ration_card_no,ashaworker_login_id) values('"+hname+"','"+hno+"','"+address+"','"+rno+"','"+lid+"')"
    result = db.insert(q)

    today = DT.date.today()
    week_ago = today + DT.timedelta(days=14)
    print("date out is " + str(week_ago))

    q1="INSERT INTO `quarantine_duration`(houseid,datein,dateout) VALUES('"+str(result)+"',CURDATE(),'"+str(week_ago)+"')"
    res=db.insert(q1)
    if (result > 0):
        r['status'] = "success"
    else:
        r['status'] = "failed"
    print(demjson.encode(r))
    return demjson.encode(r)

@app.route('/ViewHouseDetails',methods=['POST'])
def viewHouseDetails():
    r = {}
    db = Db()
    lid = request.form['lid']
    utype = request.form['utype']
    if utype == "ashaworker":
        q = "select * from house where ashaworker_login_id='" + lid + "'"
    else:
        q = "SELECT `house`.* FROM house,`asha_worker`,`volunter_reg` WHERE `house`.`ashaworker_login_id`=`asha_worker`.`asha_worker_login_id` AND `asha_worker`.`health_login_id`=`volunter_reg`.`health_login_id` AND `volunter_reg`.`volunteer_login_id`='"+lid+"'"
    result = db.select(q)
    if (len(result) > 0):
        r['status'] = "success"
        r['results'] = result
    else:
        r['status'] = "failed"
    print(demjson.encode(r))
    return demjson.encode(r)

@app.route('/AddFamilyMemeber',methods=['POST'])
def addFamilyMember():
    r = {}
    db = Db()
    name = request.form['name']
    gender = request.form['gender']
    age = request.form['age']
    houseid = request.form['houseid']
    aadhar = request.form['adarno']
    photo = request.form['photo']
    covid = request.form['covid']
    print(name)
    q = "insert into login(email,password,usertype) values ('"+name+"','"+aadhar+"','member')"
    lid = db.insert(q)

    filename = str(lid) + ".jpg"

    a = base64.b64decode(photo)

    # path = "C:\\Users\\USER\\PycharmProjects\\unaiscovicare\\covi care\\src\\static\\ashaworkerPics\\" + filename

    fh = open("C:\\Users\\UNAIS\\PycharmProjects\\covi care\\src\\static\\MemberPics\\" + filename,
              "wb")
    path = "/MemberPics/" + filename
    fh.write(a)
    fh.close()


    qry = "insert into house_members(house_id,member_name,member_login_id,gender,age,photo,covid_positive,aadhar_no) values ('"+houseid+"','"+name+"','"+str(lid)+"','"+gender+"','"+age+"','"+filename+"','"+covid+"','"+aadhar+"')"
    result = db.insert(qry)
    q1 = "insert into health_status(status_id,member_login_id,temperature,heartbeat,cough,status) values(null,"+ str(lid)+",'nodata','nodata','nodata','positive')"
    result1 = db.insert(q1)
    if (result1 > 0):
        r['status'] = "success"
    else:
        r['status'] = "failed"
    #print(demjson.encode(r))
    return demjson.encode(r)

@app.route('/ViewMembers',methods=['POST'])
def viewMembers():
    r = {}
    db = Db()
    houseid=request.form['houseid']
    q = "SELECT * FROM house_members WHERE house_id='"+houseid+"'"
    result = db.select(q)
    if (len(result) > 0):
        r['status'] = "success"
        r['results'] = result
    else:
        r['status'] = "failed"
    print(demjson.encode(r))
    return demjson.encode(r)

@app.route('/MemberHealthStatus',methods=['POST'])
def MemberHealthStatus():
    r = {}
    db = Db()
    mlid=request.form['mlid']
    q = "SELECT * FROM `health_status` WHERE `member_login_id`='"+mlid+"'"
    result = db.select(q)
    if (len(result) > 0):
        r['status'] = "success"
        r['results'] = result
    else:
        r['status'] = "failed"
    print(demjson.encode(r))
    return demjson.encode(r)

@app.route('/ViewVolunteers',methods=['POST'])
def viewVolunteers():
    r = {}
    db = Db()
    lid=request.form['lid']
    q = "select volunter_reg.* from volunter_reg,health_reg,asha_worker,house,house_members where volunter_reg.health_login_id=health_reg.health_login_id and health_reg.health_login_id=asha_worker.health_login_id and asha_worker.asha_worker_login_id=house.ashaworker_login_id and house.house_id=house_members.house_id and house_members.member_login_id='"+lid+"'"
    result = db.select(q)
    if (len(result) > 0):
        r['status'] = "success"
        r['results'] = result
    else:
        r['status'] = "failed"
    print(demjson.encode(r))
    return demjson.encode(r)

@app.route('/ViewEmergencyOptions')
def viewEmergencyOptions():
    r = {}
    db = Db()
    q = "select * from emergency_option"
    result = db.select(q)
    if (len(result) > 0):
        r['status'] = "success"
        r['results'] = result
    else:
        r['status'] = "failed"
    print(demjson.encode(r))
    return demjson.encode(r)

@app.route('/SendEmergencyOptionRequest',methods=['POST'])
def sendEmergencyOptionRequest():
    r = {}
    db = Db()
    emid = request.form['emid']
    lid = request.form['lid']
    q = "insert into emergency_request(emergency_id,member_logid,date) values('"+emid+"','"+lid+"',curdate())"
    result = db.insert(q)
    if (result > 0):
        r['status'] = "success"
    else:
        r['status'] = "failed"
    print(demjson.encode(r))
    return demjson.encode(r)

@app.route('/ViewEmergencyRequest',methods=['POST'])
def viewEmergencyRequest():
    r = {}
    db = Db()
    utype = request.form['utype']
    lid = request.form['lid']
    if utype=="ashaworker":
        q = "select emergency_request.*,emergency_option.*,house_members.*,house.* from emergency_option,emergency_request,house,house_members where emergency_option.emergency_id=emergency_request.emergency_id and emergency_request.status='Pending' and emergency_request.member_logid=house_members.member_login_id and house_members.house_id=house.house_id and house.ashaworker_login_id='"+lid+"'"
    else:
        q="select emergency_request.*,emergency_option.*,house_members.*,house.* from emergency_option,emergency_request,house,house_members,asha_worker,volunter_reg where emergency_option.emergency_id=emergency_request.emergency_id and emergency_request.status='Pending' and emergency_request.member_logid=house_members.member_login_id and house_members.house_id=house.house_id and house.ashaworker_login_id=asha_worker.asha_worker_login_id and asha_worker.health_login_id=volunter_reg.health_login_id and volunter_reg.volunteer_login_id='"+lid+"'"
    result = db.select(q)
    if (len(result) > 0):
        r['status'] = "success"
        r['results'] = result
    else:
        r['status'] = "failed"
    print(demjson.encode(r))
    return demjson.encode(r)

@app.route('/EmergencyRequestUpdate',methods=['POST'])
def requestUpdate():
    r = {}
    db = Db()
    reqid = request.form['reqid']
    q = "update emergency_request set status='Completed' where requestid='"+reqid+"'"
    result = db.update(q)
    if (result > 0):
        r['status'] = "success"
    else:
        r['status'] = "failed"
    print(demjson.encode(r))
    return demjson.encode(r)

@app.route('/ViewApprovedMedicineRequest',methods=['POST'])
def ViewApprovedMedicineRequest():
    r = {}
    db = Db()
    lid = request.form['lid']
    q = "SELECT `medicine_request`.*,`house_members`.*,`house`.* FROM `house`,`house_members`,`medicine_request` WHERE `medicine_request`.`status`='Approved' AND `medicine_request`.`member_lid`=`house_members`.`member_login_id` AND `house_members`.`house_id`=`house`.`house_id` AND `house`.`ashaworker_login_id`='"+lid+"' ORDER BY `house`.`house_id`"
    result = db.select(q)

    if (len(result) > 0):
        r['status'] = "success"
        r['results'] = result
    else:
        r['status'] = "failed"
    print(demjson.encode(r))
    return demjson.encode(r)

@app.route('/MedicineRequestUpdate',methods=['POST'])
def MedicineRequestUpdate():
    r = {}
    db = Db()
    reqid = request.form['reqid']
    q = "UPDATE `medicine_request` SET STATUS='Delivered' WHERE `request_id`='"+reqid+"'"
    result = db.update(q)
    if (result > 0):
        r['status'] = "success"
    else:
        r['status'] = "failed"
    print(demjson.encode(r))
    return demjson.encode(r)

@app.route('/ViewMedicineRequest',methods=['POST'])
def viewMedicineyRequest():
    r = {}
    db = Db()
    lid = request.form['lid']
    q = "SELECT `medicine_request`.*,house_members.*,house.* FROM `medicine_request`,house,house_members WHERE `medicine_request`.member_lid=house_members.member_login_id AND `medicine_request`.status='Approved' AND house_members.house_id=house.house_id AND house.ashaworker_login_id='"+lid+"'"
    result = db.select(q)
    if (len(result) > 0):
        r['status'] = "success"
        r['results'] = result
    else:
        r['status'] = "failed"
    print(demjson.encode(r))
    return demjson.encode(r)

@app.route('/MedicineRequestStatus',methods=['POST'])
def MedicineRequestStatus():
    r = {}
    db = Db()
    lid = request.form['lid']
    q = "SELECT `medicine_request`.* FROM `medicine_request` WHERE `member_lid`='"+lid+"'"
    result = db.select(q)
    if (len(result) > 0):
        r['status'] = "success"
        r['results'] = result
    else:
        r['status'] = "failed"
    print(demjson.encode(r))
    return demjson.encode(r)

@app.route('/SendMedicineRequest',methods=['POST'])
def sendMedicineRequest():
    r = {}
    db = Db()
    mnam = request.form['mnam']
    description = request.form['details']
    mlid = request.form['lid']
    q = "INSERT INTO `medicine_request`(`member_lid`,`medicine_name`,`description`,`date`,`status`) VALUES('"+mlid+"','"+mnam+"','"+description+"',CURDATE(),'Pending')"
    result = db.update(q)
    if (result > 0):
        r['status'] = "success"
    else:
        r['status'] = "failed"
    print(demjson.encode(r))
    return demjson.encode(r)

@app.route('/ViewNearestHouse',methods=['POST'])
def ViewNearestHouse():
    r = {}
    db = Db()
    lid = request.form['lid']
    q = "SELECT `house`.* FROM `house` WHERE `ashaworker_login_id`=(SELECT `ashaworker_login_id` FROM house,`house_members` WHERE `house_members`.`member_login_id`='"+lid+"' AND `house_members`.`house_id`=`house`.`house_id`)"
    result = db.select(q)
    if (len(result) > 0):
        r['status'] = "success"
        r['results'] = result
    else:
        r['status'] = "failed"
    print(demjson.encode(r))
    return demjson.encode(r)
@app.route('/insert_readings',methods=['get','post'])
def insert_readings():
    r={}
    db = Db()
    temp=request.form['temp']
    hbeat=request.form['hbeat']
    cough=request.form['sound']
    print(temp)
    q = "update health_status set temperature='"+temp+"',heartbeat='"+hbeat+"',cough='"+cough+"' where member_login_id=33"
    result = db.update(q)
    if (result > 0):
        return jsonify({"result":'success'})
    else:
        return jsonify({"result": 'error'})


app.run(debug=True,threaded=True,host="0.0.0.0",port=5000)

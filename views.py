from plistlib import Data

from flask import render_template, request, url_for, flash
from werkzeug.utils import redirect

from databese import ProductModel, FeaturesModel,UserModel,OrganizationsModel
from app import app,db
import binascii
@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/checkuser',methods = ['POST'])
def checkuser():
    if request.method == 'POST':
        person_name = request.form['person_name']
        person_password = request.form['person_password']
        login = UserModel.query.filter_by(person_name=person_name, person_password=person_password).first()
        if login is not None:
            return redirect(url_for('features'))

        return redirect(url_for("hello_world"))

@app.route('/insertuser',methods = ['POST'])
def insertuser():
    if request.method == 'POST':
        person_name = request.form['person_name']
        person_password = request.form['person_password']

        myUser =UserModel(person_name,person_password)
        db.session.add(myUser)
        db.session.commit()
    return redirect(url_for('hello_world'))


@app.route('/features')
def features():
    all_data = db.session.query(FeaturesModel).all()
    return render_template('features.html',feat = all_data)

@app.route('/insertfeatures',methods = ['POST'])
def insertfeatures():
    if request.method == 'POST':
        feature_name = request.form['feature_name']
        myFeatures=FeaturesModel(feature_name)
        db.session.add(myFeatures)
        db.session.commit()
        #Flash("New Feature is added")
    return redirect(url_for('features'))

@app.route('/updatefeatures',methods = ['GET','POST'])
def updatefeatures():
    if request.method == 'POST':
        m_name = request.form['feature_name']
        num = request.form['feature_id']

        my_data = db.session.query(FeaturesModel).get(num)
        my_data.feature_name = request.form['feature_name']
        db.session.commit()


    return redirect(url_for('features'))

@app.route('/deletefeatures', methods = ['GET', 'POST'])
def deletefeatures():
    num = request.form['feature_id']

    my_data = db.session.query(FeaturesModel).get(num)
    db.session.delete(my_data)
    db.session.commit()

    return redirect(url_for('features'))


@app.route('/product')
def product():
    all_data = db.session.query(ProductModel).all()
    return render_template('product.html', feat=all_data)


@app.route('/insertproduct', methods = ['POST'])
def insertproduct():
    if request.method == 'POST':
        m_code = request.form['m_code']
        m_name = request.form['m_name']
        m_short_name = request.form['m_short_name']
        m_parent_code = request.form['m_parent_code']
        m_abstract = request.form['m_abstract']
        m_category = request.form['m_category']
        is_active = request.form['is_active']
        m_abstract.strip()
        is_active.strip()
        guid_tag = binascii.unhexlify(m_abstract)
        isac = binascii.unhexlify(is_active)
        my_data = ProductModel(m_code,m_name,m_short_name,m_parent_code,guid_tag,m_category,isac)
        db.session.add(my_data)
        db.session.commit()

        return redirect(url_for('product'))

@app.route('/updateproduct', methods=['GET', 'POST'])
def updateproduct():
    if request.method == 'POST':
        m_code = request.form['m_code']
        m_name = request.form['m_name']
        m_short_name = request.form['m_short_name']
        m_parent_code = request.form['m_parent_code']
        m_abstract = request.form['m_abstract']
        m_category = request.form['m_category']
        is_active = request.form['is_active']

        guid_tag = binascii.unhexlify(m_abstract)
        isac = binascii.unhexlify(is_active)


        my_data = db.session.query(ProductModel).get(m_code)
        my_data.m_name = request.form['m_name']
        my_data.m_short_name = request.form['m_short_name']
        my_data.m_parent_code = request.form['m_parent_code']
        my_data.m_abstract = guid_tag
        my_data.m_category = request.form['m_category']
        my_data.is_active = isac

        db.session.commit()
        return redirect(url_for('product'))


@app.route('/deleteproduct', methods = ['GET', 'POST'])
def deleteproduct():
    num = request.form['m_syscode']

    my_data = db.session.query(ProductModel).get(num)
    db.session.delete(my_data)
    db.session.commit()

    return redirect(url_for('product'))


@app.route('/insorg')
def insorg():
    return render_template('RegisterOrganization.html')

@app.route('/insertorganization', methods = ['POST'])
def insertorganization():
    if request.method == 'POST':
        org_name = request.form['org_name']
        org_Address = request.form['org_Adress']
        org_District = request.form['org_District']
        parent_org=0
        org_abstract=''
        isac = binascii.unhexlify(org_abstract)
        org_City=0
        org_Type=0
        myOrg=OrganizationsModel(org_name, parent_org, isac, org_Address, org_City, org_District, org_Type)
        db.session.add(myOrg)
        db.session.commit()
        person_name = request.form['person_name']
        person_password = request.form['person_password']
        myUser = UserModel(person_name, person_password)
        db.session.add(myUser)
        db.session.commit()
    return redirect(url_for('hello_world'))

if __name__ == '__main__':
    app.run()


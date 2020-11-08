from plistlib import Data

from flask import render_template, request, url_for, flash
from werkzeug.utils import redirect

from databese import ProductModel, FeaturesModel
from app import app,db


@app.route('/insertuser',methods = ['POST'])
def insertuser():
    if request.method == 'POST':
        feature_name = request.form['feature_name']
        myFeatures=FeaturesModel(feature_name)
        db.session.add(myFeatures)
        db.session.commit()
        #Flash("New Feature is added")
    return redirect(url_for('features'))


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

@app.route('/deletefeatures/<int:id>', methods = ['GET', 'POST'])
def deletefeatures(id):
    num = request.form['feature_id']

    my_data = db.session.query(FeaturesModel).get(id)
    db.session.delete(my_data)
    db.session.commit()

    return redirect(url_for('features'))


@app.route('/product')
def product():
    return render_template('product.html')


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
        abs = ' '.join(format(ord(x), 'b') for x in m_abstract)
        actv = ' '.join(format(ord(x), 'b') for x in is_active)


        my_data = ProductModel(m_code,m_name,m_short_name,m_parent_code,bin(abs),m_category,bin(actv))
        db.session.add(my_data)
        db.session.commit()

        return redirect(url_for('product'))

if __name__ == '__main__':
    app.run()


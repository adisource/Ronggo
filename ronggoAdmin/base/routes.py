from flask import render_template, redirect, request, url_for, session
from ronggoAdmin.base import blueprint
from ronggoAdmin.models import models
from ronggoAdmin import db
from sqlalchemy.sql import text

@blueprint.route('/')
def index():

    total_nasabah = models.Nasabah.query.count()
    total_transaksi = models.Transaksi.query.count()
    

    query = ("SELECT  sum(berat_sampah) FROM sampah")
    connection = db.engine.connect()
    result = connection.execute(query)
    for row in result:
        hasil= row[0]
    
    
    return render_template('dashboard.html',total_nasabah=total_nasabah,total_transaksi=total_transaksi,hasil=hasil)
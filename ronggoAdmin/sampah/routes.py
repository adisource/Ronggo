from ronggoAdmin.sampah import blueprint
from flask import Flask, render_template, redirect, url_for, request, make_response, session
import alregcode
from alregcode import regGenerate
from ronggoAdmin.models import models
from ronggoAdmin import db

@blueprint.route('/sampah',methods=["GET"])
def sampah():
    kode = models.Sampah.query.order_by(models.Sampah.kode_urutan.desc()).first()

    if isinstance(kode,type(None)):
        kodereg = regGenerate("S-",None,3)
    else:
        kodereg =regGenerate("S-",kode.kode_urutan,3)

    sampah = models.Sampah.query.filter_by(status=1)
    data = models.Sampah.query.filter_by(status=0)
    inc = regGenerate.inc
    
    query = ("SELECT kode FROM nasabah")
    connection = db.engine.connect()
    result = connection.execute(query)
    fect= result.fetchall()
    for i in fect:
        record = i
        

    nasabah_id = models.Nasabah.query.order_by(models.Nasabah.kode.desc()).first()


    return render_template('sampah.html', sampah = sampah, data=data, kodereg=kodereg,inc=inc,nasabah_id=nasabah_id,record=record)

@blueprint.route('/sampah/tambah', methods=["POST"])
def tambahSampah():
    kode = request.form.get("kode")
    kode_urutan = request.form.get("kode_urutan")
    tanggal =request.form.get("tanggal")
    jenis_sampah =request.form.get("jenis_sampah")
    berat_sampah = request.form.get("berat_sampah")
    harga = request.form.get("harga")

    dataSampah = models.Sampah(
        kode_urutan = kode_urutan,
        kode = kode,
        tanggal =tanggal,
        jenis_sampah = jenis_sampah,
        berat_sampah = berat_sampah,
        harga = harga,
        status = 1
    )

    db.session.add(dataSampah)
    db.session.commit()

    return redirect(url_for('sampah_blueprint.sampah'))

@blueprint.route('/sampah/update', methods=["POST"])
def sampahUpdate():

    kode = request.form.get("kode")
    tanggal = request.form.get("tanggal")
    jenis_sampah =request.form.get("jenis_sampah")
    berat_sampah = request.form.get("berat_sampah")
    harga = request.form.get("harga")

    sampah = models.Sampah.query.filter_by(kode=kode).first()
    
    sampah.tanggal =tanggal
    sampah.jenis_sampah =jenis_sampah
    berat_sampah = berat_sampah
    harga = harga
   
    db.session.commit()
    
    return redirect(url_for('sampah_blueprint.sampah'))


@blueprint.route('/sampah/edit/<kode>',methods=["GET"])
def sampahEdit(kode):
    
    sampah = models.Sampah.query.filter_by(kode=kode).first()

    return render_template('sampah_edit.html', sampah=sampah)


@blueprint.route('/sampah/delete/<kode>', methods=["GET"])
def sampahDelete(kode):

    sampah = models.Sampah.query.filter_by(kode=kode).first()
    sampah.status = 0

    db.session.commit()
    return redirect(url_for('sampah_blueprint.sampah'))


@blueprint.route('/sampah/restore/<kode>', methods=["GET"])
def sampahRestore(kode):

    sampah = models.Sampah.query.filter_by(kode=kode).first()
    sampah.status = 1

    db.session.commit()

    return redirect(url_for('sampah_blueprint.sampah'))


@blueprint.route('/sampah/deletep/<kode>', methods=["GET"])
def sampahDeletep(kode):

    sampah = models.Sampah.query.filter_by(kode=kode).first()

    db.session.delete(sampah)
    db.session.commit()

    return redirect(url_for('sampah_blueprint.sampah'))




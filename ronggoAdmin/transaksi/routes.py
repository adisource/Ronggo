from ronggoAdmin.transaksi import blueprint
from flask import Flask, render_template, redirect, url_for, request, make_response, session
import alregcode
from alregcode import regGenerate
from ronggoAdmin.models import models
from ronggoAdmin import db

@blueprint.route('/transaksi',methods=["GET"])
def transaksi():

    kode = models.Transaksi.query.order_by(models.Transaksi.kode_urutan.desc()).first()

    if isinstance(kode,type(None)):
        kodereg = regGenerate("T-",None,3)
    else:
        kodereg =regGenerate("T-",kode.kode_urutan,3)

    transaksi = models.Transaksi.query.filter_by(status=1)
    data = models.Transaksi.query.filter_by(status=0)
    inc = regGenerate.inc

    query = ("SELECT * FORM transaksi")
    connect = db.engine.connect()
    cursor = connect.cursor()
    cursor.execute(query)
    record = cursor.fethall()



    dataTr = models.Nasabah.query.order_by(models.Nasabah.kode.desc()).first()


    return render_template('transaksi.html', transaksi = transaksi, data=data, kodereg=kodereg,inc=inc,dataTr=dataTr)

@blueprint.route('/transaksi/tambah', methods=["POST"])
def tambahTransaksi():

    kode = request.form.get("kode")
    kode_urutan = request.form.get("kode_urutan")
    nama = request.form.get("nama")
    jenis_transaksi = request.form.get("jenis_transaksi")
    tanggal =  request.form.get("tanggal")
    jumlah_transaksi = request.form.get("jumlah_transaksi")
    tujuan_transaksi = request.form.get("tujuan_transaksi")
    status_transaksi = request.form.get("status_transaksi") 

    
    

    dataTransaksi = models.Transaksi(
        kode_urutan = kode_urutan,
        kode = kode,
        nama = nama,
        jenis_transaksi =jenis_transaksi,
        tanggal = tanggal,
        jumlah_transaksi = jumlah_transaksi,
        tujuan_transaksi = tujuan_transaksi,
        status_transaksi = status_transaksi,
        status = 1
       
    )

    db.session.add(dataTransaksi)
    db.session.commit()

    return redirect(url_for('transaksi_blueprint.transaksi'))

@blueprint.route('/transaksi/update', methods=["POST"])
def transaksiUpdate():

    kode = request.form.get("kode")
    nama = request.form.get("nama")
    jenis_transaksi = request.form.get("jenis_transaksii")
    tanggal =  request.form.get("tanggal")
    jumlah_transaksi = request.form.get("jumlah_transaksi")
    tujuan_transaksi = request.form.get("tujuan_transaksi")
    status_transaksi = request.form.get("Status_transaksi") 

    


    transaksi = models.Transaksi.query.filter_by(kode=kode).first()

  
    transaksi.nama = nama
    transaksi.jenis_transaksi = jenis_transaksi
    transaksi.tanggal = tanggal
    transaksi.jumlah_transaksi = jumlah_transaksi
    transaksi.tujuan_transaksi = tujuan_transaksi
    transaksi.status_transaksi = status_transaksi
   
    db.session.commit()
    
    return redirect(url_for('transaksi_blueprint.transaksi'))


@blueprint.route('/transaksi/edit/<kode>',methods=["GET"])
def transaksiEdit(kode):
    
    transaksi = models.Transaksi.query.filter_by(kode=kode).first()

    return render_template('transaksi_edit.html', transaksi=transaksi)


@blueprint.route('/transaksi/delete/<kode>', methods=["GET"])
def transaksiDelete(kode):

    transaksi = models.Transaksi.query.filter_by(kode=kode).first()
    transaksi.status = 0

    db.session.commit()
    return redirect(url_for('transaksi_blueprint.transaksi'))


@blueprint.route('/transaksi/restore/<kode>', methods=["GET"])
def transaksiRestore(kode):

    transaksi = models.Transaksi.query.filter_by(kode=kode).first()
    transaksi.status = 1

    db.session.commit()

    return redirect(url_for('transaksi_blueprint.transaksi'))


@blueprint.route('/transaksi/deletep/<kode>', methods=["GET"])
def transaksiDeletep(kode):

    transaksi = models.Transaksi.query.filter_by(kode=kode).first()

    db.session.delete(transaksi)
    db.session.commit()

    return redirect(url_for('transaksi_blueprint.transaksi'))




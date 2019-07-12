from ronggoAdmin.buku_tabungan import blueprint
from flask import Flask, render_template, redirect, url_for, request, make_response, session
import alregcode
from alregcode import regGenerate
from ronggoAdmin.models import models
from ronggoAdmin import db

@blueprint.route('/tabungan')
def tabungan():
 
    kode = models.Tabungan.query.order_by(models.Tabungan.kode_urutan.desc()).first()
    
    if isinstance(kode,type(None)):
        kodereg = regGenerate("TB-",None,3)
    else:
        kodereg =regGenerate("TB-",kode.kode_urutan,3)

    tabungan = models.Tabungan.query.filter_by(status=1)
    data = models.Tabungan.query.filter_by(status=0)
    inc = regGenerate.inc


    
    dataT = models.Nasabah.query.all()
    return render_template('tabungan.html', tabungan = tabungan, data=data, kodereg=kodereg,inc=inc)

@blueprint.route('/tabungan/tambah', methods=["POST"])
def tambahTabungan():
    
    kode = request.form.get("kode")
    kode_urutan = request.form.get("kode_urutan")
    tanggal = request.form.get("tanggal")
    debet = request.form.get("debet")
    saldo = request.form.get("saldo")
   
    dataTabungan = models.Tabungan(
        
        kode_urutan = kode_urutan,
        kode = kode,
        tanggal = tanggal,
        debet = debet,
        saldo = saldo,
        status = 1


    )


    db.session.add(dataTabungan)
    db.session.commit()

    return redirect(url_for('tabungan_blueprint.tabungan' ))


@blueprint.route('/tabungan/update', methods=["POST"])
def tabunganUpdate():

    kode = request.form.get("kode")
    tanggal = request.form.get("tanggal")
    debet = request.form.get("debet")
    saldo = request.form.get("saldo")

    tabungan = models.Tabungan.query.filter_by(kode=kode).first()
    tabungan.tanggal = tanggal
    tabungan.debet = debet
    tabungan.saldo = saldo
   
    db.session.commit()
    
    return redirect(url_for('tabungan_blueprint.tabungan'))


@blueprint.route('/tabungan/edit/<kode>',methods=["GET"])
def tabunganEdit(kode):
    
    tabungan = models.Tabungan.query.filter_by(kode=kode).first()

    return render_template('tabungan_edit.html', tabungan=tabungan)


@blueprint.route('/tabungan/delete/<kode>', methods=["GET"])
def tabunganDelete(kode):

    tabungan = models.Tabungan.query.filter_by(kode=kode).first()
    tabungan.status = 0

    db.session.commit()
    return redirect(url_for('tabungan_blueprint.tabungan'))


@blueprint.route('/tabungan/restore/<kode>', methods=["GET"])
def tabunganRestore(kode):

    tabungan = models.Tabungan.query.filter_by(kode=kode).first()
    tabungan.status = 1

    db.session.commit()

    return redirect(url_for('tabungan_blueprint.tabungan'))


@blueprint.route('/tabungan/deletep/<kode>', methods=["GET"])
def tabunganDeletep(kode):

    tabungan = models.Tabungan.query.filter_by(kode=kode).first()

    db.session.delete(tabungan)
    db.session.commit()

    return redirect(url_for('tabungan_blueprint.tabungan'))




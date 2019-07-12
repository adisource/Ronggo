from ronggoAdmin.nasabah import blueprint
from flask import Flask, render_template, redirect, url_for, request, make_response, session
import alregcode
from alregcode import regGenerate
from ronggoAdmin.models import models
from ronggoAdmin import db
from flask_sqlalchemy import SQLAlchemy

@blueprint.route('/nasabah',methods=["GET"])
def nasabah():
    kode = models.Nasabah.query.order_by(models.Nasabah.kode_urutan.desc()).first()

    if isinstance(kode,type(None)):
        kodereg = regGenerate("N-",None,3)
    else:
        kodereg = regGenerate("N-",kode.kode_urutan,3)

    nasabah = models.Nasabah.query.filter_by(status=1)
    data = models.Nasabah.query.filter_by(status=0)
    inc = regGenerate.inc


    return render_template('nasabah.html', nasabah = nasabah, data=data, kodereg=kodereg,inc=inc )

@blueprint.route('/nasabah/tambah', methods=["POST"])
def tambahNasabah():
    kode = request.form.get("kode")
    kode_urutan = request.form.get("kode_urutan")
    nama = request.form.get("nama")
    tempat_lahir = request.form.get("tempat_lahir")
    tanggal_lahir = request.form.get("tanggal_lahir")
    alamat = request.form.get("alamat")
    email = request.form.get("email")
    nomer_hp =  request.form.get("nomer_hp") 

    dataNasabah = models.Nasabah(
        kode_urutan = kode_urutan,
        kode = kode,
        nama = nama,
        tempat_lahir = tempat_lahir,
        tanggal_lahir = tanggal_lahir,
        alamat = alamat,
        email = email,
        nomer_hp = nomer_hp,
        status = 1
    )

   
    db.session.add(dataNasabah)
    db.session.commit()

    return redirect(url_for('nasabah_blueprint.nasabah'))

@blueprint.route('/nasabah/update', methods=["POST"])
def nasabahUpdate():

    kode = request.form.get("kode")
    nama = request.form.get("nama")
    tempat_lahir = request.form.get("tempat_lahir")
    tanggal_lahir = request.form.get("tanggal_lahir")
    alamat = request.form.get("alamat")
    email = request.form.get("email")
    nomer_hp =  request.form.get("nomer_hp")

    nasabah = models.Nasabah.query.filter_by(kode=kode).first()

    nasabah.nama = nama
    nasabah.tempat_lahir = tempat_lahir
    nasabah.tanggal_lahir = tanggal_lahir
    nasabah.alamat = alamat
    nasabah.email = email
    nasabah.nomer_hp = nomer_hp
   
    db.session.commit()
    
    return redirect(url_for('nasabah_blueprint.nasabah'))


@blueprint.route('/nasabah/detail/<kode>',methods=["GET","POST"])
def nasabahEdit(kode):

    nasabah = models.Nasabah.query.filter_by(kode=kode).first()

    return render_template('detail_nasabah.html', nasabah=nasabah)


@blueprint.route('/nasabah/delete/<kode>', methods=["GET"])
def nasabahDelete(kode):

    nasabah = models.Nasabah.query.filter_by(kode=kode).first()
    nasabah.status = 0

    db.session.commit()
    return redirect(url_for('nasabah_blueprint.nasabah'))


@blueprint.route('/nasabah/restore/<kode>', methods=["GET"])
def nasabahRestore(kode):

    nasabah = models.Nasabah.query.filter_by(kode=kode).first()
    nasabah.status = 1

    db.session.commit()

    return redirect(url_for('nasabah_blueprint.nasabah'))


@blueprint.route('/nasabah/deletep/<kode>', methods=["GET"])
def nasabahDeletep(kode):

    nasabah = models.Nasabah.query.filter_by(kode=kode).first()

    db.session.delete(nasabah)
    db.session.commit()

    return redirect(url_for('nasabah_blueprint.nasabah'))



@blueprint.route('/nasabah/nasabahPersonal<kode>',methods=["GET"])
def nasabahPersonal(kode):


    return render_template('nasabah_personal.html')


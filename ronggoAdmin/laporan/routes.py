from ronggoAdmin.laporan import blueprint
from flask import Flask, render_template, redirect, url_for, request, make_response, session
import alregcode
from alregcode import regGenerate
from ronggoAdmin.models import models
from ronggoAdmin import db

@blueprint.route('/data_sampah')
def data_sam():


    return render_template("data_sampah.html")


@blueprint.route('/data_tabungan')
def data_tabungan():


    return render_template("data_tabungan.html")


@blueprint.route('/data_transaksi')
def data_transaksi():


    return render_template("data_transaksi.html")




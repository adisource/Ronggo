from ronggoAdmin import db

class Nasabah(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    kode = db.Column(db.String(20))
    kode_urutan = db.Column(db.String(20))
    nama = db.Column(db.String(20))
    alamat = db.Column(db.String(20))
    tempat_lahir = db.Column(db.String(20))
    tanggal_lahir =db.Column(db.String(20))
    email = db.Column(db.String(80))
    nomer_hp = db.Column(db.String(15))
    status = db.Column(db.Integer)
    tabungan = db.relationship('Tabungan',backref='nasabah')
    transaksi = db.relationship('Transaksi',backref='nasabah')
    sampah = db.relationship('Sampah',backref='nasabah')
    
   

    
class Tabungan(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    kode = db.Column(db.String(20))
    kode_urutan = db.Column(db.String(20))
    nama = db.Column(db.String(20))
    tanggal = db.Column(db.String(20))
    debet = db.Column(db.Integer)
    saldo = db.Column(db.Integer)
    status = db.Column(db.Integer)
    nasabah_id = db.Column(db.Integer,db.ForeignKey('nasabah.id'))
    

class Transaksi(db.Model):    
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    jenis_transaksi = db.Column(db.String(20))
    kode = db.Column(db.String(20))
    kode_urutan =db.Column(db.String(20))
    nama = db.Column(db.String(20))
    tanggal = db.Column(db.String(20))
    jumlah_transaksi = db.Column(db.Integer)
    tujuan_transaksi = db.Column(db.String(20))
    status_transaksi = db.Column(db.String(20))
    status = db.Column(db.Integer)
    nasabah_id = db.Column(db.Integer,db.ForeignKey('nasabah.id'))

class Sampah(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    nama = db.Column(db.String(20))
    kode = db.Column(db.String(20))
    kode_urutan = db.Column(db.String(20))
    tanggal = db.Column(db.String(20))
    jenis_sampah = db.Column(db.String(20))
    berat_sampah = db.Column(db.Integer)
    harga = db.Column(db.Integer)
    status = db.Column(db.Integer)
    nasabah_id = db.Column(db.Integer,db.ForeignKey('nasabah.id'))


class Admin(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20))
    email = db.Column(db.String(20))
    password = db.Column(db.String(20))
    nama = db.Column(db.String(20))





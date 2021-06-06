from connector import *
from datetime import datetime

class Model:
    def __init__(self):
        self.database = Database()
        self.table_login = ['idUser','username','password']
        self.table_barang = ('idBarang','namaBarang','stok','hargaBarang')
        self.table_transaksi = ('idOrder','idBarang','jumlah','jenis_transaksi','time')

    def userValidation(self,usr,passwd):
        query = f"SELECT * FROM login WHERE username='{usr}' AND password='{passwd}'"
        try:
            return self.database.fetchall(query)[0][0]
        except Exception as e:
            return False
    
    def getDataBarang(self):
        return self.database.fetchall("SELECT * FROM barang")
    
    def getBarangByID(self,id_item):
        query = f"SELECT * FROM barang WHERE idBarang='{id_item}'"
        return self.database.fetchone(query)

    def getOrder(self):
        return self.database.fetchall("SELECT * FROM transaksi")

    def getOrderByID(self,id_item):
        query = f"SELECT * FROM transaksi WHERE idOrder='{id_item}'"
        return self.database.fetchone(query)
    
    def deleteByID(self,id_item):
        query = f"DELETE FROM barang WHERE idBarang={id_item}"
        return self.database.execute(query)
    
    def searchByKeyword(self,keyword):
        query = f"SELECT * FROM barang WHERE {self.table_barang[1]} LIKE '%{keyword}%' OR {self.table_barang[2]} LIKE '%{keyword}%' OR {self.table_barang[3]} LIKE '%{keyword}%'"
        return self.database.fetchall(query)
    
    def insertBarang(self,data):
        query = f"""INSERT INTO `barang` (`namaBarang`,`stok`,`hargaBarang`) VALUES {data};"""
        return self.database.execute(query)
    
    def updateBarang(self, data):
        query = f"UPDATE barang SET {self.table_barang[3]}='{data[3]}' WHERE {self.table_barang[0]} = {data[0]}"
        return self.database.execute(query)
    
    def updateStok(self,data):
        query = f"UPDATE barang SET stok = stok + {data[1]} WHERE idBarang = {data[0]}"
        return self.database.execute(query)

    def insertStok(self,data):
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        query = f"INSERT INTO transaksi VALUES (idOrder,'{data[0]}','{data[1]}','masuk','"+(formatted_date)+"')"
        return self.database.execute(query)
    
    def searchByKey(self,key):
        query = f"SELECT * FROM transaksi WHERE {self.table_transaksi[1]} LIKE '%{key}%' OR {self.table_transaksi[2]} LIKE '%{key}%' OR {self.table_transaksi[3]} LIKE '%{key}%' OR {self.table_transaksi[4]} LIKE '%{key}%'"
        return self.database.fetchall(query)
    
    def deleteOrder(self,id_item):
        query = f"DELETE FROM transaksi WHERE idOrder={id_item}"
        return self.database.execute(query)

    def updateStokKeluar(self,data):
        query = f"UPDATE barang SET stok = stok - {data[1]} WHERE idBarang = {data[0]}"
        return self.database.execute(query)

    def insertStokKeluar(self,data):
        now = datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
        query = f"INSERT INTO transaksi VALUES (idOrder,'{data[0]}','{data[1]}','keluar','"+(formatted_date)+"')"
        return self.database.execute(query)
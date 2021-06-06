import wx
import interface
import model

class Aplikasi:
    def __init__(self):
        self.model = model.Model()
        self.viewLogin = interface.loginFrame(None)
        self.viewBeranda = interface.berandaFrame(None)
        self.viewHome = interface.homeFrame(None)
        self.viewTambah = interface.tambahFrame(None)
        self.viewEdit = interface.editFrame(None)
        self.viewOrder = interface.orderFrame(None)
        self.viewOrderMasuk = interface.masukFrame(None)
        self.viewOrderKeluar = interface.keluarFrame(None)

        self.set_event_login()
        self.set_event_beranda()
        self.set_event_home()
        self.set_event_tambah()
        self.set_event_edit()
        self.set_event_order()
        self.set_event_orderTambah()
        self.set_event_orderKeluar()

        self.stokSelected = None
        self.ordSelected = None
        
    ###LOGIN    
    def set_event_login(self):
        self.viewLogin.loginButton.Bind( wx.EVT_BUTTON, self.clickLogin )
    def clickLogin(self,event):
        usr = self.viewLogin.user.GetValue()
        passwd = self.viewLogin.password.GetValue()
        if self.model.userValidation(usr,passwd):
            self.viewLogin.Destroy()
            return self.viewBeranda.Show()
        return wx.MessageDialog(None,f"Username/Password Salah",'Gagal!',wx.OK|wx.ICON_INFORMATION).ShowModal()

    def main(self):
        self.viewLogin.Show()

    ###BERANDA
    def set_event_beranda(self):
        self.viewBeranda.barang.Bind( wx.EVT_BUTTON, self.barangOnButtonClick )
        self.viewBeranda.transaksi.Bind( wx.EVT_BUTTON, self.transaksiOnButtonClick )

    def barangOnButtonClick(self, event):
        self.viewBeranda.Hide()
        self.viewHome.Show()
    
    def transaksiOnButtonClick(self, event):
        self.viewBeranda.Hide()
        self.viewOrder.Show()

    ###HOME
    def set_event_home(self):
        self.viewHome.backButton.Bind( wx.EVT_BUTTON, self.clickBack )
        self.viewHome.limit.Bind( wx.EVT_SPINCTRL, self.limitData )
        self.viewHome.limit.Bind( wx.EVT_TEXT, self.limitData )
        self.viewHome.limit.Bind( wx.EVT_TEXT_ENTER, self.limitData )
        self.viewHome.limit.SetMax(len(self.getDataBarang()))
        self.viewHome.tambahButton.Bind( wx.EVT_BUTTON, self.clickTambah )
        self.viewHome.updateButton.Bind( wx.EVT_BUTTON, self.clickUpdate )
        self.viewHome.hapusButton.Bind( wx.EVT_BUTTON, self.clickHapus )
        self.viewHome.searchText.Bind( wx.EVT_TEXT, self.onSearch )
        self.viewHome.listControl.Bind( wx.EVT_LIST_ITEM_SELECTED, self.itemSelected )
    
    def onSearch(self,event):
        keyword = self.viewHome.searchText.GetValue()
        if keyword != '':
            result = self.model.searchByKeyword(keyword)
            return self.set_BodyTableBarang(result)
        return self.set_BodyTableBarang()
    
    def valuelimit(self):
        return self.viewHome.limit.GetValue()
    
    def limitData(self,event):
        return self.set_BodyTableBarang()
    
    def itemSelected(self,event):
        self.stokSelected = event.GetIndex()
    
    def clickBack(self,event):
        self.viewHome.Hide()
        return self.viewBeranda.Show()
    
    ###HAPUS BARANG
    def clickHapus(self,event):
        if self.stokSelected != None:
            id_stok = self.viewHome.listControl.GetItemText(self.stokSelected,0)
            self.model.deleteByID(id_stok)
            self.viewHome.limit.SetMax(len(self.getDataBarang()))
            self.stokSelected = None
            return self.set_BodyTableBarang()
    
    def clickUpdate(self,event):
        if self.stokSelected != None:
            self.viewHome.Hide()
            self.viewEdit.Show()
            idBarang = self.viewHome.listControl.GetItemText(self.stokSelected,0)
            data = self.model.getBarangByID(idBarang)
            return self.fillFormEdit(data)

    def fillFormEdit(self,data):
        self.viewEdit.textNamaEdit.SetValue(data[1])
        self.viewEdit.textStokEdit.SetValue(f'{data[2]}')
        self.viewEdit.textHargaEdit.SetValue(f'{data[3]}')

    def clickTambah(self,event):
        self.viewHome.Hide()
        self.viewTambah.Show()
    
    def getDataBarang(self):
        return self.model.getDataBarang()
    
    def set_HeaderTableBarang(self):
        table = ['ID','Nama Barang','Stok','Harga Barang']
        for i,j in enumerate(table):
            self.viewHome.listControl.InsertColumn(i,j)
    
    def set_BodyTableBarang(self, data=None):
        data = self.getDataBarang() if data==None else data
        self.viewHome.listControl.ClearAll()
        self.set_HeaderTableBarang()
        for index,row in enumerate(data):
           if index < self.valuelimit():
                self.viewHome.listControl.InsertItem(index,row[0])
                for i in range(4):
                   self.viewHome.listControl.SetItem(index,i,str(row[i]))

    ###TAMBAH DATA
    def set_event_tambah(self):
        self.viewTambah.backTambah.Bind( wx.EVT_BUTTON, self.backTambahClick )
        self.viewTambah.buttonTambah.Bind( wx.EVT_BUTTON, self.buttonTambahClick )
    
    def backTambahClick(self,event):
        self.resetForm()
        self.viewTambah.Hide()
        return self.viewHome.Show()
    
    def buttonTambahClick(self,event):
        nama = self.viewTambah.textNama.GetValue()
        stok = self.viewTambah.textStok.GetValue()
        harga = self.viewTambah.textHarga.GetValue()
        if stok.isnumeric():
            self.model.insertBarang((nama,int(stok),int(harga)))
            self.resetForm()
            self.viewTambah.Hide()
            self.viewHome.limit.SetMax(len(self.getDataBarang()))
            self.viewHome.Show()
            return self.set_BodyTableBarang()
    
    def resetForm(self):
        self.viewTambah.textNama.SetValue('')
        self.viewTambah.textStok.SetValue('')
        self.viewTambah.textHarga.SetValue('')

    ###EDIT HARGA
    def set_event_edit(self):
        self.viewEdit.backEdit.Bind( wx.EVT_BUTTON, self.backEditClick )
        self.viewEdit.hargaButton.Bind( wx.EVT_BUTTON, self.editHargaClick )
    
    def backEditClick(self,event):
        self.viewEdit.Hide()
        return self.viewHome.Show()
    
    def editHargaClick(self, event):
        nama = self.viewEdit.textNamaEdit.GetValue()
        stok = self.viewEdit.textStokEdit.GetValue()
        harga = self.viewEdit.textHargaEdit.GetValue()
        if harga.isnumeric():
            id_barang = self.viewHome.listControl.GetItemText(self.stokSelected,0)
            self.model.updateBarang((id_barang,nama,int(stok),int(harga)))
            self.resetFormEdit()
            self.viewEdit.Hide()
            self.viewHome.limit.SetMax(len(self.getDataBarang()))
            self.viewHome.Show()
            return self.set_BodyTableBarang()
    
    def resetFormEdit(self):
        self.viewEdit.textNamaEdit.SetValue('')
        self.viewEdit.textStokEdit.SetValue('')
        self.viewEdit.textHargaEdit.SetValue('')
        self.stokSelected = None

###############################-------------------------------------------###############################

    ###HOME ORDER
    def set_event_order(self):
        self.viewOrder.backOrderButton.Bind( wx.EVT_BUTTON, self.backOrderButtonClick )
        self.viewOrder.limitOrder.Bind( wx.EVT_SPINCTRL, self.limitOrderData )
        self.viewOrder.limitOrder.Bind( wx.EVT_TEXT, self.limitOrderData )
        self.viewOrder.limitOrder.Bind( wx.EVT_TEXT_ENTER, self.limitOrderData )
        self.viewOrder.limitOrder.SetMax(len(self.getDataBarang()))
        self.viewOrder.masuk.Bind( wx.EVT_BUTTON, self.masukClick )
        self.viewOrder.keluar.Bind( wx.EVT_BUTTON, self.keluarClick )
        self.viewOrder.hapusOrder.Bind( wx.EVT_BUTTON, self.hapusOrderClick )
        self.viewOrder.cariOrder.Bind( wx.EVT_TEXT, self.orderSearch )
        self.viewOrder.listOrder.Bind( wx.EVT_LIST_ITEM_SELECTED, self.orderSelected )
    
    def masukClick(self,event):
        self.viewOrder.Hide()
        self.viewOrderMasuk.Show()

    def backOrderButtonClick(self, event):
        self.viewOrder.Hide()
        return self.viewBeranda.Show()
    
    def orderSearch(self,event):
        key = self.viewOrder.cariOrder.GetValue()
        if key != '':
            result = self.model.searchByKey(key)
            return self.set_BodyTableOrder(result)
        return self.set_BodyTableOrder()
    
    def valuelimitOrder(self):
        return self.viewOrder.limitOrder.GetValue()
    
    def limitOrderData(self,event):
        return self.set_BodyTableOrder()
    
    def orderSelected(self,event):
        self.ordSelected = event.GetIndex()
        
    def keluarClick(self,event):
        self.viewOrder.Hide()
        self.viewOrderKeluar.Show()

    ###HAPUS ORDER
    def hapusOrderClick(self,event):
        if self.ordSelected != None:
            id_stok = self.viewOrder.listOrder.GetItemText(self.ordSelected,0)
            self.model.deleteOrder(id_stok)
            self.viewOrder.limitOrder.SetMax(len(self.getOrder()))
            self.ordSelected = None
            return self.set_BodyTableOrder()

    def getOrder(self):
        return self.model.getOrder()

    def set_HeaderTableOrder(self):
        table = ['ID','ID Barang','Jumlah','Jenis Transaksi','Time']
        for i,j in enumerate(table):
            self.viewOrder.listOrder.InsertColumn(i,j)
    
    def set_BodyTableOrder(self, data=None):
        data = self.getOrder() if data==None else data
        self.viewOrder.listOrder.ClearAll()
        self.set_HeaderTableOrder()
        for index,row in enumerate(data):
           if index < self.valuelimitOrder():
                self.viewOrder.listOrder.InsertItem(index,row[0])
                for i in range(5):
                   self.viewOrder.listOrder.SetItem(index,i,str(row[i]))
    
    
    ###ORDER MASUK
    def set_event_orderTambah(self):
        self.viewOrderMasuk.backButtonOrd.Bind( wx.EVT_BUTTON, self.backButtonOrdClick )
        self.viewOrderMasuk.masukStokButt.Bind( wx.EVT_BUTTON, self.masukStokButtClick )
    def backButtonOrdClick(self,event):
        self.viewOrderMasuk.Hide()
        return self.viewOrder.Show()
    def masukStokButtClick(self,event):
        id_barang = self.viewOrderMasuk.textIdOrder.GetValue()
        stok = self.viewOrderMasuk.textStokMasuk.GetValue()
        if stok.isnumeric():
            self.model.updateStok((id_barang,int(stok)))
            self.model.insertStok((id_barang,int(stok)))
            self.resetForm()
            self.viewOrderMasuk.Hide()
            self.viewOrder.limitOrder.SetMax(len(self.getOrder()))
            self.viewOrder.Show()
            return self.set_BodyTableOrder()
    def resetForm(self):
        self.viewOrderMasuk.textIdOrder.SetValue('')
        self.viewOrderMasuk.textStokMasuk.SetValue('')
        self.ordSelected = None

    ###ORDER KELUAR
    def set_event_orderKeluar(self):
        self.viewOrderKeluar.backButt.Bind( wx.EVT_BUTTON, self.backButtClick )
        self.viewOrderKeluar.keluarStokButt.Bind( wx.EVT_BUTTON, self.keluarStokButtClick )
    def backButtClick(self,event):
        self.viewOrderKeluar.Hide()
        return self.viewOrder.Show()
    def keluarStokButtClick(self,event):
        id_barang = self.viewOrderKeluar.textIdOrder.GetValue()
        stok = self.viewOrderKeluar.textStokKeluar.GetValue()
        if stok.isnumeric():
            self.model.updateStokKeluar((id_barang,int(stok)))
            self.model.insertStokKeluar((id_barang,int(stok)))
            self.resetForm()
            self.viewOrderKeluar.Hide()
            self.viewOrder.limitOrder.SetMax(len(self.getOrder()))
            self.viewOrder.Show()
            return self.set_BodyTableOrder()
    def resetForm(self):
        self.viewOrderKeluar.textIdOrder.SetValue('')
        self.viewOrderKeluar.textStokKeluar.SetValue('')
        self.ordSelected = None




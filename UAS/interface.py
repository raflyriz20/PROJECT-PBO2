# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class loginFrame
###########################################################################

class loginFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Aplikasi Gudang Toko", pos = wx.DefaultPosition, size = wx.Size( 350,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 223, 223 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Selamat datang di aplikasi gudang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )

		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, wx.EmptyString ), wx.VERTICAL )

		self.m_staticText4 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Username :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		sbSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )

		self.user = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		sbSizer1.Add( self.user, 0, wx.ALL|wx.EXPAND, 5 )

		self.pw = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Password : ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.pw.Wrap( -1 )

		sbSizer1.Add( self.pw, 0, wx.ALL, 5 )

		self.password = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,30 ), wx.TE_PASSWORD )
		sbSizer1.Add( self.password, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText6 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		sbSizer1.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.loginButton = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.Size( 100,30 ), 0 )
		sbSizer1.Add( self.loginButton, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( sbSizer1, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.loginButton.Bind( wx.EVT_BUTTON, self.clickLogin )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clickLogin( self, event ):
		event.Skip()


###########################################################################
## Class homeFrame
###########################################################################

class homeFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Aplikasi Gudang Toko", pos = wx.DefaultPosition, size = wx.Size( 750,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 223, 223 ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer11 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.backButton = wx.Button( self.m_panel1, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.backButton.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.backButton.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.backButton.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer4.Add( self.backButton, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.limit = wx.SpinCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer4.Add( self.limit, 0, wx.ALL, 5 )

		self.tambahButton = wx.Button( self.m_panel1, wx.ID_ANY, u"Tambah barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.tambahButton, 0, wx.ALL, 5 )

		self.updateButton = wx.Button( self.m_panel1, wx.ID_ANY, u"Update harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.updateButton, 0, wx.ALL, 5 )

		self.hapusButton = wx.Button( self.m_panel1, wx.ID_ANY, u"Hapus barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.hapusButton, 0, wx.ALL, 5 )


		bSizer4.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.searchText = wx.SearchCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.searchText.ShowSearchButton( True )
		self.searchText.ShowCancelButton( False )
		bSizer4.Add( self.searchText, 0, wx.ALL, 5 )


		bSizer11.Add( bSizer4, 1, wx.EXPAND, 5 )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.listControl = wx.ListCtrl( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_AUTOARRANGE|wx.LC_REPORT )
		self.listControl.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )
		self.listControl.SetMinSize( wx.Size( 720,340 ) )

		fgSizer1.Add( self.listControl, 0, wx.ALL, 5 )


		bSizer11.Add( fgSizer1, 0, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer11 )
		self.m_panel1.Layout()
		bSizer11.Fit( self.m_panel1 )
		bSizer3.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.backButton.Bind( wx.EVT_BUTTON, self.clickBack )
		self.limit.Bind( wx.EVT_SPINCTRL, self.limitData )
		self.limit.Bind( wx.EVT_TEXT, self.limitData )
		self.limit.Bind( wx.EVT_TEXT_ENTER, self.limitData )
		self.tambahButton.Bind( wx.EVT_BUTTON, self.clickTambah )
		self.updateButton.Bind( wx.EVT_BUTTON, self.clickUpdate )
		self.hapusButton.Bind( wx.EVT_BUTTON, self.clickHapus )
		self.searchText.Bind( wx.EVT_TEXT, self.onSearch )
		self.listControl.Bind( wx.EVT_LIST_ITEM_SELECTED, self.itemSelected )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def clickBack( self, event ):
		event.Skip()

	def limitData( self, event ):
		event.Skip()



	def clickTambah( self, event ):
		event.Skip()

	def clickUpdate( self, event ):
		event.Skip()

	def clickHapus( self, event ):
		event.Skip()

	def onSearch( self, event ):
		event.Skip()

	def itemSelected( self, event ):
		event.Skip()


###########################################################################
## Class berandaFrame
###########################################################################

class berandaFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Aplikasi Gudang Toko", pos = wx.DefaultPosition, size = wx.Size( 500,220 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 233, 233 ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"MENU", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		self.m_staticText7.SetFont( wx.Font( 26, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial Rounded MT Bold" ) )

		bSizer9.Add( self.m_staticText7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.barang = wx.Button( self, wx.ID_ANY, u"Data Barang", wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		self.barang.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer9.Add( self.barang, 0, wx.ALL|wx.EXPAND, 5 )

		self.transaksi = wx.Button( self, wx.ID_ANY, u"Data Transaksi", wx.DefaultPosition, wx.Size( -1,50 ), 0 )
		self.transaksi.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer9.Add( self.transaksi, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.barang.Bind( wx.EVT_BUTTON, self.barangOnButtonClick )
		self.transaksi.Bind( wx.EVT_BUTTON, self.transaksiOnButtonClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def barangOnButtonClick( self, event ):
		event.Skip()

	def transaksiOnButtonClick( self, event ):
		event.Skip()


###########################################################################
## Class tambahFrame
###########################################################################

class tambahFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Aplikasi Gudang Toko", pos = wx.DefaultPosition, size = wx.Size( 500,330 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 233, 233 ) )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Tambah Data" ), wx.VERTICAL )

		self.m_staticText6 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Nama barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )

		sbSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )

		self.textNama = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		sbSizer2.Add( self.textNama, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText7 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Stok", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		sbSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.textStok = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		sbSizer2.Add( self.textStok, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText8 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		sbSizer2.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.textHarga = wx.TextCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		sbSizer2.Add( self.textHarga, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText9 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		sbSizer2.Add( self.m_staticText9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.backTambah = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.backTambah.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.backTambah.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		gSizer1.Add( self.backTambah, 0, wx.ALL, 5 )

		self.buttonTambah = wx.Button( sbSizer2.GetStaticBox(), wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.buttonTambah.SetBackgroundColour( wx.Colour( 0, 255, 0 ) )

		gSizer1.Add( self.buttonTambah, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		sbSizer2.Add( gSizer1, 1, wx.EXPAND, 5 )


		bSizer6.Add( sbSizer2, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer6 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.backTambah.Bind( wx.EVT_BUTTON, self.backTambahClick )
		self.buttonTambah.Bind( wx.EVT_BUTTON, self.buttonTambahClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def backTambahClick( self, event ):
		event.Skip()

	def buttonTambahClick( self, event ):
		event.Skip()


###########################################################################
## Class editFrame
###########################################################################

class editFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Aplikasi Gudang Toko", pos = wx.DefaultPosition, size = wx.Size( 500,330 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 233, 233 ) )

		bSizer7 = wx.BoxSizer( wx.VERTICAL )

		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Edit Harga" ), wx.VERTICAL )

		self.m_staticText10 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Nama barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		sbSizer3.Add( self.m_staticText10, 0, wx.ALL, 5 )

		self.textNamaEdit = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,30 ), wx.TE_READONLY )
		sbSizer3.Add( self.textNamaEdit, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText11 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Stok", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		sbSizer3.Add( self.m_staticText11, 0, wx.ALL, 5 )

		self.textStokEdit = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,30 ), wx.TE_READONLY )
		sbSizer3.Add( self.textStokEdit, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText12 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Harga", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		sbSizer3.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.textHargaEdit = wx.TextCtrl( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		sbSizer3.Add( self.textHargaEdit, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText13 = wx.StaticText( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		sbSizer3.Add( self.m_staticText13, 0, wx.ALL, 5 )

		gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

		self.backEdit = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.backEdit.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.backEdit.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		gSizer2.Add( self.backEdit, 0, wx.ALL, 5 )

		self.hargaButton = wx.Button( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.hargaButton.SetBackgroundColour( wx.Colour( 0, 255, 0 ) )

		gSizer2.Add( self.hargaButton, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		sbSizer3.Add( gSizer2, 1, wx.EXPAND, 5 )


		bSizer7.Add( sbSizer3, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer7 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.backEdit.Bind( wx.EVT_BUTTON, self.backEditClick )
		self.hargaButton.Bind( wx.EVT_BUTTON, self.editHargaClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def backEditClick( self, event ):
		event.Skip()

	def editHargaClick( self, event ):
		event.Skip()


###########################################################################
## Class orderFrame
###########################################################################

class orderFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Aplikasi Gudang Toko", pos = wx.DefaultPosition, size = wx.Size( 750,450 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 233, 233 ) )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.backOrderButton = wx.Button( self.m_panel2, wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( 50,-1 ), 0 )
		self.backOrderButton.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.backOrderButton.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		bSizer11.Add( self.backOrderButton, 0, wx.ALL, 5 )


		bSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.limitOrder = wx.SpinCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 60,-1 ), wx.SP_ARROW_KEYS, 0, 10, 0 )
		bSizer11.Add( self.limitOrder, 0, wx.ALL, 5 )

		self.masuk = wx.Button( self.m_panel2, wx.ID_ANY, u"Masukkan barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.masuk, 0, wx.ALL, 5 )

		self.keluar = wx.Button( self.m_panel2, wx.ID_ANY, u"Keluarkan barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.keluar, 0, wx.ALL, 5 )

		self.hapusOrder = wx.Button( self.m_panel2, wx.ID_ANY, u"Hapus data", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.hapusOrder, 0, wx.ALL, 5 )


		bSizer11.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.cariOrder = wx.SearchCtrl( self.m_panel2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.cariOrder.ShowSearchButton( True )
		self.cariOrder.ShowCancelButton( False )
		bSizer11.Add( self.cariOrder, 0, wx.ALL, 5 )


		bSizer10.Add( bSizer11, 1, wx.EXPAND, 5 )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.listOrder = wx.ListCtrl( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size( 720,340 ), wx.LC_AUTOARRANGE|wx.LC_REPORT )
		self.listOrder.SetFont( wx.Font( 9, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		fgSizer2.Add( self.listOrder, 0, wx.ALL, 5 )


		bSizer10.Add( fgSizer2, 1, wx.EXPAND, 5 )


		self.m_panel2.SetSizer( bSizer10 )
		self.m_panel2.Layout()
		bSizer10.Fit( self.m_panel2 )
		bSizer9.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer9 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.backOrderButton.Bind( wx.EVT_BUTTON, self.backOrderButtonClick )
		self.limitOrder.Bind( wx.EVT_SPINCTRL, self.limitOrderData )
		self.limitOrder.Bind( wx.EVT_TEXT, self.limitOrderData )
		self.limitOrder.Bind( wx.EVT_TEXT_ENTER, self.limitOrderData )
		self.masuk.Bind( wx.EVT_BUTTON, self.masukClick )
		self.keluar.Bind( wx.EVT_BUTTON, self.keluarClick )
		self.hapusOrder.Bind( wx.EVT_BUTTON, self.hapusOrderClick )
		self.cariOrder.Bind( wx.EVT_TEXT, self.orderSearch )
		self.listOrder.Bind( wx.EVT_LIST_ITEM_SELECTED, self.orderSelected )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def backOrderButtonClick( self, event ):
		event.Skip()

	def limitOrderData( self, event ):
		event.Skip()



	def masukClick( self, event ):
		event.Skip()

	def keluarClick( self, event ):
		event.Skip()

	def hapusOrderClick( self, event ):
		event.Skip()

	def orderSearch( self, event ):
		event.Skip()

	def orderSelected( self, event ):
		event.Skip()


###########################################################################
## Class masukFrame
###########################################################################

class masukFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Aplikasi Gudang Toko", pos = wx.DefaultPosition, size = wx.Size( 500,270 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 233, 233 ) )

		bSizer12 = wx.BoxSizer( wx.VERTICAL )

		sbSizer4 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Stok masuk barang" ), wx.VERTICAL )

		self.m_staticText14 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"ID barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		sbSizer4.Add( self.m_staticText14, 0, wx.ALL, 5 )

		self.textIdOrder = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		sbSizer4.Add( self.textIdOrder, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText15 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Stok Masuk", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		sbSizer4.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.textStokMasuk = wx.TextCtrl( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		sbSizer4.Add( self.textStokMasuk, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText16 = wx.StaticText( sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		sbSizer4.Add( self.m_staticText16, 0, wx.ALL, 5 )

		gSizer3 = wx.GridSizer( 0, 2, 0, 0 )

		self.backButtonOrd = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.backButtonOrd.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.backButtonOrd.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		gSizer3.Add( self.backButtonOrd, 0, wx.ALL, 5 )

		self.masukStokButt = wx.Button( sbSizer4.GetStaticBox(), wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.masukStokButt.SetBackgroundColour( wx.Colour( 0, 255, 0 ) )

		gSizer3.Add( self.masukStokButt, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		sbSizer4.Add( gSizer3, 1, wx.EXPAND, 5 )


		bSizer12.Add( sbSizer4, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer12 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.backButtonOrd.Bind( wx.EVT_BUTTON, self.backButtonOrdClick )
		self.masukStokButt.Bind( wx.EVT_BUTTON, self.masukStokButtClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def backButtonOrdClick( self, event ):
		event.Skip()

	def masukStokButtClick( self, event ):
		event.Skip()


###########################################################################
## Class keluarFrame
###########################################################################

class keluarFrame ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Aplikasi Gudang Toko", pos = wx.DefaultPosition, size = wx.Size( 500,270 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 0, 233, 233 ) )

		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Stok keluar barang" ), wx.VERTICAL )

		self.m_staticText17 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"ID barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		sbSizer5.Add( self.m_staticText17, 0, wx.ALL, 5 )

		self.textIdOrder = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		sbSizer5.Add( self.textIdOrder, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText18 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Stok keluar", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		sbSizer5.Add( self.m_staticText18, 0, wx.ALL, 5 )

		self.textStokKeluar = wx.TextCtrl( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( -1,30 ), 0 )
		sbSizer5.Add( self.textStokKeluar, 0, wx.ALL|wx.EXPAND, 5 )

		self.m_staticText19 = wx.StaticText( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		sbSizer5.Add( self.m_staticText19, 0, wx.ALL, 5 )

		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		self.backButt = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Back", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.backButt.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		self.backButt.SetBackgroundColour( wx.Colour( 255, 0, 0 ) )

		gSizer4.Add( self.backButt, 0, wx.ALL, 5 )

		self.keluarStokButt = wx.Button( sbSizer5.GetStaticBox(), wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.Size( -1,40 ), 0 )
		self.keluarStokButt.SetBackgroundColour( wx.Colour( 0, 255, 0 ) )

		gSizer4.Add( self.keluarStokButt, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		sbSizer5.Add( gSizer4, 1, wx.EXPAND, 5 )


		bSizer13.Add( sbSizer5, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer13 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.backButt.Bind( wx.EVT_BUTTON, self.backButtClick )
		self.keluarStokButt.Bind( wx.EVT_BUTTON, self.keluarStokButtClick )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def backButtClick( self, event ):
		event.Skip()

	def keluarStokButtClick( self, event ):
		event.Skip()



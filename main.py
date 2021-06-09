from controller import *

class App(wx.App):
	def OnInit(self):
		self.frame = Aplikasi()
		self.frame.main()
		return True


Run = App()
Run.MainLoop()

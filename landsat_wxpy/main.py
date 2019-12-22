import wx
from landsat_wxpy.gui_handler import MainFrame_Handler

if __name__ == "__main__":
    # app = wx.PySimpleApp()
    app = wx.App(False)
    frame = MainFrame_Handler(None)
    frame.Show()
    app.MainLoop()



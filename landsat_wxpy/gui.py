# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Pengolah Landsat 8 - Normalized Difference Vegetation Index", pos = wx.DefaultPosition, size = wx.Size( 775,607 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 775,607 ), wx.DefaultSize )
		self.SetBackgroundColour( wx.Colour( 240, 240, 240 ) )
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu_files = wx.Menu()
		self.m_menuItem_new_project = wx.MenuItem( self.m_menu_files, wx.ID_ANY, u"Proyek Baru", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_files.AppendItem( self.m_menuItem_new_project )
		
		self.m_menuItem_file_import = wx.MenuItem( self.m_menu_files, wx.ID_ANY, u"Impor Citra", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_files.AppendItem( self.m_menuItem_file_import )
		
		self.m_menuItem_file_save = wx.MenuItem( self.m_menu_files, wx.ID_ANY, u"Simpan Hasil", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_files.AppendItem( self.m_menuItem_file_save )
		
		self.m_menu_files.AppendSeparator()
		
		self.m_menuItem_file_exit = wx.MenuItem( self.m_menu_files, wx.ID_ANY, u"Keluar", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_files.AppendItem( self.m_menuItem_file_exit )
		
		self.m_menubar1.Append( self.m_menu_files, u"File" ) 
		
		self.m_menu_process = wx.Menu()
		self.m_menuItem_process_crop_image = wx.MenuItem( self.m_menu_process, wx.ID_ANY, u"Potong Citra", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_process.AppendItem( self.m_menuItem_process_crop_image )
		
		self.m_menuItem_process_toa = wx.MenuItem( self.m_menu_process, wx.ID_ANY, u"Koreksi Top of Atmospheric", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_process.AppendItem( self.m_menuItem_process_toa )
		
		self.m_menu_process.AppendSeparator()
		
		self.m_menuItem_process_process_image = wx.MenuItem( self.m_menu_process, wx.ID_ANY, u"Proses", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_process.AppendItem( self.m_menuItem_process_process_image )
		
		self.m_menubar1.Append( self.m_menu_process, u"Proses" ) 
		
		self.m_menu_help = wx.Menu()
		self.m_menuItem_help_use = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"Cara Menggunakan", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.AppendItem( self.m_menuItem_help_use )
		
		self.m_menuItem_help_about = wx.MenuItem( self.m_menu_help, wx.ID_ANY, u"Tentang Kami...", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu_help.AppendItem( self.m_menuItem_help_about )
		
		self.m_menubar1.Append( self.m_menu_help, u"Bantuan" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		self.m_toolBar1 = self.CreateToolBar( wx.TB_FLAT|wx.TB_HORZ_TEXT, wx.ID_ANY )
		self.m_toolBar1.SetToolBitmapSize( wx.Size( 16,15 ) )
		self.m_tool_new_project = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"Proyek Baru", wx.Bitmap( u"assets/icon-new-project-32x32.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_tool_import_image = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"Impor Gambar", wx.Bitmap( u"assets/icon-add-file-32x32.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, u"Import Citra Landsat 8 dan Metadata", wx.EmptyString, None ) 
		
		self.m_toolBar1.AddSeparator()
		
		self.m_tool_crop_image = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"Potong Citra", wx.Bitmap( u"assets/icon-crop-image-32x32.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_tool_toa = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"Koreksi TOA", wx.Bitmap( u"assets/icon-toa-32x32.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_tool_process_image = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"Proses", wx.Bitmap( u"assets/icon-process-32x32.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar1.AddSeparator()
		
		self.m_tool_save_image = self.m_toolBar1.AddLabelTool( wx.ID_ANY, u"Simpan Hasil", wx.Bitmap( u"assets/icon-save-32x32.png", wx.BITMAP_TYPE_ANY ), wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.m_toolBar1.Realize() 
		
		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )
		
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		gSizer2 = wx.GridSizer( 2, 0, 0, 0 )
		
		self.m_panel4 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel4.SetBackgroundColour( wx.Colour( 240, 240, 240 ) )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel4, wx.ID_ANY, u"Isi Metadata" ), wx.VERTICAL )
		
		self.m_scrolledWindow1 = wx.ScrolledWindow( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		self.m_scrolledWindow1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_SCROLLBAR ) )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 10 )
		fgSizer2.AddGrowableCol( 1 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText11 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Informasi Koordinat", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )
		self.m_staticText11.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer2.Add( self.m_staticText11, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText12 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		fgSizer2.Add( self.m_staticText12, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText13 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Mulai Longitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )
		fgSizer2.Add( self.m_staticText13, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText_long_start = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_long_start.Wrap( -1 )
		fgSizer2.Add( self.m_staticText_long_start, 0, wx.ALL, 5 )
		
		self.m_staticText16 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Akhir Longitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )
		fgSizer2.Add( self.m_staticText16, 0, wx.ALL, 5 )
		
		self.m_staticText_long_end = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_long_end.Wrap( -1 )
		fgSizer2.Add( self.m_staticText_long_end, 0, wx.ALL, 5 )
		
		self.m_staticText18 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Mulai Latitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )
		fgSizer2.Add( self.m_staticText18, 0, wx.ALL, 5 )
		
		self.m_staticText_lat_start = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_lat_start.Wrap( -1 )
		fgSizer2.Add( self.m_staticText_lat_start, 0, wx.ALL, 5 )
		
		self.m_staticText20 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Akhir Latitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )
		fgSizer2.Add( self.m_staticText20, 0, wx.ALL, 5 )
		
		self.m_staticText_lat_end = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_lat_end.Wrap( -1 )
		fgSizer2.Add( self.m_staticText_lat_end, 0, wx.ALL, 5 )
		
		self.m_staticText22 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText22.Wrap( -1 )
		fgSizer2.Add( self.m_staticText22, 0, wx.ALL, 5 )
		
		self.m_staticText23 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		fgSizer2.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.m_staticText24 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Informasi Citra", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		self.m_staticText24.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		fgSizer2.Add( self.m_staticText24, 0, wx.ALL, 5 )
		
		self.m_staticText25 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		fgSizer2.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		self.m_staticText26 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"REFLECTANCE_MULT_BAND_4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		fgSizer2.Add( self.m_staticText26, 0, wx.ALL, 5 )
		
		self.m_staticText_ref_mult_band_4 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_ref_mult_band_4.Wrap( -1 )
		fgSizer2.Add( self.m_staticText_ref_mult_band_4, 0, wx.ALL, 5 )
		
		self.m_staticText28 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"REFLECTANCE_MULT_BAND_5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText28.Wrap( -1 )
		fgSizer2.Add( self.m_staticText28, 0, wx.ALL, 5 )
		
		self.m_staticText_ref_mult_band_5 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_ref_mult_band_5.Wrap( -1 )
		fgSizer2.Add( self.m_staticText_ref_mult_band_5, 0, wx.ALL, 5 )
		
		self.m_staticText30 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"REFLECTANCE_ADD_BAND_4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		fgSizer2.Add( self.m_staticText30, 0, wx.ALL, 5 )
		
		self.m_staticText_ref_add_band_4 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_ref_add_band_4.Wrap( -1 )
		fgSizer2.Add( self.m_staticText_ref_add_band_4, 0, wx.ALL, 5 )
		
		self.m_staticText32 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"REFLECTANCE_ADD_BAND_5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText32.Wrap( -1 )
		fgSizer2.Add( self.m_staticText32, 0, wx.ALL, 5 )
		
		self.m_staticText_ref_add_band_5 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_ref_add_band_5.Wrap( -1 )
		fgSizer2.Add( self.m_staticText_ref_add_band_5, 0, wx.ALL, 5 )
		
		
		self.m_scrolledWindow1.SetSizer( fgSizer2 )
		self.m_scrolledWindow1.Layout()
		fgSizer2.Fit( self.m_scrolledWindow1 )
		sbSizer1.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_panel4.SetSizer( sbSizer1 )
		self.m_panel4.Layout()
		sbSizer1.Fit( self.m_panel4 )
		gSizer2.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )
		
		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )
		
		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel5.SetBackgroundColour( wx.Colour( 240, 240, 240 ) )
		
		sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel5, wx.ID_ANY, u"Citra Band 4" ), wx.VERTICAL )
		
		self.m_bitmap_band4 = wx.StaticBitmap( sbSizer3.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer3.Add( self.m_bitmap_band4, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel5.SetSizer( sbSizer3 )
		self.m_panel5.Layout()
		sbSizer3.Fit( self.m_panel5 )
		gSizer4.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel6.SetBackgroundColour( wx.Colour( 240, 240, 240 ) )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel6, wx.ID_ANY, u"Citra Band 5" ), wx.VERTICAL )
		
		self.m_bitmap_band5 = wx.StaticBitmap( sbSizer5.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer5.Add( self.m_bitmap_band5, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel6.SetSizer( sbSizer5 )
		self.m_panel6.Layout()
		sbSizer5.Fit( self.m_panel6 )
		gSizer4.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		gSizer2.Add( gSizer4, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer8.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		
		gSizer1.Add( bSizer8, 1, wx.EXPAND, 5 )
		
		self.m_panel8 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel8.SetBackgroundColour( wx.Colour( 240, 240, 240 ) )
		
		sbSizer7 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel8, wx.ID_ANY, u"Hasil Proses" ), wx.VERTICAL )
		
		self.m_bitmap_citra_hasil = wx.StaticBitmap( sbSizer7.GetStaticBox(), wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer7.Add( self.m_bitmap_citra_hasil, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel8.SetSizer( sbSizer7 )
		self.m_panel8.Layout()
		sbSizer7.Fit( self.m_panel8 )
		gSizer1.Add( self.m_panel8, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( gSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_CLOSE, self.app_exit )
		self.Bind( wx.EVT_MENU, self.tool_create_new, id = self.m_menuItem_new_project.GetId() )
		self.Bind( wx.EVT_MENU, self.tool_import_images, id = self.m_menuItem_file_import.GetId() )
		self.Bind( wx.EVT_MENU, self.tool_save_image, id = self.m_menuItem_file_save.GetId() )
		self.Bind( wx.EVT_MENU, self.app_exit, id = self.m_menuItem_file_exit.GetId() )
		self.Bind( wx.EVT_MENU, self.tool_crop_image, id = self.m_menuItem_process_crop_image.GetId() )
		self.Bind( wx.EVT_MENU, self.tool_toa_correction, id = self.m_menuItem_process_toa.GetId() )
		self.Bind( wx.EVT_MENU, self.tool_process_image, id = self.m_menuItem_process_process_image.GetId() )
		self.Bind( wx.EVT_MENU, self.help_using, id = self.m_menuItem_help_use.GetId() )
		self.Bind( wx.EVT_MENU, self.help_about, id = self.m_menuItem_help_about.GetId() )
		self.Bind( wx.EVT_TOOL, self.tool_create_new, id = self.m_tool_new_project.GetId() )
		self.Bind( wx.EVT_TOOL, self.tool_import_images, id = self.m_tool_import_image.GetId() )
		self.Bind( wx.EVT_TOOL, self.tool_crop_image, id = self.m_tool_crop_image.GetId() )
		self.Bind( wx.EVT_TOOL, self.tool_toa_correction, id = self.m_tool_toa.GetId() )
		self.Bind( wx.EVT_TOOL, self.tool_process_image, id = self.m_tool_process_image.GetId() )
		self.Bind( wx.EVT_TOOL, self.tool_save_image, id = self.m_tool_save_image.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def app_exit( self, event ):
		event.Skip()
	
	def tool_create_new( self, event ):
		event.Skip()
	
	def tool_import_images( self, event ):
		event.Skip()
	
	def tool_save_image( self, event ):
		event.Skip()
	
	
	def tool_crop_image( self, event ):
		event.Skip()
	
	def tool_toa_correction( self, event ):
		event.Skip()
	
	def tool_process_image( self, event ):
		event.Skip()
	
	def help_using( self, event ):
		event.Skip()
	
	def help_about( self, event ):
		event.Skip()
	
	
	
	
	
	
	

###########################################################################
## Class ClipDialog
###########################################################################

class ClipDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Potong Citra", pos = wx.DefaultPosition, size = wx.Size( 485,482 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer3 = wx.FlexGridSizer( 0, 1, 5, 0 )
		fgSizer3.AddGrowableCol( 0 )
		fgSizer3.AddGrowableRow( 2 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetBackgroundColour( wx.Colour( 240, 240, 240 ) )
		
		sbSizer9 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel3, wx.ID_ANY, u"Informasi Koordinat" ), wx.VERTICAL )
		
		fgSizer4 = wx.FlexGridSizer( 0, 2, 0, 20 )
		fgSizer4.AddGrowableCol( 1 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText43 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Mulai Longitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )
		fgSizer4.Add( self.m_staticText43, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl_ori_start_lon = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer4.Add( self.m_textCtrl_ori_start_lon, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText45 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Akhir Longitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )
		fgSizer4.Add( self.m_staticText45, 0, wx.ALL, 5 )
		
		self.m_textCtrl_ori_end_lon = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer4.Add( self.m_textCtrl_ori_end_lon, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText47 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Mulai Longitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )
		fgSizer4.Add( self.m_staticText47, 0, wx.ALL, 5 )
		
		self.m_textCtrl_ori_start_lat = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer4.Add( self.m_textCtrl_ori_start_lat, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText49 = wx.StaticText( sbSizer9.GetStaticBox(), wx.ID_ANY, u"Akhir Longitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )
		fgSizer4.Add( self.m_staticText49, 0, wx.ALL, 5 )
		
		self.m_textCtrl_ori_end_lat = wx.TextCtrl( sbSizer9.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY )
		fgSizer4.Add( self.m_textCtrl_ori_end_lat, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer9.Add( fgSizer4, 1, wx.EXPAND, 5 )
		
		
		self.m_panel3.SetSizer( sbSizer9 )
		self.m_panel3.Layout()
		sbSizer9.Fit( self.m_panel3 )
		fgSizer3.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.Colour( 240, 240, 240 ) )
		
		sbSizer11 = wx.StaticBoxSizer( wx.StaticBox( self.m_panel2, wx.ID_ANY, u"Potong Citra" ), wx.VERTICAL )
		
		fgSizer7 = wx.FlexGridSizer( 0, 2, 0, 20 )
		fgSizer7.AddGrowableCol( 1 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText52 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Mulai Longitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )
		fgSizer7.Add( self.m_staticText52, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl_start_lon = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl_start_lon, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText53 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Akhir Longitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )
		fgSizer7.Add( self.m_staticText53, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl_end_lon = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl_end_lon, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText54 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Mulai Latitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )
		fgSizer7.Add( self.m_staticText54, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl_start_lat = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl_start_lat, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_staticText55 = wx.StaticText( sbSizer11.GetStaticBox(), wx.ID_ANY, u"Akhir Latitude", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )
		fgSizer7.Add( self.m_staticText55, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_textCtrl_end_lat = wx.TextCtrl( sbSizer11.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl_end_lat, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		sbSizer11.Add( fgSizer7, 1, wx.EXPAND, 5 )
		
		
		self.m_panel2.SetSizer( sbSizer11 )
		self.m_panel2.Layout()
		sbSizer11.Fit( self.m_panel2 )
		fgSizer3.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )
		
		m_sdbSizer_clip = wx.StdDialogButtonSizer()
		self.m_sdbSizer_clipOK = wx.Button( self, wx.ID_OK )
		m_sdbSizer_clip.AddButton( self.m_sdbSizer_clipOK )
		self.m_sdbSizer_clipCancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer_clip.AddButton( self.m_sdbSizer_clipCancel )
		m_sdbSizer_clip.Realize();
		
		fgSizer3.Add( m_sdbSizer_clip, 1, wx.ALIGN_RIGHT|wx.BOTTOM|wx.EXPAND, 5 )
		
		
		self.SetSizer( fgSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_sdbSizer_clipCancel.Bind( wx.EVT_BUTTON, self.sdbSizer_clip_cancel )
		self.m_sdbSizer_clipOK.Bind( wx.EVT_BUTTON, self.sdbSizer_clip_ok )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def sdbSizer_clip_cancel( self, event ):
		event.Skip()
	
	def sdbSizer_clip_ok( self, event ):
		event.Skip()
	

###########################################################################
## Class ImportDialog
###########################################################################

class ImportDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Impor Citra Landsat 8", pos = wx.DefaultPosition, size = wx.Size( 428,248 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		fgSizer1 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer1.AddGrowableCol( 1 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Citra Band 4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		fgSizer1.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_filePicker_band4 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"GeoTIFF (*.tif)|*.tif", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
		fgSizer1.Add( self.m_filePicker_band4, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_bitmap_band4_condition = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"assets/icon-cross-mark-24x24.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_bitmap_band4_condition, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Citra Band 5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer1.Add( self.m_staticText4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_filePicker_band5 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"GeoTIFF (*.tif)|*.tif", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
		fgSizer1.Add( self.m_filePicker_band5, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_bitmap_band5_condition = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"assets/icon-cross-mark-24x24.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_bitmap_band5_condition, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"Metadata Citra", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		fgSizer1.Add( self.m_staticText6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_filePicker_metadata = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"Metadata files (*.txt)|*.txt", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
		fgSizer1.Add( self.m_filePicker_metadata, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_bitmap_metadata_condition = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"assets/icon-cross-mark-24x24.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.m_bitmap_metadata_condition, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		
		bSizer2.Add( fgSizer1, 1, wx.EXPAND, 5 )
		
		m_sdbSizer_import_dialog = wx.StdDialogButtonSizer()
		self.m_sdbSizer_import_dialogOK = wx.Button( self, wx.ID_OK )
		m_sdbSizer_import_dialog.AddButton( self.m_sdbSizer_import_dialogOK )
		self.m_sdbSizer_import_dialogCancel = wx.Button( self, wx.ID_CANCEL )
		m_sdbSizer_import_dialog.AddButton( self.m_sdbSizer_import_dialogCancel )
		m_sdbSizer_import_dialog.Realize();
		
		bSizer2.Add( m_sdbSizer_import_dialog, 1, wx.ALIGN_BOTTOM|wx.ALIGN_RIGHT|wx.SHAPED, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_filePicker_band4.Bind( wx.EVT_FILEPICKER_CHANGED, self.fp_band4_on_file_changed )
		self.m_filePicker_band5.Bind( wx.EVT_FILEPICKER_CHANGED, self.fp_band5_on_file_changed )
		self.m_filePicker_metadata.Bind( wx.EVT_FILEPICKER_CHANGED, self.fp_metadata_on_file_changed )
		self.m_sdbSizer_import_dialogCancel.Bind( wx.EVT_BUTTON, self.dia_import_cancel )
		self.m_sdbSizer_import_dialogOK.Bind( wx.EVT_BUTTON, self.dia_import_ok )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def fp_band4_on_file_changed( self, event ):
		event.Skip()
	
	def fp_band5_on_file_changed( self, event ):
		event.Skip()
	
	def fp_metadata_on_file_changed( self, event ):
		event.Skip()
	
	def dia_import_cancel( self, event ):
		event.Skip()
	
	def dia_import_ok( self, event ):
		event.Skip()
	

###########################################################################
## Class CreditDialog
###########################################################################

class CreditDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Kredit", pos = wx.DefaultPosition, size = wx.Size( 598,271 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Pengolah Landsat 8 - Normalized Difference Vegetation Index", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )
		self.m_staticText34.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer3.Add( self.m_staticText34, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_staticText39 = wx.StaticText( self, wx.ID_ANY, u"Aplikasi pengolah citra Landsat 8 menjadi citra Normalized Difference Vegetation Index", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )
		bSizer3.Add( self.m_staticText39, 0, wx.ALL, 5 )
		
		self.m_staticText40 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )
		bSizer3.Add( self.m_staticText40, 0, wx.ALL, 5 )
		
		fgSizer6 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"Kredit", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText35.Wrap( -1 )
		fgSizer6.Add( self.m_staticText35, 0, wx.ALL, 5 )
		
		self.m_staticText36 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		fgSizer6.Add( self.m_staticText36, 0, wx.ALL, 5 )
		
		self.m_staticText37 = wx.StaticText( self, wx.ID_ANY, u"Pembuat:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )
		fgSizer6.Add( self.m_staticText37, 0, wx.ALL, 5 )
		
		self.m_staticText38 = wx.StaticText( self, wx.ID_ANY, u"I Dewa Gede Sathyananda Diva (1705551005)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )
		fgSizer6.Add( self.m_staticText38, 0, wx.ALL, 5 )
		
		
		bSizer3.Add( fgSizer6, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class HelpDialog
###########################################################################

class HelpDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Cara Menggunakan", pos = wx.DefaultPosition, size = wx.Size( 588,259 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"Cara Menggunakan:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		self.m_staticText41.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 90, 92, False, wx.EmptyString ) )
		
		bSizer4.Add( self.m_staticText41, 0, wx.ALL, 5 )
		
		self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, u"1. Pastikan sudah memiliki citra Landsat 8 Level 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		bSizer4.Add( self.m_staticText42, 0, wx.ALL, 5 )
		
		self.m_staticText43 = wx.StaticText( self, wx.ID_ANY, u"2. Klik 'Impor Gambar' untuk mengimpor citra dan metadata", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )
		bSizer4.Add( self.m_staticText43, 0, wx.ALL, 5 )
		
		self.m_staticText44 = wx.StaticText( self, wx.ID_ANY, u"3. Klik 'Potong Gambar' untuk memotong citra menjadi ukurang lebih kecil", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		bSizer4.Add( self.m_staticText44, 0, wx.ALL, 5 )
		
		self.m_staticText45 = wx.StaticText( self, wx.ID_ANY, u"4. Klik 'Koreksi TOA' untuk melakukan koreksi pada citra", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )
		bSizer4.Add( self.m_staticText45, 0, wx.ALL, 5 )
		
		self.m_staticText46 = wx.StaticText( self, wx.ID_ANY, u"5. Klik 'Proses' untuk mengolah citra menjadi NDVI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )
		bSizer4.Add( self.m_staticText46, 0, wx.ALL, 5 )
		
		self.m_staticText47 = wx.StaticText( self, wx.ID_ANY, u"6. Klik 'Simpan' untuk menyimpan NDVI", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )
		bSizer4.Add( self.m_staticText47, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	


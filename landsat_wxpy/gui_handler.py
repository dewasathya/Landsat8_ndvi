# User Interface
import wx
import wx.xrc

from landsat_wxpy.gui import MainFrame
from landsat_wxpy.gui import ImportDialog
from landsat_wxpy.gui import ClipDialog
from landsat_wxpy.gui import HelpDialog
from landsat_wxpy.gui import CreditDialog

# NDVI
from landsat_wxpy.NDVI import NDVI
from PIL import Image
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os
import sys

class MainFrame_Handler(MainFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.ndvi = NDVI()

    # Local Methods
    def convertToImage(self, array, isfloat):
        if isfloat:
            rgb = array * 255
        else:
            rgb = array / 255

        pilImage = Image.fromarray(rgb).convert('RGB')
        image = wx.EmptyImage(pilImage.size[0], pilImage.size[1])
        image.SetData(pilImage.tobytes())

        H = image.GetHeight()
        W = image.GetWidth()
        newH = 250
        newW = 250
        if (W > H):
            newH = 250 * H / W
        else:
            newW = 250 * W / H

        image = image.Scale(newW, newH)
        return image

    def onCropFinish(self, red, nir):
        red_image = self.convertToImage(red, False)
        nir_image = self.convertToImage(nir, False)
        print(red)
        print(nir)

        scaledImageRed = red_image.Scale(180, 180, wx.IMAGE_QUALITY_HIGH)
        scaledImageNir = nir_image.Scale(180, 180, wx.IMAGE_QUALITY_HIGH)

        self.m_bitmap_band4.SetBitmap(wx.Bitmap(scaledImageRed))
        self.m_bitmap_band5.SetBitmap(wx.Bitmap(scaledImageNir))

        self.Layout()
        wx.MessageBox("Citra Berhasil Dipotong!", "Potong Berhasil!", wx.OK | wx.ICON_INFORMATION)

    def onCorrectionFinish(self, b4ref, b5ref, b4rad, b5rad):
        # save file
        plt.imshow(b4rad)
        plt.savefig("temp/radiance_red.png")

        plt.imshow(b5rad)
        plt.savefig("temp/radiance_nir.png")

        plt.imshow(b4ref)
        plt.savefig("temp/reflectance_red.png")

        plt.imshow(b5ref)
        plt.savefig("temp/reflectance_nir.png")

        # Band 4 Reflectance
        b4refImage = wx.Bitmap("temp/reflectance_red.png", wx.BITMAP_TYPE_ANY)
        W = b4refImage.GetWidth()
        H = b4refImage.GetHeight()
        if W > H:
            NewW = 180
            NewH = 180 * H / W
        else:
            NewH = 180
            NewW = 180 * W / H
        image = wx.Bitmap.ConvertToImage(b4refImage)
        scaledImage = image.Scale(NewW, NewH, wx.IMAGE_QUALITY_HIGH)
        bitmap = wx.Bitmap(scaledImage)
        self.m_bitmap_band4.SetBitmap(wx.Bitmap(bitmap))

        # Band 5 Reflectance
        b5refImage = wx.Bitmap("temp/reflectance_nir.png", wx.BITMAP_TYPE_ANY)
        image = wx.Bitmap.ConvertToImage(b5refImage)
        scaledImage = image.Scale(NewW, NewH, wx.IMAGE_QUALITY_HIGH)
        bitmap = wx.Bitmap(scaledImage)
        self.m_bitmap_band5.SetBitmap(wx.Bitmap(bitmap))

        # b4radImage = wx.Bitmap("temp/radiance_red.png", wx.BITMAP_TYPE_ANY)
        # image = wx.Bitmap.ConvertToImage(b4radImage)
        # scaledImage = image.Scale(NewW, NewH, wx.IMAGE_QUALITY_HIGH)
        # bitmap = wx.Bitmap(scaledImage)
        # self.m_bitmap42.SetBitmap(wx.Bitmap(bitmap))
        #
        # b5radImage = wx.Bitmap("temp/radiance_nir.png", wx.BITMAP_TYPE_ANY)
        # image = wx.Bitmap.ConvertToImage(b4radImage)
        # scaledImage = image.Scale(NewW, NewH, wx.IMAGE_QUALITY_HIGH)
        # bitmap = wx.Bitmap(scaledImage)
        # self.m_bitmap411.SetBitmap(wx.Bitmap(bitmap))

        self.Layout()
        wx.MessageBox("Koreksi Citra Berhasil Dilakukan!", "Koreksi Berhasil!", wx.OK | wx.ICON_INFORMATION)

    def onNDVIFinish(self, result):
        image = self.convertToImage(result, True)
        print('result ', image)
        self.m_bitmap_citra_hasil.SetBitmap(wx.Image.ConvertToBitmap(image))

        wx.MessageBox("Proses NDVI Berhasil Dilakukan!", "Proses Berhasil!", wx.OK | wx.ICON_INFORMATION)
        self.Layout()

    # Event Handlers
    def app_exit( self, event ):
        dialog = wx.MessageDialog(None, "Apakah Benar Ingin Keluar?", "Keluar?", wx.YES_NO | wx.ICON_INFORMATION)
        result = dialog.ShowModal()

        if result:
            if os.path.exists('temp/radiance_nir.png'):
                os.remove('temp/radiance_nir.png')

            if os.path.exists('temp/radiance_red.png'):
                os.remove('temp/radiance_red.png')

            if os.path.exists('temp/reflectance_nir.png'):
                os.remove('temp/reflectance_nir.png')

            if os.path.exists('temp/reflectance_red.png'):
                os.remove('temp/reflectance_red.png')

            wx.CallAfter(sys.exit(0))

    def help_about( self, event ):
        dialog = CreditDialog_Handler(None)
        dialog.ShowModal()

    def help_using( self, event ):
        dialog = HelpDialog_Handler(None)
        dialog.ShowModal()

    def tool_create_new( self, event ):
        print('nya new')
        dialog = wx.MessageDialog(None, 'Apakah Ingin Membuat Baru?', 'Buat Baru?', wx.YES_NO | wx.ICON_INFORMATION)
        result = dialog.ShowModal()

        if result == wx.ID_YES:
            self.ndvi = NDVI()
            self.m_bitmap_band4.SetBitmap(wx.NullBitmap)
            self.m_bitmap_band5.SetBitmap(wx.NullBitmap)
            self.m_bitmap_citra_hasil.SetBitmap(wx.NullBitmap)

            self.m_staticText_ref_mult_band_5.SetLabelText("")
            self.m_staticText_ref_mult_band_4.SetLabelText("")
            self.m_staticText_ref_add_band_5.SetLabelText("")
            self.m_staticText_ref_add_band_4.SetLabelText("")
            self.m_staticText_long_start.SetLabelText("")
            self.m_staticText_long_end.SetLabelText("")
            self.m_staticText_lat_start.SetLabelText("")
            self.m_staticText_lat_end.SetLabelText("")

    def tool_import_images( self, event ):
        dial_import = ImportDialog_Handler(None, self.ndvi)
        dial_import.ShowModal()

        if self.ndvi.isOpenB4 and self.ndvi.isOpenB5 and self.ndvi.isMtl:
            # Change Metadata Information
            self.m_staticText_long_start.SetLabelText(self.ndvi.lonStartDefault)
            self.m_staticText_long_end.SetLabelText(self.ndvi.lonEndDefault)
            self.m_staticText_lat_start.SetLabelText(self.ndvi.latStartDefault)
            self.m_staticText_lat_end.SetLabelText(self.ndvi.latEndDefault)

            self.m_staticText_ref_add_band_4.SetLabelText(self.ndvi.b4AddReflectance)
            self.m_staticText_ref_add_band_5.SetLabelText(self.ndvi.b5AddReflectance)
            self.m_staticText_ref_mult_band_4.SetLabelText(self.ndvi.b4MultiReflectance)
            self.m_staticText_ref_mult_band_5.SetLabelText(self.ndvi.b5MultiReflectance)

            # Add Image Band 4
            openImage = mpimg.imread(self.ndvi.path_b4)
            image = self.convertToImage(openImage, False)
            scaledImage = image.Scale(180, 180, wx.IMAGE_QUALITY_HIGH)
            bitmap = wx.Bitmap(scaledImage)
            self.m_bitmap_band4.SetBitmap(bitmap)

            # Add Image Band 5
            openImage = mpimg.imread(self.ndvi.path_b5)
            image = self.convertToImage(openImage, False)
            scaledImage = image.Scale(180, 180, wx.IMAGE_QUALITY_HIGH)
            bitmap = wx.Bitmap(scaledImage)
            self.m_bitmap_band5.SetBitmap(bitmap)

            self.Layout()

    def tool_crop_image( self, event ):
        if self.ndvi.isOpenB4 and self.ndvi.isOpenB5:
            clip_dialog = ClipDialog_Handler(None, self.ndvi)
            clip_dialog.ShowModal()

            if self.ndvi.isCropped:
                self.onCropFinish(self.ndvi.crop_B4, self.ndvi.crop_B5)
        else:
            wx.MessageBox("Citra Tidak Dapat Dipotong, Karena Citra Belum Diimpor!", "Tidak Dapat Memotong Citra",
                          wx.OK | wx.ICON_ERROR)

    def tool_toa_correction( self, event ):
        if self.ndvi.isCropped:
            self.ndvi.StartCorrection()

            if self.ndvi.isCorrection:
                self.onCorrectionFinish(self.ndvi.correctionB4Reflectance, self.ndvi.correctionB5Reflectance,
                                        self.ndvi.correctionB4Radiance, self.ndvi.correctionB5Radiance)
        else:
            wx.MessageBox("Citra Tidak Dapat Dikoreksi, Karena Citra Belum Dipotong!", "Tidak Dapat Mengkoreksi Citra",
                          wx.OK | wx.ICON_ERROR)

    def tool_process_image( self, event ):
        if self.ndvi.isCorrection:
            self.ndvi.StartNDVI()

            if self.ndvi.isNdvi:
                self.onNDVIFinish(self.ndvi.ndviResult)
        else:
            wx.MessageBox("Citra Tidak Dapat Diproses, Karena Citra Belum Dikoreksi!", "Tidak Dapat Mengproses Citra",
                          wx.OK | wx.ICON_ERROR)

    def tool_save_image( self, event ):
        if self.ndvi.isNdvi:
            print('nya save')
            saveFileDialog = wx.FileDialog(self, 'Save to TIF', '', 'ndvi', 'GeoTiff Files(*tif)|*.tif',
                                           wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

            if (saveFileDialog.ShowModal() == wx.ID_OK):
                path = saveFileDialog.GetPath()
                self.ndvi.SaveResult(path)
                wx.MessageBox("Hasil Proses Berhasil Disimpan!", "Simpan Hasil Berhasil!", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox("Citra Tidak Dapat Disimpan, Karena Citra Belum Diproses!", "Tidak Dapat Menyimpan Citra",
                          wx.OK | wx.ICON_ERROR)

class ImportDialog_Handler(ImportDialog):
    def __init__(self, parent, ndvi):
        super().__init__(parent)
        self.ndvi = ndvi

    def fp_band4_on_file_changed( self, event ):
        band4_path = event.GetPath()
        self.ndvi.OpenB4File(band4_path)

        if self.ndvi.isOpenB4:
            if self.ndvi.open_B4:
                self.m_bitmap_band4_condition.SetBitmap(wx.Bitmap('assets/icon-tick-mark-24x24.png'))

            else:
                self.m_bitmap_band4_condition.SetBitmap(wx.Bitmap('assets/icon-cross-mark-24x24.png'))
                wx.MessageBox("Gagal Membuka Citra Band 4!", "Gagal Membuka!", wx.OK | wx.ICON_ERROR)
        else:
            self.m_bitmap_band4_condition.SetBitmap(wx.Bitmap('assets/icon-cross-mark-24x24.png'))
            wx.MessageBox("Gagal Membuka Karena Bukan Citra Band 4!", "Gagal Membuka!", wx.OK | wx.ICON_ERROR)

    def fp_band5_on_file_changed( self, event ):
        band5_path = event.GetPath()
        self.ndvi.OpenB5File(band5_path)

        if self.ndvi.isOpenB5:
            if self.ndvi.open_B5:
                self.m_bitmap_band5_condition.SetBitmap(wx.Bitmap('assets/icon-tick-mark-24x24.png'))

            else:
                self.m_bitmap_band5_condition.SetBitmap(wx.Bitmap('assets/icon-cross-mark-24x24.png'))
                wx.MessageBox("Gagal Membuka Citra Band 5!", "Gagal Membuka!", wx.OK | wx.ICON_ERROR)
        else:
            self.m_bitmap_band5_condition.SetBitmap(wx.Bitmap('assets/icon-cross-mark-24x24.png'))
            wx.MessageBox("Gagal Membuka Karena Bukan Citra Band 5!", "Gagal Membuka!", wx.OK | wx.ICON_ERROR)

    def fp_metadata_on_file_changed( self, event ):
        metadata_path = event.GetPath()
        self.ndvi.OpenMtlFile(metadata_path)

        if self.ndvi.isMtl:
            self.m_bitmap_metadata_condition.SetBitmap(wx.Bitmap('assets/icon-tick-mark-24x24.png'))
        else:
            self.m_bitmap_metadata_condition.SetBitmap(wx.Bitmap('assets/icon-cross-mark-24x24.png'))

    def dia_import_cancel( self, event ):
        self.Destroy()

    def dia_import_ok( self, event ):
        if self.ndvi.isOpenB4 and self.ndvi.isOpenB5 and self.ndvi.isMtl:
            self.Destroy()
        else:
            wx.MessageBox("Pastikan Semua File Telah Dipilih Dengan Benar!", "Kesalahan Pemilihan File!", wx.OK | wx.ICON_ERROR)

class ClipDialog_Handler(ClipDialog):
    def __init__(self, parent, ndvi):
        super().__init__(parent)
        self.ndvi = ndvi

        self.m_textCtrl_ori_start_lon.SetValue(str(self.ndvi.lonStartDefault))
        self.m_textCtrl_ori_end_lon.SetValue(str(self.ndvi.lonEndDefault))
        self.m_textCtrl_ori_start_lat.SetValue(str(self.ndvi.latStartDefault))
        self.m_textCtrl_ori_end_lat.SetValue(str(self.ndvi.latEndDefault))

    def sdbSizer_clip_cancel( self, event ):
        self.Destroy()

    def sdbSizer_clip_ok( self, event ):
        print('nya')
        if self.ndvi.isMtl and (self.ndvi.isOpenB4 and self.ndvi.isOpenB5):
            lonStart = self.m_textCtrl_start_lon.GetValue()
            latStart = self.m_textCtrl_start_lat.GetValue()
            lonEnd = self.m_textCtrl_end_lon.GetValue()
            latEnd = self.m_textCtrl_end_lat.GetValue()

            print(lonStart)
            print(latStart)
            print(lonEnd)
            print(latEnd)

            self.ndvi.SetCropCoordinate(lonStart, lonEnd, latStart, latEnd)
            self.ndvi.CropImage()

            self.Destroy()
        else:
            wx.MessageBox("Gagal Potong Citra Karena Citra Tidak Dibuka Atau Metadata Tidak Dibuka!", "Potong Citra Gagal!", wx.OK | wx.ICON_ERROR)

class HelpDialog_Handler(HelpDialog):
    def __init__(self, parent):
        super().__init__(parent)

class CreditDialog_Handler(CreditDialog):
    def __init__(self, parent):
        super().__init__(parent)

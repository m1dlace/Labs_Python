#Лаба 2 задание 4

#Напишите скрипт, который позволяет ввести с клавиатуры имя текстового файла,

#найти в нем с помощью регулярных выражений все подстроки определенного вида,

#в соответствии с вариантом. Например, для варианта № 1 скрипт должен вывести

#на экран следующее:

# Строка 3, позиция 10 : найдено '11-05-2014' 

# Строка 12, позиция 2 : найдено '23-11-2014' 

# Строка 12, позиция 17 : найдено '23-11-2014' 



#Вариант 5: Найты все номера типа (000)1234567.
#Вар5

import string
import wx
import os
import re
from glob import glob
import datetime
import logging


class Window(wx.Frame):
    def check_log(self):

        log_filename = "Log.log"
        path = os.path.join(os.getcwd(), log_filename)
        if os.path.exists(path) == False:
            dlg = wx.MessageDialog(self, "Файл лога не найден. Файл будет создан", "Проверка лога", wx.OK)
            dlg.ShowModal()
            logging.basicConfig(filename=log_filename, level=logging.INFO)

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(600, 400))
        self.control = wx.ListBox(self, style=wx.LB_SINGLE)
        self.statusbar = self.CreateStatusBar(2)
        self.statusbar.SetStatusWidths([-6, -4])
        self.Show(True)
        self.check_log()

        menu_file = wx.Menu()
        openItem = menu_file.Append(wx.ID_OPEN, "Открыть", "Откройте файл")
        menu_log = wx.Menu()
        exportItem = menu_log.Append(wx.ID_SAVE, "Экспорт", "Экспорт файла")
        addItem = menu_log.Append(wx.ID_ADD, "Добавить в лог", "Обновление лог файла")
        viewItem = menu_log.Append(wx.ID_ABOUT, "Просмотр", "Просмотреть лог файл")

        bar = wx.MenuBar()
        bar.Append(menu_file, "Файл")
        bar.Append(menu_log, "Лог")

        self.SetMenuBar(bar)
        self.Bind(wx.EVT_MENU, self.OnOpen, openItem)
        self.Bind(wx.EVT_MENU, self.OnExport, exportItem)
        self.Bind(wx.EVT_MENU, self.AddLog, addItem)
        self.Bind(wx.EVT_MENU, self.View, viewItem)



    def OnOpen(self, e):
        self.dirname = " "
        openDlg = wx.FileDialog(self, "Выберите файл для открытия", self.dirname, " ", "*.*")
        if openDlg.ShowModal() == wx.ID_OK:
            self.filename = openDlg.GetFilename()
            self.dirname = openDlg.GetDirectory()
            path = os.path.join(self.dirname, self.filename)
            mask = re.compile("[(]\d{3}[)]\d{7}")
            with open(path) as file:
                date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
                self.control.Append("Файл " + path +" был обработан, " + date + ":")
                self.control.Append("")
                for i, line in enumerate(file):
                    for match in re.finditer(mask, line):
                        self.control.Append("Строка " + str(i+1) + ", позиция " + str(match.start()+1) +" : найдено '{}'".format(line[match.start():match.end()]))

            self.control.Append("")
            self.statusbar.SetStatusText("Обработан файл " + path)
            size = str(os.path.getsize(path))
            size = [''.join(size[::-1][i:i+3])[::-1]
            for i in range(0, len(size), 3)]
            size = ' '.join(size[::-1])
            self.statusbar.SetStatusText(size + " байт", 1)
    def AddLog(self, e):
        path = os.path.join(os.getcwd(), "Log.log")
        with open(path, "a") as file:
            for line in self.control.GetStrings():
                file.write(line + "\n")
    def View(self, e):
        dlg = wx.MessageDialog(
            self, "Открыть лог?", "Просмотр лога", wx.YES_NO)
        if dlg.ShowModal() == wx.ID_YES:
            self.control.Clear()
            path = os.path.join(os.getcwd(), "Log.log")
            with open(path, "r") as file:
                self.control.AppendItems(file.readlines())
            self.statusbar.SetStatusText("Открыт лог")
            self.statusbar.SetStatusText("", 1)
        else:
            dlg.Destroy()

    def OnExport(self, e):
        self.dirname = " "
        openDlg = wx.FileDialog(self, "Выберите файл для записи", self.dirname, " ", "*.*")
        if openDlg.ShowModal() == wx.ID_OK:
            self.filename = openDlg.GetFilename()
            self.dirname = openDlg.GetDirectory()
            path = os.path.join(self.dirname, self.filename)
            with open(path, "w") as file:
                for line in self.control.GetStrings():
                    file.write(line + "\n")

if __name__ == "__main__":
    app = wx.App()
    wnd = Window(None, "Поиск строк")
    app.MainLoop()
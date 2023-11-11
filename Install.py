import win32api
import win32con
import ctypes
import sys
import shutil
import os
from tkinter.ttk import *
import tkinter.filedialog
import tkinter as tk

class mainThread:
    def __init__(self):
        self.dir = ""
        self.path_old = os.getcwd()
        self.root = tk.Tk()
        self.root.title("输入WPS目录。")
        x = int((self.root.winfo_screenwidth() - self.root.winfo_reqwidth()) / 2)
        y = int((self.root.winfo_screenheight() - self.root.winfo_reqheight()) / 2)
        self.root.geometry("500x75")
        self.root.geometry("+{}+{}".format(x, y))
        self.root.iconbitmap("YS.ico")
        self.entry = Entry(self.root)
        self.entry.pack(fill=tk.X, padx=30)
        f1 = Frame(self.root)
        f1.pack(side=tk.BOTTOM, pady=5)
        button = Button(f1, text="确定", command=self.get)
        button.grid(column=0, row=0, padx=3)
        button_dir = Button(f1, text="浏览目录...", command=self.browse_dir)
        button_dir.grid(column=1, row=0, padx=3)
        self.root.protocol("WM_DELETE_WINDOW", lambda: os._exit(0))
        self.root.mainloop()

        try:
            shutil.copy("./splash_default_bg.png", r"\office6\mui\zh_CN\resource\splash")
            shutil.copy("./hdpi/splash_default_bg.png", r"\office6\mui\zh_CN\resource\splash\hdpi")
            win32api.MessageBox(0, "替换完成。", "", win32con.MB_OK | win32con.MB_TOPMOST | win32con.MB_ICONINFORMATION)

        except FileExistsError as f:
            win32api.MessageBox(0, str(f), "", win32con.MB_OK | win32con.MB_TOPMOST)

        except Exception as e:
            win32api.MessageBox(0, str(e), "", win32con.MB_OK | win32con.MB_TOPMOST)


    def get(self):

        if self.entry.get() == "":
            win32api.MessageBox(0, "不允许空目录。", "",
                                win32con.MB_TASKMODAL | win32con.MB_TOPMOST | win32con.MB_ICONWARNING)
            return

        self.dir = self.entry.get()
        self.root.destroy()

    def browse_dir(self):
        self.dir = tkinter.filedialog.askdirectory(mustexist=True, initialdir="~")
        self.entry.insert(0, self.dir)


if __name__ == '__main__':
    try:
        Admin = ctypes.windll.shell32.IsUserAnAdmin()

    except Exception:
        Admin = False

    if not Admin:
        win32api.MessageBox(0, "此程序需要管理员权限。", "错误: 过低的权限", win32con.MB_ICONHAND | win32con.MB_TOPMOST)
        sys.exit()

    mainThread()

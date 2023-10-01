"""Landing page of tkinter(GUI)."""
import os
import tkinter

import upload_single_file


def insert_listbox():
    """Insert a file to listbox."""
    current_directory = os.getcwd()  # دریافت مسیر پوشه فعلی
    current_directory = os.path.join(current_directory, "files")
    files = os.listdir(current_directory)  # دریافت لیست فایل‌ها در پوشه فعلی

    # فقط فایل‌ها را انتخاب می‌کنیم و به Listbox اضافه می‌کنیم
    for file in files:
        if os.path.isfile(os.path.join(current_directory, file)):
            listbox.insert(tkinter.END, file)


def download():
    """Direct to download module."""
    print("hello")


def upload():
    """Direct to upload_single-file module."""
    upload_single_file.main(listbox)
    insert_listbox()


master = tkinter.Tk()
master.title("Share media")

master.geometry("400x250")  # تنظیم ابعاد پنجره اصلی|

listbox = tkinter.Listbox(master, selectmode=tkinter.SINGLE, width=60)
insert_listbox()
listbox.pack()


frame = tkinter.Frame(master)
frame.pack(padx=10, pady=5)

button_download = tkinter.Button(
    frame,
    text="Download",
    width=10,
    height=1,
    command=download,
)
button_upload = tkinter.Button(
    frame,
    text="Upload",
    width=10,
    height=1,
    command=upload,
)

button_download.pack(side=tkinter.LEFT, padx=10)
button_upload.pack(side=tkinter.LEFT, padx=10)


master.mainloop()

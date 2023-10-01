"""Upload file in single way on tkinter."""
import os
import shutil
import tkinter
from tkinter import filedialog


def upload_file():
    """Upload file in to serever."""
    file_path = filedialog.askopenfilename(multiple=False)
    current_directory = os.getcwd()  # دریافت مسیر پوشه فعلی
    current_directory = os.path.join(current_directory, "files")
    shutil.copy(
        file_path,
        current_directory,
    )  # move file to distenation folder


def main(listbox):
    """Manage the main module."""
    master = tkinter.Tk()
    master.title("Upload Single File")  # set the title

    master.geometry("400x250")  # set the window size

    listbox = tkinter.Listbox(
        master,
        selectmode=tkinter.SINGLE,
        width=60,
    )  # create a list box
    listbox.pack(padx=10, pady=10)

    upload_button = tkinter.Button(
        master,
        text="Upload",
        command=upload_file,
    )  # create a button for upload onclick
    upload_button.pack(pady=10)

    # master.mainloop()

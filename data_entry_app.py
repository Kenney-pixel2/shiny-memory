import tkinter as tk
from tkinter import ttk
from datetime import datetime
from pathlib import Path
import csv
from decimal import Decimal, InvalidOperation


##################
# Widget Classes #
##################

class ValidatedMixin:
    """Adds a validation functionality to an input widget"""

    def __init__(self, *args, error_var=None, **kwargs):
        self.error = error_var or tk.StringVar()
        super().__init__(*args, **kwargs)

        vcmd = self.register(self._validate)
        invcmd = self.register(self._invalid)

        self.configure(
            validate='all',
            validatecommand=(vcmd, '%P', '%s', '%S', '%V', '%i', '%d'),
            invalidcommand=(invcmd, '%P', '%s', '%S', '%V', '%i', '%d')
        )

class Application(tk.Tk):
    """Application root window"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("ABQ Data Entry Application")
        self.columnconfigure(0, weight=1)

        ttk.Label(
                self,
                text="ABQ Data Entry Application",
                font=("TkDefaultFont", 16)
        ).grid(row=0)

        self.recordform = DataRecordForm(self)
        self.recordform.grid(row=1, padx=10, sticky=(tk.W + tk.E))


if __name__ == "__main__":

    app = Application()
    app.mainloop()

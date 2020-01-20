import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Combobox
import csv

class dsdfreqparser(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.rrsystemNamelbl = tk.Label(self, text="System Name")
        self.rrsystemNamelbl.grid(sticky=tk.W, column=0, row=0)

        self.rrProtocollbl = tk.Label(self, text="Trunking Protocol")
        self.rrProtocollbl.grid(sticky=tk.W, column=0, row=2)

        self.rrNetIDlbl = tk.Label(self, text="Network ID")
        self.rrNetIDlbl.grid(sticky=tk.W, column=0, row=3)

        self.rrsystemNameEnt = tk.Entry(self)
        self.rrsystemNameEnt.grid(sticky=tk.W, column=1, row=0)

        self.rrProtocolCombo = Combobox(self)
        self.rrProtocolCombo['values']= ('D-Star', 'IDAS', 'NEXEDGE48', 'NEXEDGE96', 'dPMR', 'DMR', 'Cap+', 'Con+', 'TIII', 'P25', 'ProVoice')
        self.rrProtocolCombo.current(7)
        self.rrProtocolCombo.grid(sticky=tk.W, column=1, row=2)

        self.rrNetIDEnt = tk.Entry(self)
        self.rrNetIDEnt.grid(sticky=tk.W, column=1, row=3)

        self.convertBTN = tk.Button(self, text="Convert", command=self.parse_file)
        self.convertBTN.grid(sticky=tk.W, padx=5, pady=5, column=0, row=5)

        self.rrParsedOutput = tk.Text(self, selectborderwidth=2)
        self.rrParsedOutput.grid(sticky=tk.W, padx=5, pady=5, columnspan=2, row=7)
    
    def RadioRefCSV(self):
        fileLocation = filedialog.askopenfilename(title="Select your Radio Reference CSV", filetypes=(("CSV files","*.csv"),("All Files","*.*")))
        return fileLocation

    def parse_file(self):
        rrsysname = self.rrsystemNameEnt.get()
        rrfilename = self.RadioRefCSV()
        rrprotocol = self.rrProtocolCombo.get()
        rrnetid = self.rrNetIDEnt.get()

        with open(rrfilename) as csvfile:
            readCSV = csv.DictReader(csvfile, delimiter=',')
            self.rrParsedOutput.insert(tk.INSERT, ";" + rrsysname + "\n")
            for row in readCSV:
                self.rrParsedOutput.insert(tk.INSERT, rrprotocol + ", " + rrnetid + ", " + row['Site Dec'] + ', 1, ' + row['Frequencies'] + ", 0.0, 0\n")
                for freqs in row[None]:
                    self.rrParsedOutput.insert(tk.INSERT, rrprotocol + ", " + rrnetid + ", " + row['Site Dec'] + ", ***OTANUMBER***, " + str(freqs) + ", 0.0, 0\n")

app = dsdfreqparser()
app.mainloop()
class Mietektek (object):
    def Bimbingan(self, meeting):
        self.switcher = {
            "pertemuan1": "Pertemuan 1",
            "pertemuan2": "Pertemuan 2",
            "pertemuan3": "Pertemuan 3",
            "pertemuan4": "Pertemuan 4",
            "pertemuan5": "Pertemuan 5",
            "pertemuan6": "Pertemuan 6",
            "pertemuan7": "Pertemuan 7",
            "pertemuan8": "Pertemuan 8",
            "pertemuan9": "Pertemuan 9",
            "pertemuan10": "Pertemuan 10"
        }

        return self.switcher.get(meeting, "kosong")
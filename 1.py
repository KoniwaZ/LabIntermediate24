data = {
    "Dr. A": {("Matematika", "Ganjil"), ("Fisika", "Genap")},
    "Dr.    B": {("Kimia", "Ganjil")},
}


def addD(data, dosen, matkul, sem):
    if dosen not in data:
        data[dosen] = set()
        data[dosen].add((matkul, sem))
    else:
        data[dosen].add((matkul, sem))


def removeM(data, dosen, matkul, sem):
    if dosen in data:
        if (matkul, sem) in data[dosen]:
            data[dosen].remove((matkul, sem))


def removeD(data, dosen):
    if dosen in data:
        del data[dosen]


def printData(data):
    for dosen in data:
        for matkul, sem in data[dosen]:
            print(dosen, matkul, sem)


addD(data, "Dr. A", "Biologi", "Ganjil")
addD(data, "Dr. A", "Bahasa", "Genap")
addD(data, "Dr. B", "Astronomi", "Ganjil")

printData(data)

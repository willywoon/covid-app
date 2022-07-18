import requests


class Consulta:
    def __init__(self, url):
        self.url = url
        self.listaPasises = []
        self.consulta = ''

    def getUrl(self):
        return self.url

    def getListaPasises(self):
        return self.listaPasises

    def consultar(self):
        self.consulta = requests.get(self.url).json()
        self.guardarEnLista()

    def guardarEnLista(self):
        for pais in self.consulta['Countries']:
            pais['Date'] = self.cortarFecha(pais['Date'])
            self.listaPasises.append([pais['CountryCode'], pais['Slug'], pais['TotalConfirmed'],
                                      pais['TotalDeaths'], pais['NewDeaths'], pais['Date']])

    def cortarFecha(self, fecha):
        return fecha[:10]

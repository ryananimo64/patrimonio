from PyQt5.QtWidgets import QWidget,QLabel,QBoxLayout,QVBoxLayout,QHBoxLayout,QApplication,QLineEdit,QPushButton
import sys

class patrimonio(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(400,100,700,350)
        self.setWindowTitle("Patrimônio da empresa")

        self.layout_v = QVBoxLayout()

        # ID
        self.label_id = QLabel("ID do Equipamento: ")
        self.label_id.setStyleSheet("QLabel {font-size:18pt}")

        self.edit_id =  QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:12pt}")

        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)

        # Numero de serie
        self.label_ns = QLabel("Número de Série: ")
        self.label_ns.setStyleSheet("QLabel{font-size:18pt}")

        self.edit_ns = QLineEdit()
        self.edit_ns.setStyleSheet("QLineEdit {font-size:18pt}")

        self.layout_v.addWidget(self.label_ns)
        self.layout_v.addWidget(self.edit_ns)

        # Nome do Patrimônio
        self.label_nomept = QLabel("Nome do Patrimônio: ")
        self.label_nomept.setStyleSheet("QLabel{font-size:18pt}")

        self.edit_nomept = QLineEdit()
        self.edit_nomept.setStyleSheet("QLineEdit {font-size:18pt}")

        self.layout_v.addWidget(self.label_nomept)
        self.layout_v.addWidget(self.edit_nomept)

        # Tipo
        self.label_tipo = QLabel("Tipo de Equipamento: ")
        self.label_tipo.setStyleSheet("QLabel{font-size:18pt}")

        self.edit_tipo = QLineEdit()
        self.edit_tipo.setStyleSheet("QLineEdit {font-size:18pt}")

        self.layout_v.addWidget(self.label_tipo)
        self.layout_v.addWidget(self.edit_tipo)

        #Descrição
        self.label_desc = QLabel("Descrição do Equipamento: ")
        self.label_desc.setStyleSheet("QLabel{font-size:18pt}")

        self.edit_desc = QLineEdit()
        self.edit_desc.setStyleSheet("QLineEdit{font-size:18pt}")

        self.layout_v.addWidget(self.label_desc)
        self.layout_v.addWidget(self.edit_desc)

        #Localização
        self.label_loc = QLabel("localização do Equipamento: ")
        self.label_loc.setStyleSheet("QLabel{font-size:18pt}")

        self.edit_loc = QLineEdit()
        self.edit_loc.setStyleSheet("QLineEdit{font-size:18pt}")

        self.layout_v.addWidget(self.label_loc)
        self.layout_v.addWidget(self.edit_loc)

        #Data de Fabricação
        self.label_data = QLabel("Data de Fabricação: ")
        self.label_data.setStyleSheet("QLabel{font-size:18pt}")

        self.edit_data = QLineEdit()
        self.edit_data.setStyleSheet("QLineEdit{font-size:18pt}")

        self.layout_v.addWidget(self.label_data)
        self.layout_v.addWidget(self.edit_data)
        
        #Data de Aquisição
        self.label_dtaqui = QLabel("Data de Aquisição: ")
        self.label_dtaqui.setStyleSheet("QLabel{font-size:18pt}")

        self.edit_dtaqui = QLineEdit()
        self.edit_dtaqui.setStyleSheet("QLineEdit{font-size:18pt}")

        self.layout_v.addWidget(self.label_dtaqui)
        self.layout_v.addWidget(self.edit_dtaqui)




        #BUTÂO
        self.botao = QPushButton("Cadastrar")
        self.botao.setStyleSheet("QPushButton{background-color:navy;color:white;font-size:12pt;font-weight:bold}")

        self.botao.clicked.connect(self.cadastrar)

        self.layout_v.addWidget(self.botao)


        self.setLayout(self.layout_v)
    
    def cadastrar(self):
       #vamos criar uma variavel que fará 
       # referencia ao arquivo de texto
       arquivo = open("Patrimônio.txt","+a")
       arquivo.write(f"ID: {self.edit_id.text()}\n")
       arquivo.write(f"Numero de Serie: {self.edit_ns.text()}\n")
       arquivo.write(f"Nome do Patrimonio: {self.edit_nomept.text()}\n")
       arquivo.write(f"Tipo: {self.edit_tipo.text()}\n")
       arquivo.write(f"Descricao: {self.edit_desc.text()}\n")
       arquivo.write(f"Localizacao: {self.edit_loc.text()}\n")
       arquivo.write(f"Data de Fabricacao: {self.edit_data.text()}\n")
       arquivo.write(f"Data de Aquisicao: {self.edit_dtaqui.text()}\n")
       arquivo.write(f"-----------------------------------------------\n")
       arquivo.close()




app = QApplication(sys.argv)
tela = patrimonio()
tela.show()
app.exec()
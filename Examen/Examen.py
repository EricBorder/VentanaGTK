import gi
gi.require_version("Gtk", "3.0")
import sqlite3 as dbapi
from gi.repository import Gtk
from reportlab.platypus import Paragraph
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


class Examen (Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Examen")
        grid = Gtk.Grid()
        self.add(grid)
        grid.set_row_spacing(5)
        grid.set_column_spacing(5)
        grid.set_border_width(10)
        self.set_size_request(250, 100)

        lblNumAlb = Gtk.Label(label="Número de albará")
        grid.attach(lblNumAlb, 0, 0, 1, 1)
        modeloCombo = Gtk.ListStore(int)

        try:
            bbdd = dbapi.connect("modelosClasicos.dat")
        except dbapi.StandardError as e:
            print(e)
        #else:
            #print("Base de datos aberta")
        try:
            cursor = bbdd.cursor()
            cursor.execute("select numeroAlbaran from ventas")

            for fila in cursor.fetchall():
                modeloCombo.append(fila)

        except dbapi.DatabaseError as e:
            print("Erro facendo a consulta: " + str(e))
        #else:
            #print("Consulta executada")
        finally:
            cursor.close()
            bbdd.close()

        cmbAlbaran = Gtk.ComboBox.new_with_model(modeloCombo)
        grid.attach_next_to(cmbAlbaran, lblNumAlb, Gtk.PositionType.RIGHT, 1, 1)
        renderer_text = Gtk.CellRendererText()
        cmbAlbaran.pack_start(renderer_text, True)
        cmbAlbaran.add_attribute(renderer_text, "text", 0)

        modeloTreeView = Gtk.ListStore(int, str, int, int)

        try:
            bbdd = dbapi.connect("modelosClasicos.dat")
        except dbapi.StandardError as e:
            print(e)
        #else:
            #print("Base de datos aberta")
        try:
            cursor = bbdd.cursor()
            cursor.execute("select numeroAlbaran,codigoProducto, cantidade, prezoUnitario from detalleVentas")

            for fila in cursor.fetchall():
                modeloTreeView.append(fila)

        except dbapi.DatabaseError as e:
            print("Erro facendo a consulta: " + str(e))
            #else:
            #print("Consulta executada")
        finally:
            cursor.close()
            bbdd.close()

        filtro_albaran = modeloTreeView.filter_new()
        self.filtrado_albaran = None
        filtro_albaran.set_visible_func(self.filtro_albaran_num)

        trvDatos = Gtk.TreeView(model=filtro_albaran)
        for i, tituloColumna in enumerate(["numeroAlbaran", "codigoProducto", "cantidade", "prezoUnitario"]):
            celda = Gtk.CellRendererText()
            columna = Gtk.TreeViewColumn(tituloColumna, celda, text=i)
            trvDatos.append_column(columna)

        grid.attach(trvDatos, 0, 1, 2, 5)
        cmbAlbaran.connect("changed", self.on_cmbAlbaran_changed, filtro_albaran)

        btnInforme = Gtk.Button(label="Informe")
        grid.attach_next_to(btnInforme, trvDatos, Gtk.PositionType.BOTTOM, 1, 1)
        btnInforme.connect("clicked", self.on_btnInforme_clicked, modeloTreeView)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def on_cmbAlbaran_changed (self, combo, modeloTreeView):
        fila = combo.get_active()
        if fila != -1:
            modelo = combo.get_model()
            numAlbaran = modelo[fila][0]
            self.filtrado_albaran = numAlbaran
        else:
            self.filtrado_albaran = "None"
        modeloTreeView.refilter()

    def filtro_albaran_num(self, modelo, fila, datos):
        if self.filtrado_albaran is None or self.filtrado_albaran == "None":
            return True
        else:
            return modelo[fila][0] == self.filtrado_albaran

    def on_btnInforme_clicked(self, boton, modelo):
        listaInfo = Gtk.ListStore(int, str, str, int)
        listaVentas = modelo
        # numero albaran, dataAlb, dataEntrega, numCliente, codP, cantidade, prezoU
        try:
            bbdd = dbapi.connect("modelosClasicos.dat")
        except dbapi.StandardError as e:
            print(e)
        #else:
            #print("Base de datos aberta")
        try:
            cursor = bbdd.cursor()
            cursor.execute("select * from ventas")

            for fila in cursor.fetchall():
                listaInfo.append(fila)

        except dbapi.DatabaseError as e:
            print("Erro facendo a consulta: " + str(e))
        #else:
            #print("Consulta executada")
        finally:
            cursor.close()
            bbdd.close()
        follaEstilo = getSampleStyleSheet()

        doc = []
        cabeceira = follaEstilo['Heading4']
        cabeceira.pageBreakBefore = 0
        cabeceira.keepWithNext = 1
        cabeceira.backColor = colors.ivory
        corpoTexto = follaEstilo['BodyText']
        doc.append(Spacer(0, 20))
        for j in range (len(listaInfo)):
            parragrafo = Paragraph("NºAlbaran:" + str(listaInfo[j][0]), cabeceira)
            doc.append(parragrafo)
            cadea = "Fecha Alb: " + listaInfo[j][1] + ", Data entrega: " + listaInfo[j][2] + ", Num Cliente: " + str(
                listaInfo[j][3])
            parragrafo = Paragraph(cadea, corpoTexto)
            doc.append(parragrafo)
            doc.append(Spacer(0, 20))
            for i in range(len(listaVentas)):
                if listaInfo[j][0]==listaVentas[i][0]:
                    cadea2= "Codigo Producto: "+str(listaVentas[i][1])+", Cantidade: "+str(listaVentas[i][2])+", Prezo: "+str(listaVentas[i][3])
                    parragrafo2 = Paragraph(cadea2, corpoTexto)
                    doc.append(parragrafo2)

        doc.append(Spacer(0, 20))

        informe = SimpleDocTemplate("InformeAlbaran.pdf", pagesize=A4, showBoundary=1)
        informe.build(doc)


if __name__ == "__main__":
    Examen()
    Gtk.main()

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from sqlite3 import dbapi2


class Aplication(Gtk.Window):

    def __init__(self):
        super().__init__(title="Ejemplo TreeView ComboBox BD")

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        self.modelo = Gtk.ListStore(str, str, str)

        # CONEXIONES BASE DE DATOS
        try:
            bbdd = dbapi2.connect("bbdd.dat")
        except dbapi2.StandarError as e:
            print(e)
        else:
            print("Base de datos abierta")
        try:
            cursor = bbdd.cursor()
        except dbapi2.Error as e:
            print(e)
        else:
            print("cursor preparado")
        try:
            consulta = "SELECT * FROM usuarios"
            cursor.execute(consulta)
            for rexistro in cursor.fetchall():
                self.modelo.append(rexistro)
        except dbapi2.DatabaseError as e:
            print("Error haciendo la consulta" + str(e))
        else:
            print("Consulta ejecutada")
        finally:
            cursor.close()
            bbdd.close()

        # MODELO FILTRADO
        self.modeloFiltrado = self.modelo.filter_new()
        self.dniFiltro = None
        self.modeloFiltrado.set_visible_func(self.dni_filtro_func)

        # CREAMOS EL TREEVIEW Y LE ASIGNAMOS EL MODELO
        self.tvwUsuarios = Gtk.TreeView()
        self.tvwUsuarios.set_model(self.modeloFiltrado)

        # COLUMNA DNI
        self.celdaDni = Gtk.CellRendererText()
        # self.celdaTarea.set_property("editable",True)
        # self.celdaTarea.connect("edited", self.on_celdaTarea_edited,self.modelo)
        self.columna = Gtk.TreeViewColumn("Dni", self.celdaDni, text=0)
        self.tvwUsuarios.append_column(self.columna)

        # COLUMNA NOMBRE
        self.celdaNombre = Gtk.CellRendererText()
        # self.celdaTarea.set_property("editable",True)
        # self.celdaTarea.connect("edited", self.on_celdaTarea_edited,self.modelo)
        self.columna = Gtk.TreeViewColumn("Nombre", self.celdaNombre, text=1)
        self.tvwUsuarios.append_column(self.columna)

        # COLUMNA DIRECCION
        self.celdaDireccion = Gtk.CellRendererText()
        # self.celdaTarea.set_property("editable",True)
        # self.celdaTarea.connect("edited", self.on_celdaTarea_edited,self.modelo)
        self.columna = Gtk.TreeViewColumn("Direccion", self.celdaDireccion, text=2)
        self.tvwUsuarios.append_column(self.columna)

        # CREAMOS COMBOBOX
        self.cmbDni = Gtk.ComboBox.new_with_model(self.modelo)
        self.celda = Gtk.CellRendererText()
        self.cmbDni.pack_start(self.celda, False)
        self.cmbDni.add_attribute(self.celda, "text", 0)
        self.cmbDni.connect("changed", self.on_cmbDni_changed)
        caixaV.pack_start(self.cmbDni, False, False, 2)

        caixaV.pack_start(self.tvwUsuarios, True, True, 1)

        self.add(caixaV)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


    def dni_filtro_func(self,modelo,fila,data):
        if (self.dniFiltro is None or self.dniFiltro == "None"):
            return True
        else:
            return modelo [fila][0] == self.dniFiltro

    def on_cmbDni_changed(self, combo):
        fila = combo.get_active_iter()
        if fila is not None:
            modelo = combo.get_model()
            self.dniFiltro = modelo [fila][0]
            self.modeloFiltrado.refilter()


if __name__ == "__main__":
    Aplication()
    Gtk.main()

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from sqlite3 import dbapi2


class Aplication(Gtk.Window):

    def __init__(self):
        super().__init__(title="BD en TreeView")

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        self.modelo = Gtk.ListStore(str, str, int)
        self.modeloCombo = Gtk.ListStore(str, int, int)

        # CONEXIONES BASE DE DATOS
        try:
            bbdd = dbapi2.connect("perfisUsuarios.bd")
        except dbapi2.StandarError as e:
            print(e)
        else:
            print("Base de datos abierta")

        # CONSULTA USUARIOS Y PERFISUSUARIOS
        try:
            cursor = bbdd.cursor()
        except dbapi2.Error as e:
            print(e)
        else:
            print("cursor preparado")
        try:
            consulta = "SELECT nome,dni,idPerfil FROM usuarios INNER JOIN perfisUsuario WHERE usuarios.dni = perfisUsuario.dniUsuario"
            consulta2 = "SELECT descricion FROM perfis INNER JOIN perfisUsuario WHERE perfis.idPefil = perfisUsuario.idPerfil"
            cursor.execute(consulta)
            for rexistro in cursor.fetchall():
                self.modelo.append(rexistro)

        except dbapi2.DatabaseError as e:
            print("Error haciendo la consulta" + str(e))

        else:
            print("Consulta ejecutada")

        # PARA LA CONSULTA DEL PERFILUSUARIO
        try:
            cursor = bbdd.cursor()
        except dbapi2.Error as e:
            print(e)
        else:
            print("cursor preparado")
        try:
            consulta = "SELECT dniUsuario, idPerfil, permiso FROM perfisUsuario WHERE dniUsuario in (SELECT dni FROM usuarios)"
            cursor.execute(consulta)
            for rexistro in cursor.fetchall():
                self.modeloCombo.append(rexistro)

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

        # COLUMNA NOME
        self.celdaNome = Gtk.CellRendererText()
        # self.celdaTarea.set_property("editable",True)
        # self.celdaTarea.connect("edited", self.on_celdaTarea_edited,self.modelo)
        self.columna = Gtk.TreeViewColumn("Nome", self.celdaNome, text=0)
        self.tvwUsuarios.append_column(self.columna)

        # COLUMNA DNI
        self.celdadDni = Gtk.CellRendererText()
        # self.celdaTarea.set_property("editable",True)
        # self.celdaTarea.connect("edited", self.on_celdaTarea_edited,self.modelo)
        self.columna = Gtk.TreeViewColumn("Dni", self.celdadDni, text=1)
        self.tvwUsuarios.append_column(self.columna)

        # COLUMNA PERFIL DE USUARIO
        self.celdaPUsuario = Gtk.CellRendererText()
        # self.celdaTarea.set_property("editable",True)
        # self.celdaTarea.connect("edited", self.on_celdaTarea_edited,self.modelo)
        self.columna = Gtk.TreeViewColumn("Perfil de Usuario", self.celdaPUsuario, text=2)
        self.tvwUsuarios.append_column(self.columna)

        '''# COLUMNA PERFIL DE USUARIO
        self.celdaPUsuario = Gtk.CellRendererText()
        # self.celdaTarea.set_property("editable",True)
        # self.celdaTarea.connect("edited", self.on_celdaTarea_edited,self.modelo)
        self.columna = Gtk.TreeViewColumn("Descripcion", self.celdaPUsuario, text=3)
        self.tvwUsuarios.append_column(self.columna)'''

        # ESTO ES PARA QUE SALGAN LOS DATOS EN LA VENTANA
        caixaV.pack_start(self.tvwUsuarios, True, True, 0)

        # CREAMOS COMBOBOX
        # self.cmbPerfil = Gtk.ComboBox.new_with_model(self.modeloCombo)
        self.celda = Gtk.CellRendererCombo()
        self.celda.set_property("editable", True)
        self.celda.set_property("model", self.modeloCombo)
        self.celda.set_property("text-column", 0)
        self.celda.set_property("has-entry", False)
        columna3 = Gtk.TreeViewColumn("Perfil", self.celda, text=3)
        self.tvwUsuarios.append_column(columna3)
        # self.cmbPerfil.pack_start(self.celda, True)
        # self.cmbPerfil.add_attribute(self.celda, "text", 0)
        # self.cmbPerfil.connect("changed", self.on_cmbPUsuario_changed)
        # caixaV.pack_start(self.cmbPerfil, False, False, 2)

        self.add(caixaV)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def dni_filtro_func(self, modelo, fila, data):
        if (self.dniFiltro is None or self.dniFiltro == "None"):
            return True
        else:
            return modelo[fila][0] == self.dniFiltro

    def on_cmbPUsuario_changed(self, combo):
        fila = combo.get_active_iter()
        if fila is not None:
            modelo = combo.get_model()
            self.dniFiltro = modelo[fila][0]
            self.modeloFiltrado.refilter()


if __name__ == "__main__":
    Aplication()
    Gtk.main()

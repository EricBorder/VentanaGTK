import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from conexionBD import ConexionBD


class Aplication(Gtk.Window):

    def __init__(self):
        super().__init__(title="Exemplo treeview con cellrendererCombo")

        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        modelo = Gtk.ListStore(str, str, int, str)
        modeloP = Gtk.ListStore(str, int)

        trvPerfilesUsuarios = Gtk.TreeView(model=modelo)

        # COLUMNA 1
        celda = Gtk.CellRendererText()
        columna = Gtk.TreeViewColumn("DNI", celda, text=0)
        trvPerfilesUsuarios.append_column(columna)

        # COLUMNA 2
        celda2 = Gtk.CellRendererText()
        columna2 = Gtk.TreeViewColumn("NOME", celda2, text=1)
        trvPerfilesUsuarios.append_column(columna2)

        # COLUMNA 3
        # celda3 = Gtk.CellRendererText()
        # columna3 = Gtk.TreeViewColumn("Perfil", celda3, text=2)
        # trvPerfilesUsuarios.append_column(columna3)

        bd = ConexionBD("perfisUsuarios.bd")
        connectBD = bd.conectaBD()
        cursorBD = bd.creaCursor()
        sqlUsuarios = "Select dni, nome from usuarios"
        sqlPerfisUsuario = "SELECT idPerfil FROM perfisUsuario WHERE dniUsuario=?"
        sqlPerfil = "SELECT descricion FROM idPefil=?"
        sqlTodosPerfis = "SELECT descricion, idPefil FROM perfis"

        lUsuarios = bd.consultaSenParametros(sqlUsuarios)
        # usuariosPerfil = list()
        for dniUsuario in lUsuarios:
            idPerfil = bd.consultaConParametros(sqlPerfisUsuario, dniUsuario[0])
            descricionPerfil = bd.consultaConParametros(sqlPerfil, idPerfil[0][0])
            elemento = list(dniUsuario)
            # elemento = list(descricionPerfil)
            elemento.append(idPerfil[0][0])
            elemento.append(descricionPerfil[0][0])
            # print(elemento)
            # usuariosPerfil.append(elemento)
            modelo.append(elemento)
        # print(lUsuarios)
        lTodosPerfis = bd.consultaSenParametros(sqlTodosPerfis)
        for perfil in lTodosPerfis:
            modeloP.append(perfil)

        # COLUMNA 3
        celda3 = Gtk.CellRendererCombo()
        celda3.set_property("editable", True)
        celda3.set_property("model", modeloP)
        celda3.set_property("text-colum", 0)
        celda3.set_property("has-entry", False)
        columna3 = Gtk.TreeViewColumn("Perfil", celda3, text=3)
        trvPerfilesUsuarios.append_column(columna3)

        caixaV.pack_start(trvPerfilesUsuarios, True, True, 0)

        self.add(caixaV)
        self.connect("destroy", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    Aplication()

    Gtk.main()

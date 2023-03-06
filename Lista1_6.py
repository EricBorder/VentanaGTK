import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplication(Gtk.Window):
    def __init__(self):
        super().__init__()
        caixaV = Gtk.Box (orientation=Gtk.Orientation.VERTICAL, spacing=4)
        self.modelo = Gtk.ListStore(str,bool)
        self.tvwTarefas = Gtk.TreeView()
        self.tvwTarefas.set_model(self.modelo)

        self.celdaTarea = Gtk.CellRendererText()
        self.celdaTarea.set_property("editable",True)
        self.celdaTarea.connect("edited", self.on_celdaTarea_edited,self.modelo)
        self.columna = Gtk.TreeViewColumn("Tarefa",self.celdaTarea,text=0)
        self.tvwTarefas.append_column(self.columna)

        self.celdaToggle = Gtk.CellRendererToggle()
        self.columnaToggle = Gtk.TreeViewColumn("Feito", self.celdaToggle, active=1)
        self.tvwTarefas.append_column(self.columnaToggle)
        self.celdaToggle.connect("toggled",self.on_ch2_toogled,self.modelo)

        self.modelo.append(["Debian", False])
        self.modelo.append(["OpenSuse", True])
        self.modelo.append(["Fedora", False])

        self.btnBorrar = Gtk.Button(label="Borrar")
        self.btnFeito = Gtk.Button(label="Feito")

        caixaV.add(self.tvwTarefas)



        self.celdaToggle.connect("toggled", self.on_ch2_toogled)

        sinais = {
            "gtk_main_quit": self.gtk_main_quit,
            "on_btnBorrar_clicked": self.on_btnBorrar_clicked,
            "on_btnFeito_clicked": self.on_btnFeito_clicked,
            "engadir_tarefa": self.engadir_tarefa,
            "on_ch2_toogled": self.on_ch2_toogled
        }

        self.add(caixaV)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

    def gtk_main_quit(*args):
        Gtk.main_quit()

    def on_btnBorrar_clicked(self, boton):
        seleccion = self.lblSaludo.get_selection()
        modelo, fila = seleccion.get_selected()
        if fila is not None:
            modelo.remove(fila)

    def on_btnFeito_clicked(self, boton):
        seleccion = self.lblSaludo.get_selection()
        modelo, fila = seleccion.get_selected()
        if fila is not None:
            modelo.set(fila, (1,), (False,))

    def engadir_tarefa(self, control):
        modelo = self.lblSaludo.get_model()
        print(self.txtnome.get_text())
        pos = modelo.append()
        modelo.set(pos, (0, 1), (self.txtnome.get_text(), True))

    def on_ch2_toogled(self, celda, fila, modelo):
        # modelo[fila][0] = not modelo[fila][0]
        selected_path = Gtk.TreePath(fila)
        for row in self.lblSaludo:
            row[2] = row.path == selected_path

    def on_celdaTarea_edited(self,celda,fila,texto,modelo):
        modelo[fila][0] = texto


if __name__ == "__main__":
    Aplication()
    Gtk.main()

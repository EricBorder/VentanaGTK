import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplication:
    def __init__(self):
        super().__init__()

        builder = Gtk.Builder()
        builder.add_from_file("Lista1_5(1).glade")

        self.buffer = Gtk.TextBuffer()

        ventanaPrincipal = builder.get_object("VentanaPrincipal")
        self.tmodelo = builder.get_object("liststore")
        self.txtnome = builder.get_object("escribir")
        self.lblSaludo = builder.get_object("TV")
        self.columnaTarefa = builder.get_object("1")
        self.columnaFeito = builder.get_object("2")
        self.renderer1 = builder.get_object("ch1")
        self.renderer2 = builder.get_object("ch2")
        #self.renderer2.set_property("active",True)
        self.btnBorrar = builder.get_object("btnBorrar")
        self.btnFeito = builder.get_object("btnFeito")
        self.btnAñadir = builder.get_object("btnAñadir")

        sinais = {"on_Nome_activate": self.on_Nome_activate,
                  "gtk_main_quit": self.gtk_main_quit,
                  "on_engadir_clicked": self.on_engadir_clicked,
                  "engadir_tarefa": self.engadir_tarefa,
                  "on_btnFeito_clicked": self.on_btnFeito_clicked,
                  "on_btnBorrar_clicked": self.on_btnBorrar_clicked,
                  "on_ch2_toggled": self.on_ch2_toggled
                  }

        builder.connect_signals(sinais)

    # self.lblSaludo.set_buffer(self.buffer)

    def gtk_main_quit(*args):
        Gtk.main_quit()

    def on_Nome_activate(self):
        tarefa = self.txtnome.get_text()
        self.buffer.insert(tarefa, 2)

    def on_engadir_clicked(self, control):
        tarefa = self.txtnome.get_text()
        #self.buffer.insert_at_cursor(tarefa)

    def engadir_tarefa(self,control):
        modelo = self.lblSaludo.get_model()
        print(self.txtnome.get_text())
        pos = modelo.append((self.txtnome.get_text(), False))
        #modelo.set(pos, (0, 1), (self.txtnome.get_text(), False))
        print(modelo[pos][0])

    def on_btnFeito_clicked(self,boton):
        seleccion = self.lblSaludo.get_selection()
        modelo, fila = seleccion.get_selected()
        if fila is not None:
            modelo.set(fila,(1,),(True,))

    def on_btnBorrar_clicked(self,boton):
        seleccion = self.lblSaludo.get_selection()
        modelo, fila = seleccion.get_selected()
        if fila is not None:
            modelo.remove(fila)

    def on_ch2_toggled(self,celda,fila):
        self.tmodelo[fila][1] = not self.tmodelo [fila][1]


if __name__ == "__main__":
    Aplication()
    Gtk.main()

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplication:
    def __init__(self):
        super().__init__()

        builder = Gtk.Builder()
        builder.add_from_file("Lista1.glade")

        self.buffer = Gtk.TextBuffer()

        ventanaPrincipal = builder.get_object("VentanaPrincipal")
        self.txtnome = builder.get_object("escribir")
        self.lblSaludo = builder.get_object("lblLista")
        self.btnBorrar = builder.get_object("btnBorrar")
        self.btnFeito = builder.get_object("btnFeito")
        self.btnAñadir = builder.get_object("btnAñadir")

        sinais = {"on_Nome_activate": self.on_Nome_activate,
                  "gtk_main_quit": self.gtk_main_quit,
                  "on_engadir_clicked": self.on_engadir_clicked
                  }

        builder.connect_signals(sinais)
        self.lblSaludo.set_buffer(self.buffer)

    def gtk_main_quit(*args):
        Gtk.main_quit()

    def on_Nome_activate(self):
        tarefa = self.txtnome.get_text()
        self.buffer.insert(tarefa,2)

    def on_engadir_clicked(self, control):
        tarefa = self.txtnome.get_text()
        self.buffer.insert_at_cursor(tarefa)


if __name__ == "__main__":
    Aplication()
    Gtk.main()

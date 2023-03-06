import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Aplicacion:
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("saludo.glade")

        ventanaPrincipal = builder.get_object("VentanaPrincipal")
        self.txtNombre = builder.get_object("txtNombre")
        self.lblSaludo = builder.get_object("lblSaludo")

        # ventanaPrincipal.show_all()
        # ventanaPrincipal.connect("delete-event",Gtk.main_quit)

        sinais = {"gtk_main_quit": Gtk.main_quit,
                  "on_txtNombre_activate": self.on_txtNombre_clicked,
                  "on_botonSaludar_clicked": self.on_txtNombre_clicked
                  }

        builder.connect_signals(sinais)

    def on_txtNombre_clicked(self, control):
        self.lblSaludo.set_text("Hola " + self.txtNombre.get_text())


if __name__ == "__main__":
    Aplicacion()
    Gtk.main()

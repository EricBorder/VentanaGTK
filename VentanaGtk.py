import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Ventana(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Ventana GTK")
        caixaV = Gtk.Box(orientation= Gtk.Orientation.VERTICAL, spacing=10)
        caixaV.add(Gtk.Button(label="Boton 1"))
        caixaV.add(Gtk.Button(label="Boton 2"))
        #caixaV.add(Gtk.Button(label="Boton 3"))


        caixaH = Gtk.Box(orientation= Gtk.Orientation.HORIZONTAL, spacing=10)
        caixaH.add(Gtk.Button(label="Boton 4"))
        caixaH.add(Gtk.Button(label="Boton 5"))
        caixaH.add(Gtk.Button(label="Boton 6"))
        caixaV.add(caixaH)

        self.add(caixaV)

        self.connect("delete-event", Gtk.main_quit)
        self.show_all()


if __name__ == "__main__":
    Ventana()
    Gtk.main()
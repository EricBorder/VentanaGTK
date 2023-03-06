import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Ventana(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_title("Calculadora")

        # enseñar resultados
        self.entry = Gtk.Entry()

        # layout

        grid = Gtk.Grid()
        grid.set_column_homogeneous(True)

        # botones
        but9 = Gtk.Button(label="9")
        but8 = Gtk.Button(label="8")
        but7 = Gtk.Button(label="7")
        but6 = Gtk.Button(label="6")
        but5 = Gtk.Button(label="5")
        but4 = Gtk.Button(label="4")
        but3 = Gtk.Button(label="3")
        but2 = Gtk.Button(label="2")
        but1 = Gtk.Button(label="1")
        but0 = Gtk.Button(label="0")
        butsum = Gtk.Button(label="+")
        butrest = Gtk.Button(label="-")
        butmulti = Gtk.Button(label="*")
        butdiv = Gtk.Button(label="/")
        butigual = Gtk.Button(label="=")

        # posicion de los botones
        grid.attach(self.entry, 0, 0, 3, 1)
        grid.attach(butsum, 3, 0, 1, 1)
        grid.attach(butrest, 3, 1, 1, 1)
        grid.attach(butmulti, 3, 2, 1, 1)
        grid.attach(butdiv, 3, 3, 1, 1)
        grid.attach(butigual, 3, 4, 1, 1)
        grid.attach(but9, 2, 3, 1, 1)
        grid.attach(but8, 1, 3, 1, 1)
        grid.attach(but7, 0, 3, 1, 1)
        grid.attach(but6, 2, 2, 1, 1)
        grid.attach(but5, 1, 2, 1, 1)
        grid.attach(but4, 0, 2, 1, 1)
        grid.attach(but3, 2, 1, 1, 1)
        grid.attach(but2, 1, 1, 1, 1)
        grid.attach(but1, 0, 1, 1, 1)
        grid.attach(but0, 0, 4, 3, 1)

        self.connect ("delete_event", Gtk.main_quit)
        self.add(grid)
        self.show_all()


if __name__ == "__main__":
    Ventana()
    Gtk.main()

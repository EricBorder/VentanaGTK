
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk


class Exame(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exame 16-12-2021")
        self.set_border_width(10)
        caixaVprincipal = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.add(caixaVprincipal)
        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        caixaVprincipal.add(caixaH)
        caixaV = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        caixaH.add(caixaV)

        imaxe = Gtk.Image()
        imaxe.set_from_icon_name("media-optical", Gtk.IconSize.DIALOG)
        caixaV.pack_start(imaxe, False, False, 0)
        chkAnimado = Gtk.CheckButton(label="Animado")
        caixaV.pack_start(chkAnimado, False, False, 0)

        bDesplazamento = Gtk.ScrolledWindow()
        bDesplazamento.set_policy(Gtk.PolicyType.NEVER, Gtk.PositionType.LEFT)
        tvwTaboa = Gtk.TextView()
        tvwTaboa.set_size_request(420, 100)
        self.bufer = tvwTaboa.get_buffer()
        bDesplazamento.add(tvwTaboa)
        caixaH.pack_start(bDesplazamento, True, True, 0)

        grid = Gtk.Grid()
        caixaH.pack_start(grid, False, False, 0)
        btnReproducir = Gtk.Button(label="Engadir a pista a reproducir")
        grid.attach(btnReproducir, 0, 0, 3, 1)
        btnPausa = Gtk.Button(label="Subir na lista")
        grid.attach(btnPausa, 0, 1, 3, 1)
        btnParar = Gtk.Button(label="Baixar na lista")
        grid.attach(btnParar, 0, 2, 3, 1)
        btnSaltar = Gtk.Button(label="Saltar")
        grid.attach(btnSaltar, 0, 3, 1, 1)
        cmbPosicionSaltar = Gtk.ComboBoxText()
        cmbPosicionSaltar.set_size_request(140, 10)
        grid.attach(cmbPosicionSaltar, 1, 3, 2, 1)
        btnAbrirFicheiro = Gtk.Button(label="Abrir ficheiro...")
        grid.attach(btnAbrirFicheiro, 0, 4, 3, 1)
        btnFalarFicheiro = Gtk.Button(label="Reproducir ficheiro...")
        grid.attach(btnFalarFicheiro, 0, 5, 3, 1)
        btnGardarComo = Gtk.Button(label="Gardar como...")
        grid.attach(btnGardarComo, 0, 6, 3, 1)
        btnEliminar = Gtk.Button(label="Eliminar pista")
        grid.attach(btnEliminar, 0, 7, 3, 1)

        caixaH = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        caixaVprincipal.add(caixaH)

        builder = Gtk.Builder()
        builder.add_from_file("cadroSonGlade.glade")
        grid2 = builder.get_object("grid2")
        caixaH.add(grid2)

        cmbFormato = builder.get_object("cmbFormato")
        cmbFormato.append_text("wma")
        cmbFormato.append_text("ogg")
        cmbFormato.connect("changed", self.on_cmbFormato_changed)
        '''
        contedorH2 = Gtk.Frame()
        caixaH.pack_start(contedorH2, True, True, 0)
        contedorH2.set_label("Opcións de reproducción")
        grid3 = Gtk.Grid()
        contedorH2.add(grid3)
        chkAsincrono = Gtk.CheckButton(label="Asíncrono")
        grid3.add(chkAsincrono)
        chkENomeFicheiro = Gtk.CheckButton(label="É nome de ficheiro")
        grid3.attach(chkENomeFicheiro, 0, 1, 1, 1)
        chkXmlPersistente = Gtk.CheckButton(label="XML persistente")
        grid3.attach(chkXmlPersistente, 0, 2, 1, 1)
        chkFiltrarAntesReproducir = Gtk.CheckButton(label="Filtrar antes de reproducir")
        grid3.attach(chkFiltrarAntesReproducir, 0, 3, 1, 1)
        chkExml = Gtk.CheckButton(label="É XML")
        grid3.attach(chkExml, 0, 4, 1, 1)
        chkReproduccionNpl = Gtk.CheckButton(label="Reproducción NPL")
        grid3.attach(chkReproduccionNpl, 0, 5, 1, 1)
        '''
        chkAsincrono = builder.get_object("chkAsincrono")

        chkAsincrono.connect("toggled", self.on_chkButton_toggled)

        chkENomeFicheiro = builder.get_object("chkENomeFicheiro")

        chkENomeFicheiro.connect("toggled", self.on_chkButton_toggled)

        chkXmlPersistente = builder.get_object("chkXmlPersistente")

        chkXmlPersistente.connect("toggled", self.on_chkButton_toggled)

        chkReproduccionNpl = builder.get_object("chkReproduccionNpl")

        chkReproduccionNpl.connect("toggled", self.on_chkButton_toggled)

        chkFiltrarAntesReproducir = builder.get_object("chkFiltrarAntesReproducir")

        chkFiltrarAntesReproducir.connect("toggled", self.on_chkButton_toggled)

        chkExml=builder.get_object("chkExml")

        chkExml.connect("toggled", self.on_chkButton_toggled)

        self.connect("destroy", Gtk.main_quit)
        self.show_all()

    def on_cmbFormato_changed(self, control):
        print(control.get_active_text())

    def on_chkButton_toggled(self, control):
        punteiro = self.bufer.get_end_iter()
        self.bufer.insert(punteiro, "Modo de reproducción " + control.get_label() + " seleccionado \n")


if __name__ == "__main__":
    Exame()
    Gtk.main()
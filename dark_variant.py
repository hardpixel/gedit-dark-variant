from gi.repository import GObject, Gedit, Gtk

class DarkVariantAppActivatable(GObject.Object, Gedit.AppActivatable):

	app = GObject.property(type=Gedit.App)

	def __init__(self):
		GObject.Object.__init__(self)

		self.settings = Gtk.Settings.get_default()

	def do_activate(self):
		self.settings.set_property('gtk-application-prefer-dark-theme', True)

	def do_deactivate(self):
		self.settings.set_property('gtk-application-prefer-dark-theme', False)

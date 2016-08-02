import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Gedit', '3.0')

from gi.repository import GObject, Gtk, Gedit

class DarkVariantAppActivatable(GObject.Object, Gedit.AppActivatable):

	app = GObject.property(type=Gedit.App)

	def __init__(self):
		GObject.Object.__init__(self)

		self._settings = Gtk.Settings.get_default()

	def do_activate(self):
		self._settings.set_property('gtk-application-prefer-dark-theme', True)

	def do_deactivate(self):
		self._settings.set_property('gtk-application-prefer-dark-theme', False)

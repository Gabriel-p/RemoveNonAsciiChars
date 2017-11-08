import sublime
import sublime_plugin
import unicodedata


class RemoveNonAsciiCharsFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        entire_view = sublime.Region(0, self.view.size())
        ascii_only = unicodedata.normalize(
            'NFKD', self.view.substr(entire_view)).encode(
            'ascii', 'ignore').decode('utf-8')
        self.view.replace(edit, entire_view, ascii_only)


class RemoveNonAsciiCharsSelecCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel_view = self.view.sel()
        for region in sel_view:
            if not region.empty():
                # Get the selected text
                s = self.view.substr(region)
                ascii_only = unicodedata.normalize(
                    'NFKD', s).encode('ascii', 'ignore').decode('utf-8')
                self.view.replace(edit, region, ascii_only)

#!/usr/bin/python
import sublime
import sublime_plugin

class AutoSaveCommand(sublime_plugin.EventListener):
    def on_modified(self, view):
        # New unsaved files musn't be saved automatically
        if not view.file_name():
            return

        # Do things only if the setting is enabled
        if not view.settings().get("hayaku_autosave_enabled"):
            return

        # Autosave only in specific scopes
        # TODO: move this to settings
        if not view.score_selector(view.sel()[0].begin(),'source.css, source.stylus, source.sass, source.scss, text.html'):
            return

        view.run_command('save')

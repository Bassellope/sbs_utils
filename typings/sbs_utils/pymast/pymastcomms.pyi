from sbs_utils.consoledispatcher import ConsoleDispatcher
from sbs_utils.engineobject import EngineObject
from sbs_utils.pymast.pollresults import PollResults
class PyMastComms(object):
    """class PyMastComms"""
    def __init__ (self, task, player_id, npc_id_or_filter, buttons, continuous) -> None:
        """Initialize self.  See help(type(self)) for accurate signature."""
    def get_other (self):
        ...
    def get_player (self):
        ...
    def have_other_tell_player (self, text, color=None, face=None, comms_id=None):
        ...
    def have_player_tell_other (self, text, color=None, face=None, comms_id=None):
        ...
    def message (self, sim, message, player_id, event):
        ...
    def run (self):
        ...
    def selected (self, sim, _, event):
        ...
    def stop (self):
        ...
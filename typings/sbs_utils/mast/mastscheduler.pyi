from sbs_utils.agent import Agent
from sbs_utils.mast.mast import Assign
from sbs_utils.mast.mast import Await
from sbs_utils.mast.mast import AwaitInlineLabel
from sbs_utils.mast.mast import Button
from sbs_utils.mast.mast import Comment
from sbs_utils.mast.mast import DecoratorLabel
from sbs_utils.mast.mast import DescribableNode
from sbs_utils.mast.mast import ExpParseData
from sbs_utils.mast.mast import FuncCommand
from sbs_utils.mast.mast import IfStatements
from sbs_utils.mast.mast import Import
from sbs_utils.mast.mast import InlineData
from sbs_utils.mast.mast import InlineLabel
from sbs_utils.mast.mast import Jump
from sbs_utils.mast.mast import Label
from sbs_utils.mast.mast import LoopBreak
from sbs_utils.mast.mast import LoopEnd
from sbs_utils.mast.mast import LoopStart
from sbs_utils.mast.mast import Mast
from sbs_utils.mast.mast import MastDataObject
from sbs_utils.mast.mast import MastNode
from sbs_utils.mast.mast import MatchStatements
from sbs_utils.mast.mast import OnChange
from sbs_utils.mast.mast import ParseData
from sbs_utils.mast.mast import PyCode
from sbs_utils.mast.mast import RouteDecoratorLabel
from sbs_utils.mast.mast import Rule
from sbs_utils.mast.mast import Scope
from sbs_utils.mast.mast import WithEnd
from sbs_utils.mast.mast import WithStart
from sbs_utils.mast.mast import Yield
from sbs_utils.procedural.gui import ButtonPromise
from enum import Enum
from enum import IntEnum
from sbs_utils.helpers import FrameContext
from sbs_utils.mast.pollresults import PollResults
from sbs_utils.futures import Promise
from sbs_utils.futures import Trigger
from sbs_utils.futures import Waiter
from zipfile import ZipFile
from functools import partial
def DEBUG (msg):
    ...
def STRING_REGEX_NAMED (name):
    ...
def STRING_REGEX_NAMED_2 (name):
    ...
def STRING_REGEX_NAMED_3 (name):
    ...
def find_exp_end (s, expect_block):
    ...
def first_newline_index (s):
    ...
def first_non_newline_index (s):
    ...
def first_non_space_index (s):
    ...
def first_non_whitespace_index (s):
    ...
def format_exception (message, source):
    ...
def get_fall_through (inner):
    ...
def get_task_id ():
    ...
def getmembers (object, predicate=None):
    ...
def isfunction (object):
    ...
def mast_print (*args, **kwargs):
    ...
def signature (obj, *, follow_wrapped=True, globals=None, locals=None, eval_str=False):
    ...
class AssignRuntimeNode(MastRuntimeNode):
    """class AssignRuntimeNode"""
    def __init__ (self) -> 'None':
        """Initialize self.  See help(type(self)) for accurate signature."""
    def poll (self, mast, task: 'MastAsyncTask', node: 'Assign'):
        ...
class AwaitInlineLabelRuntimeNode(MastRuntimeNode):
    """class AwaitInlineLabelRuntimeNode"""
    def enter (self, mast: 'Mast', task: 'MastAsyncTask', node: 'AwaitInlineLabel'):
        ...
    def poll (self, mast: 'Mast', task: 'MastAsyncTask', node: 'AwaitInlineLabel'):
        ...
class AwaitRuntimeNode(MastRuntimeNode):
    """class AwaitRuntimeNode"""
    def enter (self, mast: 'Mast', task: 'MastAsyncTask', node: 'Await'):
        ...
    def poll (self, mast: 'Mast', task: 'MastAsyncTask', node: 'Await'):
        ...
class ButtonRuntimeNode(MastRuntimeNode):
    """class ButtonRuntimeNode"""
    def enter (self, mast: 'Mast', task: 'MastAsyncTask', node: 'Button'):
        ...
    def poll (self, mast: 'Mast', task: 'MastAsyncTask', node: 'Button'):
        ...
class ChangeRuntimeNode(MastRuntimeNode):
    """class ChangeRuntimeNode"""
    def enter (self, mast: 'Mast', task: 'MastAsyncTask', node: 'Change'):
        ...
    def poll (self, mast: 'Mast', task: 'MastAsyncTask', node: 'Change'):
        ...
    def test (self):
        ...
class FuncCommandRuntimeNode(MastRuntimeNode):
    """class FuncCommandRuntimeNode"""
    def enter (self, mast, task: 'MastAsyncTask', node: 'FuncCommand'):
        ...
    def poll (self, mast, task: 'MastAsyncTask', node: 'FuncCommand'):
        ...
class IfStatementsRuntimeNode(MastRuntimeNode):
    """class IfStatementsRuntimeNode"""
    def first_true (self, task: 'MastAsyncTask', node: 'IfStatements'):
        ...
    def poll (self, mast, task, node: 'IfStatements'):
        ...
class InlineLabelRuntimeNode(MastRuntimeNode):
    """class InlineLabelRuntimeNode"""
class JumpRuntimeNode(MastRuntimeNode):
    """class JumpRuntimeNode"""
    def poll (self, mast: 'Mast', task: 'MastAsyncTask', node: 'Jump'):
        ...
class LoopBreakRuntimeNode(MastRuntimeNode):
    """class LoopBreakRuntimeNode"""
    def enter (self, mast, task: 'MastAsyncTask', node: 'LoopBreak'):
        ...
    def poll (self, mast, task, node: 'LoopBreak'):
        ...
class LoopEndRuntimeNode(MastRuntimeNode):
    """class LoopEndRuntimeNode"""
    def poll (self, mast, task, node: 'LoopEnd'):
        ...
class LoopStartRuntimeNode(MastRuntimeNode):
    """class LoopStartRuntimeNode"""
    def enter (self, mast, task: 'MastAsyncTask', node: 'LoopStart'):
        ...
    def poll (self, mast, task, node: 'LoopStart'):
        ...
class MastAsyncTask(Agent, Promise):
    """class MastAsyncTask"""
    def __init__ (self, main: "'MastScheduler'", inputs=None, name=None):
        """Initialize self.  See help(type(self)) for accurate signature."""
    def _add (id, obj):
        ...
    def _remove (id):
        ...
    @property
    def active_label (self):
        ...
    def add_dependency (id, task):
        ...
    def clear ():
        ...
    def compile_and_format_string (self, value):
        ...
    def emit_signal (self, name, sender_task, label_info, data):
        ...
    def end (self):
        ...
    def eval_code (self, code):
        ...
    def exec_code (self, code, vars, gbls):
        ...
    def format_string (self, message):
        ...
    def get (id):
        ...
    def get_as (id, as_cls):
        ...
    def get_objects_from_set (the_set):
        ...
    def get_role_object (link_name):
        ...
    def get_role_objects (role):
        ...
    def get_role_set (role):
        ...
    def get_runtime_error_info (self, rte):
        ...
    def get_scoped_value (self, key, defa, scope):
        ...
    def get_shared_variable (self, key, default=None):
        ...
    def get_symbols (self):
        ...
    def get_value (self, key, defa=None):
        ...
    def get_variable (self, key, default=None):
        ...
    def has_inventory_list (collection_name):
        ...
    def has_inventory_set (collection_name):
        ...
    def has_links_list (collection_name):
        ...
    def has_links_set (collection_name):
        ...
    @property
    def is_observable (self):
        ...
    def jump (self, label='main', activate_cmd=0):
        ...
    def poll (self):
        ...
    def pop_label (self, inc_loc=True, true_pop=False):
        ...
    def push_inline_block (self, label, activate_cmd=0, data=None):
        ...
    def push_label (self, label, activate_cmd=0, data=None):
        ...
    def queue_on_change (self, runtime_node):
        ...
    def remove_all_sub_tasks (self):
        ...
    def remove_sub_task (self, t):
        ...
    def resolve_id (other: 'Agent | CloseData | int'):
        ...
    def resolve_py_object (other: 'Agent | CloseData | int'):
        ...
    def run_on_change (self):
        ...
    def runtime_error (self, msg):
        ...
    def set_shared_variable (self, key, value):
        ...
    def set_value (self, key, value, scope):
        ...
    def set_value_keep_scope (self, key, value):
        ...
    def set_variable (self, key, value):
        ...
    def start_sub_task (self, label='main', inputs=None, task_name=None, defer=False) -> 'MastAsyncTask':
        ...
    def start_task (self, label='main', inputs=None, task_name=None, defer=False) -> 'MastAsyncTask':
        ...
    def stop_for_dependency (id):
        ...
    def swap_on_change (self):
        ...
    def tick (self):
        ...
    def tick_in_context (self):
        ...
    @property
    def tick_result (self):
        ...
    def tick_subtasks (self):
        ...
class MastRuntimeNode(object):
    """class MastRuntimeNode"""
    def enter (self, mast, scheduler, node):
        ...
    def leave (self, mast, scheduler, node):
        ...
    def poll (self, mast, scheduler, node):
        ...
class MastScheduler(Agent):
    """class MastScheduler"""
    def __init__ (self, mast: 'Mast', overrides=None):
        """Initialize self.  See help(type(self)) for accurate signature."""
    def _add (id, obj):
        ...
    def _remove (id):
        ...
    def _start_task (self, label='main', inputs=None, task_name=None) -> 'MastAsyncTask':
        ...
    def cancel_task (self, name):
        ...
    def clear ():
        ...
    def get (id):
        ...
    def get_as (id, as_cls):
        ...
    def get_inventory_value (self, collection_name, default=None):
        ...
    def get_objects_from_set (the_set):
        ...
    def get_role_object (link_name):
        ...
    def get_role_objects (role):
        ...
    def get_role_set (role):
        ...
    def get_seconds (self, clock):
        """Gets time for a given clock default is just system """
    def get_symbols (self):
        ...
    def get_value (self, key, defa=None):
        """MastStoryScheduler completely overrided this so changes here should go there"""
    def get_variable (self, key, defa=None):
        ...
    def has_inventory_list (collection_name):
        ...
    def has_inventory_set (collection_name):
        ...
    def has_links_list (collection_name):
        ...
    def has_links_set (collection_name):
        ...
    def is_running (self):
        ...
    def on_start_task (self, t):
        ...
    def resolve_id (other: 'Agent | CloseData | int'):
        ...
    def resolve_py_object (other: 'Agent | CloseData | int'):
        ...
    def runtime_error (self, message):
        ...
    def set_inventory_value (self, collection_name, value):
        ...
    def set_value (self, key, value, scope):
        ...
    def set_variable (self, key):
        ...
    def start_task (self, label='main', inputs=None, task_name=None, defer=False) -> 'MastAsyncTask':
        ...
    def tick (self):
        ...
class MastTicker(object):
    """class MastTicker"""
    def __init__ (self, task, main):
        """Initialize self.  See help(type(self)) for accurate signature."""
    def call_leave (self):
        ...
    def do_jump (self, label='main', activate_cmd=0):
        ...
    def do_resume (self, label, activate_cmd, runtime_node):
        ...
    def end (self):
        ...
    def get_runtime_error_info (self, rte):
        ...
    def jump (self, label='main', activate_cmd=0):
        ...
    def next (self):
        ...
    def pop_label (self, inc_loc=True, true_pop=False):
        ...
    def push_inline_block (self, label, activate_cmd=0, data=None):
        ...
    def push_label (self, label, activate_cmd=0, data=None):
        ...
    def runtime_error (self, rte):
        ...
    def tick (self):
        ...
class MatchStatementsRuntimeNode(MastRuntimeNode):
    """class MatchStatementsRuntimeNode"""
    def first_true (self, task: 'MastAsyncTask', node: 'MatchStatements'):
        ...
    def poll (self, mast, task, node: 'MatchStatements'):
        ...
class OnChangeRuntimeNode(MastRuntimeNode):
    """class OnChangeRuntimeNode"""
    def dequeue (self):
        ...
    def enter (self, mast: 'Mast', task: 'MastAsyncTask', node: 'OnChange'):
        ...
    def poll (self, mast: 'Mast', task: 'MastAsyncTask', node: 'OnChange'):
        ...
    def run (self):
        ...
    def test (self):
        ...
class PushData(object):
    """class PushData"""
    def __init__ (self, label, active_cmd, data=None, resume_node=None):
        """Initialize self.  See help(type(self)) for accurate signature."""
class PyCodeRuntimeNode(MastRuntimeNode):
    """class PyCodeRuntimeNode"""
    def poll (self, mast, task: 'MastAsyncTask', node: 'PyCode'):
        ...
class PyTicker(object):
    """class PyTicker"""
    def __init__ (self, task) -> 'None':
        """Initialize self.  See help(type(self)) for accurate signature."""
    def do_jump (self):
        ...
    def end (self):
        ...
    def get_gen (self, label):
        ...
    def get_runtime_error_info (self, rte):
        ...
    def jump (self, label):
        ...
    def pop (self):
        ...
    def push (self, label):
        ...
    def push_inline_block (self, label, _loc=0, data=None):
        ...
    def quick_push (self, func):
        ...
    def runtime_error (self, rte):
        ...
    def tick (self):
        ...
class WithEndRuntimeNode(MastRuntimeNode):
    """class WithEndRuntimeNode"""
    def poll (self, mast, task, node: 'WithEnd'):
        ...
class WithStartRuntimeNode(MastRuntimeNode):
    """class WithStartRuntimeNode"""
    def poll (self, mast, task, node: 'WithStart'):
        ...
class YieldRuntimeNode(MastRuntimeNode):
    """class YieldRuntimeNode"""
    def poll (self, mast, task, node: 'Yield'):
        ...

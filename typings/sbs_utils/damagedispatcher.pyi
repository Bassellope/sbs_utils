class CollisionDispatcher(object):
    """class CollisionDispatcher"""
    def add_any (cb: callable):
        ...
    def add_any_internal (cb: callable):
        ...
    def add_internal (id: int, cb: callable):
        ...
    def add_source (id: int, cb: callable):
        ...
    def add_target (id: int, cb: callable):
        ...
    def dispatch_collision (collision_event):
        ...
    def dispatch_internal (collision_event):
        ...
    def remove_any (cb: callable):
        ...
    def remove_any_internal (cb: callable):
        ...
    def remove_internal (id: int):
        ...
    def remove_source (id: int):
        ...
    def remove_target (id: int):
        ...
class DamageDispatcher(object):
    """class DamageDispatcher"""
    def add_any (cb: callable):
        ...
    def add_any_heat (cb: callable):
        ...
    def add_any_internal (cb: callable):
        ...
    def add_heat (id: int, cb: callable):
        ...
    def add_internal (id: int, cb: callable):
        ...
    def add_source (id: int, cb: callable):
        ...
    def add_target (id: int, cb: callable):
        ...
    def dispatch_damage (damage_event):
        ...
    def dispatch_heat (damage_event):
        ...
    def dispatch_internal (damage_event):
        ...
    def remove_any (cb: callable):
        ...
    def remove_any_heat (cb: callable):
        ...
    def remove_any_internal (cb: callable):
        ...
    def remove_heat (id: int):
        ...
    def remove_internal (id: int):
        ...
    def remove_source (id: int):
        ...
    def remove_target (id: int):
        ...
from enum import Enum
from Controllers.EventController import EventController
from Controllers.game_events import OnKillSelfEvent, OnInventoryDisplay, OnPrayEvent

class PlayerStandardActions(Enum):
    KILL_SELF = "Kill Self"
    MOVE_FORWARD = "Move Forward"
    MOVE_BACKWARD = "Move Backward"
    MOVE_LEFT = "Move Left"
    MOVE_RIGHT = "Move Right"
    JUMP = "Jump"
    CROUCH = "Crouch"
    PRAY = "Pray"
    BLASPHEME = "Blaspheme"
    INVESTIGATE = "Investigate"
    ACTIVATE_SWITCH = "Activate Switch"
    PICKUP_BOOK = "Pickup Book"
    INVENTORY = "Inventory"

class UniversalPlayerActions():
    actions = {
        "k": PlayerStandardActions.KILL_SELF.value,
        "p": PlayerStandardActions.PRAY.value,
        "i": PlayerStandardActions.INVENTORY.value
    }

    @classmethod
    def take_action(cls, action: str):
        evt = None
        if cls.actions[action] == PlayerStandardActions.KILL_SELF.value:
            evt = OnKillSelfEvent()
        elif cls.actions[action] == PlayerStandardActions.INVENTORY.value:
            evt = OnInventoryDisplay()
        elif cls.actions[action] == PlayerStandardActions.PRAY.value:
            evt = OnPrayEvent()
            
        EventController.broadcast_event(event_object=evt)
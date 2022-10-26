from abc import abstractmethod
from enum import Enum
from Controllers.EventController import EventController
from Controllers.game_events import OnSfxPlayEvent, OnSfxStopEvent, OnItemDrop
from Controllers.Player_Controller.item_slots import ItemSlots
from Controllers.game_events import OnItemEquip

class BaseItemRegistry():
    @classmethod
    @abstractmethod
    def get_registered_items(cls):
        raise NotImplementedError("")

class UniversalAction(Enum):
    DROP = "d"
    EQUIP = "e"
    CANCEL = "c"

class GameItem():
    def __init__(self) -> None:
        self.name = "unknown item"
        self.inv_socket_weight = 0
        self.description = ""
        self.pickup_sfx_name = None
        self.universal_actions = {
            UniversalAction.DROP.value: "Drop",
            UniversalAction.EQUIP.value: "Equip",
            UniversalAction.CANCEL.value: "Cancel"
        }
        self.actions = {
            **self.universal_actions
        }

    def perform_universal_action(self, player_action, item):
        if player_action == self.universal_actions[UniversalAction.CANCEL.value]:
            pass
        elif player_action == self.universal_actions[UniversalAction.DROP.value]:
            evt = OnItemDrop()
            evt.item = item
            EventController.broadcast_event(evt)
        elif player_action == self.universal_actions[UniversalAction.EQUIP.value]:
            # PlayerController.equip_item(item=item, slot=item_slots.RIGHT_HAND)
            equip_evt = OnItemEquip()
            equip_evt.item = item
            equip_evt.slot = ItemSlots.RIGHT_HAND
            EventController.broadcast_event(equip_evt)

        else:
            raise ValueError("That item action is not yet supported!")

    def play_on_use_sfx(self, sfx_name, sfx_loops: int = 0):
        evt = OnSfxPlayEvent()
        evt.sfx_name = sfx_name
        evt.sfx_loops = sfx_loops
        EventController.broadcast_event(evt)

    def stop_sfx(self, sfx_name):
        evt = OnSfxStopEvent()
        evt.sfx_name = sfx_name
        EventController.broadcast_event(evt)
    
    def use_item(self, **kwargs):
        print("This item has no use to you right now.")


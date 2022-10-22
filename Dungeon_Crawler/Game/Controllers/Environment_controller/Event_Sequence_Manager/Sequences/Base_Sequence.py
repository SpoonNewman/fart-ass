from abc import abstractmethod
from typing import Dict
from Controllers.EventController import EventController

from Controllers.game_events import OnStaggeredMessageDisplayEvent
from Controllers.game_events import OnShowAvailableActionsEvent


class BaseSequence():
    @classmethod
    @abstractmethod
    def handle_sequence():
        raise NotImplementedError("This is using base class abstract property, please make your own!")

    @classmethod
    @abstractmethod
    def trigger_event_sequence():
        raise NotImplementedError("This is using base class abstract property, please make your own!")

    @classmethod
    def get_player_input(cls):
        return input("\nWhat do you choose?  ")

    @classmethod
    def display_room_description(cls, description: list[str] = None):
        evt = OnStaggeredMessageDisplayEvent()
        evt.messages = description
        EventController.broadcast_event(evt)
 
    @classmethod
    def setup_rooms(cls, room_exits = None, registered_rooms: Dict = {}, room_description: list[str] = None):
        cls.registered_rooms=registered_rooms
        if room_exits and len(room_exits) > 0:
            cls.room_exits = room_exits

        if room_description:
            cls.display_room_description(description=room_description)

    @classmethod
    def handle_actions(cls, possible_actions):
        evt = OnShowAvailableActionsEvent(possible_actions=possible_actions)
        EventController.broadcast_event(evt)
        return str(cls.get_player_input())
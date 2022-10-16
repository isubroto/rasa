# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

#  from typing import Any, Text, Dict, List

#  from rasa_sdk import Action, Tracker
#  from rasa_sdk.executor import CollectingDispatcher


#  class ActionHelloWorld(Action):

#      def name(self) -> Text:
#          return "action_hello_world"

#      def run(self, dispatcher: CollectingDispatcher,
#              tracker: Tracker,
#              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#          dispatcher.utter_message(text="Hello World!")

#          return []
from email import message
from html import entities
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_ActionChecker"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         entities = tracker.latest_message['entities']
         print(entities)

         for e in entities:
             if e['entity'] == 'services':
                 name = e['value']

             if name == "superannuation":
                 message = "Super is savings for your retirement. And who you choose and how you choose to invest and grow those savings is up to you. learn more: https://www.hesta.com.au/members/your-superannuation"
             
             if name == "investments":
                 message = "Super is one of the biggest investments most of us will make, so it’s important to understand your investment options and how performance will affect your super when you're ready to retire. Learn more: https://www.hesta.com.au/members/investments"

             if name == "retirement":
                 message = "Whether you're two or twenty years away from retiring, we're here to help you understand your options and how to transition into this new phase of life. Learn more: https://www.hesta.com.au/members/retirement"

         dispatcher.utter_message(text=message)

         return []
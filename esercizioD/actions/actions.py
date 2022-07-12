# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from ctypes import string_at
from pdb import Restart
from random import Random, randint
from typing import Any, Text, Dict, List

from rasa_sdk.events import EventType, Restarted 
from rasa_sdk import Action, Tracker , FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

numeri = ["1","2","3","4","5","6"]

class AskForNumeroPallaAction(Action):

    def name(self) -> Text:
        return "action_ask_numero_palla"
    
    def db_parole(self):
        return {
            1: "palla",
            2: "palla palla",
            3: "palla palla palla",
            4: "palla palla palla palla ",
            5: "palla palla palla palla palla",
            6: "palla palla palla palla palla palla"
        }

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        n = randint(1,6)
        stringa = "{}"
        numeri.insert(0,stringa.format(n))
        parola = self.db_parole().get(n)
        dispatcher.utter_message(text = parola + "\nQuante volte ho scritto la parola palla?"
        + "\nRispondi con un numero: 1,2,3...")                
        return []
    

class ValidatePlayForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_play_form"

    def db_numeri(self) -> List[Text]:
        return ["1","2","3","4","5","6"]

    def lista_numeri(self) -> List[Text]:
        return numeri

    def validate_numero_palla(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        if slot_value.lower() not in self.db_numeri() or slot_value.lower() != self.lista_numeri()[0]:
            dispatcher.utter_message(text = "Purtroppo hai sbagliato :-( \nDai riprova")
            return {"numero_palla": None}

        dispatcher.utter_message(
            text = "Corretto, il numero è giusto!"
        )   
        return {"numero_palla": slot_value}



class AskForNumeroMeleAction(Action):

    def name(self) -> Text:
        return "action_ask_numero_mele"

    def lista_numeri_mele(self):
        return ["1 mela", "2 mele", "3 mele", "4 mele","5 mele", "6 mele"]
    
    def db_parole(self):
        return {
            "1 mela": "pera mela pera",
            "2 mele": "mela pera mela pera pera",
            "3 mele": "pera pera mela pera mela mela pera",
            "4 mele": "mela pera pera mela pera mela mela",
            "5 mele": "mela mela pera mela pera mela mela",
            "6 mele": "pera mela mela mela mela pera mela pera mela"
        }

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        n = randint(0,5)
        stringa = self.lista_numeri_mele()[n]
        numeri.insert(0,stringa)
        parola = self.db_parole().get(stringa)
        dispatcher.utter_message(text = parola + "\nQuante mele ci sono in questa frase?"+
        "\nRispondi nel seguente modo: 1 mela, 2 mele,...")                
        return []
    

class ValidatePlayLevel2Form(FormValidationAction):
    def name(self) -> Text:
        return "validate_play_level2_form"

    def db_numeri(self) -> List[Text]:
        return ["1 mela","2 mele","3 mele","4 mele","5 mele","6 mele"]

    def lista_numeri(self) -> List[Text]:
        return numeri

    def validate_numero_mele(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        if slot_value.lower() not in self.db_numeri() or slot_value.lower() != self.lista_numeri()[0]:
            dispatcher.utter_message(text = "Purtroppo hai sbagliato :-( \nDai riprova")
            return {"numero_mele": None}

        dispatcher.utter_message(
            text = "Corretto, il numero è giusto!"
        )   
        return {"numero_mele": slot_value}

class AskForNumeroAction(Action):

    def name(self) -> Text:
        return "action_ask_numero"

    def lista_numeri_oggetti(self):
        return ["1 casa", "2 case", "3 case", "4 case","5 case", "6 case"]
    
    def db_parole(self):
        return {
            "1 casa": "hotel villa casa hotel villa villa",
            "2 case": "casa villa villa hotel casa hotel villa",
            "3 case": "villa hotel casa hotel casa casa villa hotel",
            "4 case": "casa villa casa hotel hotel hotel villa casa villa casa ",
            "5 case": "villa hotel villa casa casa hotel casa villa casa hotel casa villa",
            "6 case": "hotel casa villa casa casa casa villa hotel villa casa hotel villa casa villa hotel"
        }

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        n = randint(0,5)
        stringa = self.lista_numeri_oggetti()[n]
        numeri.insert(0,stringa)
        parola = self.db_parole().get(stringa)
        dispatcher.utter_message(text = parola + "\nQuante case ci sono in questa frase?"+
        "\nRispondi nel seguente modo: 1 casa, 2 case,...")                
        return []
    

class ValidatePlayLevel3Form(FormValidationAction):
    def name(self) -> Text:
        return "validate_play_level3_form"

    def db_numeri(self) -> List[Text]:
        return ["1 casa","2 case","3 case","4 case","5 case","6 case"]

    def lista_numeri(self) -> List[Text]:
        return numeri

    def validate_numero(
        self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict ) -> Dict[Text,Any]: 
        
        if slot_value.lower() not in self.db_numeri() or slot_value.lower() != self.lista_numeri()[0]:
            dispatcher.utter_message(text = "Purtroppo hai sbagliato :-( \nDai riprova")
            return {"numero": None}

        dispatcher.utter_message(
            text = "Corretto, il numero è giusto!"
        )   
        return {"numero": slot_value}

class ActionRestart(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: "CollectingDispatcher", tracker: Tracker, domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Digita di nuovo 'giochiamo' per giocare di nuovo")
        return [Restarted()]

# x = {
#         "1 mela": "pera mela pera",
#         "2 mele": "mela pera mela pera pera",
#         "3 mele": "pera pera mela pera mela mela pera",
#         "4 mele": "mela pera pera mela pera mela mela",
#         "5 mele": "mela mela pera mela pera mela mela",
#         "6 mele": "pera mela mela mela mela pera mela pera mela"
# }

# z = ["1 mela", "2 mele", "3 mele", "4 mele","5 mele", "6 mele"]

# n = randint(1,6)
# stringa = z[n]
# print(stringa)
# numeri.insert(0,stringa)
# print(numeri)
# parola = x[stringa]
# print(parola)


#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

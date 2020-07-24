from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
import wikipedia
import datetime
from babel.dates import format_date, format_time
import cv2
import subprocess
url = "https://id.wikipedia.org"


class ActionAnswerSearch(Action):

    def name(self):
        return "action_answer_search"

    def run(
        self, dispatcher, tracker: Tracker, domain: [Text, Any]
    ) -> List[Dict[Text, Any]]:
        wikipedia.set_lang("id")
        search = tracker.get_slot("who")
        if tracker.get_slot("who"):
            result = wikipedia.summary(search, sentences=2)
            dispatcher.utter_message(result)
        else:
            result = input('')
            dispatcher.utter_message(wikipedia.summary(result, sentences=2))

        return []


class ActionAnswerDate(Action):
    def name(self) -> Text:
        return "action_answer_date"

    def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        date_obj = datetime.date.today()
        dispatcher.utter_message(format_date(date_obj, format='long', locale='id'))

        return []


class ActionAnswerHour(Action):
    def name(self) -> Text:
        return "action_answer_hour"

    def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        time_obj = datetime.datetime.now()
        dispatcher.utter_message(format_time(time_obj, 'h:mm a', locale='id'))

        return []


class ActionAnswerDay(Action):
    def name(self) -> Text:
        return "action_answer_day"

    def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        day_obj = datetime.datetime.now()
        dispatcher.utter_message(format_date(day_obj, 'EEEE', locale='id'))

        return []


class ActionAnswerYear(Action):
    def name(self) -> Text:
        return "action_answer_year"

    def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        year_obj = datetime.datetime.now()
        dispatcher.utter_message(format_date(year_obj, 'yyyy', locale='id'))

        return []


class ActionAnswerMonth(Action):
    def name(self) -> Text:
        return "action_answer_month"

    def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        month_obj = datetime.datetime.now()
        dispatcher.utter_message(format_date(month_obj, 'MMMM', locale='id'))

        return []


class ActionOpenCamera(Action):
    def name(self):
        return 'action_open_camera'

    def run(self, dispatcher, tracker, domain):
        cap = cv2.VideoCapture(0)
        dispatcher.utter_message(text="OK")
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()

            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # When everything done, release the capture
        cap.release()
        cv2.destroyAllWindows()
        return []


class ActionOpenNote(Action):
    def name(self):
        return 'action_open_note'

    def run(
        self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Baik akan kubuka note")
        subprocess.run('notepad.exe', shell=True)
        return []

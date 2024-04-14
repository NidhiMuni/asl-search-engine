from django.core.management.base import BaseCommand
from translator.models import Question, Choice
from django.utils import timezone


# to run -> python3 manage.py add_options

class Command(BaseCommand):
    help = 'Adds a list of questions and choices to the database'

    def handle(self, *args, **options):
        questions = [
    {"question": "Contact", "choices": ["False", "True"]},
    {"question": "Dominant_end_handshape", "choices": ["l", "full–m", "7", "bent–u", "b", "crvd–3", "flat–o", "i", "flat–o_2", "tight–c–2", "i_j", "m", "bent–n", "10", "d", "25", "#5–c–l", "crvd–l", "t", "x–over–thumb", "bent–1", "l–x", "s", "fanned–flat–o", "bent–horns", "6", "bent–b–xd", "u", "cocked–f", "r–l", "loose–e", "crvd–v", "flat–o–2", "u–l", "bent–b–l", "1", "crvd–sprd–b", "psv", "n", "open–8", "b–l", "w", "bent–m", "horns", "v", "x", "flat–b", "#5–c–tt", "bent–u–l", "g", "tight–c", "flat–g", "3", "5", "a", "r", "8", "k", "alt–g_bent–l", "bent–b", "crvd–w", "crvd–b", "4", "crvd–flat–b", "sml–c–3", "crvd–u", "bent–v", "b–xd", "#5–c", "i–l–y", "baby–o", "o", "e", "y", "o–2–horns", "open–7", "f", "open–f", "c", "cocked–s", "crvd–5"]},
    {"question": "Dominant_start_handshape", "choices": ["l", "full–m", "7", "bent–u", "b", "crvd–3", "flat–o", "i", "flat–o_2", "tight–c–2", "i_j", "m", "bent–n", "10", "d", "25", "#5–c–l", "crvd–l", "t", "x–over–thumb", "bent–1", "l–x", "s", "fanned–flat–o", "bent–horns", "cocked–8", "6", "bent–b–xd", "u", "cocked–f", "r–l", "loose–e", "crvd–v", "u–l", "flat–o–2", "bent–b–l", "1", "crvd–sprd–b", "psv", "n", "open–8", "b–l", "w", "bent–m", "horns", "v", "x", "flat–b", "bent–u–l", "g", "tight–c", "flat–g", "3", "5", "a", "r", "8", "k", "alt–g_bent–l", "bent–b", "cocked–7.png", "crvd–w", "crvd–b", "4", "crvd–flat–b", "sml–c–3", "cocked–u", "crvd–u", "bent–v", "b–xd", "#5–c", "i–l–y", "baby–o", "o", "e", "y", "o–2–horns", "open–7", "bent–l", "f", "open–f", "c", "cocked–s", "crvd–5"]},
    {"question": "Flexion", "choices": ["fully closed", "stacked", "curved", "crossed", "flat", "fully open", "bent"]},
    {"question": "Flexion_Change", "choices": ["False", "True"]},
    {"question": "Handshape", "choices": ["baby_o", "l", "7", "goody_goody", "curved_5", "flat_h", "open_8", "open_b", "bent_1", "g", "4", "i", "flat_4", "flat_ily", "3", "5", "a", "closed_b", "flat_o", "1", "flat_n", "curved_l", "spread_e", "d", "flat_1", "stacked_5", "r", "o", "closed_e", "bent_v", "e", "p", "y", "open_e", "8", "flatspread_5", "t", "k", "w", "ily", "open_f", "bent_l", "curved_h", "flat_horns", "s", "v", "spread_open_e", "horns", "curved_4", "f", "flat_v", "curved_1", "flat_m", "h", "flat_b", "c", "curved_v", "open_h"]},
    {"question": "Location", "choices": ["False", "True", "none", "#0+0", "–&0", "#1+0", "#1&1", "#0&0", "?", "#0+0&–", "#0&1"]},
    {"question": "Major_Location", "choices": ["other", "head", "neutral", "arm", "body", "hand"]},
    {"question": "Minor_Location", "choices": ["other", "forearm back", "waist", "neutral", "wrist front", "torso mid", "torso top", "head top", "hand away", "finger back", "head away", "palm back", "neck", "under chin", "clavicle", "cheek nose", "finger tip", "wrist back", "palm", "mouth", "heel", "upper lip", "hips", "torso bottom", "chin", "finger radial", "shoulder", "elbow back", "upper arm", "eye", "body away", "arm away", "forehead", "finger front", "forearm ulnar", "finger ulnar", "forearm front"]},
    {"question": "Nondominant_Handshape", "choices": ["dominance condition violation", "baby_o", "symmetry violation", "l", "curved_5", "flat_h", "b", "open_8", "open_b", "bent_1", "g", "4", "i", "curved_b", "flat_4", "3", "5", "a", "closed_b", "flat_o", "1", "curved_l", "flat_1", "stacked_5", "r", "o", "bent_v", "e", "p", "y", "8", "open_e", "flatspread_5", "w", "ily", "bent_l", "flat_horns", "s", "v", "spread_open_e", "horns", "curved_4", "f", "flat_v", "curved_1", "flat_m", "h", "flat_b", "lax", "c", "curved_v", "open_h"]},
    {"question": "Path_Movement", "choices": ["none", "other", "curved", "x-shaped", "straight", "z–shaped", "back and forth", "x–shaped", "z-shaped", "circular"]},
    {"question": "Repeated_Movement", "choices": ["False", "True"]},
    {"question": "Second_Minor_Location", "choices": ["other", "forearm back", "waist", "neutral", "torso mid", "torso top", "forearm radial", "hand away", "head top", "finger back", "head away", "palm back", "neck", "under chin", "other away", "clavicle", "cheek nose", "finger tip", "palm", "mouth", "heel", "hips", "upper lip", "torso bottom", "chin", "finger radial", "shoulder", "elbow back", "upper arm", "eye", "body away", "arm away", "forehead", "finger front", "forearm ulnar", "finger ulnar", "forearm front"]},
    {"question": "Selected_Fingers", "choices": ["r", "m", "mrp", "imp", "im", "imrp", "p", "imr", "i", "t", "ip", "mr"]},
    {"question": "Sign_Duration", "choices": ["200", "300", "400", "500", "600", "700", "800", "900", "1000", "1100", "1200", "1300", "1400", "1500", "1600", "1700", "1800", "1900", "2000", "2100", "2200", "2300", "2400", "2600"]},
    {"question": "Sign_Type", "choices": ["symmetry violation", "symmetrical or alternating", "one handed", "dominance violation", "asymmetrical different handshape", "asymmetrical same handshape", "classifiers", "lexical signs", "fingerspelled signs", "loan signs", "gestures", "number signs", "compound signs"]},
    {"question": "Spread", "choices": ["False", "True"]},
    {"question": "Spread_Change", "choices": ["False", "True"]},
    {"question": "Thumb_Contact", "choices": ["False", "True"]},
    {"question": "Thumb_Position", "choices": ["open", "closed"]},
    {"question": "Wrist_Twist", "choices": ["False", "True"]},
]


        for q in questions:
            question = Question(question_text=q['question'], pub_date=timezone.now())
            question.save()
            for choice_text in q['choices']:
                Choice.objects.create(question=question, choice_text=choice_text, votes=0)

        self.stdout.write(self.style.SUCCESS('Questions and choices added'))

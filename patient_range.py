from kivy.lang import Builder
from kivymd.app import MDApp
from patient_muscle_upper import PatientMuscleUpper
import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()
KV = '''
FloatLayout:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1.0  # White background color (RGBA values)
        Rectangle:
            pos: self.pos
            size: self.size

    MDLabel:
        text: "Patient Assessment"
        theme_text_color: "Custom"
        text_color: "blue"
        pos_hint: {"center_x": 0.6,"center_y": 0.9}
        size_hint: 0.3, 0.1
    MDLabel:
        text: "Range of motion : Lower limb"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.58, "center_y": 0.8}
        size_hint: 0.3, 0.1
    MDLabel:
        text: "Hip :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.4, "center_y": 0.7}
        size_hint: 0.3, 0.1
    MDTextField:
        id: hip_active_textfield_l
        hint_text: "Active range (L)"
        multiline: True
        pos_hint: {"center_x": 0.38, "center_y": 0.7}
        size_hint: 0.1, 0.1
    MDTextField:
        id: hip_active_textfield_r
        hint_text: "Active range (R)"
        multiline: True
        pos_hint: {"center_x": 0.5, "center_y": 0.7}
        size_hint: 0.1, 0.1  
    MDTextField:
        id: hip_passive_textfield_l
        hint_text: "Passive range (L)"
        multiline: True
        pos_hint: {"center_x": 0.62, "center_y": 0.7}
        size_hint: 0.1, 0.1 
    MDTextField:
        id: hip_passive_textfield_r
        hint_text: "Passive range (R)"
        multiline: True
        pos_hint: {"center_x": 0.74, "center_y": 0.7}
        size_hint: 0.1, 0.1     
    MDLabel:
        text: "Knee :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.4, "center_y": 0.6}
        size_hint: 0.3, 0.1
    MDTextField:
        id: knee_active_textfield_l
        hint_text: "Active range (L)"
        multiline: True
        pos_hint: {"center_x": 0.38, "center_y": 0.6}
        size_hint: 0.1, 0.1 
    MDTextField:
        id: knee_active_textfield_r
        hint_text: "Active range (R)"
        multiline: True
        pos_hint: {"center_x": 0.5, "center_y": 0.6}
        size_hint: 0.1, 0.1    
    MDTextField:
        id: knee_passive_textfield_l
        hint_text: "Passive range (L)"
        multiline: True
        pos_hint: {"center_x": 0.62, "center_y": 0.6}
        size_hint: 0.1, 0.1 
    MDTextField:
        id: knee_passive_textfield_r
        hint_text: "Passive range (R)"
        multiline: True
        pos_hint: {"center_x": 0.74, "center_y": 0.6}
        size_hint: 0.1, 0.1    
    MDLabel:
        text: "Ankle-Foot :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.4, "center_y": 0.5}
        size_hint: 0.3, 0.1
    MDTextField:
        id: ankle_active_textfield_l
        hint_text: "Active range (L)"
        multiline: True
        pos_hint: {"center_x": 0.38, "center_y": 0.5}
        size_hint: 0.1, 0.1
    MDTextField:
        id: ankle_active_textfield_r
        hint_text: "Active range (R)"
        multiline: True
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        size_hint: 0.1, 0.1
    MDTextField:
        id: ankle_passive_textfield_l
        hint_text: "Passive range (L)"
        multiline: True
        pos_hint: {"center_x": 0.62, "center_y": 0.5}
        size_hint: 0.1, 0.1
    MDTextField:
        id: ankle_passive_textfield_r
        hint_text: "Passive range (R)"
        multiline: True
        pos_hint: {"center_x": 0.74, "center_y": 0.5}
        size_hint: 0.1, 0.1 
    MDLabel:
        text: "Neck :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.4, "center_y": 0.4}
        size_hint: 0.3, 0.1
    MDTextField:
        id: neck_active_textfield_l
        hint_text: "Active range (L)"
        multiline: True
        pos_hint: {"center_x": 0.38, "center_y": 0.4}
        size_hint: 0.1, 0.1
    MDTextField:
        id: neck_active_textfield_r
        hint_text: "Active range (R)"
        multiline: True
        pos_hint: {"center_x": 0.5, "center_y": 0.4}
        size_hint: 0.1, 0.1   
    MDTextField:
        id: neck_passive_textfield_l
        hint_text: "Passive range (L)"
        multiline: True
        pos_hint: {"center_x": 0.62, "center_y": 0.4}
        size_hint: 0.1, 0.1
    MDTextField:
        id: neck_passive_textfield_r
        hint_text: "Passive range (R)"
        multiline: True
        pos_hint: {"center_x": 0.74, "center_y": 0.4}
        size_hint: 0.1, 0.1   
    MDLabel:
        text: "Trunk :"
        theme_text_color: "Custom"
        text_color: "black"
        pos_hint: {"center_x": 0.4, "center_y": 0.3}
        size_hint: 0.3, 0.1
    MDTextField:
        id: trunk_active_textfield_l
        hint_text: "Active range (L)"
        multiline: True
        pos_hint: {"center_x": 0.38, "center_y": 0.3}
        size_hint: 0.1, 0.1
    MDTextField:
        id: trunk_active_textfield_r
        hint_text: "Active range (R)"
        multiline: True
        pos_hint: {"center_x": 0.5, "center_y": 0.3}
        size_hint: 0.1, 0.1   
    MDTextField:
        id: trunk_passive_textfield_l
        hint_text: "Passive range (L)"
        multiline: True
        pos_hint: {"center_x": 0.62, "center_y": 0.3}
        size_hint: 0.1, 0.1
    MDTextField:
        id: trunk_passive_textfield_r
        hint_text: "Passive range (R)"
        multiline: True
        pos_hint: {"center_x": 0.74, "center_y": 0.3}
        size_hint: 0.1, 0.1      
    MDRaisedButton:
        text: "Next"
        md_bg_color: "green"
        pos_hint: {"center_x": 0.5, "center_y": 0.2}
        size_hint: 0.1, 0.08
        on_press: app.next()                  
'''

class PatientRange(MDApp):
    def __init__(self,patient_no,date,email, **kwargs):
        super().__init__(**kwargs)
        mongo_uri = os.getenv('MONGODB_URI')
        self.client = MongoClient(mongo_uri)
        self.db = self.client['rehab']
        self.collection = self.db['patient_data']
        self.patient = patient_no
        self.date = date
        self.email = email
        
  


    limb_textfield_ids = {
        "Hip": ("hip_active_textfield_l","hip_active_textfield_r","hip_passive_textfield_l","hip_passive_textfield_r"),
        "Knee": ("knee_active_textfield_l","knee_active_textfield_r","knee_passive_textfield_l","knee_passive_textfield_r"),
        "Ankle-Foot": ("ankle_active_textfield_l","ankle_active_textfield_r","ankle_passive_textfield_l","ankle_passive_textfield_r"),
        "Neck": ("neck_active_textfield_l","neck_active_textfield_r","neck_passive_textfield_l","neck_passive_textfield_r"),
        "Trunk": ("trunk_active_textfield_l","trunk_active_textfield_r","trunk_passive_textfield_l","trunk_passive_textfield_r")
    }

    def build(self):
        return Builder.load_string(KV)
    

    def set_error_message(self, instance_textfield, value):
        if not instance_textfield.text.strip():
            instance_textfield.error = True
            instance_textfield.helper_text = "Required field"
        else:
            instance_textfield.error = False
            instance_textfield.helper_text = ""

    def next(self):
        
        
        for limb, (active_left_id,active_right_id, passive_left_id,passive_right_id) in self.limb_textfield_ids.items():
            active_left_range = self.root.ids[active_left_id].text.strip()
            active_right_range = self.root.ids[active_right_id].text.strip()
            passive_left_range = self.root.ids[passive_left_id].text.strip()
            passive_right_range = self.root.ids[passive_right_id].text.strip()
            
            if not active_left_range:
                self.root.ids[active_left_id].error = True
                self.root.ids[active_left_id].helper_text = "Required field"
            else:
                self.root.ids[active_left_id].error = False
                self.root.ids[active_left_id].helper_text = ""

            if not active_right_range:
                self.root.ids[active_right_id].error = True
                self.root.ids[active_right_id].helper_text = "Required field"
            else:
                self.root.ids[active_right_id].error = False
                self.root.ids[active_right_id].helper_text = ""
    
            if not passive_left_range:
                self.root.ids[passive_left_id].error = True
                self.root.ids[passive_left_id].helper_text = "Required field"
            else:
                self.root.ids[passive_left_id].error = False
                self.root.ids[passive_left_id].helper_text = ""

            if not passive_right_range: 
                self.root.ids[passive_right_id].error = True
                self.root.ids[passive_right_id].helper_text = "Required field"
            else:
                self.root.ids[passive_right_id].error = False
                self.root.ids[passive_right_id].helper_text = ""
        
        if (
           
             all(
                not self.root.ids[active_left_id].error and not self.root.ids[active_right_id].error and not self.root.ids[passive_left_id].error and not self.root.ids[passive_right_id].error
                for active_left_id,active_right_id,passive_left_id,passive_right_id in self.limb_textfield_ids.values()
            )
        ):
            
            lower_limb_ass = {}

            for limb, (active_left_id,active_right_id,passive_left_id, passive_right_id) in self.limb_textfield_ids.items():
                active_left_range = self.root.ids[active_left_id].text.strip()
                active_right_range = self.root.ids[active_right_id].text.strip()
                passive_left_range = self.root.ids[passive_left_id].text.strip()
                passive_right_range = self.root.ids[passive_right_id].text.strip()

                lowerlimb_values = {"Active Range (L)": active_left_range,
                                   "Active Range (R)" : active_right_range,
                                   "Passive Range (L)" : passive_left_range,
                                    "Passive Range (R)": passive_right_range }
                lower_limb_ass[limb] = lowerlimb_values

            

            key_email = self.email
            key_patient = self.patient
            key_date = self.date
            existing_document = self.collection.find_one({f"{key_email}.{key_patient}.{key_date}": {'$exists': True}})
            if existing_document :
                update = {
                    '$set': {
                        f"{key_email}.{key_patient}.{key_date}.Range of motion for Lower limb": lower_limb_ass,
                        }
                }
                self.collection.update_one(
                    {f"{key_email}.{key_patient}.{key_date}": {'$exists': True}},
                    update,
                    upsert=True
                )     
            self.stop()
            PatientMuscleUpper(self.patient,self.date,self.email).run()       
            
           

if __name__ == '__main__':
    PatientRange().run()

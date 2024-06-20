from datetime import datetime, timedelta
import threading
import datetime
import os
from dotenv import load_dotenv

import firebase_admin
from firebase_admin import firestore, credentials

load_dotenv()  # Loading Environment

cred = credentials.Certificate(os.getenv("FIREBASE_CREDENTIAL"))
firebase_admin.initialize_app(cred)
db = firestore.client()


class getUserDetails:
    def __init__(self, uid):
        self.uid = uid

    def start_process(self):
        try:
            doc_ref = db.collection("users").document(self.uid)
            doc = doc_ref.get()
            dict = doc.to_dict()
            return dict


        except:
            return 0


class getStudentDetails:

    def __init__(self, phone):
        self.phone = phone

    def start_process(self):
        try:
            existing_reg_phone = db.collection("users").where('phone', "==", self.phone).stream()
            for docId in existing_reg_phone:
                docRef = docId.id

                get_user_details = db.collection('users').document(docRef).get()
                fetch_user_details = get_user_details.to_dict()
                print("USER_DETAILS", fetch_user_details)
                return fetch_user_details
        except:
            return 0


class getUserLoggedOnSpecificDate:

    def __init__(self,regDate):
        self.regDate = regDate

    def start_process(self):
        try:
            registration_date = datetime.datetime.strptime(self.regDate, "%d/%m/%Y")
            registration_date2 = registration_date + timedelta(days=1)
            docs = db.collection('users').where('registration_date', ">=", registration_date).where('registration_date', "<",
                                                                                            registration_date2).stream()

            if docs:

                self.final_List = []

                for doc_id in docs:
                    fetch_data = doc_id.to_dict()
                    print("--------getting Data", fetch_data)
                    self.final_List.append(fetch_data)
                return self.final_List

        except:
            return 0


class createbatch:

    def __init__(self,serializer):
        self.serializer = serializer
        # self.uid = self.serializer.data['uid']
        # self.batch_title = self.serializer.data['batch_title']
        # self.batch_description = self.serializer.data['batch_description']

    def get_data_from_serializer(self):

        self.uid = self.serializer.data['uid']
        self.batch_title = self.serializer.data['batch_title']
        self.batch_description = self.serializer.data['batch_description']

    def save_to_fb(self):

        doc1 = db.collection('batches').document(self.uid)
        self.batch_data = {
            "batch_title": self.batch_title,
            "batch_description": self.batch_description}
        doc1.set(self.batch_data)

    def start_process(self):
        try:
            t1 = threading.Thread(target=self.get_data_from_serializer())
            t2 = threading.Thread(target=self.save_to_fb())
            t1.start()
            t2.start()
            t1.join()
            t2.join()

        except:
            print("ERROR - in  Thread 1")
            return 0


        return self.batch_data





class updateBatch:

    def __init__(self, serializer):
        self.serializer = serializer
        self.batch_title = self.serializer.data['batch_title']
        self.batch_description = self.serializer.data['batch_description']
        self.uid = self.serializer.data['uid']

    def update_batch_details(self):
        doc_ref = db.collection('batches'). \
         document(self.uid)

        self.data = {
         'batch_description':self.batch_description,
          "batch_title": self.batch_title,

        }

        try:
            doc_ref.update(self.data)

        except:
            print("ERROR - in - for batch details update")

    def save_log(self):
        pass

    def start_process(self):
        try:
            t1 = threading.Thread(target=self.update_batch_details)
            t2 = threading.Thread(target=self.save_log)

            t1.start()
            t2.start()
            t1.join()
            t2.join()
        except:
            print("ERROR - in - Thread 1")
            return 0
        return 1


class getStudentDetailsUsingEmail:

        def __init__(self, email):
            self.email = email

        def start_process(self):
            try:
                existing_reg_email = db.collection("users").where('email_id', "==", self.email).stream()
                for docId in existing_reg_email:
                    docRef = docId.id

                    get_user_details = db.collection('users').document(docRef).get()
                    fetch_user_details = get_user_details.to_dict()
                    print("USER_DETAILS", fetch_user_details)
                    return fetch_user_details

            except:
                return 0

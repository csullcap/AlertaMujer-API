import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#  cred = credentials.Certificate('./src/credentials/android-backend-8f0f1-firebase-adminsdk-hpexy-4e3beb0da7.json')
cred = credentials.Certificate('./src/credentials/api-alertamujer-aux-firebase-adminsdk-5wn7n-e410316a0b.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
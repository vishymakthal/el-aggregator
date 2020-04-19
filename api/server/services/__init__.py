from server.services.firebase import Firebase
from server.services.algolia import Algolia
from server.config import cfg

firebase = Firebase(cfg.FIREBASE_CERT_PATH, cfg.FIREBASE_DB_URL)
algolia_search = Algolia()

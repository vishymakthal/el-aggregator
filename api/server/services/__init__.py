from server.services.firebase import Firebase
from server.services.algolia import Algolia
from server.services.reddit import Reddit
from server.config import cfg

firebase = Firebase(cfg.FIREBASE_CERT_PATH, cfg.FIREBASE_DB_URL)
algolia_search = Algolia()
reddit = Reddit(cfg.CLIENT_ID, cfg.CLIENT_SECRET, cfg.USER_AGENT)

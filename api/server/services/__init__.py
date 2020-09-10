from server.services.firebase import Firebase
from server.services.algolia import Algolia
from server.services.reddit import Reddit
from server.services.youtube import YouTube
from server.config import cfg

firebase = Firebase(cfg.FIREBASE_CERT_PATH, cfg.FIREBASE_DB_URL, cfg.FIREBASE_STORAGE_URL)
firebase.read_from_storage()

algolia_search = Algolia()
reddit = Reddit(cfg.CLIENT_ID, cfg.CLIENT_SECRET, cfg.USER_AGENT)
youtube = YouTube(cfg.YT_KEY)
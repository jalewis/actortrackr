'''
Elasticsearch Settings
'''

ES_PREFIX   = "tp-"
ES_HOSTS    = ['http://localhost:9200',]

'''
MySQL Settings
'''

MYSQL_USER      = '<user>'
MYSQL_PASSWD    = '<password>'
MYSQL_DB        = 'threat_actors'

'''
Log Settings
'''

LOG_FILE        = "/var/log/actortrackr/actortrackr.log"
LOG_TO_CONSOLE  = True
LOG_LEVEL       = "DEBUG" #NOSET, DEBUG, INFO, WARNING, ERROR, CRITICAL

'''
Email Settings
'''

#the email address of the sender
EMAIL_SENDER    =  "Your email here"

#alerts go to these addresses
EMAIL_ADDRESSES =  [ "Your email here", ] 

'''
Application Settings
'''

MAINTENANCE_MODE = False

APPLICATION_DOMAIN  = "http://actortrackr.com/"
APPLICATION_ORG     = "Lookingglass"
APPLICATION_NAME    = "ActorTrackr"

TLPS    =   [
                ("0", "White"),
                ("1", "Green"),
                ("2", "Amber"),
                ("3", "Red"),
                ("4", "Black")
        ]

SOURCE_RELIABILITY    =   [
                            ("A", "A. Reliable - No doubt about the source's authenticity, trustworthiness, or competency. History of complete reliability."),
                            ("B", "B. Usually Reliable - Minor doubts. History of mostly valid information."),
                            ("C", "C. Fairly Reliable - Doubts. Provided valid information in the past."),
                            ("D", "D. Not Usually Reliable - Significant doubts. Provided valid information in the past."),
                            ("E", "E. Unreliable - Lacks authenticity, trustworthiness, and competency. History of invalid information."),
                            ("F", "F. Can’t Be Judged - Insufficient information to evaluate reliability. May or may not be reliable.")
                    ]

INFORMATION_RELIABILITY    =   [
                            ("1", "1. Confirmed - Logical, consistent with other relevant information, confirmed by independent sources."),
                            ("2", "2. Probably True - Logical, consistent with other relevant information, not confirmed by independent sources."),
                            ("3", "3. Possibly True - Reasonably logical, agrees with some relevant information, not confirmed."),
                            ("4", "4. Doubtfully True - Not logical but possible, no other information on the subject, not confirmed."),
                            ("5", "5. Improbable - Not logical, contradicted by other relevant information."),
                            ("6", "6. Can’t Be Judged - The validity of the information can not be determined.")
                    ]

SALTS = {
    "actor" : "salt",
    "report" : "salt",
    "ttp" : "salt",
    "user" : "salt",
    "email_verification" : "salt"
}

SESSION_EXPIRE = -1 # in seconds, -1 to disable

'''
Recaptcha Settings
'''

RECAPTCHA_ENABLED       =   True  
RECAPTCHA_PUBLIC_KEY    =   ''
RECAPTCHA_PRIVATE_KEY   =   ''




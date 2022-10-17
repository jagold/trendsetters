from os import environ

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc="",
    keywords='bonus, study',
    title='Title for your experiment',
    description='Description for your experiment',
    frame_height=500,
    template='global/mturk_template.html',
    minutes_allotted_per_assignment=60,
    expiration_hours=7 * 24,
    qualification_requirements=[]
    #grant_qualification_id='YOUR_QUALIFICATION_ID_HERE', # to prevent retakes
)


SESSION_CONFIGS = [
    dict(
        name='complete',
        display_name="Complete",
        num_demo_participants=4,
        app_sequence=['survey','complete_understanding_b1','complete_block1','complete_understanding_b2','complete_block2','complete_understanding_b3','complete_block3','complete_understanding_b4','complete_block4','complete_understanding_b5','complete_block5','complete_understanding_b6','complete_block6','end'
                      ]
	)
]

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True



ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


# don't share this with anybody.
SECRET_KEY = '{{ secret_key }}'

INSTALLED_APPS = ['otree','otreeutils']

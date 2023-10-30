from sqlalchemy import Boolean, Column, String

from . import BASE, SESSION


class Locks(BASE):
    __tablename__ = "locks"
    chat_id = Column(String(14), primary_key=True)
    # Booleans are for "is this locked", _NOT_ "is this allowed"
    bots = Column(Boolean, default=False)
    commands = Column(Boolean, default=False)
    email = Column(Boolean, default=False)
    forward = Column(Boolean, default=False)
    url = Column(Boolean, default=False)

    def __init__(self, chat_id):
        self.chat_id = str(chat_id)  # ensure string
        self.bots = False
        self.commands = False
        self.email = False
        self.forward = False
        self.url = False


Locks.__table__.create(checkfirst=True)


def init_locks(chat_id, reset=False):
    curr_restr = SESSION.query(Locks).get(str(chat_id))
    if reset:
        SESSION.delete(curr_restr)
        SESSION.flush()
    restr = Locks(str(chat_id))
    SESSION.add(restr)
    SESSION.commit()
    return restr









def update_lock(chat_id, lock_type, locked):
    curr_perm = SESSION.query(Locks).get(str(chat_id))
    if not curr_perm:
        curr_perm = init_locks(chat_id)
    if lock_type == "bots":
        curr_perm.bots = locked
    elif lock_type == "commands":
        curr_perm.commands = locked
    elif lock_type == "email":
        curr_perm.email = locked
    elif lock_type == "forward":
        curr_perm.forward = locked
    elif lock_type == "url":
        curr_perm.url = locked
    SESSION.add(curr_perm)
    SESSION.commit()


def is_locked(chat_id, lock_type):
    curr_perm = SESSION.query(Locks).get(str(chat_id))
    SESSION.close()
    if not curr_perm:
        return False
    if lock_type == "bots":
        return curr_perm.bots
    if lock_type == "commands":
        return curr_perm.commands
    if lock_type == "email":
        return curr_perm.email
    if lock_type == "forward":
        return curr_perm.forward
    if lock_type == "url":
        return curr_perm.url

iqvois1 = "IqArab/helpers/styles/Voic/ابو عباس لو تاكل خره.ogg"
iqvois2 = "IqArab/helpers/styles/Voic/استمر نحن معك.ogg"
iqvois3 = "IqArab/helpers/styles/Voic/افحط بوجه.ogg"
iqvois4 = "IqArab/helpers/styles/Voic/اكعد لا اسطرك سطره العباس.ogg"
iqvois5 = "IqArab/helpers/styles/Voic/اللهم لا شماته.ogg"
iqvois6 = "IqArab/helpers/styles/Voic/امرع دينه.ogg"
iqvois7 = "IqArab/helpers/styles/Voic/امشي بربوك.ogg"
iqvois8 = "IqArab/helpers/styles/Voic/انت اسكت انت اسكت.ogg"
iqvois9 = "IqArab/helpers/styles/Voic/انت سايق زربه.ogg"
iqvois10 = "IqArab/helpers/styles/Voic/اوني تشان.ogg"
iqvois11 = "IqArab/helpers/styles/Voic/برافو عليك استادي.ogg"
iqvois12 = "IqArab/helpers/styles/Voic/بلوك محترم.ogg"
iqvois13 = "IqArab/helpers/styles/Voic/بووم في منتصف الجبهة.ogg"
iqvois14 = "IqArab/helpers/styles/Voic/بيتش.ogg"
iqvois15 = "IqArab/helpers/styles/Voic/تخوني ؟.ogg"
iqvois15 = "IqArab/helpers/styles/Voic/تره متكدرلي.ogg"
iqvois17 = "IqArab/helpers/styles/Voic/تعبان اوي.ogg"
iqvois18 = "IqArab/helpers/styles/Voic/تكذب.ogg"
iqvois19 = "IqArab/helpers/styles/Voic/حسبي الله.ogg"
iqvois20 = "IqArab/helpers/styles/Voic/حشاش.ogg"
iqvois21 = "IqArab/helpers/styles/Voic/حقير.ogg"
iqvois22 = "IqArab/helpers/styles/Voic/خاص.ogg"
iqvois23 = "IqArab/helpers/styles/Voic/خاله ما تنامون.ogg"
iqvois24 = "IqArab/helpers/styles/Voic/خرب شرفي اذا ابقى بالعراق.ogg"
iqvois25 = "IqArab/helpers/styles/Voic/دكات الوكت الاغبر.ogg"
iqvois26 = "IqArab/helpers/styles/Voic/ررردح.ogg"
iqvois27 = "IqArab/helpers/styles/Voic/سلامن عليكم.ogg"
iqvois28 = "IqArab/helpers/styles/Voic/شعليك.ogg"
iqvois29 = "IqArab/helpers/styles/Voic/شكد شفت ناس مدودة.ogg"
iqvois30 = "IqArab/helpers/styles/Voic/شلون ،.ogg"
iqvois31 = "IqArab/helpers/styles/Voic/صح لنوم.ogg"
iqvois32 = "IqArab/helpers/styles/Voic/صمت.ogg"
iqvois33 = "IqArab/helpers/styles/Voic/ضحكة مصطفى الحجي.ogg"
iqvois34 = "IqArab/helpers/styles/Voic/طماطه.ogg"
iqvois35 = "IqArab/helpers/styles/Voic/طيح الله حضك.ogg"
iqvois36 = "IqArab/helpers/styles/Voic/فاك يوو.ogg"
iqvois37 = "IqArab/helpers/styles/Voic/فرحان.ogg"
iqvois38 = "IqArab/helpers/styles/Voic/لا تضل تضرط.ogg"
iqvois39 = "IqArab/helpers/styles/Voic/لا تقتل المتعه يا مسلم.ogg"
iqvois40 = "IqArab/helpers/styles/Voic/لا مستحيل.ogg"
iqvois41 = "IqArab/helpers/styles/Voic/لا والله شو عصبي.ogg"
iqvois42 = "IqArab/helpers/styles/Voic/لش.ogg"
iqvois43 = "IqArab/helpers/styles/Voic/لك اني شعليه.ogg"
iqvois44 = "IqArab/helpers/styles/Voic/ما اشرب.ogg"
iqvois45 = "IqArab/helpers/styles/Voic/مع الاسف.ogg"
iqvois46 = "IqArab/helpers/styles/Voic/مقتدى.ogg"
iqvois47 = "IqArab/helpers/styles/Voic/من رخصتكم.ogg"
iqvois48 = "IqArab/helpers/styles/Voic/منو انت.ogg"
iqvois49 = "IqArab/helpers/styles/Voic/منورني.ogg"
iqvois50 = "IqArab/helpers/styles/Voic/نتلاكه بالدور الثاني.ogg"
iqvois51 = "IqArab/helpers/styles/Voic/نستودعكم الله.ogg"
iqvois52 = "IqArab/helpers/styles/Voic/ها شنهي.ogg"
iqvois53 = "IqArab/helpers/styles/Voic/ههاي الافكار حطها.ogg"
iqvois54 = "IqArab/helpers/styles/Voic/وينهم.ogg"
iqvois55 = "IqArab/helpers/styles/Voic/يموتون جهالي.ogg"
iqvois56 = "IqArab/helpers/styles/Voic/اريد انام.ogg"
iqvois57 = "IqArab/helpers/styles/Voic/افتحك فتح.ogg"
iqvois58 = "IqArab/helpers/styles/Voic/اكل خره لدوخني.ogg"
iqvois59 = "IqArab/helpers/styles/Voic/السيد شنهو السيد.ogg"
iqvois60 = "IqArab/helpers/styles/Voic/زيج2.ogg"
iqvois61 = "IqArab/helpers/styles/Voic/زيج لهارون.ogg"
iqvois62 = "IqArab/helpers/styles/Voic/زيج الناصرية.ogg"
iqvois63 = "IqArab/helpers/styles/Voic/راقبو اطفالكم.ogg"
iqvois64 = "IqArab/helpers/styles/Voic/راح اموتن.ogg"
iqvois65 = "IqArab/helpers/styles/Voic/ذس اس مضرطة.ogg"
iqvois66 = "IqArab/helpers/styles/Voic/دروح سرسح منا.ogg"
iqvois67 = "IqArab/helpers/styles/Voic/خويه ما دكوم بيه.ogg"
iqvois68 = "IqArab/helpers/styles/Voic/خلصت تمسلت ديلة كافي انجب.ogg"
iqvois69 = "IqArab/helpers/styles/Voic/بعدك تخاف.ogg"
iqvois70 = "IqArab/helpers/styles/Voic/بسبوس.ogg"
iqvois71 = "IqArab/helpers/styles/Voic/اني بتيتة كحبة.ogg"
iqvois72 = "IqArab/helpers/styles/Voic/انعل ابوكم لابو اليلعب وياكم طوبة.ogg"
iqvois73 = "IqArab/helpers/styles/Voic/انت شدخلك.ogg"
iqvois74 = "IqArab/helpers/styles/Voic/انا ماشي بطلع.ogg"
iqvois75 = "IqArab/helpers/styles/Voic/امداك وامده الخلفتك.ogg"
iqvois76 = "IqArab/helpers/styles/Voic/امبيههههه.ogg"
iqvois77 = "IqArab/helpers/styles/Voic/هدي بيبي.ogg"
iqvois78 = "IqArab/helpers/styles/Voic/هاه صدك تحجي.ogg"
iqvois79 = "IqArab/helpers/styles/Voic/مو كتلك رجعني.ogg"
iqvois80 = "IqArab/helpers/styles/Voic/مامرجية منك هاية.ogg"
iqvois81 = "IqArab/helpers/styles/Voic/ليش هيجي.ogg"
iqvois82 = "IqArab/helpers/styles/Voic/كـــافـي.ogg"
iqvois83 = "IqArab/helpers/styles/Voic/كس اخت السيد.ogg"
iqvois84 = "IqArab/helpers/styles/Voic/شنو كواد ولك اني هنا.ogg"
iqvois85 = "IqArab/helpers/styles/Voic/شجلبت.ogg"
iqvois86 = "IqArab/helpers/styles/Voic/شبيك وجه الدبس.ogg"
iqvois87 = "IqArab/helpers/styles/Voic/سييييي.ogg"
iqvois88 = "IqArab/helpers/styles/Voic/زيجج1.ogg"
iqvois89 = "IqArab/helpers/styles/Voic/يموتون جهالي.ogg"
iqvois90 = "IqArab/helpers/styles/Voic/ياخي اسكت اسكت.ogg"
iqvois91 = "IqArab/helpers/styles/Voic/وينهم.ogg"
iqvois92 = "IqArab/helpers/styles/Voic/هيلو سامر وحود.ogg"
iqvois93 = "IqArab/helpers/styles/Voic/هو.ogg"
iqvois94 = "IqArab/helpers/styles/Voic/ههاي الافكار حطها.ogg"
iqvois95 = "IqArab/helpers/styles/Voic/الله يساعدك عيوني.ogg"
iqvois96 = "IqArab/helpers/styles/Voic/يلعن دين امك.ogg"
iqvois97 = "IqArab/helpers/styles/Voic/ياخي والله فشله.ogg"
iqvois98 = "IqArab/helpers/styles/Voic/صدقني لو اعرف.ogg"
iqvois99 = "IqArab/helpers/styles/Voic/لك قفصوني.ogg"
iqvois100 = "IqArab/helpers/styles/Voic/علاوي حبيب قلبي.ogg"
iqvois101 = "IqArab/helpers/styles/Voic/كاله انه2.ogg"
iqvois102 = "IqArab/helpers/styles/Voic/هي انداست.ogg"
iqvois103 = "IqArab/helpers/styles/Voic/اني سمعي ثقيل.ogg"
iqvois104 = "IqArab/helpers/styles/Voic/خوات كحه.ogg"
iqvois105 = "IqArab/helpers/styles/Voic/بالامس كانو معي.ogg"
iqvois106 = "IqArab/helpers/styles/Voic/لالتغلط.ogg"
iqvois107 = "IqArab/helpers/styles/Voic/مفخخة.ogg"
iqvois108 = "IqArab/helpers/styles/Voic/قررت احتل العالم.ogg"
iqvois109 = "IqArab/helpers/styles/Voic/صوت صرصور.ogg"
iqvois110 = "IqArab/helpers/styles/Voic/تعال كلكله.ogg"
iqvois111 = "IqArab/helpers/styles/Voic/ياساتر.ogg"
iqvois112 = "IqArab/helpers/styles/Voic/كال انه.ogg"
iqvois113 = "IqArab/helpers/styles/Voic/تعال احط رجلي.ogg"
iqvois114 = "IqArab/helpers/styles/Voic/احمد محسن.ogg"








def get_locks(chat_id):
    try:
        return SESSION.query(Locks).get(str(chat_id))
    finally:
        SESSION.close()

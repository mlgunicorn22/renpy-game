# =========================================================
# CORPORATE EMPIRE GAME
# script.rpy
# =========================================================

# ---------------------------------------------------------
# VARIABLES
# ---------------------------------------------------------

default stock = 50
default corruption = 50

# ---------------------------------------------------------
# CHARACTERS
# ---------------------------------------------------------

define p = Character("Player")
define a = Character("Amelia", color="#c8c8ff")

define clara = Character("Clara Vane", color="#ffd7d7")
define marcus = Character("Marcus Hale", color="#d7ffd7")
define victoria = Character("Victoria Graves", color="#ffb3b3")
define daniel = Character("Daniel Reed", color="#b3d9ff")
define arthur = Character("Arthur Wynn", color="#ffe0a3")
define naomi = Character("Dr. Naomi Bell", color="#d9b3ff")

# ---------------------------------------------------------
# IMAGES
# ---------------------------------------------------------

image bg funeral = "images/funeral.jpg"
image bg lobby = "images/lobby.jpg"
image bg office = "images/office.jpg"
image bg executives = "images/executives.jpg"
image bg dinner = "images/dinner.jpg"

image clara = "images/clara.png"
image marcus = "images/marcus.png"
image victoria = "images/victoria.png"
image daniel = "images/daniel.png"
image arthur = "images/arthur.png"
image naomi = "images/naomi.png"

# ---------------------------------------------------------
# PROFILE CARD UI
# ---------------------------------------------------------

screen profile_card(name, role, traits, quality, notes):

    frame:
        background "#1a1a1ae6"
        xalign 0.03
        yalign 0.2
        xsize 520
        padding (18, 18)

        vbox:
            spacing 8

            text "EMPLOYEE FILE" size 24 bold True color "#ffffff"

            null height 6

            text "NAME: [name]" color "#9fd3ff"
            text "ROLE: [role]" color "#9fd3ff"

            text "TRAITS: [traits]" color "#d0d0d0"
            text "WORK QUALITY: [quality]" color "#d0d0d0"

            null height 6

            text "NOTABLE ACTIONS / NOTES:" color "#ffcc66"
            text "[notes]" size 18

# =========================================================
# START
# =========================================================

label start:

    scene bg funeral
    with fade

    show screen corruption_meter
    show screen stock_meter

    show corruption symbol onlayer screens zorder 20:
        xalign 0.99
        yalign 0.81
    
    show stock symbol onlayer screens zorder 20:
        xalign 0.99
        yalign 0.81

    play music "audio/opening.mp3"

    "Your father built one of the largest corporate empires in the country."

    "Energy. Pharmaceuticals. Logistics. Media."

    "Some called him a genius."
    "Others called him a parasite."

    "Now he is dead."
    "And everything belongs to you."

    a "The board is waiting for you."
    a "Your first day as CEO begins now."

    jump lobby_stage

# =========================================================
# STAGE 1 — LOBBY
# =========================================================

label lobby_stage:

    scene bg lobby
    with dissolve

    "The lobby gleams with polished marble and cold corporate perfection."

    jump clara_scene

# ---------------------------------------------------------
# CLARA SCENE
# ---------------------------------------------------------

label clara_scene:

    show clara
    with dissolve

    show screen profile_card(
        "Clara Vane",
        "Receptionist",
        "Kind, patient, underpaid, loyal",
        "Highly effective",
        "- Secretly helped struggling employees\n- Worked for the company for 12 years\n- Loyal to your father"
    )

    clara "Congratulations on becoming CEO."

    clara "People here are nervous. Your father ruled with fear."

    menu:

        "Increase Clara's salary":
            $ stock -= 3
            $ corruption -= 5
            clara "Thank you. That means more than you know."

        "Ignore her concerns":
            $ corruption += 3
            clara "I understand."

        "Ask her about corruption rumors":
            $ corruption -= 2
            clara "There are people here you should not trust."

    hide screen profile_card
    hide clara

    jump marcus_scene

# ---------------------------------------------------------
# MARCUS SCENE
# ---------------------------------------------------------

label marcus_scene:

    show marcus
    with dissolve

    show screen profile_card(
        "Marcus Hale",
        "Security Chief",
        "Efficient, intimidating, ruthless",
        "Elite",
        "- Prevented a major security attack\n- Covered up workplace violence claims\n- Extremely loyal to executive leadership"
    )

    marcus "Your father understood sacrifice."

    marcus "Weak leadership destroys companies."

    menu:

        "Promote Marcus":
            $ stock += 7
            $ corruption += 8
            marcus "You won't regret it."

        "Investigate misconduct":
            $ stock -= 5
            $ corruption -= 7
            marcus "Careful who you turn against."

        "Keep him where he is":
            $ stock += 1
            marcus "Understood."

    hide screen profile_card
    hide marcus

    jump office_stage

# =========================================================
# STAGE 2 — OFFICE
# =========================================================

label office_stage:

    scene bg office
    with fade

    "Your office overlooks the city your company helped build."

    jump victoria_scene

# ---------------------------------------------------------
# VICTORIA SCENE
# ---------------------------------------------------------

label victoria_scene:

    show victoria
    with dissolve

    show screen profile_card(
        "Victoria Graves",
        "Chief Financial Officer",
        "Brilliant, manipulative, ambitious",
        "Exceptional",
        "- Increased profits by 340 percent\n- Used illegal offshore tax structures\n- Outsourced factories tied to worker deaths"
    )

    victoria "Ethics are expensive."
    victoria "Profit is measurable."

    menu:

        "Support Victoria fully":
            $ stock += 15
            $ corruption += 15
            victoria "Excellent decision."

        "Launch an investigation":
            $ stock -= 10
            $ corruption -= 12
            victoria "You're making dangerous enemies."

        "Quietly monitor her":
            $ stock += 5
            $ corruption += 3
            victoria "Smart."

    hide screen profile_card
    hide victoria

    jump daniel_scene

# ---------------------------------------------------------
# DANIEL SCENE
# ---------------------------------------------------------

label daniel_scene:

    show daniel
    with dissolve

    show screen profile_card(
        "Daniel Reed",
        "HR Director",
        "Honest, compassionate, idealistic",
        "Moderate",
        "- Expanded mental health programs\n- Reduced burnout rates\n- Programs reduced quarterly profits"
    )

    daniel "Employees are not numbers."

    menu:

        "Expand employee programs":
            $ stock -= 7
            $ corruption -= 10
            daniel "People will remember this."

        "Cut the programs":
            $ stock += 8
            $ corruption += 5
            daniel "I expected better."

        "Compromise":
            $ stock += 2
            $ corruption -= 2
            daniel "Fair enough."

    hide screen profile_card
    hide daniel

    jump executive_stage

# =========================================================
# STAGE 3 — EXECUTIVES
# =========================================================

label executive_stage:

    scene bg executives
    with fade

    "The executive floor feels quieter."
    "Sharper."
    "More dangerous."

    jump arthur_scene

# ---------------------------------------------------------
# ARTHUR SCENE
# ---------------------------------------------------------

label arthur_scene:

    show arthur
    with dissolve

    show screen profile_card(
        "Arthur Wynn",
        "Board Member",
        "Corrupt, charismatic, politically connected",
        "Extremely Profitable",
        "- Secured billion-dollar deals\n- Bribed government officials\n- Close friend of your father"
    )

    arthur "Your father understood how the world really works."

    menu:

        "Work with Arthur":
            $ stock += 12
            $ corruption += 14

        "Expose Arthur":
            $ stock -= 12
            $ corruption -= 15

        "Sideline Arthur quietly":
            $ stock += 2
            $ corruption -= 5

    hide screen profile_card
    hide arthur

    jump naomi_scene

# ---------------------------------------------------------
# NAOMI SCENE
# ---------------------------------------------------------

label naomi_scene:

    show naomi
    with dissolve

    show screen profile_card(
        "Dr. Naomi Bell",
        "Lead Scientist",
        "Intelligent, ethical, exhausted",
        "Genius-level contributor",
        "- Developed life-saving medication\n- Opposed extreme pricing plans"
    )

    naomi "We can save millions of lives."
    naomi "But the board wants a 60,000 percent markup."

    menu:

        "Lower the medication price":
            $ stock -= 15
            $ corruption -= 20
            naomi "Thank you."

        "Approve the markup":
            $ stock += 20
            $ corruption += 20
            naomi "People will die."

        "Choose a compromise":
            $ stock += 5
            $ corruption += 2
            naomi "I hope that's enough."

    hide screen profile_card
    hide naomi

    jump dinner_stage

# =========================================================
# FINAL STAGE — DINNER
# =========================================================

label dinner_stage:

    scene bg dinner
    with fade

    stop music
    play music "audio/dinner.mp3"

    "The business elite gather around crystal glasses and whispered deals."

    if corruption >= 70:
        "Investors praise your ruthless efficiency."
        "Outside, protestors gather in the streets."

    elif corruption <= 30:
        "Some investors openly doubt your leadership."
        "Employees throughout the company speak highly of you."

    else:
        "The room feels uncertain."
        "Neither trusted nor feared completely."

    jump final_ending

# =========================================================
# ENDINGS
# =========================================================

label final_ending:

    scene black
    with fade

    "FINAL RESULTS"
    "Stock Value: [stock]"
    "Corruption Level: [corruption]"

    if corruption <= 25 and stock >= 30:

        "The company became smaller."
        "But workers stayed."
        "Patients lived."
        "For the first time, the empire became human."

    elif corruption >= 75 and stock >= 75:

        "The company dominated global markets."
        "Governments depended on your empire."
        "People cursed your name while buying your products."

    elif stock <= 20:

        "Investigations began."
        "Executives fled."
        "Your father's empire collapsed under its own corruption."

    else:

        "You learned power could never be clean."
        "Only cleaner."
        "The empire survived."
        "Changed."
        "Scarred."

    return
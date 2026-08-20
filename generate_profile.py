# generate_profile.py
# Generates the Pokemon-style trainer card and Current Party card
# displayed on my GitHub profile.

from pathlib import Path
from datetime import datetime
from html import escape


OUTPUT_DIR = Path("assets")

TRAINER_OUTPUT_FILE = OUTPUT_DIR / "trainer-card.svg"
PARTY_OUTPUT_FILE = OUTPUT_DIR / "party-card.svg"


# =========================================================
# TRAINER DATA
# =========================================================

TRAINER_NAME = "DYLAN"
TRAINER_CLASS = "SOFTWARE TRAINER"

LEVEL = 23

CURRENT_MISSION = "Building unnecessarily cool software"

MOVES = [
    ("PYTHON", "92"),
    ("TYPESCRIPT", "89"),
    ("REACT", "87"),
    ("AWS", "84"),
]

ABILITY = "SIDE PROJECT ADDICTION"


# =========================================================
# CURRENT PARTY
# =========================================================

PROJECTS = [
    {
        "name": "CHAIN REACTION",
        "short": "CR",
        "level": 45,
        "type": "AI / FINANCE",
        "status": "ACTIVE",
        "hp": 100,
    },
    {
        "name": "GESTURE AUTOMATION",
        "short": "GA",
        "level": 41,
        "type": "VISION / IOT",
        "status": "ACTIVE",
        "hp": 100,
    },
    {
        "name": "PORTFOLIO",
        "short": "WEB",
        "level": 40,
        "type": "FULL-STACK",
        "status": "DEPLOYED",
        "hp": 100,
    },
    {
        "name": "MOVIE PREDICTOR",
        "short": "ML",
        "level": 32,
        "type": "MACHINE LEARNING",
        "status": "COMPLETE",
        "hp": 100,
    },
]


# =========================================================
# TRAINER CARD
# =========================================================

def generate_trainer_svg():
    now = datetime.now()
    updated = now.strftime("%b %d, %Y")

    move_rows = ""

    start_y = 370

    for index, (move, power) in enumerate(MOVES):
        y = start_y + (index * 45)

        move_rows += f"""
        <text x="105" y="{y}" class="move">
            ▶ {escape(move)}
        </text>

        <text x="650" y="{y}" class="power">
            PWR {escape(power)}
        </text>
        """

    svg = f"""
<svg
    width="800"
    height="650"
    viewBox="0 0 800 650"
    xmlns="http://www.w3.org/2000/svg"
>

<style>

.background {{
    fill: #9bbc0f;
}}

.screen {{
    fill: #8bac0f;
    stroke: #0f380f;
    stroke-width: 10;
}}

.title {{
    font-family: monospace;
    font-size: 36px;
    font-weight: bold;
    fill: #0f380f;
}}

.subtitle {{
    font-family: monospace;
    font-size: 20px;
    fill: #0f380f;
}}

.text {{
    font-family: monospace;
    font-size: 18px;
    fill: #0f380f;
}}

.move {{
    font-family: monospace;
    font-size: 24px;
    font-weight: bold;
    fill: #0f380f;
}}

.power {{
    font-family: monospace;
    font-size: 18px;
    fill: #0f380f;
}}

.small {{
    font-family: monospace;
    font-size: 14px;
    fill: #0f380f;
}}

</style>


<!-- Game Boy background -->

<rect
    width="800"
    height="650"
    rx="25"
    class="background"
/>


<!-- Screen -->

<rect
    x="35"
    y="35"
    width="730"
    height="580"
    rx="10"
    class="screen"
/>


<!-- Encounter -->

<text
    x="400"
    y="90"
    text-anchor="middle"
    class="subtitle"
>
A WILD SOFTWARE ENGINEER APPEARED!
</text>


<!-- Trainer -->

<text
    x="100"
    y="155"
    class="title"
>
{escape(TRAINER_NAME)}
</text>


<text
    x="100"
    y="190"
    class="subtitle"
>
{escape(TRAINER_CLASS)}
</text>


<!-- Level -->

<text
    x="610"
    y="155"
    class="subtitle"
>
LV. {LEVEL}
</text>


<!-- HP label -->

<text
    x="100"
    y="235"
    class="text"
>
HP
</text>


<!-- HP bar background -->

<rect
    x="145"
    y="217"
    width="500"
    height="22"
    fill="#306230"
/>


<!-- HP bar -->

<rect
    x="150"
    y="222"
    width="490"
    height="12"
    fill="#0f380f"
/>


<text
    x="660"
    y="235"
    class="small"
>
100/100
</text>


<!-- Types -->

<text
    x="100"
    y="290"
    class="text"
>
TYPE:
</text>

<text
    x="180"
    y="290"
    class="text"
>
SOFTWARE / AI
</text>


<!-- Ability -->

<text
    x="100"
    y="330"
    class="text"
>
ABILITY: {escape(ABILITY)}
</text>


<!-- Divider -->

<line
    x1="100"
    y1="345"
    x2="700"
    y2="345"
    stroke="#0f380f"
    stroke-width="4"
/>


<!-- Moves -->

{move_rows}


<!-- Current mission -->

<line
    x1="100"
    y1="555"
    x2="700"
    y2="555"
    stroke="#0f380f"
    stroke-width="4"
/>

<text
    x="100"
    y="585"
    class="text"
>
CURRENT QUEST:
</text>

<text
    x="100"
    y="610"
    class="small"
>
{escape(CURRENT_MISSION)}
</text>


<!-- Updated -->

<text
    x="700"
    y="610"
    text-anchor="end"
    class="small"
>
UPDATED {escape(updated)}
</text>


</svg>
"""

    TRAINER_OUTPUT_FILE.write_text(svg, encoding="utf-8")

    print(f"Generated {TRAINER_OUTPUT_FILE}")


# =========================================================
# PARTY CARD HELPERS
# =========================================================

def pokeball(cx, cy):
    return f"""
    <circle cx="{cx}" cy="{cy}" r="31" fill="#f5f5f5" stroke="#17345e" stroke-width="5"/>

    <path
        d="M {cx - 29} {cy}
           A 29 29 0 0 1 {cx + 29} {cy}"
        fill="#ef5350"
    />

    <line
        x1="{cx - 29}"
        y1="{cy}"
        x2="{cx + 29}"
        y2="{cy}"
        stroke="#17345e"
        stroke-width="6"
    />

    <circle
        cx="{cx}"
        cy="{cy}"
        r="10"
        fill="#ffffff"
        stroke="#17345e"
        stroke-width="5"
    />
    """


def project_slot(project, x, y, selected=False):
    width = 355
    height = 150

    inner_x = x + 8
    inner_y = y + 8

    outline = "#f5c842" if selected else "#d9f1ff"
    outline_width = 7 if selected else 4

    hp_width = int(180 * (project["hp"] / 100))

    return f"""
    <!-- {escape(project["name"])} -->

    <rect
        x="{x}"
        y="{y}"
        width="{width}"
        height="{height}"
        rx="20"
        fill="#17345e"
        stroke="{outline}"
        stroke-width="{outline_width}"
    />

    <rect
        x="{inner_x}"
        y="{inner_y}"
        width="{width - 16}"
        height="{height - 16}"
        rx="15"
        fill="#4c9bc7"
        stroke="#79cbe8"
        stroke-width="3"
    />

    {pokeball(x + 57, y + 72)}

    <circle
        cx="{x + 57}"
        cy="{y + 72}"
        r="21"
        fill="#296a91"
    />

    <text
        x="{x + 57}"
        y="{y + 79}"
        text-anchor="middle"
        class="project-icon"
    >
        {escape(project["short"])}
    </text>

    <text
        x="{x + 105}"
        y="{y + 38}"
        class="project-name"
    >
        {escape(project["name"])}
    </text>

    <text
        x="{x + 105}"
        y="{y + 63}"
        class="project-type"
    >
        {escape(project["type"])}
    </text>

    <text
        x="{x + 275}"
        y="{y + 88}"
        class="level"
    >
        Lv.{project["level"]}
    </text>

    <text
        x="{x + 105}"
        y="{y + 97}"
        class="hp-label"
    >
        HP
    </text>

    <rect
        x="{x + 137}"
        y="{y + 84}"
        width="190"
        height="17"
        rx="8"
        fill="#23445e"
    />

    <rect
        x="{x + 142}"
        y="{y + 89}"
        width="{hp_width}"
        height="7"
        rx="4"
        fill="#62e66c"
    />

    <text
        x="{x + 105}"
        y="{y + 128}"
        class="status"
    >
        {escape(project["status"])}
    </text>

    <text
        x="{x + 327}"
        y="{y + 128}"
        text-anchor="end"
        class="hp-number"
    >
        {project["hp"]}/{project["hp"]}
    </text>
    """


def empty_slot(x, y):
    return f"""
    <rect
        x="{x}"
        y="{y}"
        width="355"
        height="150"
        rx="20"
        fill="#17345e"
        stroke="#597c9a"
        stroke-width="4"
    />

    <rect
        x="{x + 8}"
        y="{y + 8}"
        width="339"
        height="134"
        rx="15"
        fill="#305f80"
        stroke="#477b9d"
        stroke-width="3"
    />

    {pokeball(x + 57, y + 75)}

    <text
        x="{x + 110}"
        y="{y + 70}"
        class="empty-title"
    >
        EMPTY SLOT
    </text>

    <text
        x="{x + 110}"
        y="{y + 100}"
        class="empty-text"
    >
        A new project may appear...
    </text>
    """


# =========================================================
# PARTY CARD
# =========================================================

def generate_party_svg():

    party = PROJECTS[:6]

    while len(party) < 6:
        party.append(None)

    positions = [
        (35, 85),
        (410, 85),
        (35, 250),
        (410, 250),
        (35, 415),
        (410, 415),
    ]

    slots = ""

    for index, project in enumerate(party):
        x, y = positions[index]

        if project:
            slots += project_slot(
                project,
                x,
                y,
                selected=index == 0,
            )
        else:
            slots += empty_slot(x, y)

    svg = f"""
<svg
    width="800"
    height="620"
    viewBox="0 0 800 620"
    xmlns="http://www.w3.org/2000/svg"
>

<style>

text {{
    font-family: "Courier New", monospace;
}}

.header {{
    font-size: 25px;
    font-weight: bold;
    fill: #17345e;
}}

.project-name {{
    font-size: 18px;
    font-weight: bold;
    fill: white;
}}

.project-type {{
    font-size: 12px;
    font-weight: bold;
    fill: #e8f7ff;
}}

.project-icon {{
    font-size: 14px;
    font-weight: bold;
    fill: white;
}}

.level {{
    font-size: 14px;
    font-weight: bold;
    fill: white;
}}

.hp-label {{
    font-size: 12px;
    font-weight: bold;
    fill: #ffe971;
}}

.status {{
    font-size: 12px;
    font-weight: bold;
    fill: white;
}}

.hp-number {{
    font-size: 12px;
    font-weight: bold;
    fill: white;
}}

.empty-title {{
    font-size: 19px;
    font-weight: bold;
    fill: #c0d6e4;
}}

.empty-text {{
    font-size: 11px;
    fill: #9db7c9;
}}

.footer {{
    font-size: 17px;
    font-weight: bold;
    fill: #17345e;
}}

</style>


<!-- Background -->

<rect
    width="800"
    height="620"
    rx="25"
    fill="#8aa878"
/>


<!-- top menu -->

<rect
    x="20"
    y="20"
    width="760"
    height="50"
    rx="12"
    fill="#dceaf3"
    stroke="#17345e"
    stroke-width="5"
/>

<text
    x="45"
    y="53"
    class="header"
>
CURRENT PARTY
</text>

<text
    x="745"
    y="53"
    text-anchor="end"
    class="header"
>
4 / 6
</text>


<!-- party slots -->

{slots}


<!-- bottom command bar -->

<rect
    x="35"
    y="575"
    width="570"
    height="35"
    rx="8"
    fill="#eef5f8"
    stroke="#17345e"
    stroke-width="4"
/>

<text
    x="55"
    y="599"
    class="footer"
>
Choose a project.
</text>


<rect
    x="620"
    y="570"
    width="145"
    height="42"
    rx="8"
    fill="#315cb5"
    stroke="#17345e"
    stroke-width="4"
/>

<text
    x="692"
    y="598"
    text-anchor="middle"
    font-family="monospace"
    font-size="18"
    font-weight="bold"
    fill="white"
>
CANCEL
</text>


</svg>
"""

    PARTY_OUTPUT_FILE.write_text(svg, encoding="utf-8")

    print(f"Generated {PARTY_OUTPUT_FILE}")


# =========================================================
# RUN
# =========================================================

def main():

    OUTPUT_DIR.mkdir(exist_ok=True)

    generate_trainer_svg()
    generate_party_svg()


if __name__ == "__main__":
    main()
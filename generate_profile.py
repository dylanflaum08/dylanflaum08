# generate_profile.py
# Generates the Pokemon-style trainer card displayed on my GitHub profile.

from pathlib import Path
from datetime import datetime


OUTPUT_DIR = Path("assets")
OUTPUT_FILE = OUTPUT_DIR / "trainer-card.svg"


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
# SVG
# =========================================================

def generate_svg():

    now = datetime.now()
    updated = now.strftime("%b %d, %Y")

    move_rows = ""

    start_y = 370

    for index, (move, power) in enumerate(MOVES):

        y = start_y + (index * 45)

        move_rows += f"""
        <text x="105" y="{y}" class="move">
            ▶ {move}
        </text>

        <text x="650" y="{y}" class="power">
            PWR {power}
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
{TRAINER_NAME}
</text>


<text
    x="100"
    y="190"
    class="subtitle"
>
{TRAINER_CLASS}
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
ABILITY: {ABILITY}
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
{CURRENT_MISSION}
</text>


<!-- Updated -->

<text
    x="700"
    y="610"
    text-anchor="end"
    class="small"
>
UPDATED {updated}
</text>


</svg>
"""

    OUTPUT_DIR.mkdir(exist_ok=True)

    OUTPUT_FILE.write_text(svg, encoding="utf-8")

    print(f"Generated {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_svg()
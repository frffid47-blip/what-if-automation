import random
from pathlib import Path
from datetime import datetime

topics = Path("topics.txt").read_text(
    encoding="utf-8"
).splitlines()

topics = [t.strip() for t in topics if t.strip()]

if not topics:
    raise SystemExit("No topics found in topics.txt")

topic = random.choice(topics)

script = f"""
WHAT IF: {topic}

HOOK:
Socho agar aaj aisa ho jaye, to duniya kitni badal jayegi!

SCENE 1:
Sabse pehle, is situation ka asar hamari daily life par padega.

SCENE 2:
Scientists ko samajhna hoga ki is badlav ka nature aur humans par kya impact hoga.

SCENE 3:
Asli result is baat par depend karega ki ye situation kaise hoti hai.

ENDING:
Tumhare hisaab se aisa hone par duniya kaisi hogi?
Comment mein apna opinion batao!
"""

Path("output").mkdir(exist_ok=True)

filename = datetime.now().strftime("%Y%m%d_%H%M%S")
output = Path("output") / f"script_{filename}.txt"

output.write_text(script.strip(), encoding="utf-8")

print(f"Topic: {topic}")
print(f"Script saved to: {output}")

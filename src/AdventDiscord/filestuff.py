import shutil 
import tempfile
import re
import requests
import config
from pathlib import Path
from utils import colored
from bs4 import BeautifulSoup
from markdownify import markdownify


"""
    para: year, day
    file_to_send = Path(f"{year}-{day}.zip")

    file = discord.File(file_to_send)
    await target_channel_or_user.send(file=file, content="Message to be sent")
"""

# Creating the ZIP file 
# zip_from = Path("2022")

GOTS = Path("puzzle files")
if not GOTS.exists():
    GOTS.mkdir()

def get(year, day):
    zip_to = f"AoC {year}-{day}"

    if (GOTS / zip_to).exists():
        _err = f"{zip_to} already exists"
        return colored(_err, 'red')
    
    with tempfile.TemporaryDirectory() as tmpdirname:
        temp_dir = Path(tmpdirname)
        zip_from = temp_dir / str(year)
        target_dir = temp_dir / str(year) / str(day)
        target_dir.mkdir(parents=True, exist_ok=True)

        conf = config.get_config()
        r = requests.get(f'https://adventofcode.com/{year}/day/{int(day)}',
                        cookies={'session': conf['session_cookie']})
        if r.status_code == 404:
            if 'before it unlocks!' in r.text:
                return colored(f'This puzzle has not unlocked yet.\nIt will unlock on Dec {day} {year} at midnight EST (UTC-5).', 'red')
            else:
                return colored(f'The server returned error 404 for url:  "https://adventofcode.com/{year}/day/{int(day)}/"', 'red')

        # os.makedirs(f'{year}/{day}/')

        soup = BeautifulSoup(r.text, 'html.parser')
        part1_html = soup.find('article', class_='day-desc').decode_contents()

        # remove hyphens from title sections, makes markdown look nicer
        part1_html = re.sub('--- (.*) ---', r'\1', part1_html)

        # also makes markdown look better
        part1_html = part1_html.replace('\n\n', '\n')

        files = {
            "prompt.md" : target_dir / "prompt.md",
            "input.txt" : target_dir / "input.txt",
            "solution.py" : target_dir / "solution.py",
            "example_input.txt" : target_dir / "example_input.txt",
        }

        files["prompt.md"].write_text(markdownify(part1_html))
        print(f'Downloaded prompt to {year}/{day}/prompt.md')

        r = requests.get(f'https://adventofcode.com/{year}/day/{int(day)}/input',
                        cookies={'session': conf['session_cookie']})

        files["input.txt"].write_text(r.text)
        print(f'Downloaded input to {year}/{day}/input.txt')

        files["example_input.txt"].write_text('')
        print(f'Created {year}/{day}/example_input.txt')

        solution_text = [
            f'## advent of code {year} day {day}', 
            f'## https://adventofcode.com/{year}',
            '## coder {name} {email}\n',
            'def parse_input(lines):\n\tpass\n',
            'def part1(data):\n\tpass\n',
            'def part2(data):\n\tpass',
            ]

        files["solution.py"].write_text('\n'.join(solution_text))
        print(f'Created {year}/{day}/solution.py')
        
        return create_zip(zip_to, zip_from)



def create_zip(zip_to, zip_from):
    zip_file = GOTS / zip_to
    zip_from = Path(f"{zip_from}")
    archived = shutil.make_archive(zip_file, 'zip', zip_from)
    
    if Path(f"{zip_file}.zip").exists():
        return f"{archived} created successfully"

    raise FileNotFoundError

if __name__ == "__main__":
    print(get(2022, 21))
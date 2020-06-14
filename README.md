# TimeZi
---
A calendar command line based app written in python.

---
 ## Installation (Windows)


1. Download the release to be installed.
2. Unzip the TimeZi folder to the place where you want to install the program.
3. Add the installation folder to PATH.

## Requirements

- Docopt
- JSON


---
## How to use?

- Add an appointment:
> TimeZi  add  \<name>  \<weekday>  \<hour>

- Delete an appointment:
> TimeZi  delete  \<name>

- Get all appointments for a specific weekday:
> TimeZi  get  \<weekday>

- Get all appointments for today:
> TimeZi  today

- Get the next appointment of today:
> TimeZi  next

- Reset the data file:
> TimeZi  reset

---
## Planned features:

- Support for exceptions (appointments for a specific day);
- Support for color;
- Support for a config file:
    - change the appointment's display format;
    - change the data file's location;

---
## How to build:

Use pyinstaller module to build:
- Go to the project's folder on a command line;
- Type:
>pyinstaller TimeZi.py
- The compiled program will be into:
>.\dist\TimeZi\
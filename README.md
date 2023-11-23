# Python File Manipulation CLI Tool

This Python Command Line Interface (CLI) tool provides functionalities for file manipulation and directory navigation, similar to Unix-like command-line tools. It includes a variety of commands for handling files and directories and logs each command's usage for easy tracking and debugging.

## Features

- List directory contents (`ls`)
- Change the current working directory (`cd`)
- Create a new directory (`mkdir`)
- Remove an empty directory (`rmdir`)
- Remove a file (`rm`)
- Copy files or directories (`cp`)
- Move/rename files or directories (`mv`)
- Search for files or directories (`find`)
- Display the contents of a file (`cat`)
- Advanced logging of command usage

## Setup

1. Ensure you have Python 3.8 or higher installed on your system.
2. Download the `file_cli.py` script to your local machine.

## Usage

Run the script from the command line, followed by the command and its arguments. Here are some examples:

```bash
python file_cli.py ls [path]
python file_cli.py cd [path]
python file_cli.py mkdir [path]
python file_cli.py rmdir [path]
python file_cli.py rm [file]
python file_cli.py cp [source] [destination]
python file_cli.py mv [source] [destination]
python file_cli.py find [path] [pattern]
python file_cli.py cat [file]
```

Replace [path], [file], [source], [destination], and [pattern] with your specific inputs.

## Logs

The tool logs each command's execution, including the time, command, arguments, outcome, and any errors. Logs are stored in a file named commands.log in the same directory as the script.

## GitHub Repo

<https://github.com/forrest482/Filoger_Python_Basic_Final_Project>

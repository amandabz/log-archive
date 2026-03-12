# Log Archive Tool

A simple **Python command-line tool** to compress and archive logs from a specified directory into timestamped `.tar.gz` files.

## 🗂 Project Structure

```
log_archive/
│
├── log_archive.py       # Main script to compress and archive logs
├── logs/                # Sample log files for testing
│   ├── log1.txt
│   ├── log2.txt
│   └── log3.txt
├── README.md            # Project documentation
└── .gitignore           # Files and directories to ignore in Git
```

> **Note:** The `logs/` folder is only provided as an example for testing. You can use any folder with your own log files.

## ⚙️ Features

- Compresses a specified log directory into a `.tar.gz` archive.
- Automatically names archives with the current date and time (timestamped).
- Works with a folder containing multiple logs.
- Provides a clear message if no logs are found.
- Easy to run from the command line.

Example archive file name:
```bash
logs_archive_20240816_100648.tar.gz
```

## 💻 Usage
1. Open a terminal and navigate to the project folder.
2. Run the script:
```bash
python3 log_archive.py
```

- By default, the script compresses the files inside the `logs/` folder (example folder for testing).
- You can replace it with any folder containing your log files.

Currently, the script uses the `logs/` folder in the project directory.
It will create a compressed archive with all files inside that folder.

### Example Output
If the `logs/` folder exists:
```
20240816_100648
logs_archive_20240816_100648.tar.gz was successfully created.
```

If the folder does not exist:
```
No logs folder found. No archive was created.
```

## 🛠 How It Works
1. The script checks the `logs/` folder (or a directory you specify in `files`).
2. Gets the current date and time to create a timestamp.
3. Compresses the logs into a `.tar.gz` archive using Python's `tarfile` module.
4. Saves the archive in the project directory with a timestamped filename.

## 📝 Future Improvements
- Allow passing the log directory as a command-line argument dynamically.
- Move archives to a separate `archives/` folder automatically.
- Add support for remote backup or emailing the archive.
- Schedule automatic archiving with cron jobs on Unix-based systems.
- Add logging for error handling and archive history.

## 📘 Project Information
This project is based on the [Log Archive Tool Project](https://roadmap.sh/projects/log-archive-tool) from **roadmap.sh**.

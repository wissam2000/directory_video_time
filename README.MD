# Video Length Calculator

This script calculates the total playtime of all MP4 files found in a specified directory and its subdirectories, outputting the total duration in hours, minutes, and seconds.

## Prerequisites

Ensure Python is installed on your system. You can download Python from [python.org](https://www.python.org).

## Environment Setup

### Clone or Download the Script

If the script is part of a repository, clone it to your local machine using the following command:

```git clone git@github.com:wissam2000/directory_video_time.git```

Alternatively, ensure you have the script file `video_length_calculator.py` saved in a directory on your computer.

### Prepare the Environment

1. Navigate to the directory containing the script.
2. Open a terminal in this directory.
3. Install the required dependencies:
```pip install -r requirements.txt```


## Running the Script

### Execute the Script

Run the script by entering the following command in the terminal:

```python video_length_calculator.py```


When prompted, enter the path to the directory you want to analyze for MP4 files.

### View the Results

After processing, the script will output the total playtime of all MP4 files found in the specified directory and subdirectories, formatted in hours, minutes, and seconds.

## Notes

This script depends on the `moviepy` and `tqdm` libraries as specified in the `requirements.txt`. If you encounter any issues with library versions, try updating the libraries using:

```pip install --upgrade moviepy tqdm```

This setup should help you get the Python script running smoothly on your local environment. Follow the steps carefully to ensure all dependencies are correctly installed.


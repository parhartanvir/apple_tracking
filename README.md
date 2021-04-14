# Apple Tracking
This repository has 4 files.
1. `sort_tracker_moving.py` is for tracking apples across a moving camera and removing boxes for apples not in the current frame.
2. `sort_tracker_moving_all.py` is for tracking apples across a moving camera and keeping undetected apples in the frame.
3. `sort_tracker_stationary.py` is for tracking apples across a static camera and blower agitated canopy and removing boxes for apples not in the current frame.
4. `sort_tracker_stationary_all.py` is for tracking apples across a static camera and blower agitated canopy and keeping undetected apples in the frame(colored in white).

# Requirements
1.[filterpy](https://pypi.org/project/filterpy/)
2.[matplotlib](https://pypi.org/project/matplotlib/)

# Sample Usage
`python3.6 sort_tracker_stationary.py` 

Should show the following result.

[![Stationary camera apple tracking](https://img.youtube.com/vi/a4F400MYAVY/0.jpg)](https://www.youtube.com/watch?v=a4F400MYAVY)


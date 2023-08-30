# Consciousness Detection System

The Consciousness Detection System is an advanced Python program that utilizes computer vision techniques and audio alerts to monitor a person's level of consciousness through a webcam feed. By analyzing facial landmarks and eye behaviors, this system can determine if an individual is awake and sends relevant data to a connected database while alerting medical personnel with an alarm.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Data Storage and Retrieval](#data-storage-and-retrieval)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Consciousness Detection System is a cutting-edge solution that showcases the capabilities of computer vision, real-time monitoring, and data storage. It is designed to enhance medical monitoring and response by providing an automated method to detect and record a person's awakening.

## Features

The Consciousness Detection System offers a plethora of features that contribute to its effectiveness:

### Eye Aspect Ratio Calculation

The program calculates the eye aspect ratio (EAR) using the formula:

EAR = (A + B) / (2.0 * C)

This formula is central to evaluating the state of the person's eyes and plays a pivotal role in detecting consciousness.

### Facial Landmarks Detection

The system leverages the `dlib` library's pre-trained facial landmarks predictor. By analyzing the positions of various facial landmarks, such as eyes and eyebrows, the program accurately determines if the person's eyes are open or closed. This detection is crucial for assessing consciousness levels.

Additionally, the program utilizes the `haarcascade` classifier from the OpenCV library to detect faces in the webcam feed. This initial face detection step sets the stage for subsequent facial landmarks analysis.

### Real-time Monitoring

The system seamlessly captures video frames from a webcam feed and processes them in real-time. By analyzing the position of facial landmarks and assessing eye behaviors, it can accurately determine whether the person's eyes are open or closed.

### Database Integration

Upon detecting that the person is awake, the system sends pertinent data to a connected database. This data includes a timestamp that records the exact moment when the person regained consciousness. This feature provides valuable insights for medical professionals who are monitoring the person's condition.

### Medical Personnel Alert

In addition to sending data to the database, the system employs audio alerts to notify medical personnel of the consciousness detection. This immediate and audible notification ensures that medical professionals are promptly informed about any changes in the person's state.

## Installation

To set up the Consciousness Detection System on your system, follow these steps:

1. Ensure that you have Python 3.x installed.
2. Install required libraries using the command: `pip install scipy imutils dlib opencv-python pygame firebase-admin`.

## Usage

To utilize the system effectively, perform the following actions:

1. Place the audio file "sound.wav" in the same directory as the program.
2. Run the program using a Python interpreter: `python code.py`.

## How It Works

The Consciousness Detection System employs a multi-step process to detect and monitor a person's consciousness:

1. **Eye Aspect Ratio Calculation**: The EAR is computed by measuring distances between facial landmarks associated with the eyes. This ratio forms the basis for determining eye openness.

2. **Real-time Monitoring**: The system captures video frames from a webcam feed and analyzes facial landmarks to calculate the eye aspect ratio. This information is used to evaluate the state of the person's eyes.

3. **Database Integration**: When the person's eyes open and consciousness is detected, the system sends data, including a timestamp, to a connected database. This data aids medical personnel in tracking consciousness patterns.

4. **Medical Personnel Alert**: Simultaneously, an audio alarm is triggered to alert medical professionals about the change in consciousness. This immediate notification enhances the responsiveness of medical care.

## Data Storage and Retrieval

The Consciousness Detection System utilizes the Firebase Realtime Database for data storage and retrieval. It sends consciousness detection records to the database, allowing medical personnel to access and analyze this data for patient monitoring.

## Requirements

- Python 3.x
- Libraries: scipy, imutils, dlib, opencv-python, pygame, firebase-admin

## Contributing

Contributions to the Consciousness Detection System are welcomed! If you wish to enhance the system's features, improve its performance, or fix any issues, feel free to submit a pull request.

## License

This program is open-source and distributed under the MIT License.

Feel free to customize this README to provide comprehensive information about the Consciousness Detection System. The goal is to offer clear instructions and insights to users and potential contributors.

# 202409-muscle-visualizer-demo

This Python-based application visualizes muscle usage based on workout data, providing insights into muscle group engagement and exercise effectiveness. It leverages various libraries for image processing, data manipulation, and visualization to offer a comprehensive tool for fitness enthusiasts and trainers.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Features](#features)
4. [Functions](#functions)
5. [Data Collection](#data-collection)
6. [Visualization](#visualization)
7. [Exercise Recommendation](#exercise-recommendation)

## Installation

Ensure you have the required libraries installed. You can install them using pip:

```bash
pip install pillow matplotlib seaborn pandas numpy etc.
```

## Usage

1. **Loading the Blank Muscle Diagram**: Start by loading a blank muscle diagram for visualization purposes.
2. **Data Collection**: Use the `data_gather.py` script to fetch and prepare workout data from Google Sheets.
3. **Data Manipulation**: Clean and preprocess the data to calculate muscle usage and group intensity.
4. **Visualization**: Generate heat maps to visualize muscle usage and analyze workout effectiveness.

## Features

- **Visual Dictionaries**: Maintain dictionaries for exercises, muscles, and color codes used in visualizations.
- **Data Collection**: Automate data fetching and processing from Google Sheets.
- **Muscle Usage Calculation**: Compute muscle usage based on workout data with customizable decay factors.
- **Visualization**: Create heat maps to visualize muscle intensity on muscle diagrams.
- **Exercise Similarity**: Assess exercise similarity to find alternatives targeting similar muscles.
- **Exercise Recommendations**: Generate personalized exercise recommendations focusing on target muscle groups and workout variety.

## Functions

### Data Manipulation

- **`calculate_muscle_usage`**: Computes muscle usage intensities with configurable decay.
- **`calculate_muscle_group_usage`**: Analyzes major muscle group usage from workout sessions.

### Visualization

- **`generate_title`**: Creates dynamic titles for heat maps based on selected parameters.
- **`visualize_muscle_usage`**: Generates heat maps visualizing muscle intensity on diagrams.

### Reporting

- **`print_workout_details`**: Provides detailed reports for individual workouts.
- **`print_recent_workouts`**: Summarizes recent workouts, highlighting intensity and muscle group distribution.

### Exercise Analysis

- **`calculate_similarity`**: Measures similarity between exercises based on muscle intensity.
- **`generate_similarity_dict`**: Maps exercises to similar ones for easier comparison.

### Exercise Recommendation

- **`calculate_muscle_group_percentage`**: Computes exercise contributions to muscle groups.
- **`calculate_primary_group`**: Identifies the primary muscle group targeted by an exercise.
- **`calculate_target_alignment_score`**: Evaluates how well exercises align with target muscle groups.
- **`recommend_exercises`**: Provides personalized exercise recommendations based on various factors.

## Data Collection

The `data_gather.py` script handles data collection from Google Sheets. Ensure proper API credentials and access permissions are set up.

## Visualization

The application uses the PIL and Matplotlib libraries to manipulate and display muscle diagrams. Color maps and heat maps are generated to reflect muscle usage intensity.

## Exercise Recommendation

The recommendation system considers factors such as exercise effectiveness, recent history, and similarity to ensure balanced and effective workout routines.

Feel free to adjust any sections to better match your project's specifics!

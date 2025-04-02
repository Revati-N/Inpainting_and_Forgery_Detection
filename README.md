# Project Title

## Overview
The goal is to design and implement a Deep Learning framework using python for image inpainting and forgery detection. The inpainting model will analyze and replicate surrounding pixels to create realistic image modifications, maintaining a natural appearance. The forgery detection model will identify and localize manipulated areas, ensuring image authenticity. Together, these models enhance digital image reliability for both manipulation and verification.

The model files required for execution were not uploaded to GitHub due to size constraints. Instead, they are hosted on Google Drive.

## Prerequisites
Before running the UI, please follow these steps:

1. **Download the Model File:**
   - Open the following Google Drive link: <a href = "https://drive.google.com/drive/folders/1xo4o9mLZvuaqb6WTnEeLHEWVQoN5iz6t?usp=sharing"> Link </a>
   - Navigate to the `6000` folder.
   - Download the `classifier.h5` file and place it in the appropriate directory within the project.

## Running the UI
Once the model file is downloaded and placed correctly, run the following command to start the UI:

```bash
python -m streamlit run app.py
```


import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the model
model = tf.keras.models.load_model("Models/50/classifier_model.h5")

def preprocess_image(image):
    image = image.resize((128, 128))  # Resize to match model input shape
    image = np.array(image) / 255.0  # Normalize pixel values
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

def classify_image(image):
    processed_image = preprocess_image(image)
    prediction = model.predict(processed_image)[0][0]
    # Convert from float32 to Python float
    prediction = float(prediction)
    # Return both the classification and the raw prediction value
    classification = "Forged" if prediction >= 0.6 else "Original"
    return classification, prediction

# Initialize session state variables if they don't exist
if 'image' not in st.session_state:
    st.session_state.image = None
if 'results_shown' not in st.session_state:
    st.session_state.results_shown = False
if 'result' not in st.session_state:
    st.session_state.result = None
if 'confidence' not in st.session_state:
    st.session_state.confidence = None

# Function to reset for checking another image
def check_another_image():
    st.session_state.image = None
    st.session_state.results_shown = False
    st.session_state.result = None
    st.session_state.confidence = None

# Streamlit UI
st.title("Forgery Detection System")

# Create a two-column layout
if st.session_state.image is not None:
    col1, col2 = st.columns([3, 2])
    
    with col1:
        # Display image in the left column
        st.image(st.session_state.image, caption="Uploaded Image", use_container_width=True)
        
        # Only show classify button if results aren't shown yet
        if not st.session_state.results_shown:
            if st.button("Classify Image"):
                # Run classification and store results in session state
                result, confidence = classify_image(st.session_state.image)
                st.session_state.result = result
                st.session_state.confidence = confidence
                st.session_state.results_shown = True
                st.rerun()  # Rerun to refresh the UI
    
    with col2:
        # Display results in the right column if they exist
        if st.session_state.results_shown and st.session_state.result is not None:
            st.write("## Analysis Results")
            
            # Display the result
            st.write(f"### Result: {st.session_state.result}")
            
            # Show the forgery confidence percentage if forged
            if st.session_state.result == "Forged":
                forgery_percentage = st.session_state.confidence * 100
                st.write(f"### Forgery Confidence: {forgery_percentage:.2f}%")
                
                # Add a visual indicator of the confidence level
                st.progress(st.session_state.confidence)
                
                if forgery_percentage > 90:
                    st.error("High probability of forgery detected!")
                elif forgery_percentage > 75:
                    st.warning("Moderate to high probability of forgery detected.")
                else:
                    st.info("Possible forgery detected. Further verification recommended.")
            else:
                authenticity_percentage = (1 - st.session_state.confidence) * 100
                st.write(f"### Original Confidence: {authenticity_percentage:.2f}%")
                st.progress(1 - st.session_state.confidence)
            
            # Show button to check another image
            if st.button("Check Another Image"):
                check_another_image()
                st.rerun()
else:
    # Image upload section - only show if no image is currently loaded
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        st.session_state.image = Image.open(uploaded_file).convert("RGB")
        st.rerun()
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf
import logging
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

MODEL_PATH = os.getenv('MODEL_PATH', r"C:\Users\user\Desktop\Paddy Disease Classification\models\paddy1.h5")
CLASS_NAMES = ["bacterial_leaf_blight", "bacterial_leaf_streak", "bacterial_panicle_blight", "blast", "brown_spot", "dead_heart", "downy_mildew", "hispa", "normal", "tungro"]

MODEL = tf.keras.models.load_model(MODEL_PATH)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
async def root():
    """
    Root endpoint providing basic information about the API.
    """
    return {"message": "Welcome to the Paddy Disease Classification API. Use /ping to check status and /predict to classify images."}

@app.get("/ping")
async def ping():
    """
    Endpoint to check if the server is running.
    """
    return {"message": "Hello, I am alive"}

def read_file_as_image(data) -> np.ndarray:
    """
    Converts uploaded file data into a numpy array.
    """
    try:
        image = np.array(Image.open(BytesIO(data)))
        return image
    except Exception as e:
        logger.error(f"Error reading image file: {e}")
        raise HTTPException(status_code=400, detail="Invalid image file")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    Endpoint to predict the class of an uploaded image.
    """
    try:
        image = read_file_as_image(await file.read())
        img_batch = np.expand_dims(image, 0)
        
        
        resized_images = [np.array(Image.fromarray(img).resize((224, 224))) for img in img_batch]
        resized_img_batch = np.array(resized_images)

    
        predictions = MODEL.predict(resized_img_batch)
        predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
        confidence = np.max(predictions[0])
        
        return {
            'class': predicted_class,
            'confidence': float(confidence)
        }
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        raise HTTPException(status_code=500, detail="Prediction failed")

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8080)

# Plant Disease AI

This project is an early attempt to integrate **AI with image scanning** to determine the health of plants. Using simple color analysis, the system examines leaf images and classifies them as **healthy** or **unhealthy**.  

### How It Works

- Images are scanned for dominant colors.  
- Current color mapping:  
  - **Green** → Healthy  
  - **Brown** → Disease / Pest  
  - **Yellow** → Disease / Pest  

> Future updates may include more advanced features, such as texture detection, spot recognition, and ML-based disease classification.

### Dataset

The project uses the **PlantVillage dataset** of leaf images.  
> The dataset is **not included** in this repo due to size — a symlink or local copy is required to run the code.

### Usage

1. Place your leaf images in the `dataset/` folder (or set up a symlink to the PlantVillage dataset).  
2. Run the color scanning script to classify each leaf as healthy or unhealthy.  
3. Results are returned in the terminal (or can later be displayed in a web app).  

### Future Improvements

- Train a **deep learning model** for more accurate disease detection.  
- Add a **Flask web app** for image uploads and real-time predictions.  
- Incorporate multiple features beyond color, such as **spots, texture, and shape**.  

---

This is a **work in progress** and aims to demonstrate the integration of basic AI concepts with plant image analysis.

Dataset can be downloaded at <url: "https://github.com/spMohanty/PlantVillage-Dataset">
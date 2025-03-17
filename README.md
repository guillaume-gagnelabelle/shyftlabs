# ‭Shyftlabs AI Engineer - Take Home Assignment‬

This repository was developed as part of the Shyftlabs AI Engineer Take-Home Assignment. It presents A Retrieval-Augmented Generation (RAG) application that allows users to upload PDF or HTML documents, index their contents, and ask natural language questions about them. The app incorporates both semantic search and keyword search, and streams answers from a language model (Llama) back to the user in real time.

*NOTE*: This project represents my first time developing a full-stack application around an AI model, including web server, frontend, document indexing, and retrieval-augmented generation. My background and expertise focuses more on developing novel algorithms and architectures for research purposes. I took this opportunity to step outside my comfort zone and learn practical engineering tools. I hope this project demonstrates that I’m a quick learner and excited to broaden my skill set beyond theoretical work into building AI systems.

## Execution

The following procedure was tested on Ubuntu 22.04 with Cuda 11.5 and Conda 4.14.0.

Firstly, download the Llama model and place the .gguf file (download here ```https://huggingface.co/TheBloke/zephyr-7B-beta-GGUF/blob/main/zephyr-7b-beta.Q4_0.gguf```) file in the ```model/``` folder.

Then, create and configure a new environment according to the ```requirements.txt``` file
```
conda create -n shyftlabs python=3.13.2
conda activate shyftlabs
pip install -r requirements.txt
```
Finally, run the app: 
```
uvicorn app.main:app --reload
```
and visualize the result in a web browse: ```http://127.0.0.1:8000/``` 

## Improvement and Limitations

This app presents multiple avenues for improvement.
1. **Inference Efficiency:**
   
   The current implementation is not optimized for GPU acceleration. As a result, inference time can be slow — often taking several minutes to generate a complete response.
2. **Text Segmentation:**
   
   A basic form of text segmentation was implemented, where the text is divided into segments of 32 arbitrary words. This approach was chosen due to limited computational resources and time constraints. More sophisticated semantic chunking could improve retrieval precision.
  
3. **Text Extraction:**
   
   Simple text extractors for ```pdf``` and ```html``` were utilzed (```pdfplumber``` and ```BeautifulSoup```). The text division is not perfect and may hinder the performance of the semantic and keyword searches.
4. **Scalability:**
   
   The application was developed on minimal hardware, which naturally limited its performance. With access to more robust infrastructure (e.g., GPUs), both speed and scalability could be significantly improved.

## Directory structure:
```
├── app/
│   ├── main.py     
│   ├── rag_engine.py    
│   ├── search_index.py 
│   ├── upload.py
│   ├── utils.py  
├── static/
│   └── index.html 
├── model/
│   └── <downloaded-model> 
├── requirements.txt
└── README.md
```

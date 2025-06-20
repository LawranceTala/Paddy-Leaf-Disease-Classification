# Paddy-Leaf-Disease-Classification

## Setup for Anaconda python package manager:

1. Install Anaconda ([Setup instructions](https://wiki.python.org/moin/BeginnersGuide))

2. Install Python packages

```
pip3 install -r training/requirements.txt
pip3 install -r api/requirements.txt
```

## Training the Model

1. Download the data from [kaggle](https://www.kaggle.com/arjuntejaswi/plant-village).
2. Run Jupyter Notebook in Visual Studio Code.
3. Open `training/notebook.ipynb` in Jupyter Notebook.
4. In cell #2, update the path to dataset.
5. Run all the Cells one by one.
6. Model generated will be saved with the version number in the `models` folder.
7. H5 models will be saved in the `models h5` folder.

## Running the API

### Using FastAPI

1. Get inside `api` folder
2. Run the FastAPI Server using uvicorn

```bash
uvicorn server:app --reload --host 0.0.0.0
```

3. Your API is now running at `0.0.0.0:8080`

## Setup for ReactJS

1. Install Nodejs ([Setup instructions](https://nodejs.org/en/download/package-manager/))
2. Install NPM ([Setup instructions](https://www.npmjs.com/get-npm))
3. Install dependencies
5. Change API url in `App.js`.
6. Change the css in `App.css`.

## Running the Frontend
1. Open frontend in Integrated Terminal
2. Run the frontend

```bash
npm run start
```

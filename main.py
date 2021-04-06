from sanic import Sanic, response as res
from sanic.exceptions import NotFound
from database import getAllPredictions, createPrediction
from xgboost_regression_model import predict, train_model
import os

app = Sanic(__name__)

# Endpoints for AI model
@app.post('/api/predict')
async def prediction(req):

    input = req.json
    pred_price = predict(input['TotRmsAbvGrd'], input['YearBuilt'], input['LandContour'], input['BsmtFinSF1'], input['GarageCars'], input['_1stFlrSF'], input['TotalBsmtSF'], input['_2ndFlrSF'], input['GrLivArea'], input['OverallQual'])

    return res.json(str(pred_price))


# Endpoints for database table predictions

@app.get('/rest/predictions')
async def get_predictions(req):
    return res.json(await getAllPredictions())
    

@app.post('/rest/predictions')
async def post_prediction(req):
    prediction =req.json
    
    prediction['Id'] = await createPrediction(prediction)
    return res.json(prediction)


# enable frontend to be served from root
app.static('/', './frontend/dist')

@app.exception(NotFound)
async def ignore_404s(request, exception):
    return await res.file('./frontend/dist/index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
    train_model()

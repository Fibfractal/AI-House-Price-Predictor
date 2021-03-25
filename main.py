from sanic import Sanic, response as res

app = Sanic(__name__)


# Endpoints for AI model



# Endpoints for database table predictions

@app.get('/rest/predictions')
async def get_predictions(req):
    from database import getAllPredictions
    return res.json(await getAllPredictions())

@app.post('/rest/predictions')
async def post_prediction(req):
    from database import createPrediction

    prediction =req.json

    prediction['id'] = await createPrediction(prediction)
    return res.json(prediction)



if __name__ == "__main__":
    app.run(port = 8000)
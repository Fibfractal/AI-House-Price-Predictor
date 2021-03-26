from databases import Database

db = Database('sqlite:house_price.db')

# Help-functions

async def get(query, values = {}):
    rows = await db.fetch_all(query = query, values = values)
    dicts = []
    for row in rows:
        dicts.append(dict(row))
    return dicts

async def run(query, values = {}):
    return await db.execute(query = query, values = values)


# Functions

async def getAllPredictions():
    query = 'SELECT * FROM predictions' 
    return await get(query)

async def createPrediction(prediction):
    query = 'INSERT INTO predictions (TotRmsAbvGrd, YearBuilt, LandContour, BsmtFinSF1, GarageCars, _1stFlrSF, TotBsmtSF, _2ndFlrSF, GrLivArea, OverallQual) VALUES (:TotRmsAbvGrd, :YearBuilt, :LandContour,: BsmtFinSF1, :GarageCars, :_1stFlrSF, :TotBsmtSF, :_2ndFlrSF, :GrLivArea, :OverallQual)'

    return await run(query, {
        "TotRmsAbvGrd":prediction['TotRamsAbvGrd'], 
        "YearBuilt":prediction['YearBuilt'],
        "LandContour":prediction['LandContour'],
        "BsmtFinSF1":prediction['BsmtFinSF1'], 
        "GarageCars":prediction['GarageCars'],
        "_1stFlrSF":prediction['_1stFlrSF'],
        "TotBsmtSF":prediction['TotBsmtSF'], 
        "_2ndFlrSF":prediction['_2ndFlrSF'],
        "GrLivArea":prediction['GrLivArea'],
        "OverallQual":prediction['OverallQual'], 
    })
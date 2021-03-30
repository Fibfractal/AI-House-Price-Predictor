import { createStore } from 'vuex'

const state = {
    prediction: 0,
    predictions: [],
}

const mutations = {
    setPrediction(state, prediction){
        state,prediction = prediction
    },
    setPredictions(state, predictionsList){
        state.predictions = predictionsList
    },
    appendPrediction(state, predictionToAppend){
        state.predictions.push(predictionToAppend) 
    }
}

const actions = {
    async initPredictions(store){
        let predictions = await fetch('/rest/predictions')
        predictions = await predictions.json()
        store.commit('setPredictions', predictions)
    }
}

export default createStore({state, mutations, actions})
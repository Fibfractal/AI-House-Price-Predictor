import { createStore } from 'vuex'

const state = {
    predictions: [],
}

const mutations = {
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
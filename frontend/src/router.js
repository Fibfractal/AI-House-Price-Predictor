import { createRouter, createWebHistory} from 'vue-router'
import Predict from './views/Predict.vue'
import Predictions from './views/Predictions.vue'
import About from './views/About.vue'

const routes = [
    
    {
        name: 'Predict',
        path: '/',
        component: Predict
    },
    {
        name: 'Predictions',
        path: '/predictions',
        component: Predictions
    },
    {
        name: 'About',
        path: '/about',
        component: About
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes
})


export default router
<template>
    <main class="container-fluid">
        <div class="row">
            <div class="col-12 col-md-4 p-4 data-input-col">
                
                <h3>Make a prediction</h3>

                <p class="directives">Fill out ALL the fields in the form below to predict a price of a house </p>


                <form @submit.prevent="predict" class="was-validated">

                    <ol>
                        <li>
                            <div class="form-group m-3">
                                <input v-model="grLivArea" type="number" min = 0 class="form-control" id="uname" placeholder="Enter the living area above ground in square feet" name="uname" required>
                                <div class="valid-feedback">Field is filled.</div>
                                <div class="invalid-feedback">Enter an integer.</div>
                            </div>
                        </li>
                        <li>
                            <div class="form-group m-3">
                                <input v-model="_1stFlrSF" type="number" min = 0 class="form-control" id="uname" placeholder="Enter the area of the first floor in square feet" name="uname" required>
                                <div class="valid-feedback">Field is filled.</div>
                                <div class="invalid-feedback">Enter an integer.</div>
                            </div>
                        </li>
                        <li>
                            <div class="form-group m-3">
                                <input v-model="_2ndFlrSF" type="number" min = 0 class="form-control" id="uname" placeholder="Enter the area of the second floor in square feet (enter 0 if you don't have)" name="uname" required>
                                <div class="valid-feedback">Field is filled.</div>
                                <div class="invalid-feedback">Enter an integer.</div>
                            </div>
                        </li>
                        <li>
                            <div class="form-group m-3">
                                <input v-model="totalBsmtSF" type="number" min = 0 class="form-control" id="uname" placeholder="Enter the total area of basement in square feet (enter 0 if you don't have)" name="uname" required>
                                <div class="valid-feedback">Field is filled.</div>
                                <div class="invalid-feedback">Enter an integer.</div>
                            </div>
                        </li>
                        <li>
                            <div class="form-group m-3">
                                <input v-model="bsmtFinSF1" type="number" min = 0 class="form-control" id="uname" placeholder="Enter the finished area of the basement in square feet (enter 0 if you don't have)" name="uname" required>
                                <div class="valid-feedback">Field is filled.</div>
                                <div class="invalid-feedback">Enter an integer.</div>
                            </div> 
                        </li>

                        <li>
                            <div class="form-group m-3">
                                <input v-model="totRmsAbvGrd" type="number" min = 0 class="form-control" id="uname" placeholder="Enter the total number of rooms above ground, does not include bathrooms" name="uname" required>
                                <div class="valid-feedback">Field is filled.</div>
                                <div class="invalid-feedback">Enter an integer.</div>
                            </div>
                        </li>
                        <li>
                            <div class="form-group m-3">
                                <input v-model="garageCars" type="number" min = 0 class="form-control" id="uname" placeholder="Enter the capacity of the garage in number of cars (enter 0 if you don't have)" name="uname" required>
                                <div class="valid-feedback">Field is filled.</div>
                                <div class="invalid-feedback">Enter an integer.</div>
                            </div>
                        </li>
                        <li>
                            <div class="form-group m-3">
                                <input v-model="yearBuilt" type="number" min = "1000" :max="new Date().getFullYear()" class="form-control" id="uname" placeholder="Enter the year built (format: XXXX)" name="uname" required>

                                <div class="valid-feedback">Field is filled.</div>
                                <div class="invalid-feedback">Enter an integer.</div>
                            </div>
                        </li>
                        <li>
                            <div class="form-group m-3">
                                <select class="drop-down-own" v-model="overallQual" aria-label="Default select example" required>
                                    <option value="" disabled selected>- Select the overall material finish of the house -</option>
                                    <option value="10">Very Excellent</option>
                                    <option value="9">Excellent</option>
                                    <option value="8">Very Good</option>
                                    <option value="7">Good</option>
                                    <option value="6">Above Average</option>
                                    <option value="5">Average</option>
                                    <option value="4">Below Average</option>
                                    <option value="3">Fair</option>
                                    <option value="2">Poor</option>
                                    <option value="1">Very Poor</option>
                                </select>
                                <div class="valid-feedback">Field is filled.</div>
                                <div class="invalid-feedback">Please fill out this field.</div>               
                            </div>
                        </li>
                        <li>
                            <div class="form-group m-3">
                                <select class="drop-down-own" v-model="landContour" aria-label="Default select example" required>
                                    <option value="" disabled selected>- Select the flatness of the property -</option>
                                    <option value="Lvl">Near Flat/Level</option>
                                    <option value="Bnk">Banked - Quick and significant rise from street grade to building</option>
                                    <option value="HLS">Hillside - Significant slope from side to side</option>
                                    <option value="Low">Depression</option>
                                </select>
                                <div class="valid-feedback">Field is filled.</div>
                                <div class="invalid-feedback">Please fill out this field.</div>               
                            </div>
                        </li>
                    </ol>
 
                    <button type="submit" class="btn btn-secondary m-4">Submit</button>
                    <button type="reset" class="btn btn-secondary m-4" @click="emptyVariables">Reset</button>

                </form>                                
            </div>
                    <div class="col-12 col-md-8 p-4 display-prediction-col">

                        <div class="row">

                            <img src="src\assets\buildings1.jpg" class="img-fluid" alt="Responsive image">

                        </div>
                        <div class="row">

                            <div class="col-12 col-md-4 mt-5 p-4">
                                <div class="card" style="width: 100%; background-color: white;">
                                <div class="card-body">
                                    <h4 class="card-title">The predicted house price:</h4>
                                    <h6 class="card-subtitle mb-2 text-muted">Accuray of 88 %</h6>
                                    <h3 class="card-text mt-5">{{ this.price }}</h3>
                                </div>
                                </div>
                            </div>

                            <div class="col-12 col-md-8 mt-4">
                                <div class="row">

                                    <!-- canvas -->
                                    <div class="col-12 col-md-8 mt-5">
                                        <canvas id="myChart" height="200"></canvas>
                                    </div>

                                    <div class="col-12 col-md-4 mt-5"></div>
                                </div>
                            </div>
                        </div>
                    </div>

        </div>
    </main>
</template>

<script>

    import Chart from "chart.js";

    export default {

        data(){
            return {
                
                totRmsAbvGrd: '',
                yearBuilt: '',
                landContour: '',
                bsmtFinSF1: '',
                garageCars: '',
                _1stFlrSF: '',
                totalBsmtSF: '',
                _2ndFlrSF: '',
                grLivArea: '',
                overallQual: '',
                price: '',

                canvas: "",
                chart: "",
                previousEntry: ""
            }
        },

        mounted(){

            let canvas = document.getElementById("myChart")
            let ctx = canvas.getContext("2d")
            this.canvas = ctx
            this.createChart()
        },

        methods: {

            createChart(){

                this.chart = new Chart(this.canvas, {

                    type:'bar',
                    data: {

                        labels: [''],
                        datasets: [
                            {
                                label: 'Predicted price',
                                data: [0],
                                backgroundColor: ['blue'],
                                borderColor: ['black'],
                                borderWidth: 2
                            }  
                        ],
                    },
                    options: {
                        scales: {
                            yAxes: [{
                                ticks: {
                                    beginAtZero: true,
                                    callback: function(value, index, values) {
                                        return '$' +  value;
                                    }
                                }
                            }]
                        }
                    }
                })
            },
            async predict(){

                console.log("I am in input control")

                console.log(this.totRmsAbvGrd)
                console.log(this.yearBuilt)
                console.log(this.landContour)
                console.log(this.bsmtFinSF1)

                console.log(this.garageCars)
                console.log(this._1stFlrSF)
                console.log(this.totalBsmtSF)
                console.log(this._2ndFlrSF)

                console.log(this.grLivArea)
                console.log(this.overallQual)

                // Onehot encoded variable

                let toModel = [0,0,0,0]
                let _landContour = ["Low","HLS", "Bnk", "Lvl" ]

                for (var i = 0; i < _landContour.length; i++) {
                    if(this.landContour === _landContour[i] ){
                        toModel[i] = 1
                    }
                }

                console.log(toModel)

                // To trained model

                let dataToPredict = {

                    TotRmsAbvGrd: this.totRmsAbvGrd,
                    YearBuilt: this.yearBuilt,
                    LandContour: toModel,
                    BsmtFinSF1: this.bsmtFinSF1,

                    GarageCars: this.garageCars,
                    _1stFlrSF: this._1stFlrSF,
                    TotalBsmtSF: this.totalBsmtSF,
                    _2ndFlrSF: this._2ndFlrSF,

                    GrLivArea: this.grLivArea,
                    OverallQual:this.overallQual
                }      
                
                let prediction = 0

                try{
                    let res = await fetch('/api/predict', {
                        method: 'POST',
                        body: JSON.stringify(dataToPredict)
                    })
                    prediction = await res.json()
                }
                catch(err) {
                    this.price = "Something went wrong try again!"
                }


                console.log("Prediction:", prediction)
                console.log("dataToPredict:", dataToPredict)
                console.log("Previous entry before comparison", this.$store.state.previousEntry)
                console.log("Entry comparison before if",JSON.stringify(dataToPredict) === JSON.stringify(this.$store.state.previousEntry))
                

                this.displayPrediction(prediction)

                // Compare the current input to the previous input that led to storage in db
                let prevoiusVsCurrent = JSON.stringify(dataToPredict) === JSON.stringify(this.$store.state.previousEntry)


                if(prediction > 0 && !prevoiusVsCurrent){
                    
                    let dataToDatabase = {
                        TotRmsAbvGrd: this.totRmsAbvGrd,
                        YearBuilt: this.yearBuilt,
                        LandContour: this.landContour,
                        BsmtFinSF1: this.bsmtFinSF1,
                        GarageCars: this.garageCars,
                        _1stFlrSF: this._1stFlrSF,
                        TotalBsmtSF: this.totalBsmtSF,
                        _2ndFlrSF: this._2ndFlrSF,
                        GrLivArea: this.grLivArea,
                        OverallQual: this.overallQual,
                        PredictedPrice: prediction
                    }

                    try {
                        
                        let result = await fetch('/rest/predictions', {
                            method: 'POST',
                            body: JSON.stringify(dataToDatabase)
                        })
            
                        let dataFromDatabase = await result.json()
                        console.log("from database", dataFromDatabase)
            
                        // Add the new predict to store predictions
            
                        console.log("Before:",this.$store.state.predictions)
                        this.$store.commit('appendPrediction', dataFromDatabase)
                        console.log("After:", this.$store.state.predictions)

                        // Copy last entry in database, deep copy, for later comparison

                        let previousEntry = JSON.parse(JSON.stringify(dataToPredict));
                        this.$store.commit('setPreviousEntry', previousEntry)

                    }
                    catch(err) {
                        this.price = "Error, the prediction data wasn't added to the data base!"
                    }
                }
                else if (prevoiusVsCurrent){
                    this.price = this.price

                }
                else{
                    this.price = "Something went wrong try again!"
                }

            }, 
            displayPrediction(prediction){

                // Set global variable and store prediction
    
                let priceFormat =  new Intl.NumberFormat('en-US',
                    { style: 'currency', currency: 'USD',
                        minimumFractionDigits: 0 });
    
                this.price = priceFormat.format(parseInt(prediction))
    
                this.$store.commit('setPrediction', prediction)
                console.log("Prediction in store", this.$store.state.prediction)

                // Change the bar chart
                let chartDataset = this.chart.data.datasets[0]
                chartDataset.data[0] = prediction
                this.chart.update()            
            },
            emptyVariables(){
                
                this.totRmsAbvGrd = ''
                this.yearBuilt = ''
                this.landContour = ''
                this.bsmtFinSF1 = ''

                this.garageCars = ''
                this._1stFlrSF = ''
                this.totalBsmtSF = ''
                this._2ndFlrSF = ''

                this.grLivArea = ''
                this.overallQual = ''
            }
        }
    }
</script>

<style scope>
    .data-input-col {
        background-color: rgb(199, 206, 204);
    }
    .display-prediction-col {
        background-color: white;
    }

    .drop-down-own {
        width: 100%;
        height: 38px;
        border-radius: 4px;
    }

    .directives {
        float: left;
        margin-top: 30px;
        margin-bottom: 20px;
    }

    #myChart {
        /* width: 50%; */
        /* height:100px; */
    }

</style>
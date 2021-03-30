<template>
    <main class="container-fluid">
        <div class="row">
            <div class="col-12 col-md-4 p-4 data-input-col">
                
                <h3>Make a prediction</h3>

                <p>Fill out the form below to predict a price of a house</p>
                <p class="directives">All input fields must be filled, fields 1 - 8 can only take integers, 9 - 10 is drop down menus</p>


                <form @submit.prevent="predict" class="was-validated">

                    <ol>
                        <li>
                            <div class="form-group m-3">
                                <input v-model="grLivArea" type="number" class="form-control" id="uname" placeholder="Enter the living area above gound in square feet (integer)" name="uname" required>
                                <div class="valid-feedback">Field is filled.</div>
                                <div class="invalid-feedback">Please fill out this field.</div>
                            </div>
                        </li>
                        <li>
                            <div class="form-group m-3">
                                <input v-model="_1stFlrSF" type="number" class="form-control" id="uname" placeholder="Enter the area of the first floor in square feet (integer)" name="uname" required>
                                <div class="valid-feedback">Field is filled.</div>
                                <div class="invalid-feedback">Please fill out this field.</div>
                            </div>
                        </li>
                        <li>
                            <div class="form-group m-3">
                                <input v-model="_2ndFlrSF" type="number" class="form-control" id="uname" placeholder="Enter the area of the second floor in square feet (enter 0 if you don't have)" name="uname" required>
                                <div class="valid-feedback">Field is filled.</div>
                                <div class="invalid-feedback">Please fill out this field.</div>
                            </div>
                        </li>
                        <li>
                            <div class="form-group m-3">
                                <input v-model="totalBsmtSF" type="number" class="form-control" id="uname" placeholder="Enter the total area of basement in square feet (enter 0 if you don't have)" name="uname" required>
                                <div class="valid-feedback">Field is filled.</div>
                                <div class="invalid-feedback">Please fill out this field.</div>
                            </div>
                        </li>
                        <li>
                            <div class="form-group m-3">
                                <input v-model="bsmtFinSF1" type="number" class="form-control" id="uname" placeholder="Enter the finished area of the basement in square feet (enter 0 if you don't have)" name="uname" required>
                                <div class="valid-feedback">Field is filled.</div>
                                <div class="invalid-feedback">Please fill out this field.</div>
                            </div> 
                        </li>

                        <li>
                            <div class="form-group m-3">
                                <input v-model="totRmsAbvGrd" type="number" class="form-control" id="uname" placeholder="Enter the total number of rooms above ground, does not include bathrooms (integer)" name="uname" required>
                                <div class="valid-feedback">Field is filled.</div>
                                <div class="invalid-feedback">Please fill out this field.</div>
                            </div>
                        </li>
                        <li>
                            <div class="form-group m-3">
                                <input v-model="garageCars" type="number" class="form-control" id="uname" placeholder="Enter the capacity of the garage in number of cars (enter 0 if you don't have)" name="uname" required>
                                <div class="valid-feedback">Field is filled.</div>
                                <div class="invalid-feedback">Please fill out this field.</div>
                            </div>
                        </li>
                        <li>
                            <div class="form-group m-3">
                                <input v-model="yearBuilt" type="number" class="form-control" id="uname" placeholder="Enter the year built (integer)" name="uname" required>
                                <div class="valid-feedback">Field is filled.</div>
                                <div class="invalid-feedback">Please fill out this field.</div>
                            </div>
                        </li>
                        <li>
                            <div class="form-group m-3">
                                <select class="drop-down-own" v-model="overallQual" aria-label="Default select example" required>
                                    <option selected>- Select the overall material finish of the house -</option>
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
                                    <option selected>- Select the flatness of the property -</option>
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
                </form>                                
            </div>
                    <div class="col-12 col-md-8 p-4 display-prediction-col">

                        <div class="row">

                            <img src="src\assets\buildings1.jpg" class="img-fluid" alt="Responsive image">

                        </div>
                        <div class="row">

                            <div class="col-12 col-md-4 mt-4">
                                <div class="card" style="width: 100%; background-color: rgb(219, 211, 219)">
                                <div class="card-body">
                                    <h4 class="card-title">Prediction:</h4>
                                    <h6 class="card-subtitle mb-2 text-muted">Accuray of 88 %</h6>
                                    <h3 class="card-text mt-5">{{ this.price }}</h3>
                                </div>
                                </div>
                            </div>

                            <div class="col-12 col-md-8 mt-4">
                                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempore corporis itaque perferendis eos doloribus molestiae perspiciatis obcaecati, dolorem, ullam, expedita saepe fugit tempora officiis fugiat. Provident tempore vel suscipit ipsam nemo quasi fuga. Esse nam, hic alias aliquam quas culpa iusto at amet veritatis animi sapiente distinctio pariatur dolore maxime quasi tenetur facere molestias dolor rerum tempore reprehenderit? Saepe corrupti consequatur atque laudantium accusantium molestiae enim mollitia voluptate maiores, rem animi porro doloribus blanditiis, dolor praesentium, quos reprehenderit. Et obcaecati cum esse expedita nam, autem numquam natus totam ipsa voluptas corrupti beatae, necessitatibus vero nostrum earum veniam illo consequatur excepturi!</p>
                            </div>

                        </div>




                    </div>
                    


        </div>
    </main>
</template>

<script>
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
        }
    },
    methods: {

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
            
            console.log(dataToPredict)
            

            let res = await fetch('/api/predict', {
                method: 'POST',
                body: JSON.stringify(dataToPredict)
            })

            let prediction = await res.json()
            console.log("Prediction:", prediction)

            // Set global variable and store prediction

            this.price = prediction +" $"
            this.$store.commit('setPrediction', prediction)
            console.log("Prediction in store", this.$store.state.prediction)

            // To database

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
        }, 
    }
}
</script>

<style scope>
    .data-input-col {
        background-color: rgb(199, 206, 204);
    }
    .display-prediction-col {
        background-color: rgb(219, 211, 219);
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

</style>
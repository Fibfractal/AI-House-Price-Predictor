<template>
    <main class="container-fluid">
        <div class="row">
            <div class="col-12 col-md-4 p-4 data-input-col">

                <form @submit.prevent="predict" class="was-validated">

                    <div class="form-group">
                        <input v-model="grLivArea" type="text" class="form-control" id="uname" placeholder="Enter the living area above gound in square feet (integer)" name="uname" required>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                    </div>

                    <div class="form-group">
                        <input v-model="_1stFlrSF" type="text" class="form-control" id="uname" placeholder="Enter the area of the first floor in square feet (integer)" name="uname" required>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                    </div>

                    <div class="form-group">
                        <input v-model="_2ndFlrSF" type="text" class="form-control" id="uname" placeholder="Enter the area of the second floor in square feet (integer, if don't have enter 0)" name="uname" required>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                    </div>

                    <div class="form-group">
                        <input v-model="totalBsmtSF" type="text" class="form-control" id="uname" placeholder="Enter the total area of basement in square feet (integer, if don't have enter 0)" name="uname" required>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                    </div>

                    <div class="form-group">
                        <input v-model="bsmtFinSF1" type="text" class="form-control" id="uname" placeholder="Enter the finished area of the basement in square feet (integer, if don't have enter 0)" name="uname" required>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                    </div>   

                    <div class="form-group">
                        <input v-model="totRmsAbvGrd" type="text" class="form-control" id="uname" placeholder="Enter the total number of rooms above ground, does not include bathrooms (integer)" name="uname" required>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                    </div>

                    <div class="form-group">
                        <input v-model="garageCars" type="text" class="form-control" id="uname" placeholder="Enter the capacity of the garage in number of cars (integer, if don't have enter 0)" name="uname" required>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                    </div>

                    <div class="form-group">
                        <input v-model="yearBuilt" type="text" class="form-control" id="uname" placeholder="Enter the year built (integer)" name="uname" required>
                        <div class="valid-feedback">Valid.</div>
                        <div class="invalid-feedback">Please fill out this field.</div>
                    </div>

                    <!-- Made own css class, else it wasn't validated properly by form. Removed the bootstrap class="form-select" -->
                    <div class="form-group">
                        <select class="drop-down-own" v-model="overallQual" aria-label="Default select example">
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
                    </div>

                    <div class="form-group">
                        <select class="drop-down-own" v-model="landContour" aria-label="Default select example">
                            <option selected>- Select the flatness of the property -</option>
                            <option value="Lvl">Near Flat/Level</option>
                            <option value="Bnk">Banked - Quick and significant rise from street grade to building</option>
                            <option value="HLS">Hillside - Significant slope from side to side</option>
                            <option value="Low">Depression</option>
                        </select>               
                    </div>

                    <button type="submit" class="btn btn-secondary m-4">Submit</button>
                </form>                                
            </div>

            <div class="col-12 col-md-8 p-4 display-prediction-col">
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Facere unde repudiandae debitis impedit necessitatibus perspiciatis quaerat quibusdam sequi enim laudantium!</p>
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

            price: 0
        }
    },
    methods: {

        async predict(){

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

            this.price = parseFloat(prediction)
            this.$store.commit('setPrediction', parseFloat(prediction))

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
</style>
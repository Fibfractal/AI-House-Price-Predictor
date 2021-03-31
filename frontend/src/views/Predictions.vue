<template>
  <div class="container">
      <div class="row">
          <div class="col-4">
                <h4>Filter</h4>
                <p>To the right all previous predictions can be seen in a graph.</p>
                <p>If you choose a filter below the graph will project the predicted prices compared with the parameter of your choice. </p>
                <br>
                <p>All area measurement is in Square Feet.</p>

                <select @change="prepdata" class="form-select" aria-label="Default select example" v-model="value">
                    <option disabled value="">Choose filter parameter</option>
                    <option value="None">No filter</option>
                    <option value="TotRmsAbvGrd">Total rooms above ground</option>
                    <option value="YearBuilt">Year built</option>
                    <option value="BsmtFinSF1">Finished basement area</option>
                    <option value="GarageCars">Garage space</option>
                    <option value="_1stFlrSF">First floor area</option>
                    <option value="TotalBsmtSF">Total basement area</option>
                    <option value="_2ndFlrSF">Second floor area</option>
                    <option value="GrLivArea">Ground living area</option>
                    <option value="OverallQual">Overall Quality</option>
                </select>
          </div>
          <div class="col-8">
              <h4>Display of Previously Predicted Prices</h4>
              <canvas id="myChart"></canvas>
          </div>
      </div>
  </div>
</template>

<script>
import Chart from 'chart.js'

export default {
    data(){
        return {
            canvas:"",
            chart:"",
            value:"",
            array1:[],
            array:[],
        };
    },

    computed: {
        predictions() {
            return this.$store.state.predictions
        }
    },

    created(){
        this.$store.dispatch('initPredictions');
    },

    mounted(){
        let canvas = document.getElementById("myChart");
        let ctx = canvas.getContext("2d");
        this.canvas = ctx;
        this.createPriceArray();
        
    },

    methods: {

        createPriceArray(){
            // Create an array with only the predicted prices
            let array1 = []
            
            for (let i = 0; i < this.predictions.length; i++){
                let yvalue = this.predictions[i].PredictedPrice
                
                array1.push(yvalue); 
            }
            console.log(array1);
        this.create1DChart(array1)

        },

        create1DChart(array1) {
            this.chart = new Chart(this.canvas, {
                
                // Creates a line chart
                type: 'line',
                data: {
                    datasets: [{
                        label: 'Predicted Price',
                        data: array1,
                        backgroundColor: '#FFCAD4',
                        borderColor: '#F4ACB7',
                        borderWidth: 2,
                        showLine: true,
                        lineTension: 0,
                    }]
                },
                options: {
                    scales: {
                        display: true,
                        yAxes: [{
                            ticks: {
                                // Include a dollar sign in the ticks
                                callback: function(value, index, values) {
                                    return '$' +  value;
                                }
                            }
                        }]
                    }
                    
                }
            });
        },
    
        prepdata(){
            let choice = this.value;
            let array = []
            if (choice != 'None'){
                for (let i = 0; i < this.predictions.length; i++){
                    for (let key in this.predictions[i]) {
                        if (key == choice) {

                            let xvalue = this.predictions[i][key]
                            let yvalue = this.predictions[i].PredictedPrice
                            let datapoint = {
                                x: xvalue,
                                y: yvalue,
                            };
                            array.push(datapoint); 
                        }
                    }
                }; 
                this.create2DChart(array)
            }
            else{
                this.createPriceArray()
            } 
        },

        
        create2DChart(array) {
            this.chart = new Chart(this.canvas, {
                // The type of chart we want to create
                type: "scatter",

                // The data for our dataset
                data: {
                    datasets: [{
                        label: 'Predicted Price',
                        data: array,
                        backgroundColor: '#B7E4C7',
                        borderColor: '#95D5B2',
                        borderWidth: 2,
                        showLine: true,
                        lineTension: 0,
                    }]
                },
                options: {
                    scales: {
                        display: true,
                        yAxes: [{
                            ticks: {
                                // Include a dollar sign in the ticks
                                callback: function(value, index, values) {
                                    return '$' +  value;
                                }
                            }
                        }]
                    }
                }
            })

        },
    },
}


</script>

<style scoped>

</style>
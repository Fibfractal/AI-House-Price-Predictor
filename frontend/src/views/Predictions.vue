<template>
  <div class="container-fluid">
      <div class="row">
          <div class="col-12 col-md-4 p-4 data-input-col">
                
                <h4>Filter</h4>

                <div class="input-info">
                    <p>To the right all previous predictions can be seen in a graph.</p>
                    <p>If you choose a filter below, the graph will project the predicted prices compared with the parameter of your choice. </p>
                    <br>
                    <p>All area measurement is in Square Feet.</p>
                </div>

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

          <div class="col-12 col-md-8 p-4">

            <div class="row">

                    <div class="col-12 col-md-2"></div>
                    <div class="col-12 col-md-6 p-4">
                        <h4 class = "mb-5">Display of Previously Predicted Prices</h4>

                        <!-- Canvas -->
                        <canvas id="myChart" height="200"></canvas>
                    </div>
                    <div class="col-12 col-md-1"></div>
            </div>

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
            array:[],
            labarray:[],
        };
    },

    computed: {
        predictions() {
            return this.$store.state.predictions
        }
    },

    watch:{
        predictions: {
            immediate: true,
            handler(){
                this.createPriceArray();
            }   
        }

    },

    created(){
        this.$store.dispatch('initPredictions');
    },

    mounted(){
        let canvas = document.getElementById("myChart");
        let ctx = canvas.getContext("2d");
        this.canvas = ctx;
        //this.createPriceArray();
        
    },

    methods: {

        createPriceArray(){
            // Create an array with only the predicted prices
            let array = []
            let labarray = []
            
            for (let i = 0; i < this.predictions.length; i++){
                let yvalue = this.predictions[i].PredictedPrice
                
                // Array that contains Predicted Price for all predictions done
                array.push(yvalue); 
                
                // Labels array needed for Line Chart - counted from 1 up for number of predictions 
                labarray.push(i+1);
            }
        this.create1DChart(array,labarray)

        },

        create1DChart(array, labarray) {
            
            this.chart = new Chart(this.canvas, {
                
                // Creates a line chart
                type: 'line',
                data: {
                    labels: labarray,
                    datasets: [{
                        label: 'Predicted Price',
                        data: array,
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

                            // Array containing the x,y for all predictions done, 
                            //where x is the value for the chosen filter
                            array.push(datapoint); 
                        }
                    }
                }; 

                // Resorted the array so that the x-values comes in ascending order
                // This to insure the best possable result for the graph generated 
                array.sort((a,b) => {
                    return a.x - b.x;
                });

                this.create2DChart(array)
            }
            else{
                this.createPriceArray()
            } 
        },

        
        create2DChart(array) {
            this.chart = new Chart(this.canvas, {
                // Creates a scatter chart
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

    .data-input-col {
        background-color: rgb(199, 206, 204);
    }

    
    .input-info {
        float: left;
        margin-top: 20px;
        text-align: left;
    }

</style>
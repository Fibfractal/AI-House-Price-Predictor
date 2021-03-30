<template>
  <div class="container">
      <div class="row">
          <div class="col-4">
                <h4>Filter</h4>
                <p>{{ predictions }}</p>  <!-- Test - shall be removed -->
                <select @change="prepdata" class="form-select" aria-label="Default select example" v-model="value">
                    <option disabled value="">Choose filter parameter</option>
                    <option value="TotRmsAbvGrd">Total rooms above ground</option>
                    <option value="YearBuilt">Year built</option>
                    <option value="LandContour">Land contour</option>
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
              <h3>Graph</h3>
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
            datapoints:[]
        };
    },

    mounted(){
        this.$store.dispatch('initPredictions')
        let canvas = document.getElementById("myChart");
        let ctx = canvas.getContext("2d");
        this.canvas = ctx;
        this.createChart()
    },

    computed: {
        predictions() {
            return this.$store.state.predictions
        }
    },

    methods: {
        prepdata(){
            let choice = this.value;
            console.log(choice)
            for (let i = 0; i < this.predictions.length; i++){
                let datapoint = {
                    x: this.predictions[i][choice].value,
                    y: this.predictions[i].PredictedPrice,
                };
                this.datapoints.push(datapoint)
            }; 
            console.log(this.datapoints)

        },

        createChart() {
            this.chart = new Chart(this.canvas, {
            // The type of chart we want to create
            type: "scatter",

            // The data for our dataset
            data: {
                datasets: [{
                    label: 'Scatter Dataset',
                    data: [{
                        x: 1,
                        y: 3
                    }, {
                        x: 7,
                        y: 10
                    }, {
                        x: 10,
                        y: 5
                    }],
                    showLine:true,
                }]
            },
            options: {
                scales: {
                    xAxes: [{
                        type: 'linear',
                        position: 'bottom'
                    }]
                },
            }
        });

    },
  },
};
</script>

<style scoped>

</style>
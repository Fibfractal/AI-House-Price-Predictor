<template>
  <div class="container">
      <div class="row">
          <div class="col-4">
                <h4>Filter</h4>
                <select class="form-select" aria-label="Default select example">
                    <option selected>Choose filter parameter</option>
                    <option value="1">Total rooms above ground</option>
                    <option value="2">Year built</option>
                    <option value="3">Land contour</option>
                    <option value="4">Finished basement area</option>
                    <option value="5">Garage space</option>
                    <option value="6">First floor area</option>
                    <option value="7">Total basement area</option>
                    <option value="8">Second floor area</option>
                    <option value="9">Ground living area</option>
                    <option value="10">Overall Quality</option>
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
            chosentype:""
        };
    },

    mounted(){
        let canvas = document.getElementById("myChart");
        let ctx = canvas.getContext("2d");
        this.canvas = ctx;
        this.createChart()
    },


    methods: {
        createChart() {
            this.chart = new Chart(this.canvas, {
            // The type of chart we want to create
            type: "line",

            // The data for our dataset
            data: {
                labels: [
                    'Red', 
                    'Blue', 
                    'Yellow', 
                    'Green',
                ],
                datasets: [
                    {
                    label: 'Earlier Predictions',
                    backgroundColor: ['red', 'blue', 'yellow', 'green'],
                    borderColor: 'black',
                    data: [30, 10, 5, 20],
                    order: 0
                }]
            },

            // Configuration options go here
            options: {

            }
        });

    },
  },
};
</script>

<style scoped>

</style>
<template>
   <div class="container-fluid">
      <div class="row">
          <div class="col-12 col-md-4 p-4 left-lg-col">
            <div class="row">
                <div class="col-12 col-md-2"></div>
                  <div class="col-12 col-md-8"> 
                    <img src="src\assets\jacques-bopp-wtzOhxEX4WU-unsplash-500-296.jpg" class="d-block w-100 rounded" alt="A braun, wood house">
                    <br>
                    <img src="src\assets\todd-kent-178j8tJrNlc-unsplash-500-296.jpg" class="d-block w-100 rounded" alt="A house with a porch">
                    <br>
                    <img src="src\assets\roger-starnes-sr-MINQCvKfwL4-unsplash-500-296.jpg" class="d-block w-100 rounded" alt="A blue house">
                    
                  </div>
                </div>
              <div class="col-12 col-md-2"></div>
          </div>
          <div class="col-12 col-md-8 mt-4 p-4">
              <div class="row">
                <div class="col-12 col-md-1"></div>
                <div class="col-12 col-md-10 ">
                  <div class="row">
                    <h4>About the service</h4>
                    <p class = "input-info">We use a AI model to make predictions of house prices based on a number of input values, as a part of a school project. <br> On our test data the model has an accuracy of 88%.
                  </p>
                  </div>
                  <div class="row">
                    <p class = "input-info">The model is trained on data from a specific geographic area (Ames, Iowa US), and may not project a fair picture of the value of homes in your area.</p>
                  </div>
                  <div class="row">
                    <h4>Disclaimer - At your own risk</h4>
                    <p class = "input-info">We do not make any warrenties about the completeness, reliability or accuracy of this information. <strong> Any action you take upon the information on this website is strictly at your own risk</strong>, and we will not be liable for any losses and damages in connection with the use of our website.
                    </p>
                  </div>
                </div>
                <div class="col-12 col-md-1"></div>
            </div>
          </div>
      </div>
  </div>

</template>

<script>

export default {

}
 
</script>


<style scope>
  .input-info {
    float: left;
    margin-top: 20px;
    text-align: left;
  }

  .left-lg-col {
      background-color: #dfe4ea;
  }
</style>
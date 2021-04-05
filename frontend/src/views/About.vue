<template>
   <div class="container-fluid">
      <div class="row">
          <div class="col-12 col-md-4 p-4 left-lg-col">
            <div class="row">
                <div class="col-12 col-md-2"></div>
                  <div class="col-12 col-md-8">             
                    <div id="carousel1" class="carousel slide" data-bs-ride="carousel" data-bs-interval=4000>
                      <div class="carousel-inner">
                        <div class="carousel-item active">
                          <img src="src\assets\jacques-bopp-wtzOhxEX4WU-unsplash-500-296.jpg" class="d-block w-100" alt="A braun, wood house">
                        </div>
                        <div class="carousel-item">
                          <img src="src\assets\jacques-bopp-Hh18POSx5qk-unsplash-500-296.jpg" class="d-block w-100" alt="A white house with red roof">
                        </div>
                        <div class="carousel-item">
                          <img src="src\assets\phil-hearing-IYfp2Ixe9nM-unsplash-500-296.jpg" class="d-block w-100" alt="A white house">
                        </div>
                        <div class="carousel-item">
                          <img src="src\assets\roger-starnes-sr-0MA4WC4I2tw-unsplash-500-296.jpg" class="d-block w-100" alt="Another white house">
                        </div>
                      </div>
                    </div>
                    <br>
                    <br>
                    <div id="carouse2" class="carousel slide" data-bs-ride="carousel" data-bs-interval=5000>
                      <div class="carousel-inner">
                        <div class="carousel-item active">
                          <img src="src\assets\roger-starnes-sr-MINQCvKfwL4-unsplash-500-296.jpg" class="d-block w-100" alt="A blue house">
                        </div>
                        <div class="carousel-item">
                          <img src="src\assets\roger-starnes-sr-nPmyejZsOy0-unsplash-500-296.jpg" class="d-block w-100" alt="A white house with a tall tree">
                        </div>
                        <div class="carousel-item">
                          <img src="src\assets\roger-starnes-sr-WhYsgTb1LMQ-unsplash-500-296.jpg" class="d-block w-100" alt="A white house with a flag">
                        </div>
                        <div class="carousel-item">
                          <img src="src\assets\todd-kent-178j8tJrNlc-unsplash-500-296.jpg" class="d-block w-100" alt="A house with a porch">
                        </div>
                      </div>
                    </div>
                  </div>
                  </div>
                  <div class="col-12 col-md-2"></div>
            </div>
          <div class="col-12 col-md-8 mt-4 p-4">
              <div class="row">
                <div class="col-12 col-md-1"></div>
                <div class="col-12 col-md-10 ">
                  <h4>About the service</h4>
                  <p class = "input-info">We use a AI model to make predictions of house prices based on a number of input values, as a part of a school project. <br> On our test data the model has an accuracy of 88 %.
                  </p>
                  <p class = "input-info">The model is trained on data from a specific geographic area ( Ames, Iowa US), and may not project a fair picture of the value of homes in your area.</p>
                  <h4>Disclaimer - At your own risk</h4>
                  <p class = "input-info">We do not make any warrenties about the completeness, reliability or accuracy of this information. <strong> Any action you take upon the information on this website is strictly at your own risk</strong>, and web will not be liable for any losses and damages in connection with the use of our website.
                  </p>
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
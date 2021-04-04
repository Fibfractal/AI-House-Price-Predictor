<template>
  <nav class="navbar navbar-expand-lg navbar-secondary bg-secondary p-4">

        <div class="img__wrap">
            <img id = "logo" src="src\assets\logo.png" width=50 height=50 class="img-fluid" alt="Responsive image">
            <p class="img__description">Fast predictions</p>
        </div>

        <ul id=ul-items>
            <li class="nav-item">
                <router-link to='/'>Make a prediction</router-link>
            </li>
            <li class="nav-item">
                <router-link to='/predictions'>Display predictions</router-link>
            </li>
            <li class="nav-item">
                <router-link to='/about'>About</router-link>
            </li>
        </ul>
    </nav>
</template>

<script>
export default {

}
</script>

<style scoped>

    a {
        margin: 10px;
        text-decoration:none;
        color: white;
        font-size: 25px;
        margin-right: 25px;
    }

    a:hover {
        color: pink;
        cursor: pointer;
        transition: 0.3s;
    }

    #logo {
        float: left;
        margin-left: 20px;
        margin-bottom: 20px;
    }

    #ul-items {
        margin:auto;
    }

    #ul-items li {
        display: inline-block;
    }

    .img__wrap {
        position: relative;
        height: 50px;
        width: 200px;
    }

    .img__description {
        position: absolute;
        top: 0;
        bottom: 0;
        left: 10;
        right: 0;
        background: secondary;
        color: #fff;
        visibility: hidden;
        opacity: 0;
        transition: opacity .2s, visibility .2s;
    }

    .img__wrap:hover .img__description {
        visibility: visible;
        opacity: 1;
    }

</style>
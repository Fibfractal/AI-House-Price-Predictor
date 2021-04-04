<template>
  <nav class="navbar navbar-expand-lg navbar-secondary bg-secondary p-4">
        <img id = "logo" src="src\assets\logo.png" width=50 height=50 class="img-fluid" alt="Responsive image">
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

</style>
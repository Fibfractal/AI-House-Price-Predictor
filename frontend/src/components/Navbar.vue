<template>
  <nav class="navbar navbar-expand-lg navbar-secondary bg-secondary justify-content-center p-4">
        <ul class="navbar-nav">
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
        font-size: 22px;
    }

    a:hover {
        color: rgb(190, 100, 100);
        cursor: pointer;
        transition: 0.25s;
    }
</style>
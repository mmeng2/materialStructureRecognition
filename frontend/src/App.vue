<template>
    <div id="app">
        <router-view>
            <!-- 这里是不被缓存的视图组件，比如 page3 -->
        </router-view>
    </div>
</template>

<script>
export default {
    name: 'App'
}
</script>

<style>
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        /*text-align: left;*/
        color: #2c3e50;
        margin: 0;
        /*margin-top: 60px;*/
    }
</style>

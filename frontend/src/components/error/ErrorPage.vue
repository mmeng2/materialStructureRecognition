<template>
    <div class="login-main">
        <img class="image" src="@/assets/404.png">
        <div style="margin-top: 60px">
            <label class="title">页面找不到了</label>
        </div>
        <div style="margin-top: 40px">
            <label class="loginButton" @click="back">返回</label>
        </div>
    </div>

</template>

<script>
export default {
    name: 'ErrorPage',
    methods: {
        back() {
            this.$router.go(-1);
        },
    },
}
</script>

<style lang="scss" scoped>
    .login-main {
        background-color: #ffffff;
        width: 100%;
        height: 100%;
        padding-bottom: 100px;
        text-align: center;
        .image {
            width: 615*0.6px;
            height: 359*0.6px;
            margin-top: 50px;
        }
        .title {
            color: #000000;
            font-weight: 300;
            font-size: 18px;
        }
        .loginButton {
            font-weight: 300;
            align-items: center;
            border-color: #000000;
            border-width: 1px;
            border-style: solid;
            color: #000000;
            font-size: 18px;
            padding-top: 3px;
            padding-bottom: 3px;
            padding-left: 30px;
            padding-right: 30px;
        }
    }

</style>

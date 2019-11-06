<template>
    <div>
        <el-container>
            <el-header>
                <div class="header-logo">
                    <img src="../../assets/icon2.png" class="header-icon"/>
                    &nbsp;
                    物质结构识别平台
                </div>
                <div class="header-right">
                    <el-dropdown @command="handleCommand">
                        <span class="el-dropdown-link">
                            admin<i class="el-icon-arrow-down el-icon--right"></i>
                        </span>
                        <el-dropdown-menu>
                            <el-dropdown-item command="user">用户中心</el-dropdown-item>
                            <el-dropdown-item command="logout">退出登录</el-dropdown-item>
                        </el-dropdown-menu>
                    </el-dropdown>
                </div>
            </el-header>
            <el-container class="main" :style="{'min-height':min_height+'px'}">
<!--                <el-aside width="200px" :style="{'height': asideHeight+'px'}"></el-aside>-->
                <el-container>
                    <el-main style="padding: 0px">
                        <router-view/>
                    </el-main>
                    <!-- <el-footer>Footer</el-footer>-->
                </el-container>
            </el-container>
        </el-container>
    </div>
</template>

<script>
export default {
    name: 'index',
    data() {
        return {
            asideHeight: outerHeight - 60,
            min_height: window.innerHeight - 60,
        }
    },
    mounted () {

        this.route();
    },
    methods: {
        route () {
            let hash = window.location.hash;
            let path = hash.split("#")[1];
            // this.$router.push("/mainPage");
            if (path === "/" || path === "/login") {
                this.$router.push("/mainPage");
            } else {
                if (path === "/mainPage") {
                    this.$router.push("/mainPage");
                } else {
                    let hash = window.location.hash;
                    let queryStr = hash.split("?")[1];
                    let queryObject = {};
                    if (queryStr) {
                        let newQueryStr = String(queryStr).slice(0, this.queryStr);
                        let querys = newQueryStr.split("&");
                        querys.forEach(element => {
                            let keys = element.split("=");
                            queryObject[keys[0]] = keys[1];
                        });
                    }
                    this.$router.push({
                        path: path,
                        query: queryObject
                    });
                }
            }
        },
        handleCommand(command) {
            this.$message('click on item ' + command);
        },
    },
}
</script>

<style lang="scss" scoped>
    .el-header {
        position: fixed;
        z-index: 99;
        background-color: #303133;
        box-shadow: 0 0 5px #888;
        color: #ffffff;
        text-align: center;
        width: 100%;
        line-height: 60px;
        display: flex;

        .header-logo {
            width: 200px;
            font-weight: bold;
            display: flex;
            .header-icon {
                width: 30px;
                height: 30px;
                align-self: center;
            }
        }

        .header-right {
            display: flex;
            margin-left: auto;
            margin-right: 0px;
            align-items: center;

            .el-dropdown-link {
                cursor: pointer;
                color: #C0C4CC;
                font-size: 16px;
                font-weight: bold;

                &:hover {
                    color: #ffffff;
                }
            }
        }
    }

    .main {
        margin-top: 60px;
        overflow: hidden;
        background-color: #f0f2f5;
        width: 100%;
        height: 100%;
        /*padding-top: 60px;*/
        /*margin-bottom: 0px;*/
    }

    .el-aside {
        /*background-color: #D3DCE6;*/
        /*color: #333;*/
        /*浮动，防止随页面滑动*/
        position: fixed;
        box-shadow: 2px 0 6px 0 rgba(0,21,41,.08);
        text-align: center;
        /*height: 550px;*/
        /*line-height: 200px;*/
    }

    .el-main {

    }

    body > .el-container {
        margin-bottom: 40px;
    }

</style>

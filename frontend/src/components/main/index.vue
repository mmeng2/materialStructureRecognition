<template>
    <div>
        <el-container>
            <el-header>
                <div class="header-logo">
                    HAHA
                </div>
                <div class="header-right">
                    <el-dropdown @command="handleCommand">
                        <span class="el-dropdown-link">
                            user_name<i class="el-icon-arrow-down el-icon--right"></i>
                        </span>
                        <el-dropdown-menu>
                            <el-dropdown-item command="user">用户中心</el-dropdown-item>
                            <el-dropdown-item command="logout">退出登录</el-dropdown-item>
                        </el-dropdown-menu>
                    </el-dropdown>
                </div>
            </el-header>
            <el-container class="main">
<!--                <el-aside width="200px" :style="{'height': asideHeight+'px'}"></el-aside>-->
                <el-container>
                    <el-main>
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
        }
    },
    mounted () {
        this.route();
    },
    methods: {
        route () {
            this.$router.push("/mainPage");
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
            width: 80px;
            font-weight: bold;
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

<template>
    <div>
        <div class="content" :style="{'min-height':min_height+'px'}">
            识别出的详细信息
        </div>
    </div>
</template>

<script>
    import API from "../api/api";
    export default {
        name: "projectDetail",
        data() {
            return {
                min_height: window.innerHeight - 90,
                job_id: null,
                // projectList: [],
            }
        },
        created() {
            this.job_id = this.$route.query.job_id;
        },
        mounted() {
            console.log('项目ID：', this.job_id);
        },
        methods: {
            getProjectDetail() {
                let params = {
                    job_id: this.job_id
                };
                API.getRecognizedDetail(params)
                .then(result => {
                    // this.recognizedCardList = result.data;
                    console.log(result.data);
                })
                .catch(execption => {
                    console.log(execption);
                });
            }
        },
    }
</script>

<style lang="scss" scoped>
    .content {
        margin-top: 15px;
        width: 1150px;
        height: 100%;
        margin-left: auto;
        margin-right: auto;
        background-color: #ffffff;
        border-bottom: 15px #f0f2f5 solid;
        padding: 20px 30px 20px 30px;
    }
</style>

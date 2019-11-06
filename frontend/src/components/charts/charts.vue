<template>
    <div class="">
        <div :id="id" :option="option">

        </div>
    </div>
</template>

<script>
    import HighCharts from 'highcharts'
    export default {
        name: "charts",
        props: {
            id: {
                type: String,
            },
            option: {
                type: Object,
            }
        },
        watch: {
            option() {
                HighCharts.chart(this.id, this.option);
            }
        },
        mounted() {
            HighCharts.chart(this.id, this.option);
        }
    }
</script>

<style scoped>

</style>

<template>
    <div>
        <div class="content" :style="{'min-height':min_height+'px'}">
            <div class="topdiv">
                <label class="topdiv-title">{{'test文件'}}</label>
            </div>
            <div class="line"></div>
<!--            <div>-->
<!--                识别出的详细信息-->
<!--            </div>-->
            <el-form style="margin-top:10px;margin-left: 10px;font-size: 18px" label-position="left" ref="form" label-width="130px" size="medium">
                <el-form-item class="form-item" label="主元素：">
                    <el-button class="card-top-element" :type="getElementButton('Fe')" plain circle>{{'Fe'}}</el-button>
<!--                    <label class="content-label"> {{'Fe'}}</label>-->
                </el-form-item>
                <el-form-item class="form-item" label="吸收边能量E0：">
                    <label class="content-label"> {{'7127.454' + ' ev'}}</label>
                </el-form-item>
            </el-form>
<!--            <div class="line"></div>-->
            <div class="XAFS-charts">
                <charts :id="XAFS_id" :option="XAFS_option"></charts>
            </div>
<!--            <div class="line"></div>-->
            <div class="component-charts">
                <div class="component-column-charts">
                    <charts :id="component_column_id" :option="component_column_option"></charts>
                </div>
                <div class="component-pie-charts">
                    <charts :id="component_pie_id" :option="component_pie_option"></charts>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import API from "../api/api";
    import Charts from "../charts/charts"
    export default {
        name: "projectDetail",
        components: {
            "charts": Charts,
        },
        data() {
            return {
                min_height: window.innerHeight - 90,
                job_id: null,
                XAFS_id: 'XAFS',
                component_column_id: 'component_column',
                component_pie_id: 'component_pie',
                XAFSData: [],
                norData: [],
                XAFS_option: {},
                component_column_option: {
                    chart: {
                        type: 'column'
                    },
                    title: {
                        text: '样品中的组分信息'
                    },
                    tooltip: {
                        // head + 每个 point + footer 拼接成完整的 table
                        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
                        pointFormat: '<tr><td style="padding:0"><b>{point.y:.1f}%</b></td></tr>',
                        footerFormat: '</table>',
                        shared: true,
                        useHTML: true
                    },
                    colors: ['#39F', '#4dd3b9', '#fdd67f', '#ffaca8', '#8085E9', '#F7A35C', '#90ED7D'],
                    credits: {
                        enabled: false
                    },
                    legend: {
                        enabled: false
                    },
                    xAxis: {
                        categories: [
                            'Fe foil', 'Fe2O3', 'FeN', 'Fe3O4', 'FeC', 'FeO', 'FeS2'
                        ],
                    },
                    yAxis: {
                        min: 0,
                        title: {
                            text: '组分含量（%）'
                        }
                    },
                    plotOptions: {
                        series: {
                            borderWidth: 0,
                            colorByPoint: true,
                            dataLabels: {
                                enabled: true,
                                formatter: function () {
                                    if (this.y > 0)
                                        return '<b style="font-size: 14px">' + this.y + ' %</b>'; // 这里进行判断
                                },
                            }
                        }
                    },
                    series: [{
                        // data: [0, 59, 0, 23, 0, 18, 0]
                        data: [15.2, 48.5, 1.1, 22.2, 0.7, 7.3, 5]
                    }]
                },
                component_pie_option: {
                    chart: {
                        type: 'pie'
                    },
                    title: {
                        text: '样品中的组分信息'
                    },
                    tooltip: {
                        pointFormat: '<b>{point.y:.1f}%</b>'
                    },
                    credits: {
                        enabled: false
                    },
                    colors: ['#39F', '#4dd3b9', '#fdd67f', '#ffaca8', '#8085E9', '#F7A35C', '#90ED7D'],
                    plotOptions: {
                        pie: {
                            allowPointSelect: true,
                            cursor: 'pointer',
                            dataLabels: {
                                enabled: true,
                                formatter: function () {
                                    if (this.percentage > 0)
                                        return '<b style="font-size: 14px">' + this.point.name + '</b><b style="font-size: 14px">: ' + this.percentage + ' %</b>'; // 这里进行判断
                                },
                            },
                            showInLegend: true
                        }
                    },
                    series: [{
                        name: 'Brands',
                        colorByPoint: true,
                        data: [{
                            name: 'Fe foil',
                            y: 15.2,
                        }, {
                            name: 'Fe2O3',
                            y: 48.5,
                        }, {
                            name: 'FeN',
                            y: 1.1,
                        }, {
                            name: 'Fe3O4',
                            y: 22.2,
                        }, {
                            name: 'FeC',
                            y: 0.7,
                        }, {
                            name: 'FeO',
                            y: 7.3,
                        }, {
                            name: 'FeS2',
                            y: 5,
                        }]
                    }]
                }
                // projectList: [],
            }
        },
        created() {
            this.job_id = this.$route.query.job_id;
        },
        mounted() {
            console.log('项目ID：', this.job_id);
            this.getXAFSData();

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
            },
            getElementButton(element) {
                return element.toLowerCase() === 'fe' ? 'primary': element.toLowerCase() === 'cu' ? 'warning': element.toLowerCase() === 'ni' ? 'info': element.toLowerCase() === 'pt' ? 'success': '';
            },
            // 获取XAFS数据
            getXAFSData() {
                API.getXAFSData()
                .then(result => {
                    this.XAFSData = result.data.data;
                    this.norData= result.data.nor_data;
                    this.XAFS_option = {
                        chart: {
                            type: 'spline'
                        },
                        title: {
                            text: 'XAFS谱图'
                        },
                        credits: {
                            enabled: false
                        },
                        xAxis: {
                            title: {
                                text: '能量E(ev)'
                            }
                        },
                        colors: ['#39F', '#F7A35C'],
                        yAxis: {
                            title: {
                                text: '吸收系数μ(E)'
                            },
                            // min: 0
                        },
                        plotOptions: {
                            spline: {
                                marker: {
                                    enabled: false
                                }
                            },
                        },
                        series: [{
                            name: 'XAFS原始谱图',
                            data: this.XAFSData
                        }, {
                            name: 'XAFS预处理后谱图',
                            data: this.norData
                        }]
                    };
                })
                .catch(execption => {
                    console.log(execption);
                });
            },
        },
    }
</script>

<style lang="scss">
    .content {
        margin-top: 15px;
        width: 1150px;
        height: 100%;
        margin-left: auto;
        margin-right: auto;
        background-color: #ffffff;
        border-bottom: 15px #f0f2f5 solid;
        padding: 20px 30px 20px 30px;

        .topdiv {
			display: flex;

			.topdiv-title {
				font-size: 20px;
				font-weight: 500;
				margin-left: 10px;
				margin-top: 10px;
			}
		}

        .line {
			height: 1px;
			margin: 12px 10px;
			padding: 0px;
			background-color: #e8e8e8;
		}
        .el-form-item__label {
            font-size: 16px;
            color: #000000;
        }
        .form-item {
            margin-bottom: 0px;
        }
        .card-top-element {
                width: 35px;
                height: 35px;
                padding: 0;
                font-size: 16px;
                font-weight: bold;
            }
        .content-label {
            text-align: left;
            float: left;
            font-size: 18px;
            color: #000000;
        }
        .XAFS-charts, .component-column-charts, .component-pie-charts {
            margin-top: 32px;
            padding-top: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, .12), 0 0 6px rgba(0, 0, 0, .04);
        }

        .component-charts {
            display: flex;
            justify-content: space-between;
            .component-column-charts {
                width: 49%;
            }
            .component-pie-charts {
                width: 49%;
            }
        }
        /*.old-XAFS {*/
        /*    width: 40%;*/
        /*}*/
    }
</style>

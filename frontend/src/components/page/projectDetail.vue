<template>
    <div>
        <div class="content" :style="{'min-height':min_height+'px'}">
            <div class="topdiv">
                <label class="topdiv-title">{{'测试文件3'}}</label>
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
                    <label class="content-label"> {{'7112' + ' ev'}}</label>
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
                XAFS_option: {
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
                                enabled: true
                            }
                        }
                    },
                    series: [{
                        name: 'XAFS原始谱图',
                        data: [
                            [6091, 0],
                            [6527, 0.6],
                            [7039, 0.7],
                            [7112, 0.8],
                            [7296, 0.6],
                            [7477, 0.6],
                            [7643, 0.67],
                            [7721, 0.81],
                            [7809, 0.78],
                            [7914, 0.98],
                            [8113, 1.84],
                            [8266, 1.80],
                            [8585, 1.80],
                            [8679, 1.92],
                            [8836, 2.49],
                            [8975, 2.79],
                            [9100, 2.73],
                            [9322, 2.61],
                            [9431, 2.76],
                            [9556, 2.82],
                            [9598, 2.8],
                            [9653, 2.1],
                            [9712, 1.1],
                            [9833, 0.25],
                            [9897, 0]
                        ]
                    }, {
                        name: 'XAFS预处理后谱图',
                        data: [
                            [6091, 0],
                            [6527, 1.65],
                            [7039, 1.75],
                            [7112, 1.85],
                            [7296, 1.65],
                            [7477, 1.65],
                            [7643, 1.76],
                            [7721, 1.97],
                            [7809, 1.85],
                            [7914, 2.23],
                            [8113, 2.99],
                            [8266, 2.92],
                            [8585, 2.90],
                            [8679, 3.00],
                            [8836, 3.61],
                            [8975, 3.85],
                            [9100, 3.82],
                            [9322, 3.78],
                            [9431, 3.88],
                            [9556, 3.97],
                            [9598, 3.93],
                            [9653, 3.25],
                            [9712, 2.25],
                            [9833, 1.40],
                            [9897, 0]
                        ]
                    }]
                },
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
                                        return this.y + ' %'; // 这里进行判断
                                },
                            }
                        }
                    },
                    series: [{
                        data: [0, 59, 0, 23, 0, 18, 0]
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
                                        return '<b>' + this.point.name + '</b>: ' + this.percentage + ' %'; // 这里进行判断
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
                            y: 0,
                        }, {
                            name: 'Fe2O3',
                            y: 59
                        }, {
                            name: 'FeN',
                            y: 0
                        }, {
                            name: 'Fe3O4',
                            y: 23
                        }, {
                            name: 'FeC',
                            y: 0
                        }, {
                            name: 'FeO',
                            y: 18
                        }, {
                            name: 'FeS2',
                            y: 0
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

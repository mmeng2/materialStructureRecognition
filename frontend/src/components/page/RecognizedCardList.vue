<template>
    <div class="card-list">
        <div v-for="(items,index) in recognizedCardList.slice((cardCurrentPage-1)*4,cardCurrentPage*4)" :key="index" style="display:flex;width:100%;"
             :style="{'margin-top':index==0?'0px':'32px'}">
            <div class="card" v-for="(item,sindex) in items" :key="item.id"
                 :style="{'margin-left':sindex==0?'0px':'55px', 'box-shadow':mouseover&&item.id==current?getElementShadow(item.element):'',
                 'background-color':getElementBackground(item.element)}"
                 @click="projectDetail" @mouseover="onMouseIn(item.id)" @mouseout="onMouseOut">
                <div class="card-top">
                    <label class="title-ellipsis">{{getItemTitle(item.projectName)}}</label>
                    <el-button class="card-top-element" :type="getElementButton(item.element)" plain circle>{{item.element}}</el-button>
<!--                    <label class="card-top-element">{{item.element}}</label>-->
                </div>
                <div class="card-item" style="margin-top:14px">
                    <label class="card-item-title">{{'主元素:'}}</label>
                    <label class="card-item-value">{{item.element?item.element:'未识别成功'}}</label>
                </div>
                <div class="card-item">
                    <label class="card-item-title">{{'吸收边E0:'}}</label>
                    <label class="card-item-value">{{item.e? item.e + 'ev':'未获取'}}</label>
                </div>
                <div class="card-item">
                    <label class="card-item-title">{{'上传时间:'}}</label>
                    <label class="card-item-value">{{item.uploadTime | formatDate}}</label>
                </div>
            </div>
        </div>
        <div class="pagination">
            <el-pagination style="float:right" small background @current-change="cardPageChange"
                           layout="prev, pager, next"
                           :total="cardTotal" :page-size="perPage"
                           v-show="cardTotal>0"></el-pagination>
        </div>
    </div>
</template>

<script>
    import API from "../api/api";

    export default {
        name: "RecognizedCardList",
        data() {
            return {
                mouseover: false,
                current: 0,
                cardTotal: 0,
                perPage: 12,
                cardList: 0,
                cardCurrentPage: 1,
                recognizedCardList: [],
            }
        },
        mounted() {
            this.getRecognizedProjects();
        },
        methods: {
            // 获取文件的详细信息，跳转到详细信息页面
            projectDetail() {
                console.log('获取文件的详细信息');
            },
            // 获取已识别卡片信息
            getRecognizedProjects() {
                API.getRecognizedCardList()
                .then(result => {
                    this.recognizedCardList = this.groupProjects(result.data);
                    this.cardTotal= result.data.length;
                    console.log(result.data);
                })
                .catch(execption => {
                    console.log(execption);
                });
            },
            cardPageChange(val) {
                this.cardCurrentPage = val;
            },
            groupProjects(items) {
				let num = 3; //每个子数组里的元素个数
				let projects = new Array(Math.ceil(items.length / num));
				for (let i = 0; i < projects.length; i++) {
					projects[i] = new Array();
					for (let j = 0; j < num; j++) {
						if (i * num + j < items.length) {
							projects[i][j] = items[i * num + j];
						}
					}
				}
				this.cardList = this.perPage/3;
				return projects;
			},
            getItemTitle(title) {
				if (title.length > 20) {
					let newTitle = title.slice(0, 20) + "...";
					return newTitle;
				}
				return title;
			},
            getElementButton(element) {
                return element.toLowerCase() === 'fe' ? 'primary': element.toLowerCase() === 'cu' ? 'warning': element.toLowerCase() === 'ni' ? 'info': element.toLowerCase() === 'pt' ? 'success': '';
            },
            getElementBackground(element) {
                return element.toLowerCase() === 'fe' ? 'rgba(64,158,255,0.15)': element.toLowerCase() === 'cu' ? 'rgba(230,162,60,0.15)': element.toLowerCase() === 'ni' ? 'rgba(144,147,153,0.15)': element.toLowerCase() === 'pt' ? 'rgba(5,220,16,0.15)': '#ffffff';
            },
            getElementShadow(element) {
                return element.toLowerCase() === 'cu' ? '0px 0px 10px 2px #E6A23C': element.toLowerCase() === 'ni' ? '0px 0px 10px 2px #909399': element.toLowerCase() === 'pt' ? '0px 0px 10px 2px #67C23A': '0px 0px 10px 2px #4A90E2';
            },
            // 鼠标进入时触发当前卡片的阴影
            onMouseIn: function (index) {
                this.mouseover = true; //鼠标移入显示
                this.current = index;
            },
            onMouseOut: function (index) {
                this.mouseover = false; //鼠标移出隐藏
                this.current = null;
            },
        },
        // mounted() {
        //     this.recognizedCardList = this.groupProjects([{
        //         "id": "00000000000000000000000000000003",
        //         "projectName": "测试文件3",
        //         "uploadTime": "2019-11-13T15:41:15",
        //         "textFileName": null,
        //         "comment": null,
        //         "isRecognized": 1,
        //         "element": "Fe",
        //         "e": "7112",
        //         "bz1": null,
        //         "bz2": null
        //     }, {
        //         "id": "00000000000000000000000000000030",
        //         "projectName": "测试文件30",
        //         "uploadTime": "2019-10-31T16:10:19",
        //         "textFileName": null,
        //         "comment": null,
        //         "isRecognized": 1,
        //         "element": "Cu",
        //         "e": null,
        //         "bz1": null,
        //         "bz2": null
        //     }, {
        //         "id": "00000000000000000000000000000025",
        //         "projectName": "测试文件25",
        //         "uploadTime": "2019-10-30T16:10:07",
        //         "textFileName": null,
        //         "comment": null,
        //         "isRecognized": 1,
        //         "element": "Fe",
        //         "e": null,
        //         "bz1": null,
        //         "bz2": null
        //     }, {
        //         "id": "00000000000000000000000000000024",
        //         "projectName": "测试文件24",
        //         "uploadTime": "2019-10-28T16:10:05",
        //         "textFileName": null,
        //         "comment": null,
        //         "isRecognized": 1,
        //         "element": "Cu",
        //         "e": null,
        //         "bz1": null,
        //         "bz2": null
        //     }, {
        //         "id": "00000000000000000000000000000022",
        //         "projectName": "测试文件22",
        //         "uploadTime": "2019-10-26T16:10:00",
        //         "textFileName": null,
        //         "comment": null,
        //         "isRecognized": 1,
        //         "element": "Pt",
        //         "e": null,
        //         "bz1": null,
        //         "bz2": null
        //     }, {
        //         "id": "00000000000000000000000000000018",
        //         "projectName": "测试文件18",
        //         "uploadTime": "2019-10-23T16:09:50",
        //         "textFileName": null,
        //         "comment": null,
        //         "isRecognized": 1,
        //         "element": "Pt",
        //         "e": null,
        //         "bz1": null,
        //         "bz2": null
        //     }, {
        //         "id": "00000000000000000000000000000023",
        //         "projectName": "测试文件23",
        //         "uploadTime": "2019-10-22T16:10:03",
        //         "textFileName": null,
        //         "comment": null,
        //         "isRecognized": 1,
        //         "element": "Ni",
        //         "e": null,
        //         "bz1": null,
        //         "bz2": null
        //     }, {
        //         "id": "00000000000000000000000000000019",
        //         "projectName": "测试文件19",
        //         "uploadTime": "2019-10-20T16:09:53",
        //         "textFileName": null,
        //         "comment": null,
        //         "isRecognized": 1,
        //         "element": "Fe",
        //         "e": null,
        //         "bz1": null,
        //         "bz2": null
        //     }, {
        //         "id": "00000000000000000000000000000028",
        //         "projectName": "测试文件28",
        //         "uploadTime": "2019-10-13T16:10:14",
        //         "textFileName": null,
        //         "comment": null,
        //         "isRecognized": 1,
        //         "element": "Ni",
        //         "e": null,
        //         "bz1": null,
        //         "bz2": null
        //     }, {
        //         "id": "00000000000000000000000000000010",
        //         "projectName": "测试文件10",
        //         "uploadTime": "2019-10-09T15:43:42",
        //         "textFileName": null,
        //         "comment": null,
        //         "isRecognized": 1,
        //         "element": "Ni",
        //         "e": "8907",
        //         "bz1": null,
        //         "bz2": null
        //     }, {
        //         "id": "00000000000000000000000000000016",
        //         "projectName": "测试文件16",
        //         "uploadTime": "2019-10-08T16:09:45",
        //         "textFileName": null,
        //         "comment": null,
        //         "isRecognized": 1,
        //         "element": "Fe",
        //         "e": null,
        //         "bz1": null,
        //         "bz2": null
        //     }, {
        //         "id": "00000000000000000000000000000026",
        //         "projectName": "测试文件26",
        //         "uploadTime": "2019-10-04T16:10:09",
        //         "textFileName": null,
        //         "comment": null,
        //         "isRecognized": 1,
        //         "element": "Fe",
        //         "e": null,
        //         "bz1": null,
        //         "bz2": null
        //     }, {
        //         "id": "00000000000000000000000000000029",
        //         "projectName": "测试文件29",
        //         "uploadTime": "2019-10-03T16:10:16",
        //         "textFileName": null,
        //         "comment": null,
        //         "isRecognized": 1,
        //         "element": "Cu",
        //         "e": null,
        //         "bz1": null,
        //         "bz2": null
        //     }, {
        //         "id": "00000000000000000000000000000020",
        //         "projectName": "测试文件20",
        //         "uploadTime": "2019-10-02T16:09:55",
        //         "textFileName": null,
        //         "comment": null,
        //         "isRecognized": 1,
        //         "element": "Cu",
        //         "e": null,
        //         "bz1": null,
        //         "bz2": null
        //     }, {
        //         "id": "00000000000000000000000000000017",
        //         "projectName": "测试文件17",
        //         "uploadTime": "2019-10-02T16:09:48",
        //         "textFileName": null,
        //         "comment": null,
        //         "isRecognized": 1,
        //         "element": "Ni",
        //         "e": null,
        //         "bz1": null,
        //         "bz2": null
        //     }, {
        //         "id": "00000000000000000000000000000027",
        //         "projectName": "测试文件27",
        //         "uploadTime": "2019-10-01T16:10:11",
        //         "textFileName": null,
        //         "comment": null,
        //         "isRecognized": 1,
        //         "element": "Pt",
        //         "e": null,
        //         "bz1": null,
        //         "bz2": null
        //     }, {
        //         "id": "00000000000000000000000000000021",
        //         "projectName": "测试文件21",
        //         "uploadTime": "2019-10-01T16:09:57",
        //         "textFileName": null,
        //         "comment": null,
        //         "isRecognized": 1,
        //         "element": "Ni",
        //         "e": null,
        //         "bz1": null,
        //         "bz2": null
        //     }, {
        //         "id": "00000000000000000000000000000006",
        //         "projectName": "测试文件6",
        //         "uploadTime": "2019-09-04T15:43:23",
        //         "textFileName": null,
        //         "comment": null,
        //         "isRecognized": 1,
        //         "element": "Cu",
        //         "e": "6500",
        //         "bz1": null,
        //         "bz2": null
        //     }]);
        //     console.log(this.recognizedCardList)
        // }
    }
</script>

<style lang="scss" scoped>
    .card-list {
        margin: 17px 10px;
		height: auto;

		.pagination {
			background-color: #ffffff;
			width: 100%;
			margin-top: 73px;
			height: 40px;
		}
	}
    .card {
        position: relative;
		cursor: pointer;
		background-color: #ffffff;
		border: 1px solid #c0ccda;
		text-align: left;
		float: left;
		width: 334px;
		height: 200px;
		margin-top: 0;
		overflow: hidden;

		.card-top {
			margin-top: 31px;
			margin-left: 19px;
			margin-right: 19px;

			.card-top-element {
                margin-left: auto;
				margin-right: 0px;
				float: right;
                width: 35px;
                height: 35px;
                padding: 0;
                font-size: 16px;
                font-weight: bold;
            }

			.title-ellipsis {
				margin-left: 0;
				font-size: 16px;
                font-weight: bold;
				color: #030303;
			}
		}

		.card-item {
			margin-left: 19px;
			margin-right: 10px;
			margin-top: 8px;
			height: 20px;

			.card-item-title {
				font-size: 14px;
				color: #030303;
			}

			.card-item-value {
				font-size: 14px;
				color: #3b3a3a;
			}
		}

		.card-bottom {
			height: 44px;
			background-color: #f7faff;
			text-align: center;
			display: flex;
			border-top: #c0ccda solid 1px;
            position:absolute;
            bottom:0 ;
			.card-bottom-button {
				color: #1890ff;
				font-size: 14px;
				width: 100%;
				height: 44px;
			}

			.card-bottom-vline {
				height: 25px;
				width: 1px;
				background-color: #c0ccda;
				margin-top: 10px;
			}
		}
	}
</style>

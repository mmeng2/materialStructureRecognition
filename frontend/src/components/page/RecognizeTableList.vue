<template>
    <div>
        <div style="margin-top:23px;padding-bottom:20px">
            <el-table :data="recognizeTableList.slice((tableCurrentPage-1)*perPage,tableCurrentPage*perPage)"
                      style="width: 100%" :header-cell-style="{color:'#606266'}">
                <el-table-column label="序号" type="index" :index="tableColumnIndex" align="left" min-width="5%"></el-table-column>
                <el-table-column prop="projectName" label="文件名称" align="left" min-width="20%"></el-table-column>
                <el-table-column prop="uploadTime" :formatter="setDate" label="上传时间" align="left" min-width="15%"></el-table-column>
                <el-table-column prop="comment" label="备注" align="left" min-width="30%"></el-table-column>
                <el-table-column label="操作" min-width="30%">
                    <template slot-scope="scope">
                        <el-button size="mini" type="success" plain @click="recognize(scope.row)">识别物质结构</el-button>
                        <el-button size="mini" type="primary" plain @click="recognize(scope.row)">下载文件</el-button>
                        <el-button size="mini" type="danger" @click="del(scope.row)">删除</el-button>
                    </template>
                </el-table-column>
            </el-table>
        </div>
        <div class="pagination" style="height:30px;padding-bottom:20px">
            <el-pagination style="float:right" small background @current-change="tablePageChange"
                           layout="prev, pager, next" :total="tableTotal"
                           :page-size="perPage" v-show="tableTotal>0"></el-pagination>
        </div>
    </div>
</template>

<script>
    import API from '../api/api';
    import moment from "moment";
    export default {
        name: "RecognizeTableList",
        data() {
            return {
                tableTotal: 0,
                perPage: 10,
                tableCurrentPage: 1,
                recognizeTableList: [],
                // recognizeTableList: [{
                //     id: '00001',
                //     projectName: '测试文件1',
                //     uploadTime: '2019-10-10T00:00:00',
                //     comment: 'hahahhahahahhahahhahahhhahhahahahahahhahahhahahahahahhahahahahha',
                // }, {
                //     id: '00002',
                //     projectName: '测试文件2',
                //     uploadTime: '2019-06-14T00:00:00',
                //     comment: '',
                // }, {
                //     id: '00003',
                //     projectName: '测试文件3',
                //     uploadTime: '2019-06-14T00:00:00',
                //     comment: '',
                // }, {
                //     id: '00004',
                //     projectName: '测试文件4',
                //     uploadTime: '2019-06-14T00:00:00',
                //     comment: '',
                // }, {
                //     id: '00005',
                //     projectName: '测试文件5',
                //     uploadTime: '2019-06-14T00:00:00',
                //     comment: '',
                // }, {
                //     id: '00006',
                //     projectName: '测试文件6',
                //     uploadTime: '2019-06-14T00:00:00',
                //     comment: '',
                // }, {
                //     id: '00007',
                //     projectName: '测试文件7',
                //     uploadTime: '2019-06-14T00:00:00',
                //     comment: '',
                // }, {
                //     id: '00008',
                //     projectName: '测试文件8',
                //     uploadTime: '2019-06-14T00:00:00',
                //     comment: '',
                // }, {
                //     id: '00009',
                //     projectName: '测试文件9',
                //     uploadTime: '2019-06-14T00:00:00',
                //     comment: '',
                // }, {
                //     id: '000010',
                //     projectName: '测试文件10',
                //     uploadTime: '2019-06-14T00:00:00',
                //     comment: '',
                // }, {
                //     id: '000011',
                //     projectName: '测试文件11',
                //     uploadTime: '2019-06-14T00:00:00',
                //     comment: '',
                // }, {
                //     id: '000012',
                //     projectName: '测试文件12',
                //     uploadTime: '2019-07-14T00:00:00',
                //     comment: '',
                // }, {
                //     id: '000013',
                //     projectName: '测试文件13',
                //     uploadTime: '2019-06-14T00:00:00',
                //     comment: '',
                // }, {
                //     id: '000014',
                //     projectName: '测试文件14',
                //     uploadTime: '2019-06-14T00:00:00',
                //     comment: '',
                // }],
            }
        },
        mounted() {
            // this.getRecognizeProjects();
        },
        methods: {
            // 日期时间固定格式
            setDate(row, col) {
                let newDate = row[col.property];
                return newDate === undefined ? '' : moment(newDate).format('YYYY-MM-DD HH:mm:ss');
            },
            // 每次刷新都显示首页
            tableColumnIndex(index) {
                return (this.tableCurrentPage - 1) * this.perPage + index + 1
            },
            recognize(data) {
                console.log(data);
            },
            del(data) {
                console.log(data);
            },
            tablePageChange(val) {
                this.tableCurrentPage = val;
            },
            // 获取未识别列表信息
            getRecognizeProjects() {
                API.getRecognizeTableList()
                .then(result => {
                    this.recognizeTableList = result.data;
                    this.tableTotal= result.data.length;
                    console.log(result.data);
                })
                .catch(execption => {
                    console.log(execption);
                });
            },
        },
    }
</script>

<style scoped>

</style>

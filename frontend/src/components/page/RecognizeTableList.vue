<template>
    <div>
        <div style="margin-top:23px;padding-bottom:20px">
            <el-table :data="recognizeTableList" style="width: 100%" :header-cell-style="{color:'#606266'}">
                <el-table-column label="序号" type="index" align="left" min-width="5%"></el-table-column>
                <el-table-column prop="projectName" label="文件名称" align="left" min-width="20%"></el-table-column>
                <el-table-column prop="uploadTime" label="上传时间" align="left" min-width="15%"></el-table-column>
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
    export default {
        name: "RecognizeTableList",
        data() {
            return {
                tableTotal: 0,
                perPage: 15,
                tableCurrentPage: 1,
                recognizeTableList: [{
                    id: '00001',
                    projectName: '测试文件1',
                    uploadTime: '2019-10-10',
                    comment: 'hahahhahahahhahahhahahhhahhahahahahahhahahhahahahahahhahahahahha',
                }, {
                    id: '00002',
                    projectName: '测试文件2',
                    uploadTime: '2019-6-14',
                    comment: '',
                }],
            }
        },
        methods: {
            recognize(data) {
                console.log(data);
            },
            del(data) {
                console.log(data);
            },
            tablePageChange(val) {
                this.tableCurrentPage = val;
                // 获取数据列表
				// this.getReviewedProjects();
            },
        },
    }
</script>

<style scoped>

</style>

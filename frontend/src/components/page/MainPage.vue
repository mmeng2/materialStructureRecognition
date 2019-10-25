<template>
    <div>
        <div class="content" :style="{'min-height':min_height+'px'}">
            <div class="top-content">
                <label style="font-size: 18px; font-weight: bold;">XAFS谱图文件列表</label>
                <el-popover placement="bottom" v-model="createProjectPopoverVisible" width="330" class="create-project-button">
                    <div class="label-item">
                        <label><span style="color: #D0021B;font-size: 12px">* </span>文件名称：</label>
                        <el-input size="small" v-model="projectName" :maxlength="50" placeholder="最多输入50个字符"></el-input>
                    </div>
                    <div>
                        <label class="errorMessage" v-if="errorInfo.is_projectName_error" style="margin-left: 120px;">*文件名称不能为空</label>
                    </div>
                    <div class="label-item">
                        <label>备注：</label>
                        <el-input size="small" type="textarea" :rows="3" v-model="comment" :maxlength="300" placeholder="最多输入300个字符"></el-input>
                    </div>
                    <div style="line-height: 12px; margin: 0 10px 10px 10px">
                        <el-upload
                            class=""
                            action=""
                            ref="uploadFile"
                            :file-list="fileList"
                            :auto-upload="false"
                            :limit="1"
                            :on-remove="handleRemove"
                            :on-change="handleChange"
                            :on-preview="handlePreview">
                            <el-button size="small" type="text" v-if="!file && !fileList.length">
                                <span style="color: #D0021B">* </span>
                                <i class="el-icon-upload el-icon--right"></i>
                                上传待识别的XAFS谱图文件（10M）
                            </el-button>
                        </el-upload>
                        <div>
                            <label class="errorMessage" v-if="errorInfo.is_uploadFile_error" style="margin-left: 30px;">*请上传文件</label>
                        </div>
                    </div>
                    <div style="text-align: right; margin: 0">
                        <el-button size="mini" type="text" @click="createProjectPopoverVisible = false">取消</el-button>
                        <el-button type="primary" size="mini" @click="submitPopoverButton">确定</el-button>
                    </div>
                    <el-button slot="reference" size="small" type="primary">添加待识别的XAFS谱图文件
                        <i class="el-icon-upload el-icon--right"></i>
                    </el-button>
                </el-popover>
            </div>

            <el-tabs type="card">
                <el-tab-pane>
                    <span slot="label"><i class="el-icon-brush"></i> 待识别的XAFS谱图</span>
                    <recognize_table_list></recognize_table_list>
                </el-tab-pane>
                <el-tab-pane>
                    <span slot="label"><i class="el-icon-s-open"></i> 已识别的XAFS谱图</span>
                    <recognized_card_list></recognized_card_list>
                </el-tab-pane>
            </el-tabs>

<!--            <div style="margin-top: 10px">-->
<!--                <el-button @click="haha">测试按钮</el-button>-->
<!--            </div>-->
        </div>
    </div>
</template>

<script>
import {
    Loading
} from "element-ui";
import API from '../api/api'
import RecognizeTableList from './RecognizeTableList'
import RecognizedCardList from './RecognizedCardList'

export default {
    name: 'HelloWorld',
    components: {
        'recognize_table_list': RecognizeTableList,
        'recognized_card_list': RecognizedCardList,
    },
    computed: {

    },
    data() {
        return {
            min_height: window.innerHeight - 15,
            createProjectPopoverVisible: false,
            fileList: [],
            file: null,
            projectName: '',
            comment: '',
            errorInfo: {
                is_projectName_error: false,
                is_uploadFile_error: false,
            },
        };
    },
    watch: {
        // 必填项验证，为空则提示
        projectName(newVal, oldVal) {
            this.errorInfo.is_projectName_error = !newVal;
        },
        file(newVal, oldVal) {
            this.errorInfo.is_uploadFile_error = !newVal;
        },
    },
    methods: {
        //用于验证文件名是否合法
        checkSuffix(str) {
            let strRegex = "(.txt|.dat)$";
            let re = new RegExp(strRegex);
            return re.test(str.toLowerCase());
        },
        haha() {
            console.log('haha');
            API.getTest()
                .then(result => {
                    alert(result.data);
                    console.log(result.data);
                })
                .catch(execption => {
                    console.log(execption);
                });
        },
        handleChange(file, fileList) {
            let sizeMB = file.size / 1024 / 1024;
            if (!this.checkSuffix(file.raw.name)) {
                this.$alert('文件不合法，只能为txt文件或dat文件');
                this.fileList.splice(0, 1);
            } else if (sizeMB > 10) {
                this.$alert('文件超过10MB');
                this.fileList.splice(0, 1);
            } else {
                this.file = file.raw;
                this.fileList = fileList;
                if (!this.projectName) {
                    this.projectName = this.file.name;
                }
                //this.form.label_requirement.attachment_timestamp = +new Date() / 1000;
            }
            console.log("file:", this.file)
        },
        handleRemove(file, fileList) {
            this.file = null;
            this.fileList.splice(0, 1);
        },
        handlePreview(file) {
            file.url && file.url.indexOf('blob') !== 0 && window.open(file.url, '_blank');
        },
        submitPopoverButton() {
            // 判断必填项是否为空
            if (!this.projectName && !this.file) {
                this.errorInfo.is_projectName_error = true;
                this.errorInfo.is_uploadFile_error = true;
                return;
            } else if (!this.projectName) {
                this.errorInfo.is_projectName_error = true;
                return;
            } else if (!this.file) {
                this.errorInfo.is_uploadFile_error = true;
                return;
            }
            let loadingInstance = Loading.service({
                lock: true,
                text: "Loading",
                spinner: "el-icon-loading",
                background: "rgba(0, 0, 0, 0.7)"
            });
            // this.$refs.uploadFile.submit()
            let formData = new FormData();
            formData.append('file', this.file);
            formData.append('projectName', this.projectName);
            formData.append('comment', this.comment);
            API.postUploadFile(formData)
                .then(result => {
                    // alert(result.data);
                    console.log(result.data);
                    // this.$router.go(0);
                    loadingInstance.close();
                })
                .catch(execption => {
                    console.log(execption);
                    loadingInstance.close();
                });

        },
    },
    mounted() {

    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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
    .top-content {
        display: flex;
        margin-top: 20px;

        .create-project-button {
            padding: 10px;
            margin-left: auto;
            margin-right: 0;
        }
    }
    .label-item {
        display: inline-flex;
        margin: 10px 10px;

		label:not(.el-radio) {
			width: 120px;
            margin-top: 5px;
		}
	}
    .errorMessage {
		font-size: 12px;
		color: #D0021B;
		height: 12px;
	}
</style>

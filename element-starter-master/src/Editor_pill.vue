<template>
	<div id="app">
		<el-container>
			<el-header>
				<el-menu :default-active="activeIndex" mode="horizontal">
					<el-menu-item index="0"><i class="el-icon-edit"></i>创建胶囊</el-menu-item>
					<el-menu-item index="1" @click="goTo('/')">首页</el-menu-item>
					<el-menu-item index="2" @click="goTo('home')">胶囊广场</el-menu-item>
				</el-menu>
			</el-header>
			<el-main>
<el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
  <el-form-item label="日记标题" prop="name">
    <el-input v-model="ruleForm.name"></el-input>
  </el-form-item>
<!--  <el-form-item label="日记类型" prop="dairy_type">
    <el-select v-model="ruleForm.dairy_type" placeholder="请选择活动区域">
      <el-option label="区域一" value="pill"></el-option>
      <el-option label="区域二" value="pre"></el-option>
    </el-select>
  </el-form-item> -->
  <el-form-item label="解封时间" required>
    <el-col :span="11">
      <el-form-item prop="date1">
        <el-date-picker type="date" placeholder="选择日期" v-model="ruleForm.date1" style="width: 100%;"></el-date-picker>
      </el-form-item>
    </el-col>
    <el-col class="line" :span="2">-</el-col>
    <el-col :span="11">
      <el-form-item prop="date2">
        <el-time-picker placeholder="选择时间" v-model="ruleForm.date2" style="width: 100%;"></el-time-picker>
      </el-form-item>
    </el-col>
  </el-form-item>
  <el-form-item label="是否公开" prop="isopen">
    <el-switch v-model="ruleForm.isopen"></el-switch>
  </el-form-item>

  <el-form-item label="日记内容" prop="content">
    <el-input type="textarea" v-model="ruleForm.content"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="submitForm('ruleForm')">立即创建</el-button>
    <el-button @click="resetForm('ruleForm')">重置</el-button>
  </el-form-item>
</el-form>
			
			</el-main>

			<el-footer class="bg-footer">
				<div class="footer-title">时光胶囊 © 2021 - 2021 All Copyright reserved</div>
			</el-footer>
		</el-container>
	</div>
</template>
<script>
	import axios from 'axios'
	import Qs from 'qs'
	axios.defaults.withCredentials = true; //让ajax携带cookie
  export default {
    data() {
      return {
		activeIndex: '0',
        ruleForm: {
          name: '',
          date1: '',
          date2: '',
          isopen: false,
          content: '',
		  dairy_type: 'pill'
        },
        rules: {
          name: [
            { required: true, message: '请输入日记标题', trigger: 'blur' },
            { min: 3, max: 50, message: '长度在 3 到 50 个字符', trigger: 'blur' }
          ],
          // dairy_type: [
          //   { required: true, message: '请选择dairy_type', trigger: 'change' }
          // ],
          date1: [
            { type: 'date', required: true, message: '请选择日期', trigger: 'change' }
          ],
          date2: [
            { type: 'date', required: true, message: '请选择时间', trigger: 'change' }
          ],
          isopen: [
            {required: true, message: '请选择到期是否公开', trigger: 'change' }
          ],
          content: [
            { required: true, message: '请填写日记内容', trigger: 'blur' }
          ]
        }
      };
    },
    methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            // alert('submit!');
			console.log(this.ruleForm.date1)
			console.log(this.ruleForm.date2)
			var date1 = this.ruleForm.date1
			var date2 = this.ruleForm.date2
			const month = date1.getMonth()+1
			var date3 = date1.getFullYear() + '/' + month + '/' + date1.getDate() + ' ' + date2.getHours() + ':' +  date2.getMinutes()  + ':' + date2.getSeconds()
			date3 = new Date(date3)
			console.log(date3)
			if(date3 < new Date()){
				console.log('不得小于当前时间')
				this.$notify({
				  title: "提交错误",
				  type: "error",
				  message:
				    "解封时间不得小于当前时间!",
				  duration: 5000,
				});
				return
			}else{
				console.log(this.ruleForm)
				this.$notify({
				  title: "提交成功",
				  type: "success",
				  message:
				    "新胶囊已生成!",
				  duration: 5000,
				});
				var data = {
					"title":this.ruleForm.name,
					"content":this.ruleForm.content,
					"square_open":this.ruleForm.isopen,
					"expire_time":date3,
					"diary_type":'pill',
					}
				console.log(data)
				var _this = this
				console.log(axios.defaults.withCredentials)
				axios.post("http://localhost:8000/articles/",data).then(
				  function (resp) {
					var ses = window.sessionStorage
					console.log(resp)
					_this.$router.push('/home');
					// const result = resp.data.request
					// // const flag = resp.data.request['flag']
					// if (result == 'Login ok'){
					//   // console.log(resp.data.request['flag'])
					//   _this.$router.push("/home")
					// }else if(result == 'Have Login' ){
					// 	alert(result)
					// 	_this.$router.push("/home")
					// }else {
					//   alert(result)
					// }
				  }
				)
			}
          } else {
            console.log('error submit!!');
			this.$notify({
			  title: "提交错误",
			  type: "error",
			  message:
			    "请检查表单项是否全部填写!",
			  duration: 2000,
			});
            return false;
          }
        });
      },
      resetForm(formName) {
        this.$refs[formName].resetFields();
      },
	  goTo(url){
	  //直接跳转
	  this.$router.push(url);
	  }
    }
  }
</script>

<style>
	#app {
		/* font-family: Helvetica, sans-serif; */
		font-family: "PingFang SC";
		text-align: center;
	}
</style>

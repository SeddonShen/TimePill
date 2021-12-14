<template>
  <div id="app">
  用户登录
  <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
    <el-form-item label="用户名" prop="account">
      <el-input v-model.number="ruleForm.account"></el-input>
    </el-form-item>
	<el-form-item label="密码" prop="pass">
      <el-input type="password" v-model="ruleForm.pass" autocomplete="off"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="submitForm('ruleForm')">提交</el-button>
      <el-button @click="resetForm('ruleForm')">重置</el-button>
    </el-form-item>
  </el-form>
  </div>
</template>
<style>
	#app {
		/* font-family: Helvetica, sans-serif; */
		font-family: "PingFang SC";
		text-align: center;
	}
</style>
  <script>
	  import axios from 'axios'
	  import Qs from 'qs'
	  axios.defaults.withCredentials = true; //让ajax携带cookie
    export default {
      data() {
        return {
          ruleForm: {
            pass: '',
            account: ''
          },
          rules: {
            pass: [
              { required:true, message:'请输入密码', trigger: 'blur' }
            ],
            account: [
              { required:true, message:'请输入用户名', trigger: 'blur' }
            ]
          }
        };
      },
      methods: {
        submitForm(formName) {
			console.log(formName)
          this.$refs[formName].validate((valid) => {
			  console.log(valid)
            if (valid) {
				const _this = this
				var data = Qs.stringify({"username":this.ruleForm.account,"password":this.ruleForm.pass})
				console.log(data)
				console.log(axios.defaults.withCredentials)
				axios.post("http://localhost:8000/login/",data).then(
				  function (resp) {
					var ses = window.sessionStorage
					console.log(resp)
					const result = resp.data.request
					// const flag = resp.data.request['flag']
					if (result == 'Login ok'){
					  // console.log(resp.data.request['flag'])
					  _this.$router.push("/home")
					}else if(result == 'Have Login' ){
						alert(result)
						_this.$router.push("/home")
					}else {
					  alert(result)
					}
				  }
				)
				
				
				// axios.post("http://localhost:8000/login/",data).then(
				//   function (resp) {
				// 	console.log(resp)
				// 	const result = resp.data.request
				// 	// const flag = resp.data.request['flag']
				// 	console.log(result)
				//   }
				// )
				
				
				
				
				
			  // alert('submit!');
            } else {
              console.log('error submit!!');
              return false;
            }
          });
        },
        resetForm(formName) {
          this.$refs[formName].resetFields();
        }
      }
    }
  </script>
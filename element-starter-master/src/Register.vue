<template>
  <div id="app">
  用户注册
<el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
  <el-form-item label="用户名" prop="account">
    <el-input v-model.string="ruleForm.account"></el-input>
  </el-form-item>
  <el-form-item label="密码" prop="pass">
    <el-input type="password" v-model="ruleForm.pass" autocomplete="off"></el-input>
  </el-form-item>
  <el-form-item label="确认密码" prop="checkPass">
    <el-input type="password" v-model="ruleForm.checkPass" autocomplete="off"></el-input>
  </el-form-item>
  <el-form-item label="邮箱地址" prop="email">
    <el-input v-model.string="ruleForm.email"></el-input>
  </el-form-item>
  
  
   <el-form-item label="性别">
      <el-select v-model="ruleForm.sex" placeholder="请选择性别">
        <el-option label="男" value="male"></el-option>
        <el-option label="女" value="femal"></el-option>
      </el-select>
    </el-form-item>
  
  
  <el-form-item>
    <el-button type="primary" @click="submitForm('ruleForm')">注册</el-button>
    <el-button @click="resetForm('ruleForm')">重置</el-button>
  </el-form-item>
</el-form>
  </div>
</template>


<script>
	import axios from 'axios'
	import Qs from 'qs'
	axios.defaults.withCredentials = true; //让ajax携带cookie
  export default {
    data() {
      var checkAcc = (rule, value, callback) => {
        if (!value) {
          return callback(new Error('用户名不能为空'));
        }else{
			callback()
		}
      };
      var validatePass = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请输入密码'));
        } else {
          if (this.ruleForm.checkPass !== '') {
            this.$refs.ruleForm.validateField('checkPass');
          }
          callback();
        }
      };
      var validatePass2 = (rule, value, callback) => {
        if (value === '') {
          callback(new Error('请再次输入密码'));
        } else if (value !== this.ruleForm.pass) {
          callback(new Error('两次输入密码不一致!'));
        } else {
          callback();
        }
      };
	  var checkemail = (rule, value, callback) => {
	      if (!value) {
	        return callback(new Error('邮箱不能为空'));
	      }else{
			  callback()
		  }
	    };
		var checksex = (rule, value, callback) => {
		    if (!value) {
		      return callback(new Error('性别不能为空'));
		    }else{
				callback()
			}
		  };
      return {
        ruleForm: {
          pass: '',
          checkPass: '',
          account: '',
		  email:''
        },
        rules: {
          pass: [
            { validator: validatePass, trigger: 'blur' }
          ],
          checkPass: [
            { validator: validatePass2, trigger: 'blur' }
          ],
          account: [
            { validator: checkAcc, trigger: 'blur' }
          ],
		  email:[
			  {validator:checkemail,trigger:'blur'}
		  ],
		  sex:[
			  {validator:checksex,trigger:'blur'}
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
				console.log(this.ruleForm.sex)
				var sex = this.ruleForm.sex ? this.ruleForm.sex : 'male'
				console.log(sex)
				var data = Qs.stringify({"username":this.ruleForm.account,"password1":this.ruleForm.pass,"email":this.ruleForm.email,"sex":sex})
				console.log(data)
				console.log(axios.defaults.withCredentials)
				axios.post("http://localhost:8000/register/",data).then(
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
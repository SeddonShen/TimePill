<template>
  <div id="app">
  用户注册
<el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
  <el-form-item label="用户名" prop="account">
    <el-input v-model.number="ruleForm.account"></el-input>
  </el-form-item>
  <el-form-item label="密码" prop="pass">
    <el-input type="password" v-model="ruleForm.pass" autocomplete="off"></el-input>
  </el-form-item>
  <el-form-item label="确认密码" prop="checkPass">
    <el-input type="password" v-model="ruleForm.checkPass" autocomplete="off"></el-input>
  </el-form-item>
  <el-form-item label="邮箱地址" prop="email">
    <el-input v-model.number="ruleForm.email"></el-input>
  </el-form-item>
  <el-form-item label="性别" prop="sex">
    <el-input v-model.number="ruleForm.sex"></el-input>
  </el-form-item>
  <el-form-item>
    <el-button type="primary" @click="submitForm('ruleForm')">注册</el-button>
    <el-button @click="resetForm('ruleForm')">重置</el-button>
  </el-form-item>
</el-form>
  </div>
</template>


<script>
  export default {
    data() {
      var checkAcc = (rule, value, callback) => {
        if (!value) {
          return callback(new Error('用户名不能为空'));
        }
        setTimeout(() => {
          if (!Number.isInteger(value)) {
            callback(new Error('请输入数字值'));
          } 
		  // else {
    //         if (value < 18) {
    //           callback(new Error('必须年满18岁'));
    //         } else {
    //           callback();
    //         }
    //       }
        }, 1000);
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
	      }
	  //     setTimeout(() => {
	  //       if (!Number.isInteger(value)) {
	  //         callback(new Error('请输入数字值'));
	  //       } 
	  // 	  // else {
	  // //         if (value < 18) {
	  // //           callback(new Error('必须年满18岁'));
	  // //         } else {
	  // //           callback();
	  // //         }
	  // //       }
	  //     }, 1000);
	    };
		var checksex = (rule, value, callback) => {
		    if (!value) {
		      return callback(new Error('性别不能为空'));
		    }
		//     setTimeout(() => {
		//       if (!Number.isInteger(value)) {
		//         callback(new Error('请输入数字值'));
		//       } 
		// 	  // else {
		// //         if (value < 18) {
		// //           callback(new Error('必须年满18岁'));
		// //         } else {
		// //           callback();
		// //         }
		// //       }
		//     }, 1000);
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
        this.$refs[formName].validate((valid) => {
          if (valid) {
            alert('submit!');
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
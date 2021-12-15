<template>
	<div id="app">
		<el-container>
			<el-header>
				<el-menu :default-active="activeIndex" mode="horizontal" @select="handleSelect">
					<el-menu-item>
						<div class="index-title"><i class="el-icon-edit"></i>时光胶囊</div>
					</el-menu-item>
					<el-menu-item index="1" @click="goTo('/')">首页</el-menu-item>
					<el-menu-item index="2" @click="goTo('home')">胶囊广场</el-menu-item>
					<el-menu-item index="3" @click="goTo('edit_pre')">写日记</el-menu-item>
					<el-menu-item index="4" @click="goTo('edit_pill')">写胶囊</el-menu-item>
					<el-menu-item index="5" @click="goTo('reg')" v-if="!islogin">注册</el-menu-item>
					<el-menu-item index="6" @click="goTo('login')" v-if="!islogin">登录</el-menu-item>
					<el-menu-item index="7" @click="" v-if="islogin">Hello,{{username}}!</el-menu-item>
					<el-menu-item index="8" @click="logout()" v-if="islogin">登出</el-menu-item>
				</el-menu>
			</el-header>
			<el-main>
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
		</el-main>
		<el-footer>
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
			
			var checkAcc = (rule, value, callback) => {
				if (!value) {
					return callback(new Error('用户名不能为空'));
				} else {
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
				} else {
					callback()
				}
			};
			var checksex = (rule, value, callback) => {
				if (!value) {
					return callback(new Error('性别不能为空'));
				} else {
					callback()
				}
			};
			return {
				ruleForm: {
					pass: '',
					checkPass: '',
					account: '',
					email: '',
					activeIndex: '5',
					islogin:false,
					username:''
				},
				rules: {
					pass: [{
						validator: validatePass,
						trigger: 'blur'
					}],
					checkPass: [{
						validator: validatePass2,
						trigger: 'blur'
					}],
					account: [{
						validator: checkAcc,
						trigger: 'blur'
					}],
					email: [{
						validator: checkemail,
						trigger: 'blur'
					}],
					sex: [{
						validator: checksex,
						trigger: 'blur'
					}]
				}
			};
		},
		created: function() {
			  var _this = this
			  axios.post("http://localhost:8000/login/", '').then(
			  	function(resp) {
			  		console.log(resp.data)
			  		console.log("122222222222222222222222")
					if(resp.data.request == 'Have Login'){
						_this.islogin = true
						_this.username = resp.data.user_name
					}
			  		// _this.set_user_id(resp.data.user_id)
			  		console.log(_this.islogin)
			  	}
			  )
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
						var data = Qs.stringify({
							"username": this.ruleForm.account,
							"password1": this.ruleForm.pass,
							"email": this.ruleForm.email,
							"sex": sex
						})
						console.log(data)
						console.log(axios.defaults.withCredentials)
						axios.post("http://localhost:8000/register/", data).then(
							function(resp) {
								var ses = window.sessionStorage
								console.log(resp)
								const result = resp.data.request
								// const flag = resp.data.request['flag']
								if (result == 'Login ok') {
									// console.log(resp.data.request['flag'])
									_this.$router.push("/home")
								} else if (result == 'Have Login') {
									alert(result)
									_this.$router.push("/home")
								} else {
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
			},
			goTo(url){
			//直接跳转
				this.$router.push(url);
			},
			logout(){
				var _this = this
				axios.get("http://localhost:8000/logout/", '').then(
					function(resp) {
						console.log(resp.data)
						_this.$notify({
						  title: "注销成功!",
						  type: "success",
						  message:
						    "谢谢!",
						  duration: 5000,
						});
						_this.islogin = false
						_this.username = ''
					}
				)
				this.$router.push('/');
			}
		}
	}
</script>

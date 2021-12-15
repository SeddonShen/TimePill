<template>
	<div id="app">
		<el-container>
			<el-header>

<el-menu :default-active="activeIndex" mode="horizontal" @select="handleSelect">
<el-menu-item >
<div class="index-title"><i class="el-icon-edit"></i>时光胶囊</div>
</el-menu-item>
<el-menu-item index="1" @click="goTo('/')">首页</el-menu-item>
<el-menu-item index="2" @click="goTo('home')">胶囊广场</el-menu-item>
<el-menu-item index="3" @click="goTo('edit_pre')" v-if="islogin">写日记</el-menu-item>
<el-menu-item index="4" @click="goTo('edit_pill')" v-if="islogin">写胶囊</el-menu-item>
<el-menu-item index="5" @click="goTo('reg')" v-if="!islogin">注册</el-menu-item>
<el-menu-item index="6" @click="goTo('login')" v-if="!islogin">登录</el-menu-item>
<el-menu-item index="7" @click="" v-if="islogin">Hello,{{username}}!</el-menu-item>
<el-menu-item index="8" @click="logout()" v-if="islogin">登出</el-menu-item>
</el-menu>
			</el-header>
			<el-main>
				<div>
					<span>日记广场</span>
					<el-divider></el-divider>
					<el-row :gutter="12">
						<el-col :span="8" class="margin" v-for="article in squaredata">
							<el-card class="box-card" shadow="hover">
								<div slot="header" class="clearfix">
									<span>{{article.title}}</span>
									<el-button style="float: right; padding: 3px 0" type="text" @click="toArticle(article.diary_type,article.id)">查看详情</el-button>
								</div>
								<!-- <el-tag>{{article.diary_type == 'pill' ? '普通日记' : '胶囊日记'}}</el-tag> -->
								<el-tag size="small" v-if="article.diary_type == 'pill' ">胶囊日记</el-tag>
								<el-tag size="small" type="success" v-if="article.diary_type !== 'pill' ">普通日记</el-tag>
								<div class="text item">
									{{article.content}}
								</div>
								<div class="text item">
									{{article.author}}
								</div>
							</el-card>
						</el-col>
					</el-row>
				</div>
				
				<div style="padding-top: 5%;">
					<span>我的日记</span>
					<el-divider></el-divider>
					<el-row :gutter="12">
						<el-col :span="8" class="margin" v-for="article in myarticles">
							<el-card class="box-card" shadow="hover">
								<div slot="header" class="clearfix">
									<span>{{article.title}}</span>
									<el-button style="float: right; padding: 3px 0" type="text" @click="toArticle(article.diary_type,article.id)">查看详情</el-button>
								</div>
								<!-- <el-tag>{{article.diary_type == 'pill' ? '普通日记' : '胶囊日记'}}</el-tag> -->
								<el-tag size="small" v-if="article.diary_type == 'pill' ">胶囊日记</el-tag>
								<el-tag size="small" type="success" v-if="article.diary_type !== 'pill' ">普通日记</el-tag>
								<div class="text item">
									{{article.content}}
								</div>
								<div class="text item">
									{{article.author}}
								</div>
							</el-card>
						</el-col>
					</el-row>
				</div>

				<div style="padding-top: 5%;">
					<span>我的胶囊</span>
					<el-divider></el-divider>
					<el-row :gutter="12">
						<el-col :span="8" class="margin" v-for="article in mypills">
							<el-card class="box-card" shadow="hover">
								<div slot="header" class="clearfix">
									<span>{{article.title}}</span>
									<el-button style="float: right; padding: 3px 0" type="text" @click="toArticle(article.diary_type,article.id)">查看详情</el-button>
								</div>
								<!-- <el-tag>{{article.diary_type == 'pill' ? '普通日记' : '胶囊日记'}}</el-tag> -->
								
								<el-tag size="small" v-if="article.diary_type == 'pill' ">胶囊日记</el-tag>
								<el-tag size="small" type="success" v-if="article.diary_type !== 'pill' ">普通日记</el-tag>
								<div class="text item">
									{{article.content}}
								</div>
								<div class="text item">
									{{article.author}}
								</div>
							</el-card>
						</el-col>
					</el-row>
				</div>
			</el-main>
			<el-footer class="bg-footer">
				<div class="footer-title">时光胶囊 © 2021 - 2021 All Copyright reserved</div>
			</el-footer>
		</el-container>
	</div>
</template>

<style>
	.margin {
		margin-top: 2%;
	}
	#app {
		/* font-family: Helvetica, sans-serif; */
		font-family: "PingFang SC";
	}
	.bg-footer{
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
				activeIndex: '2',
				squaredata:[],
				myarticles:[],
				mypills:[],
				islogin:false,
				username:''
			};
		},
		methods: {
			goTo(url) {
				//直接跳转
				this.$router.push(url);
			},
			toArticle(type,url){
				// this.$router.push(url)
				console.log(type)
				console.log(url)
				if(type == 'primary'){
					this.$router.push("/article/" + url);
				}else if(type == 'pill'){
					this.$router.push("/pill/" + url);
				}else{
					this.$notify({
					  title: "数据错误",
					  type: "error",
					  message:
					    "日记数据读取出错!",
					  duration: 2000,
					});
				}
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
		},
		created: function() {
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
			),
			console.log("NB")
			var _this = this
			axios.get("http://localhost:8000/articles/", '').then(
				function(resp) {
					console.log(resp.data.articles)
					const result = resp.data.articles
					_this.squaredata = result
					// console.log(_this.squaredata[0].author)
					// const flag = resp.data.request['flag']

				}
			)
			
			axios.get("http://localhost:8000/myarticles/", '').then(
				function(resp) {
					console.log(resp.data)
					console.log(resp.data.articles)
					const result = resp.data.articles
					_this.myarticles = result
				}
			)
			
			axios.get("http://localhost:8000/mypills/", '').then(
				function(resp) {
					console.log(resp.data)
					console.log(resp.data.articles)
					const result = resp.data.articles
					_this.mypills = result
					console.log("attation")
					console.log(_this.mypills)
				}
			)
			
		},
	}
</script>

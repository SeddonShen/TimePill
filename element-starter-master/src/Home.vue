<template>
	<div id="app">
		<el-container>
			<el-header>

				<el-menu :default-active="activeIndex" mode="horizontal">
					<el-menu-item index="1" @click="goTo('/')">首页</el-menu-item>
					<el-menu-item index="2" @click="goTo('home')">胶囊广场</el-menu-item>
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
									<el-button style="float: right; padding: 3px 0" type="text">查看详情</el-button>
								</div>
								<el-tag>胶囊日记</el-tag>
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
						<el-col :span="8" class="margin" v-for="article in squaredata">
							<el-card class="box-card" shadow="hover">
								<div slot="header" class="clearfix">
									<span>{{article.title}}</span>
									<el-button style="float: right; padding: 3px 0" type="text">查看详情</el-button>
								</div>
								<el-tag type="success">普通日记</el-tag>
								<div v-for="o in 4" :key="o" class="text item">
									{{'列表内容 ' + o }}
									
								</div>
							</el-card>
						</el-col>
					</el-row>
				</div>

				<div style="padding-top: 5%;">
					<span>我的胶囊</span>
					<el-divider></el-divider>
					<el-row :gutter="12">
						<el-col :span="8" class="margin" v-for="(o, index) in 6" :key="o">
							<el-card class="box-card" shadow="hover">
								<div slot="header" class="clearfix">
									<span>卡片名称</span>
									<el-button style="float: right; padding: 3px 0" type="text">查看详情</el-button>
								</div>
								<el-tag type="success">普通日记</el-tag>
								<div v-for="o in 4" :key="o" class="text item">
									{{'列表内容 ' + o }}
									
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
</style>


<script>
	import axios from 'axios'
	import Qs from 'qs'
	axios.defaults.withCredentials = true; //让ajax携带cookie
	export default {
		data() {
			return {
				activeIndex: '2',
				squaredata:[]
			};
		},
		methods: {
			goTo(url) {
				//直接跳转
				this.$router.push(url);
			},
		},
		created: function() {
			console.log("NB")
			var _this = this
			axios.get("http://localhost:8000/articles/", '').then(
				function(resp) {
					var ses = window.sessionStorage
					console.log(resp.data.articles)
					const result = resp.data.articles
					_this.squaredata = result
					console.log(_this.squaredata[0].author)
					// const flag = resp.data.request['flag']

				}
			)
			
			axios.get("http://localhost:8000/myarticles/", '').then(
				function(resp) {
					console.log(resp.data)
			
				}
			)
			
		},
	}
</script>

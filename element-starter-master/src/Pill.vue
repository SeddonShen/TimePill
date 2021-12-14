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

				
<!-- 				<div style="padding-top: 5%;">
					<span>我的日记</span>
					<el-divider></el-divider>
					<el-row :gutter="12">
						<el-col :span="8" class="margin" v-for="article in article">
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
				</div> -->

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
				id:'',
				article:[],
			};
		},
		methods: {
			goTo(url) {
				//直接跳转
				this.$router.push(url);
			},
			toArticle(url){
				// this.$router.push(url)
				console.log(url)
			}
		},
		created: function() {
			console.log("NB")
			var _this = this
			// this.id = this.$route.params.id;
			// this.myName=this.$route.params.name;
			this.id = this.$route.params.id
			console.log(this.id)
			console.log(this.$route.params.id)
			
			axios.get("http://localhost:8000/pilldetail/" + this.id, '').then(
				function(resp) {
					console.log(resp.data)
					// console.log(resp.data.articles)
					// const result = resp.data.articles
					// _this.article = result
				}
			)
			

			
		},
	}
</script>

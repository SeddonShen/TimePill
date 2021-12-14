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
				
				<el-descriptions class="margin-top" :column="3" border>
					<el-descriptions-item>
						<template slot="label">
							<i class="el-icon-user"></i>
							记录人
						</template>
						{{article.author}}
					</el-descriptions-item>
					<el-descriptions-item>
						<template slot="label">
							<i class="el-icon-mobile-phone"></i>
							文章ID
						</template>
						{{article.id}}
					</el-descriptions-item>
					<el-descriptions-item>
						<template slot="label">
							<i class="el-icon-location-outline"></i>
							日记类型
						</template>
						{{article.diary_type == 'pill' ? '胶囊日记' : '2'}}
					</el-descriptions-item>
					<el-descriptions-item>
						<template slot="label">
							<i class="el-icon-tickets"></i>
							到期公开
						</template>
						<el-tag size="small">{{article.square_open ? '公开' : '不公开'}}</el-tag>
					</el-descriptions-item>
					<el-descriptions-item>
						<template slot="label">
							<i class="el-icon-office-building"></i>
							解封时间
						</template>
						{{article.expire_time}}
					</el-descriptions-item>
				</el-descriptions>
				<div style="padding: 20px;">
					<div style="font-size: 30px; text-align: center;">{{article.title}}</div>
				</div>
				{{article.square_open ? '' : 'text-align: center;'}}
				<div style="text-align: center;" v-if="!article.status">
					<!-- content -->
					{{article.content}}
				</div>
				<div style="text-indent:2em ;" v-if="article.status">
					<!-- content -->
					{{article.content}}
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
				id: '',
				article: [],
			};
		},
		methods: {
			goTo(url) {
				//直接跳转
				this.$router.push(url);
			},
			toArticle(url) {
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
					_this.article = resp.data.article
					// console.log(resp.data.articles)
					// const result = resp.data.articles
					// _this.article = result
				}
			)
		},
	}
</script>

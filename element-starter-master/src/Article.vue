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
					   <template slot="extra">
					      <el-button type="primary" size="small" @click="toArticle(article.id)">编辑</el-button>
						  <el-button type="danger" size="small" @click="art_delete(article.id)" >删除</el-button>
					    </template>
					<el-descriptions-item>
						<template slot="label">
							<i class="el-icon-user"></i>
							记录人
						</template>
						{{article.author}}
					</el-descriptions-item>
					<el-descriptions-item>
						<template slot="label">
							<i class="el-icon-reading"></i>
							文章ID
						</template>
						{{article.id}}
					</el-descriptions-item>
					<el-descriptions-item>
						<template slot="label">
							<i class="el-icon-notebook-1"></i>
							日记类型
						</template>
						{{article.diary_type == 'pill' ? '胶囊日记' : '普通日记'}}
					</el-descriptions-item>
					<el-descriptions-item>
						<template slot="label">
							<i class="el-icon-date"></i>
							到期公开
						</template>
						<el-tag size="small" type="success" v-if="article.square_open">公开</el-tag>
						<el-tag size="small" type="danger" v-if="!article.square_open">不公开</el-tag>
					</el-descriptions-item>
					<el-descriptions-item>
						<template slot="label">
							<i class="el-icon-date"></i>
							记录时间
						</template>
						{{article.expire_time}}
					</el-descriptions-item>
				</el-descriptions>
				
				<div style="padding: 20px;">
					<div style="font-size: 30px; text-align: center;">{{article.title}}</div>
				</div>
				<!-- {{article.square_open ? '' : 'text-align: center;'}} -->
				<div style="text-align: center;" v-if="!article.status">
					<!-- content -->
					{{article.content}}
				</div>
				<div style="text-align: left;font-size: 1.25rem;margin-bottom: 1.25rem;">
					<span>日记内容:</span>
				</div>
				<div style="text-indent:2em ;" v-if="article.status">
					<!-- content -->
					{{article.content}}
				</div>
				<!-- <div style="text-align: center;">
					<comment></comment>
				</div> -->
				<div style="text-align: left;font-size: 1.25rem;margin-bottom: 1.25rem;margin-top: 1.25rem;">
					<span>评论区:</span>
				</div>
				<div style="text-align: left;" v-if="comments.length > 0">
					<div v-for="comment in comments">
					<span>
						<el-link type="primary" @click="setpre_comment(comment.id)">回复</el-link>
						<el-link type="danger" v-if="comment_owner== comment.author_id " @click="delete_comment(comment.id)">删除</el-link>     评论ID:#{{comment.id}} 评论人:{{comment.comment_author}}{{comment.pre_comment ? ' 回复#'+comment.pre_comment +'  ': ''}}    说:  {{comment.comment_content}}</span>
					    <el-divider></el-divider>
					</div>
				</div>
				<div style="text-align: center;" v-else>
					暂无评论,做第一个评论的人吧!
				</div>
				<div style="text-align: left;font-size: 1.25rem;margin-bottom: 1.25rem;">
					<span>发表评论:    </span><el-link type="primary"  @click="cancel_comment()" v-if="pre_comment">   取消回复</el-link>
				</div>
<el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
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
	// import comment from 'bright-comment'
	// // components:{
	// //   comment
	// // },
	axios.defaults.withCredentials = true; //让ajax携带cookie
	export default {
		// components:{
		//   comment
		// },
		data() {
			return {
				activeIndex: '2',
				id: '',
				article: [],
				comments:[],
				pre_comment:'',
				comment_owner:[],
				ruleForm: {
				  content: '',
				},
				rules: {
				  content: [
				    { required: true, message: '请填写日记内容', trigger: 'blur' }
				  ]
				}
			};
		},
		methods: {
			setpre_comment(id){
				this.pre_comment = id
			},
			cancel_comment(){
				this.pre_comment = ""
			},
			goTo(url) {
				//直接跳转
				this.$router.push(url);
			},
			toArticle(url) {
				// this.$router.push(url)
				console.log(url)
				this.$router.push("/edit_pre/" + url);
			},
			art_delete(id){
				        this.$confirm('此操作将永久删除该日记, 是否继续?', '提示', {
				          confirmButtonText: '确定',
				          cancelButtonText: '取消',
				          type: 'warning'
				        }).then(() => {
							// modify_article
						axios.delete("http://localhost:8000/articles/"+ this.id,'').then(
						  function (resp) {
							console.log(resp)
						  }
						)
						this.$router.push("/home")
				          this.$message({
				            type: 'success',
				            message: '删除成功!'
				          });
				        }).catch(() => {
				          this.$message({
				            type: 'info',
				            message: '已取消删除'
				          });          
				        });
			},
			submitForm(formName) {
				this.$refs[formName].validate((valid) => {
				  if (valid) {
						console.log(this.ruleForm)
						this.$notify({
						  title: "提交成功",
						  type: "success",
						  message:
						    "评论已生成,请刷新页面!",
						  duration: 5000,
						});
						var temp_pre_comment
						if(this.pre_comment ==''){
							temp_pre_comment = null
						}else{
							temp_pre_comment = this.pre_comment
						}
						var data = {
							"comment_content":this.ruleForm.content,
							"pre_comment":temp_pre_comment
							}
						console.log(data)
						var _this = this
						console.log(axios.defaults.withCredentials)
						axios.post("http://localhost:8000/add_comment/"+this.id,data).then(
						  function (resp) {
							console.log(resp)
							// window.reload()
							// _this.$router.push('/article/');
						  }
						)
						axios.get("http://localhost:8000/comments/" + this.id, '').then(
							function(resp) {
								console.log("--------------test-----------")
								console.log(resp)
								_this.comments = resp.data.comments
								// _this.article = resp.data.article
								// console.log(resp.data.articles)
								// const result = resp.data.articles
								// _this.article = result
							}
						)
						this.$refs[formName].resetFields();
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
			set_user_id(id){
				this.author_id = id
			},
			delete_comment(id){
				this.$confirm('此操作将永久删除该评论, 是否继续?', '提示', {
				  confirmButtonText: '确定',
				  cancelButtonText: '取消',
				  type: 'warning'
				}).then(() => {
					// modify_article
				axios.delete("http://localhost:8000/del_com/"+ id,'').then(
				  function (resp) {
					console.log(resp)
				  }
				)
				// this.$router.push("/home")
				  this.$message({
				    type: 'success',
				    message: '删除成功!'
				  });
				}).catch(() => {
				  this.$message({
				    type: 'info',
				    message: '已取消删除'
				  });          
				});
				// http://127.0.0.1:8000/del_com/2
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
			axios.post("http://localhost:8000/login/", '').then(
				function(resp) {
					console.log(resp.data)
					console.log("122222222222222222222222")
					// _this.set_user_id(resp.data.user_id)
					_this.comment_owner = resp.data.user_id
					console.log(_this.comment_owner)
				}
			)
			axios.get("http://localhost:8000/pilldetail/" + this.id, '').then(
				function(resp) {
					console.log(resp.data)
					_this.article = resp.data.article
					// console.log(resp.data.articles)
					// const result = resp.data.articles
					// _this.article = result
				}
			)
			//123
			axios.get("http://localhost:8000/comments/" + this.id, '').then(
				function(resp) {
					console.log("--------------test-----------")
					console.log(resp)
					_this.comments = resp.data.comments
					// _this.article = resp.data.article
					// console.log(resp.data.articles)
					// const result = resp.data.articles
					// _this.article = result
				}
			)
		},
	}
</script>

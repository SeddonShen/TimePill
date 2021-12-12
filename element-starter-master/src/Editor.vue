<template>
	<div id="app">
		<el-container>
			<el-header>

				<el-menu :default-active="activeIndex" mode="horizontal">


					<el-menu-item index="0"><i class="el-icon-edit"></i>写日记</el-menu-item>
					<el-menu-item index="1" @click="goTo('/')">首页</el-menu-item>
					<el-menu-item index="2" @click="goTo('home')">胶囊广场</el-menu-item>


				</el-menu>
			</el-header>
			<el-main>


				<el-form ref="form" :model="form" label-width="80px">
					<el-form-item label="日记标题">
						<el-input v-model="form.name"></el-input>
					</el-form-item>


					<el-form :inline="true">
						<el-form-item label="广场公开">
							<el-switch v-model="form.delivery"></el-switch>
						</el-form-item>
						<el-form-item label="日记类型">
							<el-select v-model="form.region" placeholder="请选择日记类型">
								<el-option label="胶囊日记" value="shanghai"></el-option>
								<el-option label="普通日记" value="beijing"></el-option>
							</el-select>
						</el-form-item>
					</el-form>


					<el-form-item label="解封时间">
						<el-col :span="11">
							<el-date-picker type="date" placeholder="选择日期" v-model="form.date1" style="width: 100%;"></el-date-picker>
						</el-col>
						<el-col class="line" :span="2">-</el-col>
						<el-col :span="11">
							<el-time-picker placeholder="选择时间" v-model="form.date2" style="width: 100%;"></el-time-picker>
						</el-col>
					</el-form-item>

					<!--  <el-form-item label="活动性质">
    <el-checkbox-group v-model="form.type">
      <el-checkbox label="美食/餐厅线上活动" name="type"></el-checkbox>
      <el-checkbox label="地推活动" name="type"></el-checkbox>
      <el-checkbox label="线下主题活动" name="type"></el-checkbox>
      <el-checkbox label="单纯品牌曝光" name="type"></el-checkbox>
    </el-checkbox-group>
  </el-form-item>
  <el-form-item label="特殊资源">
    <el-radio-group v-model="form.resource">
      <el-radio label="线上品牌商赞助"></el-radio>
      <el-radio label="线下场地免费"></el-radio>
    </el-radio-group>
  </el-form-item> -->
					<el-form-item label="日记内容">
						<el-input type="textarea" v-model="form.desc"></el-input>
					</el-form-item>
					<el-form-item>
						<el-button type="primary" @click="onSubmit">立即创建</el-button>
						<el-button>取消</el-button>
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
	export default {
		data() {
			return {
				activeIndex: '0',
				form: {
					name: '',
					region: '',
					date1: '',
					date2: '',
					delivery: false,
					// type: [],
					// resource: '',
					desc: ''
				}
			};
		},
		methods: {
			goTo(url) {
				//直接跳转
				this.$router.push(url);
			},
			onSubmit() {
				console.log('submit!');
			}
		},
	};
</script>

<style>
	#app {
		/* font-family: Helvetica, sans-serif; */
		font-family: "PingFang SC";
		text-align: center;
	}
</style>

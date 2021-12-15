<template>
  <div id="app">
    <el-container>
      <el-header>
        
<el-menu :default-active="activeIndex" mode="horizontal" @select="handleSelect">
<el-menu-item >
<div class="index-title"><i class="el-icon-edit"></i>时光胶囊</div>
</el-menu-item>
<el-menu-item index="1">首页</el-menu-item>
<el-menu-item index="2" @click="goTo('home')">胶囊广场</el-menu-item>
<el-menu-item index="3" @click="goTo('edit_pre')">写日记</el-menu-item>
<el-menu-item index="4" @click="goTo('edit_pill')">写胶囊</el-menu-item>
<el-menu-item index="5" @click="goTo('reg')" v-if="!islogin">注册</el-menu-item>
<el-menu-item index="6" @click="goTo('login')" v-if="!islogin">登录</el-menu-item>
<el-menu-item index="7" @click="" v-if="islogin">Hello,{{username}}!</el-menu-item>
<el-menu-item index="8" @click="logout()" v-if="islogin">登出</el-menu-item>
</el-menu>
      </el-header>
      <el-main class="bg-purple">

        <el-row :gutter="20">
      <el-col :span="8" :offset="8">
        <!-- <div class="grid-content bg-purple">
          
          <el-card :body-style="{ padding: '0px' }" class="icon">
            <img src="./pixel.png" />
          </el-card>

        </div> -->
        <div class="icon"><img src="./pixel.jpg" /></div>
      </el-col>
      <!-- 每日一记， -->
    </el-row>
      <el-button @click="goTo('edit_pill')">写一颗胶囊</el-button>
      <el-button @click="goTo('edit_pre')">写一封日记</el-button>
    </el-main>

      <el-footer class="bg-footer">
		   <!-- <comment></comment> -->
        <div class="footer-title">时光胶囊 © 2021 - 2021 All Copyright reserved</div>
      </el-footer>
  </el-container>
    
    

  </div>
</template>

<script>
	import {store} from './store.js'
	// import comment from 'hbl-comment'
	import axios from 'axios'
	axios.defaults.withCredentials = true; //让ajax携带cookie
export default {
	// components:{
	//   comment
	// },
	
  data() {
      return {
        activeIndex: '1',
		// state:store.state,
		islogin:false,
		username:''
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
    startHacking() {
	  console.log(this.state)
	  console.log(store)
	  store.set_login('ssd')
	  console.log(store)
      this.$notify({
        title: "启动成功!",
        type: "success",
        message:
          "老宣勇敢飞，东东永相随!",
        duration: 1000,
      });
	  console.log(store)
	  // store.logout()
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
  },
};
</script>

<style>
#app {
  /* font-family: Helvetica, sans-serif; */
  font-family: "PingFang SC";
  text-align: center;
}

.icon img{
  text-align: center;
  width: 50%;
  /* height: 10%; */
  /* width: 10%; */
  border-radius: 2500px;
  animation: rotate 10s linear infinite;
}

.el-col {
  border-radius: 4px;
}
.bg-purple {
  background: rgb(236, 245, 255);
}
.bg-purple-light {
  background: #e5e9f2;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.row-bg {
  padding: 10px 0;
  background-color: #f9fafc;
}
.index-title{
  font-size: 20px;
  /* line-height: 1.7; */
}
.bg-footer{
  background-color: #f7fbfd;
}
.footer-title{
  text-align: center;
  line-height: 1.7;
    position: relative;
  top:25%;
}
</style>

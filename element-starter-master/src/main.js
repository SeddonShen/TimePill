import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import Home from './Home.vue'
import Index from './Index.vue'
import Login from './Login.vue'
import Register from './Register.vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import Editor_pill from './Editor_pill.vue'
import Editor_pre from './Editor_pre.vue'
import Article from './Article.vue'
import Pill from './Pill.vue'
import comment from 'bright-comment'
// import comment from 'hbl-comment'
import axios from 'axios'
axios.defaults.withCredentials = true; //让ajax携带cookie

Vue.use(ElementUI)
Vue.use(VueRouter)
// 路由参考文章
// https://blog.csdn.net/sinat_17775997/article/details/80688397

//SessionStorage
//https://www.jianshu.com/p/2578cc444b70


let router = new VueRouter({
  routes: [
      //一个个对象
      { path: '/', component: Index ,meta:{needLogin:false}},
      { path: '/home', component: Home ,meta:{needLogin:true}},
      { path: '/login', component: Login ,meta:{needLogin:false}},
      { path: '/reg', component: Register ,meta:{needLogin:false}},
	  { path: '/edit_pre', component: Editor_pre ,meta:{needLogin:true}},
	  { path: '/edit_pre/:id', component: Editor_pre ,meta:{needLogin:true}},
	  { path: '/edit_pill', component: Editor_pill ,meta:{needLogin:true}},
	  { path: '/edit_pill/:id', component: Editor_pill ,meta:{needLogin:true}},
	  { path: '/article/:id', component: Article ,meta:{needLogin:true}},
	  { path: '/pill/:id', component: Pill ,meta:{needLogin:true}}
  ]
});

router.beforeEach((to,from,next)=>{
	console.log(to)
	if(to.meta.needLogin){
		console.log("要登录")
		var _this = this
		axios.post("http://localhost:8000/login/", '').then(
			function(resp) {
				console.log(resp.data)
				console.log("122222222222222222222222")
			  if(resp.data.request == 'Have Login'){
				next()
			  }else{
				  alert('未登录')
			  }
				// _this.set_user_id(resp.data.user_id)
			}
		)

	}else{
		console.log("无需登录")
		next()
	}
})



//new Vue 启动
new Vue({
  el: '#app',
  //让vue知道我们的路由规则
  router: router, //可以简写router
  render: c => c(App),
  components:{
		comment
  },
})
// Vue.component('comment', { /* ... */ })

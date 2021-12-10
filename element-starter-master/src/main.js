import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import Home from './Home.vue'
import Index from './Index.vue'
import Login from './Login.vue'
import Register from './Register.vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'

Vue.use(ElementUI)
Vue.use(VueRouter)
// 路由参考文章
// https://blog.csdn.net/sinat_17775997/article/details/80688397
let router = new VueRouter({
  routes: [
      //一个个对象
      { path: '/', component: Index },
      { path: '/home', component: Home },
      { path: '/login', component: Login },
      { path: '/reg', component: Register },
  ]
});
//new Vue 启动
new Vue({
  el: '#app',
  //让vue知道我们的路由规则
  router: router, //可以简写router
  render: c => c(App),
})

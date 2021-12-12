// axios 配置
import axios from 'axios'
import store from './store.js'
// axios 全局配置
axios.defaults.baseURL = 'http://127.0.0.1:8000/';
axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true

// 请求拦截
axios.interceptors.request.use(
  config => {
    if (store.getters.token) { // 若存在token，则每个Http Header都加上token
      config.headers.Authorization = `token ${store.getters.token}`
    }
    console.log('request请求配置', config)
    console.log(`token is ${store.getters.token}`)
    return config
  },
  err => {
    return Promise.reject(err)
  })
// 响应 拦截
axios.interceptors.response.use(
  response => {
    // console.log('成功响应：', response)
    return response
  },
  error => {
    if (error.response) {
      console.log(error.response)
    }
    return Promise.reject(error.response) // 返回接口返回的错误信息
  }
)
export default axios
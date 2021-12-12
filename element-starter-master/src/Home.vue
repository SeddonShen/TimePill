<template>
  <div id="app">
  Home
  看和一个写的链接
  </div>
</template>

<script>
	import axios from 'axios'
	import Qs from 'qs'
	axios.defaults.withCredentials = true; //让ajax携带cookie
    export default {
        data(){
            return {}
        },
		created:function(){
			console.log("NB")
			axios.get("http://localhost:8000/articles/",'').then(
			  function (resp) {
				var ses = window.sessionStorage
				console.log(resp)
				const result = resp.data.request
				// const flag = resp.data.request['flag']

			  }
			)
		},
    }
</script>
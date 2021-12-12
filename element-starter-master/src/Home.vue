<template>
  <div id="app">
  Home
  看和一个写的链接
  </div>
</template>

<script>
    export default {
        data(){
            return {}
        },
		created:function(){
			console.log("NB")
		},
		axios.post("http://localhost:8000/login/",data).then(
		  function (resp) {
			var ses = window.sessionStorage
			console.log(resp)
			const result = resp.data.request
			// const flag = resp.data.request['flag']
			if (result == 'Login ok'){
			  // console.log(resp.data.request['flag'])
			  _this.$router.push("/home")
			}else if(result == 'Have Login' ){
				alert(result)
				_this.$router.push("/home")
			}else {
			  alert(result)
			}
		  }
		)
    }
</script>
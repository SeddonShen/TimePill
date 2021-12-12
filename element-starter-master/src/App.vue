<template>
    <div>
		
<!-- 	    <div class="A">
	        我是 A组件
	       <ul>
	           <li v-for="(todo,index) in todos" 
	           :key="index" :class="todo.done?'done':''" @click="setDone(index)">
	           {{todo.text}}
	           </li>
	       </ul>
	    </div>	 -->
		
        <!-- 留坑，非常重要 -->
        <router-view></router-view>
    </div>
</template>
<!-- // <script>
//     export default {
//         data(){
//             return {}
//         }
//     }
// </script> -->



<script>
import {store} from './store.js'
export default {
    name: 'A',
    data(){
        return store.state
    },
    methods: {
        setDone(index){
            store.setDone(index)
			sessionStorage.getItem()
        }
    }
}
</script>





<style scoped>
.A{
    background: red;
    color: white;
    padding: 20px;
}
.A li.done{
    background: green;
}
</style>
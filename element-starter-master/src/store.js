//store.js
export const store = {
    state: {
		is_login:false,
		username:""
        // todos: [
        //     {text: '写语文作业', done: false},
        //     {text: '做数学卷子', done: false}
        // ]
    },
    set_login(username){
		this.state.is_login = true
		this.state.username = username
    },
    logout(){
		this.state.is_login = false
		this.state.username = ''
    }
}
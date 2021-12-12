//store.js
export const store = {
    state: {
        todos: [
            {text: '写语文作业', done: false},
            {text: '做数学卷子', done: false}
        ]
    },
    addTodo(str){
        const obj = {text: str, done: false}
        this.state.todos.push(obj)
    },
    setDone(index){
        this.state.todos[index].done = true
    }
}
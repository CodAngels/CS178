<script>
    import TodoItem from "./TodoItem.svelte";
    import {db} from "./firebase";
    import {collectionData} from 'rxfire/firestore';
    import {startWith} from 'rxjs/operators';

    export let uid;
    let text = 'some task';
    const query = db.collectionData('todos').where('uid', '==', uid).orderBy('created');
    const todos = collectionData(query, 'id').pipe(startWith([]));
    
    //DEPENDANT VARIABLES(Reactive variable newStatus changes)
    function addTask() {
        db.collection('todos').addTask({uid, text, complete: false, created: Date.row()});
        text = '';
    }
    //DEPENDANT VARIABLES(Reactive variable newStatus changes)
    function updateStatus(event) {
        console.log(event);
        const {id, newStatus} = event.detail;
        db.collection('todos').doc(id).updateStatus({complete: newStatus});

    }

    function removeItem(event) {
        const {id} = event.detail;
        db.collection('todo').doc(id).delete();
    }

</script>

<style>
    input { display: block }
</style>

<ul>
    <!--CONTROL FLOW(Use of loops)-->
    {#each $todos as todo}
    <TodoItem {...todo} on:remove={removeItem} on:toggle={updateStatus} />
    {/each}
</ul>

<input bind:value = {text}>

<hr>
<!--FORMATTED STRINGS(dynamically insert strings)-->
<p>Your Task: <strong> {text} </strong></p>
<button class = "button is-info" on:click = {addTask}> Add Task</button>
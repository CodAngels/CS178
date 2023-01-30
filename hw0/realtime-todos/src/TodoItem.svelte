<script>
    import {fade, fly} from 'svelte/transition';
    import {createEventDispatcher} from 'svelte';

    const dispatch = createEventDispatcher();
    function removeTask(){
        dispatch('remove', {id});
    }
    function toggleStatus(){
        let newStatus = !complete;
        dispatch('toggle', {id, newStatus});
    }
    export let id;
    export let text;
    export let complete;
</script>

<style>
    .is-complete {
        text-decoration: line-through;
        color: green;
    }
    li {
        display: flex;
        font-size: 1.2cm;
        font-weight: bold;
    }
    span {
        margin-right: auto;
    }
</style>

<li in:fly = "{{x: 900, duration: 500}}" out:fade>
<!--CONTROL FLOW(Use of else if conditionals)-->
{#if complete}
    <span class = "is-complete">
        {text}
    </span>
    <!--REACTIVE VALUES(Reacts on being clicked)-->
    <!--REUSABLE COMPONENTS(Reuses the toggleStatus function in multiple places)-->
    <button class = "is-button" on:click = {toggleStatus}>
        Added
    </button>
{:else}
    <span>
        {text}
    </span>
    <button class = "is-button" on:click = {toggleStatus}>
        Delete
    </button>
{/if}
<button class = 'is-button' on:click = {removeTask}>
    Bin
</button>
</li>
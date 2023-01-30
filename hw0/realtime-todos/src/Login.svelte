<script>
    import Profile from "./Profile.svelte";
    import Todos from "./Todos.svelte";
    import { authState } from 'rxfire/auth';
    import { auth, GoogleAuthProvider } from "firebase/auth";
    
    let user;
    const unsubcribe = authState(auth).subscribe(u => user = u);
    function login(){
        auth.signInWithPopup(GoogleAuthProvider);
    }

</script>

<style>
    section{
        background: rgb(235, 235, 235);
        padding: 20x;
    }
</style>

<section>
<!-- #CONTROL FLOW(Use of if and else) -->
{#if user}
    <Profile {...user}/>
    <button on:click = {() => auth.signOut()} class = "button"> Logout</button>
    <hr>
    <Todos uid = {user.uid}/>
{:else}
    <button on:click = {login} class = "button">
        Sign in with Google
    </button>
{/if}
</section>
<script>
    export let displayName;
    export let photoURL;
    export let uid;
</script>

<!--FORMATTED STRINGS(dynamically insert strings)-->
<h3>Hi { displayName }</h3>
<img src= {photoURL} width = "100" alt = "user avatar">
<p>Your user id is {uid} </p>
<template>
    <div class="wrapper">
        Profile
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';


export default defineComponent({
    name: 'Profile',
    mounted() {
        document.title = 'Profile'
    }
})

</script>

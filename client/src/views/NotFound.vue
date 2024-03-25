<template>
    <div class="center">
       <h1>404</h1>
       <span>Page not found</span>
    </div>
</template>
   
<script>
import { defineComponent } from 'vue';

    export default defineComponent({
        name: 'NotFound'
    })
</script>

<style scoped lang="scss">
    .center {
        display: flex;
        flex-direction: column;
        width: 100%;
        height: 100vh;
        align-items: center;
        justify-content: center;

        h1 {
            color: rgba(221, 221, 221, 1);
            font-size: 200px;
            font-weight: 400;
            line-height: 0;
        }

        span {
            color: rgba(119, 119, 119, 1);
            font-size: 32px;
            font-weight: 400;
        }
    }
</style>
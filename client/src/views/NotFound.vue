<template>
    <div class="center">
       <h1>404</h1>
       <span>Page not found</span>
    </div>
</template>
   
<script>
import { defineComponent } from 'vue';

    export default defineComponent({
        name: 'NotFound',
        mounted() {
            document.title = '404'
        }
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
            color: var(--color-not-found-h1);
            font-size: 200px;
            font-weight: 400;
            line-height: 0;
        }

        span {
            color: var(--form-placeholder-color);
            font-size: 32px;
            font-weight: 400;
        }
    }
</style>
<template>
    <button class="button" type="submit">{{ text }}</button>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'Button',
    props: {
        text: {
            type: String,
            required: true,
        }
    },
})
</script>

<style scoped lang="scss">
.button {
    all: unset;

    background: #fff;
    cursor: pointer;
    font-size: 28px;
    font-weight: 400;
    line-height: 52px;
    color: rgba(51, 51, 51, 1);
    padding: 0 35px;
    box-shadow: var(--box-shadow);
    border-radius: 4px;
    margin-top: 40px;
}
</style>

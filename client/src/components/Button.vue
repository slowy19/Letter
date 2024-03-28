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

    background: var(--white);
    cursor: pointer;
    font-size: 28px;
    font-weight: 400;
    line-height: 52px;
    color: var(--black);
    padding: 0 35px;
    box-shadow: var(--box-shadow);
    border-radius: 4px;
    margin-top: 40px;
}
</style>

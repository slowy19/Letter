<template>
    <input type="text" class="input" />
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'InputSearch',
})
</script>

<style scoped lang="scss">
.input {
    all: unset;

    width: 100%;
    // max-width: 250px;
    // box-shadow: var(--box-shadow);
    font-size: 16px;
    font-weight: 400;
    color: var(--black);
    text-align: left;
    padding: 14px 25px;
    border-radius: 40px;
    background: rgba(238, 238, 238, 1);

    &::placeholder {
        font-size: 16px;
        font-weight: 400;
        color: var(--gray);
    }
}
</style>

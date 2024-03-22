<template>
    <input type="text" class="input" />
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';

export default class InputDefault extends Vue {}
</script>

<style scoped lang="scss">
.input {
    all: unset;

    width: 100%;
    max-width: 480px;
    border-bottom: 1px solid rgba(221, 221, 221, 1);
    // box-shadow: var(--box-shadow);
    font-size: 24px;
    font-weight: 400;
    line-height: 44px;
    color: #fff;
    text-align: left;
    padding: 0 10px;

    &::placeholder {
        font-size: 24px;
        font-weight: 400;
        line-height: 44px;
        color: rgba(119, 119, 119, 1);
    }
}
</style>

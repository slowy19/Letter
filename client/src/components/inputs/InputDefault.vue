<template>
    <div class="inputParrent">
        <Field :name="name" class="input" :placeholder="placeholder" />
        <ErrorMessage :name="error" class="error" />
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { Field, ErrorMessage } from 'vee-validate';


export default defineComponent({
    name: 'InputDefault',
    props: {
        name: {
            type: String,
            required: true
        },
        error: {
            type: String,
            required: true
        },
        placeholder: {
            type: String,
            required: false
        },
    },
    components: {
        Field,
        ErrorMessage
    }
})
</script>

<style scoped lang="scss">
.inputParrent {
    display: flex;
    flex-direction: column;
    gap: 8px;
}

.input {
    all: unset;

    width: 100%;
    max-width: 500px;
    border-bottom: 1px solid rgba(221, 221, 221, 1);
    // box-shadow: var(--box-shadow);
    font-size: 24px;
    font-weight: 400;
    line-height: 44px;
    color: var(--white);
    text-align: left;
    padding: 0 10px;

    &::placeholder {
        font-size: 24px;
        font-weight: 400;
        line-height: 44px;
        color: var(--form-placeholder-color);
    }

    &.is-invalid {
        border-bottom: 1px solid var(--red);
    }
}

.error {
    color: var(--red);
    text-align: left;
}
</style>

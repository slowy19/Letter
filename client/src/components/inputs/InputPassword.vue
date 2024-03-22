<template>
    <div class="inputDiv">
        <input :type="inputType" class="input" :placeholder="placeholder" />
        <img src="@/assets/icons/eye.png" alt="Icon" @click="toggleInputType" :style="{ opacity: isEye ? 1 : 0.3 }">
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'InputPassword',
    props: {
        placeholder: {
            type: String,
            required: false,
            default: '',
        }
    },
    data() {
        return {
            inputType: 'password', 
            isEye: false,
        };
    },
    methods: {
        toggleInputType() {
            this.inputType = this.inputType === 'password' ? 'text' : 'password';
            this.toggleIsEye();
        },
        toggleIsEye() {
            this.isEye = !this.isEye;
        }
    }
})
</script>

<style scoped lang="scss">
.inputDiv {
    width: 100%;
    max-width: 500px;
    border-bottom: 1px solid rgba(221, 221, 221, 1);
    display: flex;
    justify-content: space-between;
    gap: 20px;

    .input {
    all: unset;

    width: 100%;
    max-width: 480px;
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

    img {
        width: 24px;
        height: 24px;
        object-fit: contain;
        // opacity: 0.3;
        margin-top: 10px;   
        cursor: pointer;
        transition: all .1s ease;
    }
}

</style>

<template>
    <div class="inputDiv">
        <input class="input" :placeholder="placeholder" />
        <div class="imgBg">
            <img src="@/assets/icons/arrow.png" alt="Icon">
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'InputMessage',
    props: {
        placeholder: {
            type: String,
            required: false,
            default: '',
        }
    },
    // data() {
    //     return {
    //         inputType: 'password', 
    //         isEye: false,
    //     };
    // },
    // methods: {
    //     toggleInputType() {
    //         this.inputType = this.inputType === 'password' ? 'text' : 'password';
    //         this.toggleIsEye();
    //     },
    //     toggleIsEye() {
    //         this.isEye = !this.isEye;
    //     }
    // }
})
</script>

<style scoped lang="scss">
.inputDiv {
    background: #fff;
    display: flex;
    justify-content: space-between;
    gap: 20px;
    padding: 0 15px 0 25px;
    border-radius: 16px;

    .input {
    all: unset;

    width: 100%;
    // box-shadow: var(--box-shadow);
    font-size: 16px;
    font-weight: 400;
    line-height: 44px;
    color: #333;
    text-align: left;

        &::placeholder {
            font-size: 16px;
            font-weight: 400;
            line-height: 44px;
            color: rgba(128, 128, 128, 1);
        }
    }

    .imgBg {
        background: rgba(221, 221, 221, 1);
        border-radius: 99px;
        width: 100%;
        max-width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        cursor: pointer;
        margin: 10px 0;   

        img {
            width: 24px;
            height: 24px;
            object-fit: contain;
        }
    }
}

</style>

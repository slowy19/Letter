<template>
    <div class="wrapper">
        <h1 class="title">Letter</h1>
        <div class="form">
            <div class="inputs">
                <InputDefault placeholder="Login" />
                <InputPassword placeholder="Password" />
                <div class="flexLinks">
                    <RouterLink to="/signup" class="link">Sign up</RouterLink>
                    <RouterLink to="/" class="link">Remaind password?</RouterLink>
                </div>
            </div>
            <Button text="Log In" />
        </div>
    </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import InputDefault from '@/components/inputs/InputDefault.vue';
import InputPassword from '@/components/inputs/InputPassword.vue';
import Button from '@/components/Button.vue'
// import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src

@Options({
    components: {
        InputDefault,
        InputPassword,
        Button
    },
})
export default class Login extends Vue {}
</script>

<style scoped lang="scss">
.wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 100px;
    width: 100%;
    max-width: 500px;
    margin: 0 auto;

    .title {
        font-size: 100px;
        font-weight: 400;
        line-height: 183px;
    }

    .form {
        display: flex;
        flex-direction: column;
        gap: 16px;
        width: 100%;
        align-items: center;

        .inputs {
            display: flex;
            flex-direction: column;
            gap: 60px;
            width: 100%;

            .flexLinks {
                margin-top: -60px;
                display: flex;
                gap: 10px;
                justify-content: space-between;
                flex-wrap: wrap;
                align-items: center;
                margin-left: 10px;

                .link {
                    font-size: 20px;
                    font-weight: 400;
                    line-height: 37px;
                }
            }
        }
    }
}
</style>

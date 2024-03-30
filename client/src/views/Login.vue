<template>
    <div class="wrapper">
        <h1 class="title">Letter</h1>
        <Form @submit="onSubmit" @keyup.enter="onSubmit" :validation-schema="validationSchema" as="div" class="form">
            <div class="inputs">
                <InputDefault name="login" error="login" placeholder="Login" />
                <InputPassword name="password" error="password" placeholder="Password" />
                <div class="flexLinks">
                    <RouterLink to="/signup" class="link">Sign up</RouterLink>
                    <RouterLink to="/" class="link">Remaind password?</RouterLink>
                </div>
            </div>
            <Button text="Log In" />
        </Form>
    </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import InputDefault from '@/components/inputs/InputDefault.vue';
import InputPassword from '@/components/inputs/InputPassword.vue';
import Button from '@/components/Button.vue';
import { defineComponent } from 'vue';
import { object, string } from 'zod';
import { toTypedSchema } from '@vee-validate/zod';
import { useForm } from 'vee-validate';

const loginSchema = object({
    login: string().min(3),
    password: string().min(8, 'Password must be at least 8 characters'),
})

const validationSchema = toTypedSchema(loginSchema);

export default defineComponent({
    name: 'Login',
    components: {
        InputDefault,
        InputPassword,
        Button,
    },
    mounted() {
        document.title = 'Login';
    },
    setup() {
        const { handleSubmit } = useForm({
            validationSchema,
        });

        const onSubmit = handleSubmit((values) => {
            console.log(values);
        });

        return {
            handleSubmit,
            onSubmit,
            validationSchema,
        };
    },
});
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
            }
        }
    }
}
</style>

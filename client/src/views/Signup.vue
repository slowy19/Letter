<template>
    <div class="wrapper">
        <h1 class="title">Letter</h1>
        <Form @submit="onSubmit" @keyup.enter="onSubmit" :validation-schema="validationSchema" as="div" class="form">
            <div class="inputs">
                <InputDefault name="username" error="username" placeholder="Username" />
                <InputDefault name="login" error="login" placeholder="Login" />
                <InputPassword name="password" error="password" placeholder="Password" />
                <InputPassword name="confirmPassword" error="confirmPassword" placeholder="Confirm password" />

                <div class="flexLinks">
                    <RouterLink to="/login" class="link"
                        >You have an account?</RouterLink
                    >
                    <RouterLink to="/login" class="link">Log in</RouterLink>
                </div>
            </div>
            <Button text="Sign Up" />
        </Form>
    </div>
</template>

<script lang="ts">
import InputDefault from '@/components/inputs/InputDefault.vue';
import InputPassword from '@/components/inputs/InputPassword.vue';
import Button from '@/components/Button.vue';
import { defineComponent } from 'vue';
import { object, string } from 'zod';
import { toTypedSchema } from '@vee-validate/zod';
import { useForm } from 'vee-validate';

const signupSchema = object({
    login: string().min(3),
    password: string().min(8, 'Password must be at least 8 characters'),
    confirmPassword: string().min(8, 'Password must be at least 8 characters'),
}).superRefine(({ confirmPassword, password }, ctx) => {
    if (confirmPassword !== password) {
        ctx.addIssue({
            code: "custom",
            message: "Passwords must match",
            path: ["confirmPassword"]
        });
    }
});

const validationSchema = toTypedSchema(signupSchema);

export default defineComponent({
    name: 'Signup',
    components: {
        Button,
        InputDefault,
        InputPassword,
    },
    mounted() {
        document.title = 'Sign up';
    },
    setup() {

        const { handleSubmit } = useForm({
            validationSchema,
        });

        const onSubmit = handleSubmit(values => {
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
    gap: 50px;
    width: 100%;
    max-width: 500px;
    margin: 0 auto;

    .title {
        font-size: 100px;
        font-weight: 400;
        // line-height: 183px;
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

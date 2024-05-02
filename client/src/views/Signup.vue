<template>
    <div class="wrapper">
      <h1 class="title">Sign Up</h1>
      <Form @submit="onSubmit" @keyup.enter="onSubmit" :validation-schema="validationSchema" as="div" class="form">
        <div class="inputs">
          <InputDefault v-model="values.username" name="username" error="username" placeholder="Username" />
          <InputDefault v-model="values.login" name="login" error="login" placeholder="Login" />
          <InputPassword v-model="values.password" name="password" error="password" placeholder="Password" />
          <InputPassword v-model="values.confirmPassword" name="confirmPassword" error="confirmPassword" placeholder="Confirm password" />
  
          <div class="flexLinks">
            <RouterLink to="/login" class="link">Already have an account?</RouterLink>
            <RouterLink to="/login" class="link">Log in</RouterLink>
          </div>
        </div>
        <Button type="submit" text="Sign Up" />
      </Form>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent, ref, onMounted } from 'vue';
  import { useForm } from 'vee-validate';
  import { object, string } from 'zod';
  import axios from 'axios';
  import { toTypedSchema } from '@vee-validate/zod';
  import InputDefault from '@/components/inputs/InputDefault.vue';
  import InputPassword from '@/components/inputs/InputPassword.vue';
  import Button from '@/components/Button.vue';
  
  const signupSchema = object({
    username: string().min(3),
    login: string().min(3),
    password: string().min(8, 'Password must be at least 8 characters'),
    confirmPassword: string().min(8, 'Password must be at least 8 characters'),
  }).superRefine(({ confirmPassword, password }, ctx) => {
    if (confirmPassword!== password) {
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
  setup() {
    const values = ref({
      username: '',
      login: '',
      password: '',
      confirmPassword: ''
    });

    const csrfToken = ref('');

    const { handleSubmit } = useForm({
      validationSchema,
      initialValues: values.value,
    });

    const onSubmit = async () => {
      try {
        const response = await axios.post('/api/v1/signup/', values.value, {
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken.value
          }
        });
        console.log(response.data);
      } catch (error) {
        console.error(error);
      }
    };

    // Получение CSRF-токена при монтировании компонента
    onMounted(async () => {
      try {
        const response = await axios.get('/api/v1/csrf/');
        csrfToken.value = response.data.csrfToken;
      } catch (error) {
        console.error('Ошибка при получении CSRF-токена:', error);
      }
    });

    return {
      values,
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
  
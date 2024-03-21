<template>
  <div class="wrapper">
      <h1 class="title">Letter</h1>
      <div class="inputs">
        <InputDefault placeholder="Login" />
        <InputDefault placeholder="Password" />
      </div>
      <button>Log In</button>
  </div>
</template>

<script lang="ts">
import { Options, Vue } from 'vue-class-component';
import InputDefault from '@/components/inputs/InputDefault.vue';
// import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src

@Options({
    components: {
        InputDefault,
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

    .inputs {
      display: flex;
      flex-direction: column;
      gap: 60px;
      width: 100%;
    }
  }
</style>

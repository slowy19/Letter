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
import { defineComponent, defineProps } from 'vue';

interface Props {
    isSignup: boolean;
}

const props = defineProps<Props>();

export default defineComponent({
    props: defineProps<Props>(),
    setup() {
        // props.isSignup;
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
    height: 100vh;

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

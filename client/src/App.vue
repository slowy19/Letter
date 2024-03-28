<template>
    <router-view />
</template>

<style lang="scss">
:root {
    --box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);

    // colors
    --black: #333;
    --white: #fff;
    --gray: rgba(128, 128, 128, 1);
    --red: rgba(255, 68, 68, 1);
    --orange: rgba(255, 101, 47, 1);
    --yellow: rgba(255, 228, 0, 1);
    --color-not-found-h1: rgba(221, 221, 221, 1);
    --color-empty: #ddd;
    --link-color: rgba(170, 170, 170, 1);
    --form-placeholder-color: rgba(119, 119, 119, 1);
    --background-item: #d9d9d9;
    --background-scrollbar: rgba(217, 217, 217, 1);
    --background-chats: rgba(85, 85, 85, 1);
}

body {
    background: var(--black);
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: var(--white);

    a {
        text-decoration: none;
    }

    .link {
        font-size: 20px;
        font-weight: 400;
        line-height: 37px;
        color: var(--link-color);
        transition: all 0.1s ease;

        &:hover {
            color: var(--white);
        }
    }
}

// nav {
//     padding: 30px;

//     a {
//         font-weight: bold;
//         color: #2c3e50;

//         &.router-link-exact-active {
//             color: #42b983;
//         }
//     }
// }
</style>

<template>
    <router-view />
</template>

<style lang="scss">
body {
    background: #333;
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #fff;
    background: #333;

    a {
        text-decoration: none;
        color: #fff;
    }

    .link {
        font-size: 20px;
        font-weight: 400;
        line-height: 37px;
        color: rgba(170, 170, 170, 1);
        transition: all 0.1s ease;

        &:hover {
            color: #fff;
        }
    }
}

#app {
    --box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
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

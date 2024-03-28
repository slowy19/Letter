<template>
    <div class="wrapper">
        <div class="left">
            <!-- <img src="" alt=""> -->
            <div class="leftTop">
                <div class="img" />
                <span class="time">last seen 3 minutes ago</span>
            </div>
            <div class="info">
                <div class="information">
                    <div class="nicknames">
                        <div class="names">
                            <h1 class="firstName">ALICE</h1>
                            <h2 class="lastName">WHITE</h2>
                        </div>
                        <span class="nick">a.k.a Alice66</span>
                    </div>
                    <div class="contacts">
                        <div class="item">
                            <span class="itemTitle">PHONE</span>
                            <span class="itemEmail">+7 123 456 7891</span>
                        </div>
                        <div class="item2">
                            <span class="itemTitle">EMAIL</span>
                            <span class="itemEmail">alice.w@test.com</span>
                        </div>
                        <div class="itemColumn">
                            <span class="itemTitle">BIO</span>
                            <p class="itemEmail">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam vel nunc sodales, convallis nunc non, commodo ipsum. Vestibulum mollis massa.</p>
                        </div>
                    </div>
                </div>
                <div class="links">
                    <img src="@/assets/icons/go-back-arrow.svg" alt="Back">
                    <!-- <RouterLink to="#" class="chat" @click.prevent="$router.go(-1)">CHAT</RouterLink> -->
                    <RouterLink to="#" class="chat">CHAT</RouterLink>
                    <img src="@/assets/icons/share.svg" alt="Share">
                </div>
            </div>
        </div>

        <div class="right">
            <div class="chats">
                <h3 class="chatsTitle">Common chats</h3>
                <div class="chatsRow">
                    <div class="chatItem">
                        <!-- <img src="" alt=""> -->
                        <div class="chatImg" />
                        <span class="chatTitle">Alice and company</span>
                    </div>
                    <div class="chatItem">
                        <div class="chatImg" />
                        <span class="chatTitle">Workteam</span>
                    </div>
                    <div class="chatItem">
                        <div class="chatImg" />
                        <span class="chatTitle">Alice and company</span>
                    </div>
                    <div class="chatItem">
                        <div class="chatImg" />
                        <span class="chatTitle">Workteam</span>
                    </div>
                    <div class="chatItem">
                        <div class="chatImg" />
                        <span class="chatTitle">Alice and company</span>
                    </div>
                    <div class="chatItem">
                        <div class="chatImg" />
                        <span class="chatTitle">Workteam</span>
                    </div>
                    <div class="chatItem">
                        <div class="chatImg" />
                        <span class="chatTitle">Workteam</span>
                    </div>
                    <div class="chatItem">
                        <div class="chatImg" />
                        <span class="chatTitle">Workteam</span>
                    </div>
                </div>
            </div>
            <div class="photosDocuments">
                <div class="navBar">
                    <RouterLink to="/profile/" class="navLink">Photos</RouterLink>
                    <RouterLink to="/profile/docs" class="navLink">Documents</RouterLink>
                </div>
                <div class="items">
                    <router-view />
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'Profile',
    mounted() {
        document.title = 'Profile'
    }
})

</script>

<style scoped lang="scss">
    .wrapper {
        width: 100%;
        max-width: 100vw;
        height: 100vh;
        margin: 0 auto;
        display: flex;

        .left {
            width: 25%;
            border-right: 1px solid transparent;
            box-shadow: var(--box-shadow);
            height: 100vh;
            display: flex;
            flex-direction: column;
            gap: 50px;
            background: var(--form-placeholder-color);
            color: var(--color-not-found-h1);

            .leftTop {
                height: 40vh;
                width: 100.2%;
                position: relative;

                .img {
                    width: 100%;
                    height: 100%;
                    background: rgba(85, 85, 85, 1);
                }

                .time {
                    position: absolute;
                    bottom: 10px;
                    left: 10px;
                    font-size: 20px;
                    font-weight: 400;
                    color: rgba(170, 170, 170, 1);
                }
            }

            .info {
                display: flex;
                flex-direction: column;
                gap: 30px;
                justify-content: space-between;
                padding: 0 35px;
                height: 52vh;

                .information {
                    display: flex;
                    flex-direction: column;
                    gap: 40px;

                    .nicknames {
                        display: flex;
                        flex-direction: column;
                        gap: 10px;
                        text-align: center;
                        align-items: center;

                        .names {
                            display: flex;
                            flex-direction: column;
                            
                            .firstName {
                                font-size: 48px;
                                font-weight: 400;
                                color: var(--color-not-found-h1);
                                text-transform: uppercase;
                                line-height: 0;
                            }

                            .lastName {
                                font-size: 24px;
                                font-weight: 400;
                                color: var(--color-not-found-h1);
                                text-transform: uppercase;
                                line-height: 0;
                                margin-top: 10px;
                            }
                        }

                        .nick {
                            padding: 12px;
                            background: var(--link-color);
                            border-radius: 40px;
                            font-size: 20px;
                            font-weight: 400;
                            color: var(--white);
                        }
                    }

                    .contacts {
                        display: flex;
                        flex-direction: column;
                        gap: 10px;

                        .item {
                            display: flex;
                            gap: 15px;
                            align-items: center;
                        }

                        .item2 {
                            display: flex;
                            gap: 26px;
                            align-items: center;
                        }

                        .itemColumn {
                            display: flex;
                            flex-direction: column;
                            align-items: flex-start;
                            gap: 6px;
                        }

                        .itemTitle {
                            font-size: 16px;
                            font-weight: 400;
                        }

                        .itemEmail {
                            font-size: 14px;
                            font-weight: 400;
                            margin: 0;
                            text-align: left;
                        }
                    }
                }

                .links {
                    display: flex;
                    justify-content: space-between;
                    gap: 10px;
                    align-items: center;

                    .chat {
                        border: 2px solid var(--color-not-found-h1);
                        border-radius: 8px;
                        background: var(--link-color);
                        color: var(--color-not-found-h1);
                        font-size: 24px;
                        font-weight: 400;
                        padding: 7px 15px;
                    }
                }
            }
        }

        .right {
            padding: 40px 0;
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            gap: 50px;
            height: 90vh;

            .chats {
                display: flex;
                flex-direction: column;

                .chatsTitle {
                    font-size: 24px;
                    font-weight: 400;
                    text-align: left;
                }

                .chatsRow {
                    width: 100%;
                    background: var(--background-chats);
                    border-radius: 8px;
                    display: flex;
                    gap: 8px;
                    overflow-x: auto;
                    padding: 10px 15px;

                    &::-webkit-scrollbar {
                        height: 4px;
                    }
                    &::-webkit-scrollbar-track {
                        background: transparent;
                    }
                    &::-webkit-scrollbar-thumb {
                        background: var(--background-scrollbar);
                        border-radius: 99px;
                    }

                    .chatItem {
                        display: flex;
                        align-items: center;
                        gap: 5px;
                        width: 100%;
                        max-width: 200px;
                        background: var(--gray);
                        padding: 4px;
                        border-radius: 99px;
                        cursor: pointer;
                        transition: all .1s linear;

                        &:hover {
                            transform: translateY(-4px);
                        }

                        .chatImg {
                            width: 50px;
                            height: 50px;
                            border-radius: 99px;
                            background: rgba(217, 217, 217, 1);
                        }

                        .chatTitle {
                            font-size: 20px;
                            font-weight: 400;
                            display: block;
                            width: 100px;
                            text-overflow: ellipsis;
                            overflow: hidden;
                            white-space: nowrap;
                        }
                    }
                }
            }

            .photosDocuments {
                display: flex;
                flex-direction: column;
                gap: 5px;

                .navBar {
                    display: flex;
                    gap: 8px;
                    border-bottom: 1px solid transparent;
                    padding-bottom: 4px;

                    .navLink {
                        border-bottom: 2px solid transparent;
                        padding-bottom: 4px;
                        color: var(--white);
                        font-size: 24px;
                        font-weight: 400;
                        transition: all .1s ease;

                        &:hover {
                            border-bottom: 2px solid #ffffffbd;
                        }
                    }

                    .router-link-exact-active {
                        border-bottom: 2px solid var(--white) !important;
                    }
                }

                .items {
                    width: 99%;
                    background: rgba(85, 85, 85, 1);
                    display: flex;
                    flex-wrap: wrap;
                    height: 100%;
                    max-height: 650px;
                    overflow-y: auto;
                    padding: 20px;
                    border-radius: 8px;

                    &::-webkit-scrollbar {
                        width: 4px;
                    }
                    &::-webkit-scrollbar-track {
                        background: transparent;
                    }
                    &::-webkit-scrollbar-thumb {
                        background: var(--background-scrollbar);
                        border-radius: 2px;
                    }
                }
            }
        }
    }
</style>
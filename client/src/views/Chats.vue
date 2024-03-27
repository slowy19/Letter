<template>
    <div class="wrapper">
        <div class="left">
            <div class="leftHeader">
                <div class="profile">
                    <img src="@/assets/icons/avatar.png" alt="Profile" />
                </div>
                <InputSearch placeholder="Search" />
            </div>
            <div class="scrollbar">
                <div class="items">
                    <Item
                        @click="setActive(item)"
                        :isActive="active === item"
                        v-for="(item, index) in chatList"
                        :key="index"
                        :item="item"
                    />
                </div>
            </div>
        </div>
        <div class="right">
            <div class="empty" v-bind:class="{ hidden: active }">
                <svg width="60px" height="60px" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M18 9V7.2C18 6.0799 18 5.51984 17.782 5.09202C17.5903 4.71569 17.2843 4.40973 16.908 4.21799C16.4802 4 15.9201 4 14.8 4H7.2C6.0799 4 5.51984 4 5.09202 4.21799C4.71569 4.40973 4.40973 4.71569 4.21799 5.09202C4 5.51984 4 6.0799 4 7.2V18L8 16M20 20L17.8062 18.5374C17.5065 18.3377 17.3567 18.2378 17.1946 18.167C17.0507 18.1042 16.9 18.0586 16.7454 18.031C16.5713 18 16.3912 18 16.0311 18H11.2C10.0799 18 9.51984 18 9.09202 17.782C8.71569 17.5903 8.40973 17.2843 8.21799 16.908C8 16.4802 8 15.9201 8 14.8V12.2C8 11.0799 8 10.5198 8.21799 10.092C8.40973 9.71569 8.71569 9.40973 9.09202 9.21799C9.51984 9 10.0799 9 11.2 9H16.8C17.9201 9 18.4802 9 18.908 9.21799C19.2843 9.40973 19.5903 9.71569 19.782 10.092C20 10.5198 20 11.0799 20 12.2V20Z" stroke="#d9d9d9" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                </svg>
                <span class="emptySpan">Select a chat or <RouterLink class="link" to="/login">create new</RouterLink></span>
            </div>
            <div class="fill" v-bind:class="{ hidden: !active }">
                <div class="fillHeader">
                    <!-- <h1 class="fillName">{{ selectedChatItem && selectedChatItem.name }}</h1> -->
                    <h1 class="fillName">Alice White</h1>
                    <span class="status">Online</span>
                </div>
                <div class="fillContent">
                    <InputMessage placeholder="Write a message..." />
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import InputSearch from '@/components/inputs/InputSearch.vue';
import Item from '@/components/chats/Item.vue';
import InputMessage from '@/components/inputs/InputMessage.vue';
import { defineComponent, onMounted, onUnmounted, ref } from 'vue';
import axios from 'axios'
import { IChatItem } from '@/interfaces';

export default defineComponent({
    name: 'Chats',
    components: {
        InputSearch,
        Item,
        InputMessage,
    },
    data() {
        return {
            chatList: [],
            selectedChatItem: null as IChatItem | null,
            intervalId: null as number | undefined | null,
        }
    },
    methods: {
        getChatList() {
            axios
                .get('/api/v1/chat-list/')
                .then(response => {
                    this.chatList = response.data
                })
                .catch(error => {
                    console.log(error);
                })
        },
        setActive(item: any) {
            this.selectedChatItem = item;
        },
    },
    beforeUnmount() {
        if (this.intervalId) {
            clearInterval(this.intervalId);
        }
    },
    mounted() {
        // Call getChatList immediately on mount
        this.getChatList();

        // Set up an interval to call getChatList every 5 seconds
        this.intervalId = setInterval(() => {
            this.getChatList();
        }, 5000);

        document.title = 'Chats'
    },
    setup() {
        const active = ref(null);

        const setActive = (item: any) => {
            active.value = item;
        };

        const handleKeydown = (event: KeyboardEvent) => {
            if (event.key === 'Escape') {
                active.value = null;
            }
        };

        onMounted(() => {
            window.addEventListener('keydown', handleKeydown);
        });

        onUnmounted(() => {
            window.removeEventListener('keydown', handleKeydown);
        });

        return {
            active,
            // chatList,
            setActive,
        };
    },
});
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

        .leftHeader {
            display: flex;
            justify-content: space-between;
            gap: 8px;
            padding: 20px 20px 20px 0;

            .profile {
                width: 100%;
                max-width: 65px;
                background: #fff;
                border-radius: 0 40px 40px 0;
                display: flex;
                align-items: center;
                justify-content: right;
                padding: 4px 6px;

                img {
                    width: 34px;
                    height: 34px;
                    object-fit: cover;
                    border-radius: 99px;
                }
            }
        }

        .scrollbar {
            overflow-y: auto;
            height: 90vh;

            &::-webkit-scrollbar {
                width: 4px;
            }
            &::-webkit-scrollbar-track {
                background: transparent;
            }
            &::-webkit-scrollbar-thumb {
                background: rgba(217, 217, 217, 1);
                border-radius: 2px;
            }

            .items {
                padding: 0 20px;
                display: flex;
                flex-direction: column;
                gap: 10px;
                width: 84%;
            }
        }
    }

    .right {
        width: 75%;
        height: 93vh;
        padding: 20px 40px 40px 40px;

        .hidden {
            display: none !important;
        }

        .empty {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100%;
            flex-direction: column;
            gap: 10px;
            width: 100%;
            max-width: 300px;
            margin: 0 auto;

            .emptySpan {
                font-size: 20px;
                font-weight: 400;
                color: #ddd;
            }
        }

        .fill {
            display: flex;
            flex-direction: column;
            gap: 50px;
            justify-content: space-between;
            height: 100%;

            .fillHeader {
                display: flex;
                width: 100%;
                gap: 15px;
                border-bottom: 1px solid #fff;

                .fillName {
                    font-size: 24px;
                    font-weight: 400;
                }

                .status {
                    font-size: 14px;
                    font-weight: 400;
                    color: rgba(255, 101, 47, 1);
                    margin-top: 25px;
                }
            }
        }
    }
}
</style>

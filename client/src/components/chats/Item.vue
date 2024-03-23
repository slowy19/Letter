<template>
    <div class="item" :class="{ active: isActive }" @click="handleClick">
        <img src="@/assets/icons/avatar.png" alt="Avatar">
        <div class="text">
            <div class="textItem">
                <span class="name">Alice White</span>
                <span class="date">8:23</span>
            </div>
            <div class="textItem">
                <span class="message">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed finibus sagittis purus pulvinar accumsan. Maecenas vitae lacus mauris. Cras ut aliquam magna. Ut felis turpis, feugiat nec fermentum id, imperdiet.</span>
                <span class="count">2</span>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';


// @Options({
//     components: {
//         InputSearch
//     },
// })

export default defineComponent({
    name: 'Item',
    props: {
        isActive: Boolean,
    },
    methods: {
        handleClick() {
            this.$emit('click', this);
        },
    },
})
</script>

<style scoped lang="scss">

    .active {
        background: rgba(255, 228, 0, 1) !important;
    }

    .item {
        border-radius: 4px;
        box-shadow: var(--box-shadow);
        display: flex;
        gap: 10px;
        // justify-content: space-between;
        align-items: center;
        padding: 10px 20px 10px 10px;
        color: rgba(0, 0, 0, 1);
        width: 100%;
        cursor: pointer;
        transition: all .1s ease;
        background: #d9d9d9;

        img {
            width: 60px;
            height: 60px;
            object-fit: cover;
            border-radius: 99px;
        }

        .text {
            display: flex;
            flex-direction: column;
            gap: 5px;
            width: 83%;

            .textItem {
                display: flex;
                justify-content: space-between;
                gap: 10px;
                align-items: center;

                .name {
                    font-size: 18px;
                    font-weight: 400;
                }

                .date {
                    font-size: 16px;
                    font-weight: 400;
                    color: rgba(128, 128, 128, 1);
                }

                .message {
                    max-width: 100%;
                    text-overflow: ellipsis;
                    overflow: hidden;
                    white-space: nowrap;
                }

                .count {
                    background: rgba(255, 101, 47, 1);
                    color: #fff;
                    border-radius: 99px;
                    font-size: 14px;
                    font-weight: 400;
                    padding: 0 5px;
                    height: 20px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                }
            }

        }
    }
</style>

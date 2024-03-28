<template>
    <div class="wrapperPhotos">
        <div class="photoParrent">
            <img class="photoAbsolute" src="@/assets/images/avatar.png" alt="Image">
            <img class="photo" src="@/assets/images/avatar.png" alt="Image">
        </div>
        <div class="photoParrent">
            <img class="photoAbsolute" src="@/assets/images/avatar.png" alt="Image">
            <img class="photo" src="@/assets/images/avatar.png" alt="Image">
        </div>
        <div class="photoParrent">
            <img class="photoAbsolute" src="@/assets/images/avatar.png" alt="Image">
            <img class="photo" src="@/assets/images/avatar.png" alt="Image">
        </div>
        <div class="photoParrent">
            <img class="photoAbsolute" src="@/assets/images/avatar.png" alt="Image">
            <img class="photo" src="@/assets/images/avatar.png" alt="Image">
        </div>
        <div class="photoParrent">
            <img class="photoAbsolute" src="@/assets/images/avatar.png" alt="Image">
            <img class="photo" src="@/assets/images/avatar.png" alt="Image">
        </div>
        <div class="photoParrent">
            <img class="photoAbsolute" src="@/assets/images/avatar.png" alt="Image">
            <img class="photo" src="@/assets/images/avatar.png" alt="Image">
        </div>
        <div class="photoParrent">
            <img class="photoAbsolute" src="@/assets/images/avatar.png" alt="Image">
            <img class="photo" src="@/assets/images/avatar.png" alt="Image">
        </div>
        <div class="photoParrent">
            <img class="photoAbsolute" src="@/assets/images/avatar.png" alt="Image">
            <img class="photo" src="@/assets/images/avatar.png" alt="Image">
        </div>
        <div class="photoParrent">
            <img class="photoAbsolute" src="@/assets/images/avatar.png" alt="Image">
            <img class="photo" src="@/assets/images/avatar.png" alt="Image">
        </div>
        <div class="photoParrent">
            <img class="photoAbsolute" src="@/assets/images/avatar.png" alt="Image">
            <img class="photo" src="@/assets/images/avatar.png" alt="Image">
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';


export default defineComponent({
    name: 'Photos',
})
</script>

<style scoped lang="scss">

.wrapperPhotos {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;

    .photoParrent {
        width: 190px;
        height: 190px;
        border-radius: 12px;
        position: relative;
        transition: all .1s ease;
        cursor: pointer;
        z-index: 1;

        &:hover {
            z-index: 2;

            .photoAbsolute {
                z-index: 3;
                transform: scale(1.1);
                box-shadow: var(--box-shadow);
            }
        }

        .photoAbsolute {
            transform-origin: center;
            position: absolute;
            top: 0;
            left: 0;
            z-index: 2;
            width: 100%;
            height: 100%;
            border-radius: 12px;
            object-fit: cover;
            transition: all .1s ease;
            cursor: pointer;
        }

        .photo {
            width: 100%;
            height: 100%;
            border-radius: 12px;
            object-fit: cover;
        }
    }
}

</style>

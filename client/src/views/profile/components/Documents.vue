<template>
    <div class="wrapperDocs">
        <div class="docItem">
            <img class="download" src="@/assets/icons/download.svg" alt="Icon">
            <img class="docIcon" src="@/assets/icons/doc.svg" alt="Icon">
            <span class="docTitle">report.txt</span>
        </div>
        <div class="docItem">
            <img class="download" src="@/assets/icons/download.svg" alt="Icon">
            <img class="docIcon" src="@/assets/icons/doc.svg" alt="Icon">
            <span class="docTitle">report.txt</span>
        </div>
        <div class="docItem">
            <img class="download" src="@/assets/icons/download.svg" alt="Icon">
            <img class="docIcon" src="@/assets/icons/doc.svg" alt="Icon">
            <span class="docTitle">report.txt</span>
        </div>
        <div class="docItem">
            <img class="download" src="@/assets/icons/download.svg" alt="Icon">
            <img class="docIcon" src="@/assets/icons/doc.svg" alt="Icon">
            <span class="docTitle">report.txt</span>
        </div>
        <div class="docItem">
            <img class="download" src="@/assets/icons/download.svg" alt="Icon">
            <img class="docIcon" src="@/assets/icons/doc.svg" alt="Icon">
            <span class="docTitle">report.txt</span>
        </div>
        <div class="docItem">
            <img class="download" src="@/assets/icons/download.svg" alt="Icon">
            <img class="docIcon" src="@/assets/icons/doc.svg" alt="Icon">
            <span class="docTitle">report.txt</span>
        </div>
        <div class="docItem">
            <img class="download" src="@/assets/icons/download.svg" alt="Icon">
            <img class="docIcon" src="@/assets/icons/doc.svg" alt="Icon">
            <span class="docTitle">report.txt</span>
        </div>
        <div class="docItem">
            <img class="download" src="@/assets/icons/download.svg" alt="Icon">
            <img class="docIcon" src="@/assets/icons/doc.svg" alt="Icon">
            <span class="docTitle">report.txt</span>
        </div>
        <div class="docItem">
            <img class="download" src="@/assets/icons/download.svg" alt="Icon">
            <img class="docIcon" src="@/assets/icons/doc.svg" alt="Icon">
            <span class="docTitle">report.txt</span>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';


export default defineComponent({
    name: 'Documents',
})
</script>

<style scoped lang="scss">

.wrapperDocs {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;

    .docItem {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 8px;
        justify-content: space-between;
        background: var(--gray);
        border-radius: 8px;
        padding: 15px;
        width: 155px;
        height: 155px;
        position: relative;
        transition: all .1s ease;
        cursor: pointer;

        &:hover {
            background: rgba(255, 255, 255, 0.5);

            .download {
                opacity: 1;
            }

            .docIcon {
                opacity: 0.3;
            }
        }

        .download {
            position: absolute;
            top: 0;
            right: 0;
            opacity: 0;
        }

        .docTitle {
            font-size: 24px;
            font-weight: 400;
        }
    }
}

</style>

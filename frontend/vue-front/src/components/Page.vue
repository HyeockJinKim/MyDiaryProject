<template>
    <div class="book-page shadow-right flow-left vertical-middle cur">
        <transition name="cur">
            <div v-if="show" class="book-header">
                <h2 class="title">일기 제목</h2>
            </div>
        </transition>
        <transition name="cur">
            <div v-if="show" class="book-content">
                <p>오늘 하루는 이렇게 일기에 시간을 쓰는구나</p>
            </div>
        </transition>
        <transition name="cur">
            <div v-if="show" class="book-footer">
                <div class="grid-two">
                    <label class="sparse" v-for="(item, index) in tags" v-bind:key="'mul'+index">{{ item.head }}
                        <span class="pointer tags checked" v-for="(value, index2) in item.data" v-bind:key="'mul_'+index2">
                            {{ value }}
                        </span>
                        &nbsp;
                    </label>
                </div>
            </div>
        </transition>
        <transition name="cur">
            <div v-if="show" class="flow-right grid-two margin-right pointer">
                <div>
                    <img src="../assets/32_pen.png" align="left" alt="writing"/>
                </div>
                <div>
                    <p>Writing</p>
                </div>
                <h2 class="right-btn" @click="next_page">&gt;</h2>
            </div>
        </transition>
    </div>
</template>

<script>
    export default {
        name: "Page",
        data: function () {
            return {
                header: '일기 제목',
                contents: '오늘 하루는 이렇게 일기에 시간을 쓰는구나',
                tags: [
                    {
                        head: 'Location',
                        name: 'location',
                        data: ['충대'],
                    },
                    {
                        head: 'Subject',
                        name: 'Subject',
                        data: ['토익스피킹'],
                    },
                    {
                        head: 'with me',
                        name: 'with_me',
                        data: ['준후형', '민호형']
                    },
                    {
                        head: 'Tags',
                        name: 'Tags',
                        data: ['랩실', '운영체제']
                    }
                ],
                show: true
            }
        },
        methods: {
            next_page: function () {
                this.show = false
                setTimeout(() => this.show = true, 500)
            }
        }
    }
</script>

<style scoped>

.right-btn {
    position: relative;
    top: -18em;
    left: 3.5em;
    float: right;
    cursor: pointer;
}

</style>
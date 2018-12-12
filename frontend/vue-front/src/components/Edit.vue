<template>
    <div>
        <div class="book-header">
            <!--<h2 class="title">{{ header }}</h2>-->
            <label>제목
                <input class="header-content" type="text">
            </label>
        </div>
        <div class="book-content">
            <label>내용
                <textarea class="content"></textarea>
            </label>
        </div>
        <div class="book-footer">
            <div class="grid-two">
                <label class="sparse" v-for="(item, index) in footer" v-bind:key="'sing'+index">{{ item.head }}
                    <select v-model="item.selected">
                        <option v-for="(value, index2) in item.data" v-bind:key="'sing_'+index2" v-bind:value="value">
                            {{ value }}
                        </option>
                    </select>
                    &nbsp;
                    <span class="btn">등록</span>
                </label>
                <label class="sparse" v-for="(item, index) in tags" v-bind:key="'mul'+index">{{ item.head }}
                    <span class="pointer tags" v-for="(value, index2) in item.data" v-bind:key="'mul_'+index2"
                          v-bind:class="{checked: value.selected}"
                          @click="value.selected = !value.selected">
                                {{ value.name }}
                            </span>
                    &nbsp;
                    <span class="btn">등록</span>
                    <br>
                </label>
            </div>
        </div>
        <div class="flow-right grid-two margin-right pointer">
            <div>
                <img src="../assets/32_pen.png" align="left" alt="writing"/>
            </div>
            <div>
                <p>Writing</p>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Edit",
        data: function () {
            return {
                header: '일기 제목',
                contents: '',
                footer: [
                    {
                        head: 'Location',
                        name: 'location',
                        data: ['충대', '집'],
                        selected: '충대'
                    },
                    {
                        head: 'Subject',
                        name: 'Subject',
                        data: ['토익스피킹', '랩실'],
                        selected: '토익스피킹'
                    }
                ],
                tags: [
                    {
                        head: 'with me',
                        name: 'with_me',
                        data: [
                            {name: '준후형', selected: false},
                            {name: '민호형', selected: false},
                        ]
                    },
                    {
                        head: 'Tags',
                        name: 'Tags',
                        data: [
                            {name: '운영체제', selected: false},
                            {name: '영어', selected: false},
                        ]
                    }
                ]
            }
        },
        methods: {

        }
    }
</script>

<style scoped>
.book-header {
    padding: 1em 2.5em 0 1.5em;
}

.book-content {
    padding: 0.5em 1.5em 0 0.5em;
}

.header-content {
    margin-top: 0.5em;
    margin-bottom: 0.8em;
    height: 100%;
    width: 100%;
}

.content {
    margin-top: 0.5em;
    margin-bottom: 0.8em;
    resize: none;
    height: 90%;
    width: 100%;
}
</style>
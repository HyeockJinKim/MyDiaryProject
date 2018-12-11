<template>
    <section class="root">
        <h2 class="banner">Diary</h2>
        <div class="grid-two book">
            <div class="book-cover shadow-right">
                <div class="book-page shadow-left flow-right vertical-middle">

                </div>
            </div>
            <div class="book-cover shadow-left">
                <div class="book-page shadow-right flow-left vertical-middle">
                    <div class="book-header">
                        <h2 class="title">일기 제목</h2>
                    </div>
                    <div class="book-content">
                        <p>오늘 하루는 이렇게 일기에 시간을 쓰는구나</p>
                    </div>
                    <div class="book-footer">
                        <div class="grid-two">
                            <label class="sparse" v-for="(item, index) in footer" v-bind:key="'sing'+index">{{ item.head }}
                                <select v-model="item.selected">
                                    <option v-for="(value, index2) in item.data" v-bind:key="'sing2'+index2" v-bind:value="value">
                                        {{ value }}
                                    </option>
                                </select>
                                &nbsp;
                                <span class="btn">등록</span>
                            </label>
                            <label class="sparse" v-for="(item, index) in tags" v-bind:key="'mul'+index">{{ item.head }}
                                <span class="pointer tags" v-for="(value, index2) in item.data" v-bind:key="'mul2'+index2"
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
            </div>
        </div>
    </section>
</template>

<script>
    export default {
        name: "Diary",
        data: function () {
            return {
                header: [
                    {}
                ],
                contents: [

                ],
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
h2 {
    text-shadow: 0.05em 0.05em rgba(0, 0, 0, 0.3);
}

label {
    font-size: 0.9em;
}

.margin-right {
    margin-top: 0.8em;
    margin-right: 2em;
}

.pointer {
    cursor: pointer;
}

.btn {
    color: #fff;
    border-radius: 3px;
    padding: 0.1em 0.5em;
    font-size: 0.8em;
    font-weight: bold;
    text-decoration: none;
    background-color: #346199;
    box-shadow: 0 3px 0 0 #418bd1;
    position: relative;
    display: inline-block;
    cursor: pointer;
    margin-right: 1em;
}

.btn:hover {
    background-color: #3779b4;
}

.btn:active {
    transform: translate(0px, 3px);
    -webkit-transform: translate(0px, 3px);
    box-shadow: 0 1px 0 0;
}

.root {
    width: 100%;
}

.grid-two {
    display: grid;
    grid-template-columns: auto auto;
}

.book {
    padding: 0;
    width: 75em;
    margin: auto;
}

.book-cover {
    width: 37em;
    height: 51em;
    border-radius: 5px;
    background-color: #1d4d7c;
    margin: 0;
    padding: 0;
}

.flow-right {
    float: right;
}

.flow-left {
    float: left;
}

.vertical-middle {
    top: 50%;
}

.shadow-right {
    box-shadow: 0.5em 0.5em rgba(0, 0, 0, 0.3);
}

.shadow-left {
    box-shadow: -0.5em 0.5em rgba(0, 0, 0, 0.3);
}

.book-page {
    text-align: left;
    width: 35em;
    height: 50em;
    background-color: white;
}

.tags {
    background-color: rgba(28, 83, 205, 0.29);
    color: #fff;
    font-size: 0.8em;
    font-weight: bold;
    padding: 0.2em 0.5em;
    margin: 0 0.2em;
    border-radius: 8px;
    text-align: center;
    vertical-align: center;
}

.book-content {
    margin: 0 1em;
    height: 35em;
}

.book-footer {
    margin: 0 1.2em;
}

.title {
    margin: 1em 0 0 0.5em;
}

.sparse {
    margin: 1em;
}

.checked {
    background-color: rgba(28, 83, 205, 0.82);
}
</style>
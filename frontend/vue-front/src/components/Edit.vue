<template>
    <div>
        <div class="book-header">
            <!--<h2 class="title">{{ header }}</h2>-->
            <label>제목
                <input v-model="header" placeholder="일기 제목" class="header-content" type="text">
            </label>
        </div>
        <div class="book-content">
            <label>내용
                <textarea v-model="contents" placeholder="내용" class="content"></textarea>
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
        <div class="flow-right grid-two margin-right pointer" @click="submit">
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
    import axios from 'axios'

    export default {
        name: "Edit",
        created() {
            axios.get('http://127.0.0.1:8000/')
                .then()
                .catch()
            this.header = 'his'
        },
        data: function () {
            return {
                header: '',
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
            submit: function () {
                let payload = {
                    header: this.header,
                    contents: this.contents
                }
                for (let i = 0; i < this.tags.length; ++i) {
                    let tag = []
                    for (let j = 0; j < this.tags[i].data.length; ++j) {
                        if (this.tags[i].data[j].selected)
                            tag.push(this.tags[i].data[j].name)
                    }
                    payload[this.tags[i].name] = tag
                }
                console.log(payload)
                if (this.$route.params.id === undefined)
                    axios.post('http://127.0.0.1:8000/diary/new', payload)
                        .then(data => data.data)
                        .then(data => {
                            console.log(data)
                        })
                        .catch(err => {
                            console.log(err)
                        })
            }
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
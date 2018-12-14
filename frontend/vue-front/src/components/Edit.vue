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
            <label class="sparse">날짜
                <input v-model="date" type="date">
            </label>
            <div class="flow-right grid-two submit pointer" @click="submit">
                <div>
                    <img src="../assets/32_pen.png" align="left" alt="writing"/>
                </div>
                <div>
                    <p>Writing</p>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "Edit",
    created() {
        axios.get('http://127.0.0.1:8000/diary/tags')
            .then(data => data.data)
            .then(data => {
                for (let i = 0; i < data.location.length; ++i) {
                    this.footer[0].data.push(data.location[i].fields.name)
                }
                this.footer[0].selected = data.location[0].fields.name
                for (let i = 0; i < data.subject.length; ++i) {
                    this.footer[1].data.push(data.subject[i].fields.name)
                }
                this.footer[1].selected = data.subject[0].fields.name
                for (let i = 0; i < data.with_me.length; ++i) {
                    this.tags[0].data.push({
                        name: data.with_me[i].fields.name,
                        selected: false
                    })
                }
                for (let i = 0; i < data.tags.length; ++i) {
                    this.tags[1].data.push({
                        name: data.tags[i].fields.name,
                        selected: false
                    })
                }
                this.date = data.date
            })
            .catch(err => {
                console.log(err)
            })
    },
    data: function () {
        return {
            header: '',
            contents: '',
            footer: [
                {
                    head: 'Location',
                    name: 'location',
                    data: [],
                    selected: ''
                },
                {
                    head: 'Subject',
                    name: 'subject',
                    data: [],
                    selected: ''
                }
            ],
            tags: [
                {
                    head: 'with me',
                    name: 'with_me',
                    data: []
                },
                {
                    head: 'Tags',
                    name: 'tags',
                    data: []
                }
            ],
            date: ''
        }
    },
    methods: {
        submit: function () {
            let payload = {
                header: this.header,
                contents: this.contents,
                location: this.footer[0].selected,
                subject: this.footer[1].selected,
                date: this.date
            }
            for (let i = 0; i < this.tags.length; ++i) {
                let tag = []
                for (let j = 0; j < this.tags[i].data.length; ++j) {
                    if (this.tags[i].data[j].selected)
                        tag.push(this.tags[i].data[j].name)
                }
                payload[this.tags[i].name] = tag
            }
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
    padding: 0.5em 1.5em 0.5em 0.5em;
}

.header-content {
    margin-top: 0.5em;
    margin-bottom: 0.6em;
    height: 100%;
    width: 100%;
}

.content {
    margin-top: 0.5em;
    margin-bottom: 0.8em;
    resize: none;
    height: 94%;
    width: 100%;
}
</style>
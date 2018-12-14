<template>
    <div class="book-page shadow-right flow-left vertical-middle cur">
        <transition name="cur">
            <div v-if="show" class="book-header">
                <h2 class="title">{{ header }}</h2>
            </div>
        </transition>
        <transition name="cur">
            <div v-if="show" class="book-content">
                <pre class="contents">{{ contents }}</pre>
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
                <label class="sparse">날짜
                    <span type="date">{{ date }}</span>
                </label>
                <div class="flow-right grid-two submit pointer" @click="write">
                    <div>
                        <img src="../assets/32_pen.png" align="left" alt="writing"/>
                    </div>
                    <div>
                        <p>Writing</p>
                    </div>
                    <h2 class="right-btn" @click="next_page">&gt;</h2>
                </div>
            </div>
        </transition>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "Page",
    created() {
        let pk = ''
        if (this.$route.params.id !== undefined)
            pk = this.$route.params.id
        axios.get('http://127.0.0.1:8000/diary/page/'+pk)
            .then(data => data.data)
            .then(data => {
                console.log(data)
                this.header = data.title
                this.contents = data.post
                this.tags[0].data.push(data.location)
                this.tags[1].data.push(data.subject)

                for (let i = 0; i < data.with_me.length; ++i) {
                    this.tags[2].data.push(data.with_me[i])
                }
                for (let i = 0; i < data.tags.length; ++i) {
                    this.tags[3].data.push(data.tags[i])
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
            tags: [
                {
                    head: 'Location',
                    name: 'location',
                    data: [],
                },
                {
                    head: 'Subject',
                    name: 'Subject',
                    data: [],
                },
                {
                    head: 'with me',
                    name: 'with_me',
                    data: []
                },
                {
                    head: 'Tags',
                    name: 'Tags',
                    data: []
                }
            ],
            date: '',
            show: true
        }
    },
    methods: {
        next_page: function () {
            this.show = false
            setTimeout(() => this.show = true, 500)
        },
        write: function () {

        }
    }
}
</script>

<style scoped>

.right-btn {
    position: relative;
    top: -18em;
    left: 4.5em;
    float: right;
    cursor: pointer;
}

.contents {
    white-space: pre-line ;
    width: 100%;
}

.book-content {
    margin: 0 1em;
    height: 36em;
}
</style>
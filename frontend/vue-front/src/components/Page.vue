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
                <router-link :to="{ name: 'edit', params: { id: prev+1 } }" class="flow-right grid-two submit pointer">
                    <div>
                        <img src="../assets/32_pen.png" align="left" alt="writing"/>
                    </div>
                    <div>
                        <p>Writing</p>
                    </div>
                </router-link>
                <h2 class="right-btn"><router-link :to="next_page">&gt;</router-link></h2>
                <h2 v-if="prev !== undefined" class="left-btn"><router-link :to="{ name: 'post', params: { id: prev }}">&lt;</router-link></h2>

            </div>
        </transition>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: "Page",
    created() {
        this.fetch_data()
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
            base: '/diary/post/',
            next: -1,
            prev: -1,
            show: false,
            next_page: ''
        }
    },
    watch: {
        '$route': 'fetch_data'
    },
    methods: {
        fetch_data: function() {
            this.show = false
            let pk = ''
            if (this.$route.params.id !== undefined)
                pk = parseInt(this.$route.params.id)
            setTimeout(axios.get('http://127.0.0.1:8000/diary/page/'+pk)
                .then(data => data.data)
                .then(data => {
                    console.log(data)
                    this.header = data.title
                    this.contents = data.post
                    this.tags[0].data = []
                    this.tags[1].data = []
                    this.tags[2].data = []
                    this.tags[3].data = []
                    this.tags[0].data.push(data.location)
                    this.tags[1].data.push(data.subject)

                    for (let i = 0; i < data.with_me.length; ++i) {
                        this.tags[2].data.push(data.with_me[i])
                    }
                    for (let i = 0; i < data.tags.length; ++i) {
                        this.tags[3].data.push(data.tags[i])
                    }
                    this.date = data.date
                    if (data.next === undefined) {
                        this.next_page = {
                            name: 'new'
                        };
                        this.next = undefined
                        console.log('new')
                    } else {
                        this.next = data.next
                        this.next_page = {
                            name: 'post',
                            params: { id: this.next }
                        }
                    }
                    this.prev = data.prev
                    this.show = true
                })
                .catch(err => {
                    console.log(err)
                }), 1500)

        }
    }
}
</script>

<style scoped>

a {
    text-decoration: none;
}

.right-btn {
    position: relative;
    top: -16em;
    left: 6.5em;
    float: right;
    cursor: pointer;
}

.left-btn {
    position: relative;
    top: -16em;
    left: -24em;
    float: left;
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
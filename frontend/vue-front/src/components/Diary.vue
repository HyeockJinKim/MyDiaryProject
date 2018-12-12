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
                    <router-view></router-view>
                </div>
            </div>
        </div>
    </section>
</template>

<script>
    export default {
        name: "Diary"
    }
</script>

<style>
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
    z-index: 3;
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
    z-index: 2;
}

.cur-enter-active, .cur-leave-active {
    transition: opacity .5s;
}
.cur-enter, .cur-leave-to /* .fade-leave-active below version 2.1.8 */ {
    opacity: 0;
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
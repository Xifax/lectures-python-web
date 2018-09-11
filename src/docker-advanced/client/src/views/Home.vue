<template>
  <section class="home">
    <div class="hero is-primary is-medium">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h1 class="title">
            Home Page
          </h1>
          <h2 class="subtitle">
            {{ msg }}
          </h2>
        </div>
      </div>
    </div>
    <div class="additional-bar has-shadow">
      <div class="container">
        <div class="content has-text-centered">
          <!-- write content here -->
        </div>
      </div>
    </div>
    <div class="section">
      <div class="container">
        <div class="content">

          <div class="card" v-for="c in cards">
            <div class="card-image">
              <figure class="image is-4by3">
                <img v-bind:src="c.image" alt="Placeholder image">
              </figure>
            </div>
            <div class="card-content">
              <div class="media">
                <div class="media-left">
                  <figure class="image is-48x48">
                    <img src="https://bulma.io/images/placeholders/96x96.png" alt="Placeholder image">
                  </figure>
                </div>
                <div class="media-content">
                  <p class="title is-4">{{ c.ceo }}</p>
                  <p class="subtitle is-6">{{ c.email }}</p>
                </div>
              </div>

    <div class="content">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit.
      Phasellus nec iaculis mauris. <a>@bulmaio</a>.
      <a href="#">#css</a> <a href="#">#responsive</a>
      <br>
      <time datetime="2016-1-1">11:09 PM - 1 Jan 2016</time>
    </div>
  </div>
</div>

        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'Home',
  data () {
    return {
      msg: 'Vue.js starter with full-featured Webpack and Buefy',
      info: null,
      cards: []
    }
  },
  mounted () {
    this.axios
        .get('https://api.coindesk.com/v1/bpi/currentprice.json')
        .then(response => (this.info = response))

    this.axios
        .get('http://localhost:8000')
        .then(response => (this.cards = response.data))
  }
}
</script>

<style lang="scss" scoped>
.additional-bar {
  padding: 15px;
}

.gh-btn {
  background-color: #eee;
  background-repeat: no-repeat;
  border: 1px solid #d5d5d5;
  border-radius: 4px;
  color: #333;
  text-decoration: none;
  text-shadow: 0 1px 0 #fff;
  white-space: nowrap;
  cursor: pointer;
}
</style>


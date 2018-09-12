<template>
  <section class="home">

    <!-- Header with useless info -->
    <div class="hero is-primary is-medium">
      <div class="hero-body">
        <div class="container has-text-centered">
          <h1 class="title">
            Drug companies from API
          </h1>
          <h2 class="subtitle">
            {{ msg }}
          </h2>
        </div>
      </div>
    </div>

    <!-- Main container -->
    <div class="additional-bar has-shadow">
      <div class="container">
        <div class="content has-text-centered">

          <!-- Cards for items from API -->
          <div class="card" v-for="c in cards">

            <div class="card-image">
              <figure class="image is-4by3">
                <img v-bind:src="upscale(c.image)"
                alt="Placeholder image">
              </figure>
            </div>

            <div class="card-content">
              <div class="media">
                <div class="media-left">
                  <figure class="image is-48x48">
                    <img v-bind:src="c.image"
                    alt="Placeholder image">
                  </figure>
                </div>

                <div class="media-content">
                  <p class="title is-4">{{ c.ceo }}</p>
                  <p class="subtitle is-6">{{ c.email }}</p>
                </div>

              </div>

              <div class="content">
                <p>{{ c.slogan }}</p>
                <p>{{ c.drug }}</p>
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
      msg: 'Let us query our other docker container',
      cards: []
    }
  },
  mounted () {
    this.axios
        .get('http://localhost:8000')
        .then(response => (this.cards = response.data))
  },
  methods: {
    upscale: function (image) {
      return image.replace(new RegExp('50', 'g'), '250')
    }
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

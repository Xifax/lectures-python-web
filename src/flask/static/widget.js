const API = 'http://localhost:5000'
new Vue ({
  el: '#widget',
  delimiters: ['[[',']]'],
  data () {
    return {
      header: 'Мнения о JS виджетах',
      opinions: [],
      opinion: ''
    }
  },
  mounted () {
    this.list()
  },
  computed: {
    pro: function () {
      return this.opinions.filter(
        (o) => { return o[1] === 'pro'})
    },
    contra: function() {
      return this.opinions.filter(
        (o) => { return o[1] === 'contra'})
    }
  },
  methods: {
    list: function() {
      axios.get(`${API}/opinions`)
        .then(response => {
          // tuple does not serialize well: {id, group, text}
          this.opinions = response.data
        })
    },
    add: function (group) {
      axios.post(`${API}/opinions`,
         {group: group, text: this.opinion})
           .then(response => { this.list() })
    },
    remove: function (opinion) {
      axios.delete(`${API}/opinions/${opinion[0]}`)
        .then(response => { this.list() })
    }
  }
})

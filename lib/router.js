Router.route('/sites', function() {
  this.render('sitesPage');
});

Router.route('/', function() {
  this.render('iframe');
})

Router.route('/categories', function() {
  this.render('categories');
})

Router.route('/categories/politics', function(){
  this.render('politics');
})

Router.route('/categories/sport', function(){
  this.render('sport');
})

Router.route('/categories/travel', function(){
  this.render('travel');
})

Router.route('/categories/business', function(){
  this.render('business');
})

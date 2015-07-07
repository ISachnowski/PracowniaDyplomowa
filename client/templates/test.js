Meteor.subscribe('sites');

  Template.sitesPage.helpers({
    sitesData: function() {
      return Sites.find({AuthorID: Meteor.userId()})
    }
    }
  );
  Template.politics.helpers({
    politicsSites: function() {
      return Sites.find({Category: "Politics"})
    }
    }
  );
  Template.travel.helpers({
    travelSites: function() {
      return Sites.find({Category: "Travel"})
    }
    }
  );
  Template.sport.helpers({
    sportSites: function() {
      return Sites.find({Category: "Sport"})
    }
    }
  );
  Template.business.helpers({
    businessSites: function() {
      return Sites.find({Category: "Business"})
    }
    }
  );
Template.site.helpers({
  domain: function () {
    var a = document.createElement('a');
    a.href = this.url;
    return a.hostname;
  }
});

Template.cSite.helpers({
  domain: function () {
    var a = document.createElement('a');
    a.href = this.url;
    return a.hostname;
  }
});

Template.cSite.events({
  'click .add': function(e) {
    e.preventDefault();
    if(confirm("Do you want to add this site to 'My sites'?"))
    {
      var Site = {
        url: this.url,
        AuthorID: Meteor.userId(),
        Author: Meteor.users.findOne({_id: Meteor.userId()}).emails[0].address
      }
      Sites.insert(Site);
      }
    }
});

Template.sitesPage.isEmpty = function () {
  return Sites.find({AuthorID: Meteor.userId()}).count() == 0;
}

Template.sitesPage.events({
  'submit form': function(e) {
    e.preventDefault();
    var Site = {
      url: $(e.target).find('[name=url]').val(),
      Category: $(e.target).find('[name=category]').val(),
      AuthorID: Meteor.userId(),
      Author: Meteor.users.findOne({_id: Meteor.userId()}).emails[0].address
    }
    Sites.insert(Site);

    Router.go('/sites');
  },
  'click .delete': function(e) {
    e.preventDefault();
    if(confirm("Do you want to delete this site?"))
    {
      Sites.remove({_id: this._id});

    }
  }
});

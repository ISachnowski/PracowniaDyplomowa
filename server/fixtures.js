if (Sites.find({Category: "Politics"}).count() == 0) {
  Sites.insert({
    url: 'http://thesun.co.uk',
    Category: 'Politics'
  });

  Sites.insert({
    url: 'http://bild.de',
    Category: 'Politics'
  });

  Sites.insert({
    url: 'http://eurosport.com',
    Category: 'Sport'
  });

  Sites.insert({
    url: 'http://zdf.de',
    Category: 'Sport'
  });

  Sites.insert({
    url: 'http://travelplanet.pl',
    Category: 'Travel'
  });

  Sites.insert({
    url: 'http://mytravel.pl',
    Category: 'Travel'
  });

  Sites.insert({
    url: 'http://businessinsider.com',
    Category: 'Business'
  });

  Sites.insert({
    url: 'http://forbes.com',
    Category: 'Business'
  });
}

# PracowniaDyplomowa

There is source code for my Engineer's Thesis. Project is not working because my computer crashed and my backups also were lost.
Only templates and scripts are in final version. Below you can find summary of my Thesis.

  In the age of access to fast amounts of information in text form, increasing the role of methods and techniques for adapting content to our preferences. Puprose of the thesis is create support system to collect, filter and aggregated presentation of informations from web (blogs, thematic sites) based on user preferences. The created solution, the user decides he would like to received articles or informations, that the system classifies and assign to appropiate category.
  
  Within the case artifical intelligence techniques has been used: SVM and "Bag of words" to create model, which help to auto-assign text to categories. The next challenge in the case was mechanism for the storage of the huge amounts of data. To resolve this issue author used non-relational system of database MongoDB nad framework to highly scalable web applications - Node.js. For the presentation of the content and application uses framework Meteor, which is a platform that allows to build real-time web applications. It's about to exchange of data between the client and the server in the real time. To receive new informations from database, user dont need to refresh site because running in the background asynchronus connection to the database gets them on regular basis.

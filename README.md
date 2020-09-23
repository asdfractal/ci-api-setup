A small guide to demonstrate setting up a backend API to assist Code Institute Students working on their Milestone 3 Flask project.

## Brief

This guide assumes you have completed the Python modules prior to the Milestone 3 project and are familiar with setting up a MongoDB database as well as connecting to it via your app. If not, please refer to the relevant Code Institute lessons or the [MongoDB docs](https://docs.mongodb.com/).

The purpose of this guide is to show a very simple backend API setup, and does not go into complex queries and the different Python packages that assist in creating APIs. It is only using Flask, PyMongo and MongoDB, and the purpose is to give a look into what is possible with providing backend data via an API so people may get ideas to pursue on their own.

### API functionality covered

-   **GET** all users
-   **GET** single user by ID
-   **POST** to create a new user
-   **POST** to delete a user

### Practical use of API in my project

-   http://clockwerks-catalogue.herokuapp.com/heroes/

I created a simple API using the methods shown here to add a JavaScript filter that allows me to filter the heroes by attribute by clicking on the button. While it would be possible to do this without an API it would require page reloading or navigation to a different page and not be a smooth user experience.

## Resources

-   [Postman](https://www.postman.com/) - For testing API functionality
-   [Awesome JSON viewer](https://github.com/rbrahul/Awesome-JSON-Viewer) - View JSON in the browser
    - Updated to show the current project link. The extension on Chrome doesn't seem to be available anymore but check this project for further information.
-   [Flask](https://flask.palletsprojects.com/en/1.1.x/)
-   [MongoDB](https://www.mongodb.com/)
-   [Flask PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
-   [JSON util](https://api.mongodb.com/python/current/api/bson/json_util.html) - Included in PyMongo

### Further reading

-   https://medium.com/quick-code/absolute-beginners-guide-to-slaying-apis-using-python-7b380dc82236
-   https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask

# Blog
Blog is a easy to use blog management system.

![alt-tag] (https://s31.postimg.org/xrqxzo9wb/blog1.png)

Blog is build to make blog creation super easy and fast. It contains an userfreindly interface for admin to manage blog.

Features
--------

- Only authenticated user can create, edit, and delete posts.
- For creating post markdown text editor can be used.

Technologies used
-----------------

- Python/Django


Getting Started
---------------

To setup your local environment you should create a virtualenv and install the
necessary requirements::

    virtualenv blog-env

On Posix systems you can activate your environment like this::

    source blog-env/bin/activate

On Windows, you'd use::

    blog-env\Scripts\activate

Then::

    cd blog
    pip install -U -r requirements.txt

Here we have to create migrations::

    ./manage.py makemigrations
    ./manage.py migrate

The web interface require admin rights. To create superuser::

    ./manage.py createsuperuser 
    
You should now be able to run the development server::

    python manage.py runserver

The Web interface will be accessible at http://localhost:8000/ 

##Contributing
Blog is in its initial state and many improvements are still possible. If you find it useful and want to contribute then fork
this repo to your local machine and follow the instructions given in above section. Small contributions count a lot.

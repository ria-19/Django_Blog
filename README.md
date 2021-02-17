<h1>Web App for Blogging</h1>
<p>This is a simple blogging website created using Django, where users can create and share their thoughts.<p>
  <ul>
    <li>This project is a part of my learning journey, therefore it will be improved over time.</li>
    <li>Feedback and ideas to improve this site are always welcome.</li>
   </ul>
   
 <h2>Built With</h2>
 <ul>
  <li>Python3.8</li>
  <li>Django3.*</li>
  <li>Bootstrap4</li>
</ul>
<p>requirements.txt file is added to look for dependencies and ease of deployment.</p>


<h2>Installation</h2>
<ol>
  
   

<li>Clone the project</li>
<p>$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY</p>

<li>Create and start a a virtual environment.</li>
<p>$ virtualenv env --no-site-packages
   $ source env/bin/activate
</p>

<li>Install the project dependencies</li>
<p>$ pip install -r requirements.txt</p>

<li>create a sqLite db and add the credentials to settings.py</li>

<p>$ python manage.py migrate</p>

<li>Create admin account</li>
    <p>$python manage.py createsuperuser
    $python manage.py migrate</p>
 
<li>Start the development server</li>
    <p>$python manage.py runserver</p>
    
<h2>Acknowledgements</h2>
<p>Python Crash Course</p>

      

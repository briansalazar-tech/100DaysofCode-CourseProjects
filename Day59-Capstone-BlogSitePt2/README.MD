[bootstraptemplate]: https://startbootstrap.com/previews/clean-blog
[npointendpoint]: https://api.npoint.io/4229128df8b9b655ba0e
[unsplash]: https://unsplash.com/photos/chinese-lanterns-hang-in-a-festive-display-Dfbdn6ySZDg
## Day 59: Blog Capstone Project Part 2
## Lesson Overview
**Day 59** expands on the blog website created on Day 57 of the course. This iteration of the project adds a Bootstrap blog template to upgrade the website's visual appearance. The enhanced styling and navigation give the blog website a modern visual appearance!

Screenshots of the rendered pages can be found under the [website screenshots folder](<website screenshots>).
## Project
### Links
Blog website bootstrap template: [Startbootstrap.com][bootstraptemplate]

Blog post data: [Npoint.io][npointendpoint]

Homepage header: [Unsplash.com][unsplash]
### Modules Used
#### Flask
**Flask** is used to render the blog website pages and routes.
#### Requests
**Requests** is used to retrieve the blog post data from npoint.io.
### Project Walkthrough
Outside of visual enhancements, this website does not add much more functionality compared to the day 57 Blog Website. Below are some of the key differences from this version and the original blog website:
-	Bootstrap template is used to enhance the visual appearance of the website.
-	Contact and about pages added.
-	Header and footer templates added to make website navigation easier to update/manage.

Below is a quick overview of the pages and files used in this website.

#### Main.py
**Main.py** is responsible for running the Flask server. Main.py also imports the blog posts returned from the post.py file. With the blog posts on hand, main.py has the following routes:
- **Home**: renders index.html with individual blog post titles and subtitles, along with a link to the complete blog post.
- **contact**: Renders the contact page.
- **about**: Renders the about page.
- **Get_post**: renders an individual blog post based on the blog post’s ID.

#### Index.html
**Index.html** displays the blog post data that is passed through using the **all_posts list**. The page lists the post’s title, subtitle, author, postdate, and a link to the individual blog post. Instead of creating individual items for each blog post, Jinja templating is used to cut down on the lines of HTML code.

#### Post.html
Based on the post ID that’s passed, **post.html** renders a blog post’s title, subtitle, and body. 

#### About.html
**About.html** displays the about me page.

#### Contact.html
**Contact.html** displays the contact me page. The page itself has a form that can be submitted by a visitor.

#### Header.html
**Header.html** displays the Navbar and header information for the website. The header is linked to other pages on the website using templating. Using templating for the navbar makes it easy to add and remove pages to the website.

#### Footert.html
**Footer.html** contains the contents of every page’s footer. The footer is linked to other pages using templating.


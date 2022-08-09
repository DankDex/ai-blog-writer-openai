from flask import Flask, render_template, request
import config
import blog


def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)
app.config.from_object(config.config['development'])

app.register_error_handler(404, page_not_found)


@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == 'POST':
        """
        if 'form1' in request.form:
            prompt = request.form['blogTopic']
            blogT = blog.generateBlogTopics(prompt)
            blogTopicIdeas = blogT.replace('\n', '<br>')

        if 'form2' in request.form:
            prompt = request.form['blogSection']
            blogT = blog.generateBlogSections(prompt)
            blogSectionIdeas = blogT.replace('\n', '<br>')

        if 'form3' in request.form:
            prompt = request.form['blogExpander']
            blogT = blog.blogSectionExpander(prompt)
            blogExpanded = blogT.replace('\n', '<br>')
        """
        if 'form1' in request.form:

            fullText = "TOPIC:\n"

            prompt = request.form['blogTopic']
            blogT = blog.generateBlogTopics(prompt)
            blogTopicIdeas = blogT.split('\n')

            if(blogTopicIdeas[2][0].isdigit()):
                blogTopicIdeas[2] = blogTopicIdeas[2][2:]

            fullText += blogTopicIdeas[2] + "\n\n";

            blogT = blog.generateBlogSections(blogTopicIdeas[2])
            blogSectionIdeas = blogT.split('\n')

            for section in range(2, len(blogSectionIdeas)-1):
                if(blogSectionIdeas[section].replace(" ", "") != ""):
                    if(blogSectionIdeas[section][0].isdigit()):
                        blogSectionIdeas[section] = blogSectionIdeas[section][2:]
                    fullText += "SECTION: \n" + blogSectionIdeas[section] + blog.blogSectionExpander(blogTopicIdeas[2],blogSectionIdeas[section]) + "\n\n\n"

            print(fullText + "\n\n\nTOPIC IDEAS:\n\n")
            print(*blogTopicIdeas, sep = "   BBB   ")
            print("\n\n\nSECTION IDEAS:\n\n")
            print(*blogSectionIdeas, sep = "   BBB   ")

            fullText = fullText.replace('\n', '<br>')


    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)

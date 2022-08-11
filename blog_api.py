import gdata.blogger.client
import gdata.client
import gdata.sample_util
import gdata.data
import atom.data


class blogConnect():

    def __init__(self):
        """Creates a GDataService and provides ClientLogin auth details to it.
        The email and password are required arguments for ClientLogin.  The
        'source' defined below is an arbitrary string, but should be used to
        reference your name or the name of your organization, the app name and
        version, with '-' between each of the three values."""

        # Authenticate using ClientLogin, AuthSub, or OAuth.
        self.client = gdata.blogger.client.BloggerClient()
        gdata.sample_util.authorize_client(
            self.client, service='blogger', source='Blogger_Python_Sample-2.0',
            scopes=['http://www.blogger.com/feeds/'])

        # Get the blog ID for the first blog.
        feed = self.client.get_blogs()
        self.blog_id = feed.entry[0].get_blog_id()


    def CreatePost(self, title, content, is_draft):
        """This method creates a new post on a blog.  The new post can be stored as
        a draft or published based on the value of the is_draft parameter.  The
        method creates an GDataEntry for the new post using the title, content,
        author_name and is_draft parameters.  With is_draft, True saves the post as
        a draft, while False publishes the post.  Then it uses the given
        GDataService to insert the new post.  If the insertion is successful, the
        added post (GDataEntry) will be returned.
        """
        return self.client.add_post(self.blog_id, title, content, draft=is_draft)


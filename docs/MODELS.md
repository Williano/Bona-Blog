Model Architecture Planning

Category

    - name
    - slug
    - image
    
AuthorProfile

    - user   (OneToOne to django contrib User)
    - image

Article

    - category  (ForeignKey  to category)
    - title
    - slug 
    - author  (ForeignKey to defualt django contrib user)
    - image 
    - body
    - tags
    - date_published
    - date_created
    - date_updated
    - status (draft, published)
    
Comment

    - name
    - email
    - comment
    - article    
    - date created
    - date updated
    - approved (True or False)
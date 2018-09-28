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
    - published date
    - created date
    - updated
    - status (draft, published)
    
Comment

    - name
    - email
    - comment
    - post     
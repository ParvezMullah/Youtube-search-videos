# youtube-search-videos
Pre-requisites:
1. install and run docker(https://www.docker.com/get-started).


Steps to run the project:
1. Clone the project
    git clone https://github.com/ParvezMullah/youtube-search-videos.git
2.Go to the project dictory and run
     docker-compose up
3. create a admin
    docker exec -it youtube-search-videos_search-api_1 python manage.py createsuperuser
4. Go to admin. Open browser and type
    localhost:8000/admin
5. Add developer key. Untill we have a valid key in our DeveloperKey table a backgroup running command wont be fetching the youtube vidoe details.
    http://localhost:8000/admin/search_videos/developerkey/
6. View Saved Video details
    http://localhost:8000/admin/search_videos/youtubevideodetail/
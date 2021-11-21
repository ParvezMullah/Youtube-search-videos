# youtube-search-videos
<h2>Pre-requisites:</h2>
1. install and run docker(https://www.docker.com/get-started).


<h2>Steps to run the project:</h2>

1. Clone the project  </br>
    <code>git clone https://github.com/ParvezMullah/youtube-search-videos.git </code>  </br>

2. Go to the project dictory and run  </br>
     <code>docker-compose up</code>  

3. create a admin username and password  </br>
    <code>docker exec -it youtube-search-videos_search-api_1 python manage.py createsuperuser</code> </br>

4. Go to admin. Open browser and type
    http://localhost:8000/admin

    ![Alt text](https://github.com/ParvezMullah/youtube-search-videos/blob/master/screenshots/admin%20login.png?raw=true "Admin Login")

5. Add developer key. Untill we have a valid key in our DeveloperKey table a backgroup running command wont be fetching the youtube vidoe details. If we have multiple keys then it will fallback to other key if one is failed and it will back failed key as inactive. 
    http://localhost:8000/admin/search_videos/developerkey/ 

    ![Alt text](https://github.com/ParvezMullah/youtube-search-videos/blob/master/screenshots/developer%20keys.png?raw=true "Add Developer Key")

6. Manually Populate Videos (By running django custom command)  </br>
    <code>docker exec -it youtube-search-videos_search-api_1 python manage.py fetch_youtube_videos</code> 
7. View Saved Video details
    http://localhost:8000/admin/search_videos/youtubevideodetail/ 
    ![Alt text](https://github.com/ParvezMullah/youtube-search-videos/blob/master/screenshots/video%20list.png?raw=true "Add Developer Key")
    
    
<h2>APIs:</h2>

1. list api
    http://localhost:8000/ 
    ![Alt text](https://github.com/ParvezMullah/youtube-search-videos/blob/master/screenshots/paginated%20video%20list.png?raw=true "List API")
    
2. Search API 
    http://localhost:8000/search/?q=football
    ![Alt text](https://github.com/ParvezMullah/youtube-search-videos/blob/master/screenshots/paginated%20video%20search.png?raw=true "Search API")

         ___
         ',_`""\        .---,
            \   :-""``/`    |
             `;'     //`\   /
             /   __     |   ('.
            |_ ./O)\     \  `) \
           _/-.    `      `"`  |`-.
       .-=; `                  /   `-.
      /o o \   ,_,           .        '.
      L._._;_.-'           .            `'-.
        `'-.`             '                 `'-.
            `.         '                        `-._
              '-._. -'                              '.
                 \                                    `\
                  |                                     \
                  |    |                                 ;   _.
                  \    |           |                     |-.((
                   ;.  \           /    /                |-.`\)
                   | '. ;         /    |                 |(_) )
                   |   \ \       /`    |                 ;'--'
                    \   '.\    /`      |                /
                     |   /`|  ;        \               /
                     |  |  |  |-._      '.           .'
                     /  |  |  |__.`'---"_;'-.     .-'
                    //__/  /  |    .-'``     _.-'`
                  jgs     //__/   //___.--''`

# Piglatinizer

## Getting started
    1.  pip install -r requirements.txt
    2.  uvicorn app.main:app --reload will start the app and reload automatically on updates.
    3.  [Open this to see your results](http://localhost:8000/piglatinize/?text=RadAI%20is%20like%20totally%20rad,%20bro)

### Docker
    1. Install Docker and Docker Compose
    2. From the project directory run: docker-compose up -d
    3. [Open this to see your results](http://localhost:8001/piglatinize?text=Hello%20World)
    4. Run docker-compose down to terminate the container

### Client Script
    1.  From the script directory run test_api.py to send bulk requests to the API
    2.  Be sure to set the port correctly do distinguish between the Docker container or local development